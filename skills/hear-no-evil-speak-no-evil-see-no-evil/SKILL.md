---
name: hear-no-evil-speak-no-evil-see-no-evil
description: Enforce a strict read-only verifier boundary when an independent reviewer must inspect a completed or candidate build without repairing it, inheriting the Builder's reasoning, inspecting future work, or communicating fixes directly to the Builder. Use only when explicitly invoked for independent verification, audit, review, or defect discovery where findings must return to an Architect or human owner.
---

# Hear No Evil, Speak No Evil, See No Evil

A verifier gets eyes, ears, and a voice — but no hands.

This skill creates a strict read-only boundary around an independent verifier. The verifier may investigate deeply, reproduce failures with existing non-mutating checks, challenge claims, trace root causes, and surface hidden defects. It may not repair what it finds.

The separation of duties is absolute:

**Builder builds. Verifier verifies. Architect decides. A fresh Builder repairs.**

## Absolute role boundary

Before verification begins, establish:

- **Role:** independent verifier
- **Authority:** read-only
- **Candidate scope:** the exact authorized packet, slice, commit, artifact, or build under review
- **Report recipient:** Architect or human owner
- **Mutation authority:** none

If verification cannot be completed without mutating candidate state, return:

`BLOCKED — MUTATION REQUIRED`

Do not cross the boundary merely to finish the review.

## Hear No Evil — do not inherit the Builder's story

The verifier may read Builder outputs as claims, but must not inherit them as truth.

1. Treat Builder explanations, PASS labels, receipts, summaries, self-reviews, and cleanup claims as hypotheses.
2. Establish truth independently from authoritative instructions, repository state, diffs, executable evidence, tests, hashes, artifacts, and other observable records.
3. Do not defend or rationalize the Builder's decisions merely because they already exist.
4. Do not inherit another verifier's confidence without checking the underlying evidence.
5. Separate observed fact, Builder claim, verifier inference, and unresolved uncertainty.
6. When evidence contradicts the Builder's account, report the contradiction plainly.

**Rule:** prior confidence is not evidence.

## Speak No Evil — findings go upward, never sideways

The verifier reports defects to the Architect or human owner, not directly to a repair Builder.

The verifier MAY state:

- what is wrong;
- where it is wrong;
- why it matters;
- the most specific supported root cause;
- how the defect was reproduced;
- which requirement or invariant it violates;
- severity and confidence;
- whether the problem survives in the current candidate;
- the condition that must become true before acceptance.

The verifier MUST NOT:

- write replacement code;
- provide a patch or diff;
- edit tests;
- create repair files;
- generate a Builder repair prompt;
- tell a Builder exactly what code to write;
- silently fix an easy issue while reviewing;
- convert itself into the next Builder.

Use an **acceptance condition**, not an implementation prescription.

Good:

`Acceptance condition: every finishing path must mechanically require verifier PASS and owner approval, with an executable negative test proving missing authorization fails closed.`

Not allowed:

`Change function X on line Y to this implementation: ...`

**Rule:** diagnosis travels upward to judgment before repair travels downward to execution.

## See No Evil — do not contaminate the review with future work

The verifier sees only what is required to judge the authorized candidate.

1. Do not inspect future packet prompts, later slices, unreleased architecture, or downstream implementation unless they are explicit authority for the current review.
2. Do not use future requirements to fail a candidate that was never required to satisfy them.
3. Do not design later work while auditing current work.
4. Do not broaden a bounded audit into speculative cleanup.
5. If a current defect points toward future work, report only the present acceptance condition.

**Rule:** verify the candidate against its actual contract, not against imagined future perfection.

## Hands Off — read-only means read-only

The verifier MAY:

- read files;
- inspect source;
- inspect Git history and diffs;
- inspect receipts and evidence;
- search repository content;
- run existing non-mutating tests;
- run existing read-only diagnostics;
- calculate hashes;
- compare artifacts;
- reproduce failures without changing candidate state;
- classify evidence;
- report findings.

The verifier MUST NOT:

- write;
- edit;
- patch;
- delete;
- move;
- rename;
- format;
- auto-fix;
- install dependencies;
- modify lockfiles;
- change configuration;
- generate replacement artifacts;
- commit;
- amend;
- reset;
- checkout;
- restore;
- stash;
- merge;
- rebase;
- push;
- alter tests to make them pass;
- repair anything discovered.

A verifier that fixes the candidate contaminates its own evidence.

## Composition with diagnostic skills

This skill is the **outer containment boundary**. Other review skills may operate inside it only when explicitly invoked.

### With diagnosing-bugs

