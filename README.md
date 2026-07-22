# LLM Learning to Larp

Me teaching myself how large language models and AI agents actually work — in public,
from the four big pieces down to running my own model and building my own agent by hand.

**The rule for the whole project:** *I can only keep a sentence if I can defend it aloud
with nothing open.* Every explanation in this repo is mine, written after I could teach it
back cold — not pasted from a model.

🔗 **Live site:** https://gitlostinthesauce.github.io/LLM-Learning-to-Larp/

---

## The phases

| Phase | Title | What I did | Deliverable |
|-------|-------|-----------|-------------|
| **1** | The Big Map | The four pillars — Model, Context, Harness/Loop, Tools — and how they hand off in a loop. Hand-drawn first. | [`big-picture.html`](big-picture.html) · [`phase-1/`](phase-1/) |
| **2** | The Parts & The Tools | Split each pillar into its real parts, then **built a tiny agent by hand** and ran a **bare-vs-configured** experiment. | [`phase-2/pillars-deep-dive.html`](phase-2/pillars-deep-dive.html) · [`phase-2/README.md`](phase-2/README.md) |
| **3** | Go Deep & Go Custom | Ran real models locally, then did **"the swap"** — same harness, model swapped from Claude to a local one — plus a two-model bake-off. | [`phase-3/deep-dive.html`](phase-3/deep-dive.html) |
| **4** | The Missing Pillar | Turned the lesson into a product argument: the context pillar is the durable one while models commoditize. | [`phase-4/index.html`](phase-4/index.html) |

## Repo layout

```
index.html                 Homepage — links every phase
guide.html                 The curriculum I'm following (the phase map)
big-picture.html           Phase 1 deliverable — the four pillars & the loop

phase-1/                   Notes + photos of the hand-drawn work
  my-work.html
  notes.md
phase-2/                   The ★ exercise: an agent built by hand
  tiny_agent.py            ~50-line agent: a loop around Claude running one tool
  pillars-deep-dive.html
  with-without/            Same app twice — naked/ vs kitted/ (CLAUDE.md, a skill,
                           permissions, a validate.py hook)
phase-3/                   Going local
  tiny_agent_local.py      "The swap" — same loop, model pointed at local Ollama
  bakeoff.py               Two small local models, side by side
  deep-dive.html
phase-4/                   The missing pillar, framed as a product
  index.html
```

## Running the code

The agents read their API key from the environment — nothing secret is ever committed
(`.gitignore` excludes `.env`, `*.key`, and similar). Phase 2 has full run instructions in
[`phase-2/README.md`](phase-2/README.md); Phase 3's local agent needs [Ollama](https://ollama.com)
with a small model pulled (e.g. `llama3.2:1b`).

The HTML pages are static — open any of them directly in a browser, or browse the
[live site](https://gitlostinthesauce.github.io/LLM-Learning-to-Larp/).
