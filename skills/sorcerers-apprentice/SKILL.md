---
name: sorcerers-apprentice
description: Bound an automation, agent loop, or batch with explicit scope, budgets, stop conditions, human override, cleanup, and rollback before it runs. Use only when explicitly invoked for autonomous or repeated execution.
---

# The Sorcerer's Apprentice

Never start a broom you cannot stop.

## Activation gate

Before state-changing automation begins, define:

- exact objective;
- allowed actions and surfaces;
- prohibited actions and side effects;
- maximum attempts, work items, cost, time, or other available budget;
- success stop condition;
- failure and uncertainty stop conditions;
- human cancel or override path;
- checkpoint or rollback method;
- cleanup requirements.

If a material control is missing, pause before activation.

## Run rules

1. Check scope and remaining budget before each cycle.
2. Stop immediately at success, a declared ceiling, material uncertainty, or a prohibited side effect.
3. Never expand scope, create persistence, spawn continuing work, or weaken a stop condition merely to finish.
4. Preserve a concise receipt of actions, results, failures, and remaining work.
5. On termination, perform the declared cleanup or rollback and report anything that could not be restored.

Do not pretend to monitor continuously when the host cannot continue running or observe time.

## Output

SORCERER CONTROL
Objective: [objective]
Allowed: [actions]
Denied: [actions]
Budgets: [limits]
Stop conditions: [success/failure/uncertainty]
Human override: [mechanism]
Rollback/cleanup: [mechanism]
State: READY | PAUSED | STOPPED | COMPLETE

## Completion

Finish when the automation is either safely bounded before execution or stopped with its final state and cleanup recorded.