"""
bakeoff.py — Phase 3 exercise: two local models, same prompts, who wins?

Runs each prompt against two models via the Ollama API and prints the answers
side by side, with timing. The prompts are chosen to EXPOSE differences:
a reasoning trap, a fact, and an instruction-following test.
"""
import json, urllib.request, time

MODELS = ["llama3.2:1b", "qwen2.5:1.5b"]
PROMPTS = [
    ("Reasoning trap",
     "A bat and a ball cost $1.10 in total. The bat costs $1.00 more than the ball. "
     "How much does the ball cost? Answer with just the amount."),
    ("Fact",
     "What year did the Apollo 11 moon landing happen? Answer with just the year."),
    ("Instruction-following",
     "List exactly three fruits, comma-separated, and nothing else."),
]

def ask(model, prompt):
    payload = {"model": model, "messages": [{"role": "user", "content": prompt}], "stream": False}
    req = urllib.request.Request("http://localhost:11434/api/chat",
                                 data=json.dumps(payload).encode(),
                                 headers={"Content-Type": "application/json"})
    t = time.time()
    with urllib.request.urlopen(req) as r:
        out = json.loads(r.read())["message"]["content"].strip()
    return out, time.time() - t

for label, prompt in PROMPTS:
    print(f"\n=== {label} ===\nQ: {prompt}")
    for m in MODELS:
        ans, secs = ask(m, prompt)
        print(f"  [{m}] ({secs:.1f}s): {ans}")
