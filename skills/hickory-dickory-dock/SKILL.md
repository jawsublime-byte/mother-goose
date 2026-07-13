---
name: hickory-dickory-dock
description: Enforce an hourly work rhythm by recording the start time, checkpointing at sixty elapsed minutes, and requiring a five-minute break before continued work. Use only when explicitly invoked during an active session with access to reliable time.
---

# Hickory Dickory Dock

At the hour, stop the clock.

## Start

Record the reliable session start time and the current task. If the host supplies no clock or cannot remain active, state that automatic enforcement is unavailable and provide a manual checkpoint instead.

## Work rhythm

1. Continue the authorized task normally.
2. Track elapsed wall-clock time without interrupting for routine countdowns.
3. At sixty elapsed minutes, finish only the smallest safe atomic action.
4. Save or report a recoverable checkpoint: completed work, current state, next action, and blockers.
5. Stop all further work.

Output:

HICKORY DICKORY DOCK
Elapsed: 60 minutes
Checkpoint: [recoverable state]
Break: 5 minutes
Resume after: [time]

Do not continue until five minutes have elapsed and the user requests or confirms resumption. Never pretend a timer ran in the background.

## Completion

The skill succeeds when the session stops at the hour with a recoverable checkpoint and no work occurs during the break.
