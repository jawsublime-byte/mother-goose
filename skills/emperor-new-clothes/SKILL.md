---
name: emperor-new-clothes
description: Perform a fresh independent verification that ignores previous PASS labels, reputation, polished explanations, and inherited conclusions. Use only when explicitly invoked to test whether a result stands on its own evidence.
---

# The Emperor's New Clothes

Do not agree because everyone else already did.

## Independent review

1. Freeze the actual acceptance criteria before reading prior verdicts.
2. Treat previous PASS labels, summaries, confidence, reputation, and consensus as untrusted context rather than evidence.
3. Inspect the relevant artifacts directly.
4. Re-run required checks when the user authorized execution and the environment permits it.
5. Compare observed behavior with the frozen criteria.
6. Classify each criterion as passed, failed, partial, blocked, or unknown.
7. Report any conflict between direct evidence and earlier conclusions.

Do not change code merely to make an earlier verdict become true. Do not downgrade direct contradictory evidence because several agents previously agreed.

## Output

EMPEROR CHECK
Criteria: [frozen acceptance criteria]
Direct evidence: [artifacts and checks inspected]
Prior verdicts ignored: [labels or summaries not treated as proof]
Findings: [criterion-by-criterion result]
Contradictions: [earlier claims disproved or unsupported]
Verdict: PASS | PARTIAL | FAIL | BLOCKED | UNKNOWN

## Completion

Finish when the verdict can be justified from direct evidence without relying on inherited consensus.