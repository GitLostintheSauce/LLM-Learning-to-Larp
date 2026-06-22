"""
tiny_agent.py — the simplest possible agent, built by hand.

This is Phase 1's pillars 3 & 4 (the Harness/Loop and the Tools) made real:

    THE MODEL    = Claude, called via client.messages.create(...). It only predicts text.
    THE CONTEXT  = the `messages` list below — everything the model can see, and all it sees.
    THE HARNESS  = the while-loop in run(). It wraps the model and loops it.
    THE TOOLS    = calculate(). The model ASKS for it; the harness RUNS it.

The model never does math itself. It asks for the calculator; our code runs it
and feeds the answer back. That hand-off, repeated in a loop, IS an agent.
"""

import ast
import operator
import anthropic

# ---- THE TOOL (the outside world) ----------------------------------------
# A safe calculator. We do NOT use eval() — we walk the parsed expression so
# only arithmetic can run, nothing else.
_OPS = {
    ast.Add: operator.add,  ast.Sub: operator.sub,
    ast.Mult: operator.mul, ast.Div: operator.truediv,
    ast.Pow: operator.pow,  ast.USub: operator.neg,
}

def _eval(node):
    if isinstance(node, ast.Constant):     # a plain number, e.g. 7
        return node.value
    if isinstance(node, ast.BinOp):        # a + b, a * b, ...
        return _OPS[type(node.op)](_eval(node.left), _eval(node.right))
    if isinstance(node, ast.UnaryOp):      # -a
        return _OPS[type(node.op)](_eval(node.operand))
    raise ValueError("unsupported expression")

def calculate(expression: str) -> str:
    """Evaluate one arithmetic expression and return the answer as text."""
    return str(_eval(ast.parse(expression, mode="eval").body))

# ---- THE TOOL DEFINITION --------------------------------------------------
# How we DESCRIBE the tool so the model knows when and how to ask for it.
TOOLS = [{
    "name": "calculate",
    "description": "Evaluate a basic arithmetic expression, e.g. '12 * (3 + 4)'.",
    "input_schema": {
        "type": "object",
        "properties": {
            "expression": {"type": "string", "description": "The math to evaluate"},
        },
        "required": ["expression"],
    },
}]

client = anthropic.Anthropic()   # reads your ANTHROPIC_API_KEY from the environment

def run(user_text: str) -> None:
    # THE CONTEXT starts as just the user's request.
    messages = [{"role": "user", "content": user_text}]

    # THE HARNESS / LOOP: keep going until the model stops asking for tools.
    while True:
        response = client.messages.create(
            model="claude-opus-4-8",
            max_tokens=1024,
            tools=TOOLS,
            messages=messages,
        )

        # The model is DONE — it produced a final answer, not a tool request.
        if response.stop_reason == "end_turn":
            print(next(b.text for b in response.content if b.type == "text"))
            return

        # Otherwise the model ASKED for a tool. Record what it said into context...
        messages.append({"role": "assistant", "content": response.content})

        # ...then RUN each requested tool and feed the RESULT back into context.
        results = []
        for block in response.content:
            if block.type == "tool_use":
                print(f"[harness runs {block.name}({block.input})]")
                answer = calculate(**block.input)
                results.append({
                    "type": "tool_result",
                    "tool_use_id": block.id,   # must match the request's id
                    "content": answer,
                })
        messages.append({"role": "user", "content": results})
        # Loop again: the model now sees the tool result in its context.

if __name__ == "__main__":
    run("What is 12 * (3 + 4), and then that result minus 19?")
