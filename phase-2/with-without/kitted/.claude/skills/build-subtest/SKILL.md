---
name: build-subtest
description: The reusable pattern for adding a cognitive subtest to the battery. Use whenever creating or editing a subtest so all five are structured the same way.
---

# build-subtest

Every subtest in this battery follows the SAME shape, so they stay consistent and
the results pipeline can rely on them. When you add or edit a subtest, follow this.

## 1. A screen section
```html
<section id="<id>" class="screen">
  <div class="card">
    <div class="progress">Task N of 5 · <name> (<domain>)</div>
    <h2>…</h2><p class="sub">… instructions …</p>
    <!-- task UI -->
  </div>
</section>
```

## 2. A `start<Name>()` function that:
- resets its own state,
- runs the task,
- writes ONE raw score into the shared `R` object (e.g. `R.fluencyCount = …`),
- calls `show('<nextId>')` and the next `start…()`.

## 3. Raw score keys (consumed by the SCORING block — do not rename)
`R.digitForward`, `R.digitBackward`, `R.stroopAcc`, `R.stroopRT`,
`R.trailA`, `R.trailB`, `R.matrixCorrect`, `R.fluencyCount`

## Rules
- The subtest computes a **raw** score only. All 0–100 mapping happens in the central
  `SCORING` block (see CLAUDE.md) — never inline magic numbers in a subtest.
- Keep each subtest self-contained: its own state vars, its own `start…()` entry point.
