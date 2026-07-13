---
name: humpty-dumpty
description: Stop repeatedly repairing the same failed implementation strategy, preserve the required behavior, and choose a materially different approach. Use when explicitly invoked after a repair has failed the stated budget; default to two reproduced failed attempts when no budget is given.
---

# Humpty Dumpty

When the same egg has fallen twice, stop spending attempts on the same reconstruction.

## Failure gate

Count only reproduced failures of the same underlying strategy. Do not abandon an approach because of an unrelated environment error or an unverified guess.

Use the user's repair budget. If none is stated, the budget is two reproduced failed attempts.

## Pivot

1. Freeze required behavior, inputs, outputs, compatibility, data, and acceptance checks.
2. Record the failed strategy, attempts, exact failures, and evidence.
3. Identify the assumption shared by the failed attempts.
4. Stop patching that strategy.
5. Select a materially different approach that preserves the frozen contract.
6. Ask before deleting files, changing public APIs, migrating data, adding dependencies, or altering architecture.
7. Implement only when the user requested a fix.
8. Run the original reproduction and acceptance checks.

Do not hide failure history. Do not call a renamed version of the same strategy a pivot.

## Output

HUMPTY DUMPTY PIVOT
Failed strategy: [strategy]
Budget used: [attempts]/[budget]
Shared failure: [evidence]
Frozen requirements: [requirements]
Replacement strategy: [different approach]
Verification: [checks]

## Completion

Finish when the replacement passes the original failed reproduction and all frozen requirements.
