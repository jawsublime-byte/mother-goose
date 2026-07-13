# Mother Goose

Old stories for recurring builder problems.

Nursery rhymes and familiar tales survive because each one compresses a lesson into a pattern people remember. Mother Goose applies that same advantage to AI building: a failed repair becomes Humpty Dumpty, escalating resilience becomes the Three Little Pigs, and an over- or under-sized setting becomes Goldilocks.

The stories are memorable. The procedures are exact.

## Router

Mother Goose selects one story whose lesson matches the current problem. It does not run every skill or blend their procedures.

Example:

    $mother-goose route this repair that has failed three times

## Skill catalog

| Skill | Story rule | Builder problem | Enforced behavior |
| --- | --- | --- | --- |
| [Mother Goose](skills/mother-goose/) | Choose the tale with the matching lesson | Unclear method | Route to exactly one story-based skill |
| [Ring Around the Rosie](skills/ring-around-the-rosie/) | One falls each round | Weak options and excess code | Eliminate exactly one weakest candidate per round |
| [Humpty Dumpty](skills/humpty-dumpty/) | Stop trying to rebuild the same broken egg | Repeated failed repairs | Preserve requirements and replace the failed strategy |
| [Hickory Dickory Dock](skills/hickory-dickory-dock/) | The clock controls the stop | Unhealthy long sessions | Checkpoint at one hour and require a five-minute break |
| [Three Little Pigs](skills/three-little-pigs/) | Straw, sticks, then bricks | Untested resilience | Test three escalating failure or threat levels |
| [Goldilocks](skills/goldilocks/) | Too much, too little, just right | Bad configuration balance | Calculate the median or justify the bounded middle choice |

## Use

Codex uses dollar mentions:

    $three-little-pigs test this upload pipeline at straw, sticks, and bricks levels

ChatGPT supports at-mentions when the skill is installed:

    @three-little-pigs test this upload pipeline at straw, sticks, and bricks levels

The skills are explicit-invocation only. A story should not silently change an ordinary task.

## Install

### Codex: repository scope

PowerShell:

    New-Item -ItemType Directory -Force .agents\skills | Out-Null
    Copy-Item -Recurse .\skills\mother-goose .agents\skills\mother-goose

Bash:

    mkdir -p .agents/skills
    cp -R skills/mother-goose .agents/skills/mother-goose

To install the complete collection, copy every folder under skills into .agents/skills.

### Codex: user scope

Copy selected folders into HOME/.agents/skills to make them available across repositories.

### Other Agent Skills-compatible builders

Each folder is self-contained. Copy the selected skill folder into the builder's configured skills directory. Tools that do not scan skills can use SKILL.md as a system or project instruction.

The repository also contains a Codex plugin manifest so the complete collection can be distributed as one plugin bundle.

## Boundaries

- Humpty Dumpty changes strategy, not requirements.
- Ring Around the Rosie never removes an option without a stated criterion and evidence.
- Goldilocks distinguishes a mathematical median from a subjective compromise.
- Hickory Dickory Dock does not pretend to monitor time when the host supplies no clock or continuing session.
- Three Little Pigs remains inside authorized, non-destructive test scope.

All skills yield to higher-level safety rules, repository policy, permission limits, and explicit approval gates.

## Validate

Run:

    python scripts/validate_repo.py

## Contributing

Read CONTRIBUTING.md before proposing a rhyme or tale. The moral must translate naturally into one repeated builder problem and a testable procedure.

## License

MIT. See LICENSE.

The names in this collection refer to traditional stories and nursery rhymes in the public cultural tradition.
