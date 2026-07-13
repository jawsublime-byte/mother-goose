---
name: three-little-pigs
description: Test a user-authorized build at three escalating resilience levels — straw, sticks, and bricks — before calling it robust. Use only when explicitly invoked with a bounded target and safe test environment.
---

# Three Little Pigs

Test the same required behavior against three stronger winds.

## Safety gate

Define the target, contract, environment, fixtures, resource ceiling, prohibited effects, and stop conditions. Default to a sandbox. Never run destructive or uncontrolled tests against production or third parties.

## Straw

Test ordinary operation and light faults:

- expected input;
- one invalid or missing value;
- clean restart;
- normal timeout or cancellation.

Record failures before advancing.

## Sticks

Test compound and operational stress:

- dependency delay or temporary failure;
- retry and duplicate delivery;
- moderate concurrency or load;
- ordering and partial completion;
- recovery after interruption.

## Bricks

Test the declared worst credible conditions:

- adversarial but authorized input;
- resource ceiling;
- repeated dependency failure;
- crash and recovery;
- integrity, authorization, and fail-closed behavior;
- rollback or restoration.

Use only cases relevant to the target. Escalation never authorizes scope expansion.

## Output

For each level report cases, expected results, actual results, evidence, failures, and recovery. Classify the build by the highest fully passed level.

## Completion

Finish when all declared cases are recorded, cleanup succeeds, and the resilience claim names the highest passed house.
