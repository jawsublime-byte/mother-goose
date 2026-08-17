---
name: tortoise-and-hare
description: Make verified completion outrank raw speed when reviewing rushed work or comparing builders, models, or approaches. Use only when explicitly invoked with a shared finish line or acceptance criteria.
---

# The Tortoise and the Hare

Fast matters only after the runner reaches the finish line.

## Finish line

Freeze the requirements, mandatory tests, quality gates, and comparable conditions before looking at elapsed time or cost.

## Race

1. Evaluate every candidate against the same required finish line.
2. Mark any candidate that skips a mandatory gate as incomplete, regardless of speed.
3. Rank correctness and completeness before latency, token use, or cost.
4. Only among equally complete passing results compare speed and efficiency.
5. Separate measured timing from self-reported timing.
6. Do not call one runner faster when environments, task scope, or acceptance gates are materially different.

A slow pass is not automatically best. A fast pass is valuable. The rule is simply that speed cannot compensate for unfinished required work.

## Output

FINISH LINE
Criteria: [shared gates]
Candidate: [name]
Completion: PASS | PARTIAL | FAIL | BLOCKED
Evidence: [checks]
Elapsed/cost: [measured values or unknown]
Rank basis: [completion first, then efficiency]

## Completion

Finish when every compared candidate is judged against the same finish line and speed is used only after required work is proven complete.