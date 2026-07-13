---
name: goldilocks
description: Find the exact median of ordered values or choose a bounded middle configuration that is neither excessive nor insufficient. Use only when explicitly invoked with values or measurable constraints. Never label an arbitrary preference as a mathematical median.
---

# Goldilocks

Separate the exact middle from the merely comfortable.

## Mathematical median

1. Validate that the supplied values are comparable.
2. Sort them without dropping duplicates.
3. For an odd count, select the middle value.
4. For an even count of numeric values, calculate the mean of the two middle values.
5. For an even count of non-numeric ordered choices, report both middle choices; do not invent an exact single median.
6. Show the ordered set and calculation.

## Bounded configuration

When the task is a trade-off rather than a true median:

1. Define the minimum acceptable floor and maximum acceptable ceiling.
2. Identify measurable constraints and disqualify choices outside them.
3. Compare remaining choices by the user's priorities.
4. Select the least extreme choice that satisfies all requirements.
5. Label it a balanced choice, not an exact median.

Do not average incompatible units or hide weighting assumptions.

## Output

GOLDILOCKS RESULT
Type: exact median | balanced choice
Inputs: [ordered values or bounded options]
Result: [value or option]
Reason: [calculation or criteria]

## Completion

Finish when the result is reproducible from the displayed values or criteria.
