---
name: old-lady-swallowed-fly
description: Stop a cascading chain of workarounds and trace it back to the earliest verified cause before adding another fix. Use only when explicitly invoked for a repair sequence where fixes are creating more fixes.
---

# There Was an Old Lady Who Swallowed a Fly

Do not swallow another animal to solve the fly.

## Cascade gate

Before adding another workaround, identify the original symptom and every compensating change already added after it. If that chain cannot be reconstructed from available evidence, pause instead of inventing it.

## Unwind

1. Freeze the required behavior and acceptance checks.
2. Reconstruct the repair chain in chronological order.
3. For every change, record what it attempted to fix, what evidence justified it, and what new failure followed.
4. Identify the earliest reproduced defect or unsupported assumption that caused the cascade.
5. Propose the smallest correction at that causal point.
6. Ask before removing workarounds when removal could change behavior, data, public interfaces, or compatibility.
7. Implement only when the user requested a fix.
8. Re-run the original reproduction and every affected acceptance check.

If the original cause remains unknown, say so. Another compensating layer is not a diagnosis.

## Output

OLD LADY TRACE
Original symptom: [symptom]
Repair chain: [change -> consequence]
Earliest verified cause: [cause and evidence]
Workarounds now unnecessary: [items or unknown]
Root-level correction: [proposed or performed]
Verification: [checks]

## Completion

Finish when the cascade is traced to a verified cause, or the work is explicitly paused because the cause remains unknown.