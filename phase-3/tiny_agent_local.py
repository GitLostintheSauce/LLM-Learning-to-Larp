"""
tiny_agent_local.py — THE SWAP (Phase 3 ★).

Same agent as phase-2/tiny_agent.py — SAME loop, SAME calculator tool — but the
MODEL is now llama3.2:1b running locally via Ollama instead of Claude over the API.

The only thing that really changed is `call_model()`. That's the whole lesson:
the harness (the loop + the tool) and the model (the brain) are separate,
swappable parts. Swap the brain, keep the body.
"""

import ast, operator, json, urllib.request

# ---- THE TOOL (identical to the Phase-2 agent) ----
_OPS = {ast.Add:operator.add, ast.Sub:operator.sub, ast.Mult:operator.mul,
        ast.Div:operator.truediv, ast.Pow:operator.pow, ast.USub:operator.neg}
def _eval(node):
    if isinstance(node, ast.Constant): return node.value
    if isinstance(node, ast.BinOp): return _OPS[type(node.op)](_eval(node.left), _eval(node.right))
    if isinstance(node, ast.UnaryOp): return _OPS[type(node.op)](_eval(node.operand))
    raise ValueError("unsupported expression")
def calculate(expression: str) -> str:
    return str(_eval(ast.parse(expression, mode="eval").body))

# ---- THE TOOL DEFINITION (Ollama's shape differs slightly from Claude's) ----
TOOLS = [{
    "type": "function",
    "function": {
        "name": "calculate",
        "description": "Evaluate a basic arithmetic expression, e.g. '12 * (3 + 4)'.",
        "parameters": {
            "type": "object",
            "properties": {"expression": {"type": "string", "description": "The math to evaluate"}},
            "required": ["expression"],
        },
    },
}]

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "llama3.2:1b"

def call_model(messages):
    """THE ONE PART THAT CHANGED: talk to the local model instead of Claude's API."""
    payload = {"model": MODEL, "messages": messages, "tools": TOOLS, "stream": False}
    req = urllib.request.Request(OLLAMA_URL, data=json.dumps(payload).encode(),
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read())["message"]

def run(user_text):
    # THE CONTEXT and THE HARNESS / LOOP are unchanged from the Phase-2 agent.
    messages = [{"role": "user", "content": user_text}]
    for _ in range(6):  # safety cap so a small model can't loop forever
        msg = call_model(messages)
        messages.append(msg)                       # record what the model said
        calls = msg.get("tool_calls")
        if not calls:                              # no tool wanted -> final answer
            print(msg.get("content", "").strip())
            return
        for call in calls:                         # the model ASKED for a tool
            args = call["function"]["arguments"]
            print(f"[harness runs calculate({args})]")
            try:
                result = calculate(args["expression"])
            except Exception as e:
                result = f"error: {e}"
            messages.append({"role": "tool", "content": result})  # feed result back
    print("(stopped: hit the loop cap)")

if __name__ == "__main__":
    run("What is 12 * (3 + 4), and then that result minus 19?")
