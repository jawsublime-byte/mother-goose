---
name: pinocchio
description: Audit concrete build, test, compatibility, performance, and completion claims against available evidence. Use only when explicitly invoked to separate verified statements from unsupported or contradicted claims.
---

# Pinocchio

A claim without evidence stays a story.

## Claim ledger

1. Extract the concrete claims that matter to acceptance, such as tests passed, requirements completed, no regressions, compatibility preserved, performance improved, or files unchanged.
2. For each claim, identify the strongest available evidence source.
3. Distinguish fresh executed evidence from inspected artifacts, user-supplied evidence, inherited summaries, and unsupported assertion.
4. Re-run a check only when execution is authorized and useful.
5. Classify each claim as VERIFIED, SUPPORTED, UNSUPPORTED, CONTRADICTED, BLOCKED, or UNKNOWN.
6. Never convert absence of evidence into evidence of absence.

Do not expose or demand hidden chain-of-thought. This skill checks observable claims and operational evidence only.

## Output

PINOCCHIO LEDGER
Claim: [statement]
Evidence class: fresh | inspected | supplied | inherited | none
Evidence: [source]
Verdict: VERIFIED | SUPPORTED | UNSUPPORTED | CONTRADICTED | BLOCKED | UNKNOWN

Repeat for every material claim, then report an overall confidence summary without averaging away contradictions.

## Completion

Finish when every material claim has an evidence class and explicit verdict.