---
name: five-little-monkeys
description: Stop repeating the same operation under unchanged conditions after the same failure signature is reproduced. Use only when explicitly invoked for blind retries; use the user's retry budget or default to three identical reproduced failures.
---

# Five Little Monkeys

If the same monkey falls the same way, stop jumping on the bed.

## Retry gate

Use the user's retry budget. If none is stated, stop after three reproduced failures with the same operation, material conditions, and failure signature.

Do not count unrelated environment outages, changed inputs, or materially different approaches as identical retries.

## After the ceiling

1. Record each counted attempt and its failure evidence.
2. Identify what remained unchanged across the attempts.
3. Prohibit another exact retry under those same conditions.
4. Choose exactly one next move:
   - change a material condition or input and explain why;
   - gather missing evidence before another attempt;
   - route to Humpty Dumpty if the underlying repair strategy itself is exhausted;
   - pause for user direction.
5. Do not reset the retry count by renaming the same command or making a cosmetic change.

## Output

MONKEY COUNT
Operation: [operation]
Failure signature: [signature]
Count: [attempts]/[budget]
Unchanged conditions: [conditions]
Next move: CHANGE CONDITION | GATHER EVIDENCE | HUMPTY DUMPTY | PAUSE
Reason: [evidence-based reason]

## Completion

Finish when another identical blind retry is prevented and the next attempt, if any, has a materially changed condition or strategy.