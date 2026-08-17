---
name: hansel-and-gretel
description: Leave concise recoverable breadcrumbs through a long or multi-agent build so work can resume from evidence instead of memory. Use only when explicitly invoked to establish or inspect an operational checkpoint trail.
---

# Hansel and Gretel

Leave enough breadcrumbs to get home.

## Breadcrumb

At each meaningful checkpoint record only operational facts needed to recover the work:

- current authoritative directive, packet, or objective;
- current step and completion state;
- concise user-visible decision rationale when a decision was made;
- files, artifacts, or interfaces changed;
- tests or evidence produced;
- unresolved questions, blockers, or known risks;
- next safe step;
- commit, hash, timestamp, or version when available.

Never record credentials, secrets, unnecessary personal data, or hidden chain-of-thought. If a fact is unavailable, mark it unknown.

Prefer append-only breadcrumbs so later work cannot silently rewrite earlier history.

## Recovery

1. Start from the latest trusted breadcrumb.
2. Verify that its named artifacts and version still exist.
3. Compare the current state with the recorded next step.
4. If a gap or contradiction appears, stop and reconstruct that interval before continuing.

## Output

BREADCRUMB
Authority: [directive or packet]
Step: [current step]
State: [complete/partial/blocked]
Changed: [artifacts]
Evidence: [tests/receipts]
Open: [questions/risks]
Next: [next safe step]
Version: [commit/hash/time or unknown]

## Completion

Finish when another worker can resume from the breadcrumb without depending on conversational memory.