---
name: ring-around-the-rosie
description: Apply R.A.T.R. — Ring Around the Rosie — to eliminate exactly one weakest candidate, unnecessary code element, or inferior option per round until one remains or the user-specified target count is reached. Use only when explicitly invoked.
---

# Ring Around the Rosie

One falls each round.

## Eliminate

1. Freeze the candidate set, required behavior, decision criteria, and stopping count.
2. Make the candidates comparable using the same evidence.
3. Identify the single weakest candidate against the locked criteria.
4. State why it loses and what would be lost by removing it.
5. Eliminate only that candidate.
6. Re-evaluate the remaining set without changing criteria.
7. Repeat until one remains or the requested target count is reached.

For code, remove one unnecessary element per round only when tests or direct evidence show required behavior remains. Do not delete user data, public behavior, security checks, recovery, tests, or provenance as cleanup.

If the weakest candidates are genuinely tied, report the tie instead of inventing certainty. Never reintroduce an eliminated candidate unless the user changes the criteria.

## Round output

ROUND: [number]
Eliminated: [candidate]
Reason: [criterion and evidence]
Remaining: [candidates]

## Completion

Finish when the stopping count is reached and the survivor satisfies every locked requirement.
