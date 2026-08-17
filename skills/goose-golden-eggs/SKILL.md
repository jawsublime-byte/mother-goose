---
name: goose-golden-eggs
description: Protect proven valuable behavior before optimizing, refactoring, simplifying, or replacing the component that produces it. Use only when explicitly invoked around a known-good capability whose value must survive the change.
---

# The Goose That Laid the Golden Eggs

Do not destroy the thing producing the value while trying to improve it.

## Golden baseline

Before mutation:

1. Name the valuable behavior or output that must survive.
2. Record the current evidence that it works.
3. Freeze the acceptance, compatibility, performance, data, and interface properties that matter.
4. Define the proposed improvement and the measurable gain it is expected to produce.
5. Establish a rollback path.

If the current value cannot be demonstrated, mark the baseline unknown rather than inventing one.

## Change gate

- Modify only the authorized surface.
- Preserve the baseline tests and evidence.
- Do not treat cleaner code, novelty, or fewer files as value by themselves.
- After the change, compare the same golden behavior against the same baseline.
- If protected behavior regresses or the promised gain is not demonstrated, reject or roll back the change when authorized.

## Output

GOLDEN EGG CHECK
Protected value: [behavior]
Baseline evidence: [evidence]
Proposed gain: [measurable improvement]
Protected constraints: [constraints]
Post-change comparison: [result]
Decision: KEEP | ROLLBACK | BLOCKED | UNKNOWN

## Completion

Finish when the valuable behavior is proven preserved and the claimed gain is measured, or the change is rejected or rolled back.