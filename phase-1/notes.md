# Phase 1 — The Big Map (my paper work, transcribed)

> These are my own words, transcribed from my handwritten notes (photos in this folder).
> The one rule: I can only keep a sentence if I can defend it aloud with nothing open.

Photos:
- `diagram.jpg` — the 4-box flow, draft 5 (loop closed)
- `four-pillars.jpg` — the four pillars defined
- `flow-narration.jpg` — the full step-by-step flow

---

## The four pillars

**The Model** — Takes in text/commands and predicts what happens next. It decides
what to do and asks the harness to do the things/tasks. It deciphers what the harness
did and interprets what should be done next. A model is static and only answers from
its current context.

**The Context** — The memory of the model at that time. The context window consists of
a past number of tokens.

**The Harness (loop)** — The bridge between the Model and the tools (like a cable/cord).
It turns the model's commands into actionable code that uses tools to actually do the
stuff you want. It sends results back to the model in order to check them, and loops
until things are correct.

**The Tools / Outside World** — Tools are digital interfaces that the AI can call to
perform tasks (e.g. API calls). The outside world is everything beyond the model's
current context.

---

## The full flow (typing a request → a file gets edited)

1. A human gives a text request (e.g. "create a file called hello.txt with 1 line in it").
2. The harness assembles the context.
3. The harness sends the context to a model.
4. The model reads the context and decides which tools to ask the harness to use.
5. The harness runs the tool, interacting with the outside world.
6. The tool reports back ("file created successfully"); the harness takes the result and
   adds it to the context.
7. The model reads the updated context and decides: if the goal is met, it sends a report
   back to the user; if not, it runs again with new instructions — looping with commands
   like `cat` until done.