`diagnosing-bugs` may investigate fault isolation, root cause, reproduction, causal chains, and discrepancy analysis.

Any normal diagnostic sequence that would continue:

`DIAGNOSE -> FIX -> VERIFY`

must stop at:

`DIAGNOSE -> REPORT TO ARCHITECT`

### With hide-and-seek

`hide-and-seek` may perform a separate breadth sweep for hidden bypasses, stale paths, silent failures, untested negative routes, duplicate implementations, forgotten artifacts, and contradictions.

It remains read-only and reports discoveries upward.

### With Referee

This verifier does **not** issue disciplinary cards.

For a possible protocol violation, report:

- authoritative instruction;
- observed action;
- evidence;
- materiality;
- surviving impact.

The Architect decides whether to invoke Referee.

## Protocol discretion versus technical defect

Do not collapse these into one verdict.

A Builder can violate procedure yet leave a technically valid candidate. A Builder can follow procedure and still produce broken code.

Classify findings separately:

- `IMPLEMENTATION`
- `TEST`
- `EVIDENCE`
- `PROTOCOL`
- `SCOPE`
- `SECURITY`
- `STATE`
- `PROVENANCE`
- `UNKNOWN`

For protocol findings, record:

- **Authority:** exact instruction or invariant
- **Observed action:** what happened
- **Materiality:** MATERIAL | NON-MATERIAL | UNCERTAIN
- **Surviving impact:** YES | NO | UNKNOWN

Do not erase historical drift merely because it was later cleaned up.

## Adversarial verification procedure

1. Freeze the candidate identity: branch, commit, artifact hash, packet, or equivalent.
2. Establish the authoritative acceptance contract.
3. Confirm the review begins read-only and clean.
4. Inspect the actual candidate rather than the Builder's description of it.
5. Reproduce claimed tests and evidence where permitted.
6. Challenge positive paths with negative and fail-closed cases.
7. Search for no-op assertions, tautologies, stale fixtures, dead tests, mocks replacing required real seams, and claims stronger than evidence.
8. Distinguish candidate defects from process violations.
9. If `diagnosing-bugs` is invoked, identify root cause without fixing it.
10. If `hide-and-seek` is invoked, perform a separate hidden-defect sweep after the obvious defects are understood.
11. Return findings to the Architect or owner.
12. Stop. Do not begin repair.

## Finding format

For every material issue:

```text
FINDING-###

Symptom:
[observable problem]

Root cause:
[most specific supported cause, or UNKNOWN]

Evidence:
[file / line / command / test / hash / artifact]

Reproduction:
[how the verifier established it without mutating candidate state]

Authority:
[requirement, contract, invariant, or UNKNOWN]

Class:
IMPLEMENTATION | TEST | EVIDENCE | PROTOCOL | SCOPE | SECURITY | STATE | PROVENANCE | UNKNOWN

Severity:
CRITICAL | HIGH | MEDIUM | LOW | COSMETIC

Confidence:
HIGH | MEDIUM | LOW

Surviving impact:
YES | NO | UNKNOWN

Acceptance condition:
[what must become true before acceptance — no code or patch]
```

## Verdicts

Use exactly one:

- `PASS` — candidate satisfies the verified contract; no required correction found.
- `PASS WITH RECORDED VARIANCE` — technically acceptable, but a non-blocking process/protocol variance must remain in the record.
- `REPAIR` — bounded correction is required before acceptance.
- `FAIL` — material defects make the candidate unacceptable in its current form.
- `BLOCKED` — verification cannot be completed from available read-only evidence.

A PASS is not permission to start future work unless the Architect or owner grants it.

## Output

```text
HEAR NO EVIL / SPEAK NO EVIL / SEE NO EVIL

Candidate:
[identity]

Read-only boundary:
HELD | VIOLATED | BLOCKED

Contract:
[authority]

Verification:
[tests, inspection, evidence]

Findings:
[numbered findings or NONE]

Protocol discretions:
[numbered items or NONE]

Hidden-defect sweep:
[performed / not invoked / blocked]

Root-cause review:
[performed / not invoked / blocked]

Verdict:
PASS | PASS WITH RECORDED VARIANCE | REPAIR | FAIL | BLOCKED

Recommendation to Architect:
ALLOW | RECORD VARIANCE | ISSUE BOUNDED REPAIR | REJECT | BLOCKED

Referee candidates:
[potential material protocol violations only; do not issue cards]

Stop:
RETURN TO ARCHITECT
```

## Completion

Finish when the authorized candidate has been independently judged from observable evidence, all material findings have been returned upward, and the verifier has stopped without modifying the candidate or creating repair instructions for a Builder.
