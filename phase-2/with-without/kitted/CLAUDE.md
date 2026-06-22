# Cognitive Self-Reflection Battery — project rules

This is the persistent context for the app. Read it before any edit. It is the
single source of truth the "naked" build never had.

## What this is (and is NOT)
A self-administered battery **modeled on** classic neuropsychological subtests.
It is **NOT a clinical evaluation**: no population norms, no clinician. Results are
self-reflection, never a diagnosis or a verdict on the user's worth.

## Hard rules
1. The intro screen and the results screen **must both show the honest disclaimer.**
   Never describe the app as clinical, diagnostic, or normed.
2. **One self-contained `index.html`** — no build step, no external dependencies.
3. **Every scoring number lives in the `SCORING` block** (single source of truth) and
   **every threshold carries a one-line rationale comment.** No scattered magic numbers.
4. Every subtest is built with the same pattern — see `.claude/skills/build-subtest/`.

## The five subtests (one per cognitive domain)
| id | subtest | domain |
|----|---------|--------|
| `digitspan` | digit span (forward + backward) | working memory |
| `stroop`    | Stroop (name the ink color) | processing speed & inhibition |
| `trails`    | trail-making A & B | attention & flexibility |
| `matrices`  | pattern series | fluid reasoning |
| `fluency`   | verbal fluency ("F" words, 60s) | verbal fluency |

## SCORING scheme (0–100 per domain) — the single source of truth
Each formula maps a raw score to 0–100, with a rationale so it is defensible:

- **working memory** = (forwardSpan + backwardSpan) / 14 × 100
  *Rationale: a strong combined span ≈ 7 forward + 7 backward = 14.*
- **speed & inhibition** = stroopAccuracy×100 − max(0, medianRT−700)/25
  *Rationale: ~700ms is a brisk response; every 25ms slower costs 1 point.*
- **attention & flexibility** = 100 − max(0, trailB−trailA)/120
  *Rationale: a 0ms switch cost = 100; every extra 120ms on the alternating trail costs 1 point.*
- **fluid reasoning** = matrixCorrect / 4 × 100
  *Rationale: 4 items, 25 points each.*
- **verbal fluency** = validWords / 16 × 100
  *Rationale: ~16 valid "F" words in 60s is strong (typical letter-fluency ≈ 12–18).*

## Domain → career directions (for the results screen)
- working memory → data analysis, accounting/finance, project coordination, software engineering
- speed & inhibition → operations, trading, editing/proofreading, emergency/clinical work
- attention & flexibility → management, UX/product design, teaching, consulting
- fluid reasoning → research, engineering, strategy, law
- verbal fluency → writing, marketing, sales, communications/PR
