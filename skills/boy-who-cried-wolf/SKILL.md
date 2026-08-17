---
name: boy-who-cried-wolf
description: Calibrate repeated verifier, security, or monitoring warnings so unsupported alarms do not drown out real evidence. Use only when explicitly invoked with a set of current or supplied alerts to assess.
---

# The Boy Who Cried Wolf

Do not make every rustle a wolf.

## Alert ledger

Use only alert history and evidence actually available in the current task or supplied records. Do not invent prior false positives.

For each warning record:

- alert signature or repeated condition;
- direct evidence;
- reproducibility;
- credible impact;
- severity if justified;
- whether it duplicates an already established finding.

Classify it as NEW_SIGNAL, DUPLICATE_SIGNAL, UNCONFIRMED, FALSE_ALARM, or CRITICAL.

## Rules

1. Repetition does not make an unsupported warning more true.
2. Duplicate warnings should point back to the established evidence instead of inflating counts.
3. A warning contradicted by direct evidence should be marked false rather than quietly retained.
4. Fresh critical evidence must always surface even if similar earlier warnings were false.
5. Never suppress a warning merely to improve a metric or reduce noise.

## Output

WOLF CHECK
Alert: [warning]
Evidence: [evidence]
Reproduced: yes | no | unknown
Impact: [impact]
Class: NEW_SIGNAL | DUPLICATE_SIGNAL | UNCONFIRMED | FALSE_ALARM | CRITICAL
Action: [investigate, deduplicate, close, escalate]

## Completion

Finish when each supplied warning is classified and real signal remains visible without duplicate or unsupported alarm inflation.