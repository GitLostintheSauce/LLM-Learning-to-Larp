# Phase 2 — the ★ exercise: a tiny agent, built by hand

[`tiny_agent.py`](tiny_agent.py) is the simplest possible agent — a loop around
Claude that runs ONE tool (a calculator) and feeds the result back, until done.
It's Phase 1's pillars 3 & 4 (the Harness/Loop and the Tools) made real.

## The four pillars, in the code
- **Model** — `client.messages.create(...)`. Predicts text; here the text is sometimes a tool request.
- **Context** — the `messages` list. All the model sees; we re-send it every loop.
- **Harness / Loop** — the `while True:` loop. Calls the model, runs tools, loops until `end_turn`.
- **Tools & world** — `calculate()`. The model *asks*; the harness *runs* it.

## Run it
```bash
# 1. Install the SDK (one time)
python3 -m pip install anthropic

# 2. Get an API key from https://console.anthropic.com  → API Keys
#    then put it in your environment (this shell only):
export ANTHROPIC_API_KEY="sk-ant-..."

# 3. Run
python3 tiny_agent.py
```

Expected: you'll see the harness print each `[harness runs calculate(...)]` line
(the loop running more than once), then the final answer.

## The rule
I can explain **every line** of `tiny_agent.py` with no AI open. The point isn't
that it runs — it's that I understand why each piece is there.
