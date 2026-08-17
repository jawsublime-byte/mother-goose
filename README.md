<p align="center">
  <img src="assets/mother-goose-hero.jpg" alt="Mother Goose sleeps while familiar nursery-tale disasters unfold around her" width="100%">
</p>

# Mother Goose

**Old stories for recurring builder problems.**

Nursery rhymes and familiar tales survive because each one compresses a lesson into a pattern people remember. Mother Goose applies that same advantage to AI building: a failed repair becomes Humpty Dumpty, escalating resilience becomes the Three Little Pigs, and an over- or under-sized setting becomes Goldilocks.

The stories are memorable. The procedures are exact.

> **Companion collection:** Mother Goose and [Simon Says](https://github.com/jawsublime-byte/simon-says) belong together. Mother Goose handles recurring repair, resilience, elimination, timing, and balance problems. Simon Says focuses more heavily on execution control, scope, investigation, testing, and keeping the agent aligned with the user's actual directive. If one collection is useful to you, I recommend cloning the other too.

## Why I built this

I'm Joe. I'm an online English teacher and a solo builder who started making these skills because the AI tools I was using kept creating problems I did not have a clean way to control.

A couple of months ago I believed I was approaching the end of a project I had spent close to a year building. Then I looked more carefully at what was actually underneath it.

From a distance everything looked reassuring: code, folders, tests, documentation, manifests, polished explanations. Up close, whole pieces had quietly changed shape. Complete implementations had become partial ones. Working behavior had been replaced by scaffolding or abstractions. Some things had simply disappeared. The project looked finished in the same way a condemned building can look fine from the street.

I eventually had to admit that continuing to patch it was worse than starting again.

That was painful, but it also gave me something useful: a year of evidence about how AI-assisted builds fail in practice.

I had seen models:

- repeat a repair strategy long after it was obvious the strategy was wrong;
- add resilience only after the first real failure exposed the weakness;
- choose an extreme configuration because it sounded more impressive;
- carry too many weak options forward instead of eliminating one cleanly;
- continue working long enough that context quality and human attention both degraded.

Those were not random annoyances anymore. They were recurring patterns.

So I started naming them and turning them into explicit procedures.

That became Mother Goose.

## Why stories?

Because "try another approach" is vague.

**Humpty Dumpty** is not vague: if the same repair strategy has failed repeatedly, preserve the requirements and replace the failed strategy.

Because "test it more thoroughly" is vague.

**Three Little Pigs** is not vague: test escalating levels—straw, sticks, then bricks—and make the system prove what it survives.

Because "pick something reasonable" is vague.

**Goldilocks** is not vague: identify too much, too little, and the bounded middle choice, and justify why the middle is appropriate.

The childhood story makes the behavior easy to remember. The skill file makes the behavior testable.

That combination turned out to be surprisingly useful in real builds.

## Router

Mother Goose selects one story whose lesson matches the current problem. It does not run every skill or blend their procedures.

Example:

    $mother-goose route this repair that has failed three times

<p align="center">
  <img src="assets/mother-goose-repair.jpg" alt="Humpty Dumpty falls above old Humpty grave markers while children circle nearby" width="80%">
</p>

## Skill catalog

| Skill | Story rule | Builder problem | Enforced behavior |
| --- | --- | --- | --- |
| [Mother Goose](skills/mother-goose/) | Choose the tale with the matching lesson | Unclear method | Route to exactly one story-based skill |
| [Ring Around the Rosie](skills/ring-around-the-rosie/) | One falls each round | Weak options and excess code | Eliminate exactly one weakest candidate per round |
| [Humpty Dumpty](skills/humpty-dumpty/) | Stop trying to rebuild the same broken egg | Repeated failed repairs | Preserve requirements and replace the failed strategy |
| [Hickory Dickory Dock](skills/hickory-dickory-dock/) | The clock controls the stop | Unhealthy long sessions | Checkpoint at one hour and require a five-minute break |
| [Three Little Pigs](skills/three-little-pigs/) | Straw, sticks, then bricks | Untested resilience | Test three escalating failure or threat levels |
| [Goldilocks](skills/goldilocks/) | Too much, too little, just right | Bad configuration balance | Calculate the median or justify the bounded middle choice |

<p align="center">
  <img src="assets/mother-goose-resilience.jpg" alt="The Three Little Pigs face an approaching wolf beneath a midnight clock" width="76%">
</p>

## The bigger idea

AI models are capable of doing excellent work. The problem is that capability is not the same thing as judgment, authority, or memory.

A model can make a locally sensible decision that is globally wrong for the project. It can confidently repeat a repair that has already failed. It can interpret "make this robust" as permission to overbuild. It can preserve five mediocre alternatives because each one sounds defensible in isolation.

I do not think the solution is to tell the model to "be smarter."

I think the solution is to give recurring failure modes explicit controls.

Mother Goose is one small part of that approach. [Simon Says](https://github.com/jawsublime-byte/simon-says) handles another part: scope, alignment, hidden defects, black-box testing, simplicity, controlled experiments, and other execution problems.

The two repositories are separate because the mental models are different. They are not unrelated projects.

## Use

Codex uses dollar mentions:

    $three-little-pigs test this upload pipeline at straw, sticks, and bricks levels

ChatGPT supports at-mentions when the skill is installed:

    @three-little-pigs test this upload pipeline at straw, sticks, and bricks levels

The skills are explicit-invocation only. A story should not silently change an ordinary task.

## Install

Skills install into the host application, not into GPT, Claude, or DeepSeek model weights.

The no-dependency installer works on Windows, macOS, and Linux.

Install the complete collection for every Codex project:

    python scripts/install.py --host codex --scope user

Install only the router:

    python scripts/install.py --host codex --scope user --skill mother-goose

Install into one Codex project:

    python scripts/install.py --host codex --scope project --project PATH_TO_PROJECT

Install for every Claude Code project:

    python scripts/install.py --host claude-code --scope user

Use a DeepSeek-powered or other Agent Skills-compatible host by naming the folder it scans:

    python scripts/install.py --host custom --destination PATH_TO_SKILLS

Add `--dry-run` to preview the copy. Existing skill folders are protected unless `--force` is explicit. Run `python scripts/install.py --list` to see the names available for selective installation.

Codex users can also ask `$skill-installer` to install skills from `https://github.com/jawsublime-byte/mother-goose`.

The included `.codex-plugin/plugin.json` packages the complete collection for ChatGPT Work, the ChatGPT desktop app, and Codex plugin distribution. A local filesystem installer cannot inject a plugin into hosted ChatGPT; use that product's plugin installation flow after publication.

## Boundaries

- Humpty Dumpty changes strategy, not requirements.
- Ring Around the Rosie never removes an option without a stated criterion and evidence.
- Goldilocks distinguishes a mathematical median from a subjective compromise.
- Hickory Dickory Dock does not pretend to monitor time when the host supplies no clock or continuing session.
- Three Little Pigs remains inside authorized, non-destructive test scope.

All skills yield to higher-level safety rules, repository policy, permission limits, and explicit approval gates.

## Free on purpose

These skills are free and open source because I built them to solve problems I was having as a solo builder.

A lot of excellent open-source work has helped me get this far. I want these repositories to do the same thing for somebody else.

There is no paywall waiting behind the collection. Use the skills, fork them, adapt them, or improve them.

## Did one of these help—or fail?

I would like to know.

If Humpty Dumpty finally broke a bad repair loop, Three Little Pigs exposed a weak boundary, Goldilocks helped you stop over-sizing something, or another skill proved useful, [open an issue and tell me what happened](https://github.com/jawsublime-byte/mother-goose/issues/new).

A few details are enough:

- which skill you used;
- what model or host you used;
- what problem you were trying to solve;
- what happened;
- what you would change about the skill.

Failures are welcome too. If the rule was unclear or the skill made the workflow worse, that is exactly the kind of thing I want to find out.

If the collection earns a place in your workflow, **please star the repository**. It helps other builders find it and lets me know the work is being used outside my own projects.

<p align="center">
  <img src="assets/mother-goose-balance.jpg" alt="Goldilocks is discovered at the table by the Three Bears" width="76%">
</p>

## Validate

Run:

    python scripts/validate_repo.py

## Contributing

Read CONTRIBUTING.md before proposing a rhyme or tale. The moral must translate naturally into one repeated builder problem and a testable procedure.

I am also interested in recurring AI-builder problems that do not have a story yet. Most of these skills started with some version of: "Why does this keep happening?"

## From the builder

I'm Joe, an online English teacher who became a very determined AI-assisted builder.

I do not have a company engineering department behind these repositories. I have projects I care about, limited resources, a lot of persistence, and a growing collection of lessons learned the hard way.

Some open-source repositories have saved me enormous amounts of time. These are my attempt to return some of that value.

Related work:

- **[Simon Says](https://github.com/jawsublime-byte/simon-says)** — companion skills for execution control, alignment, investigation, testing, simplicity, and other recurring agent problems.
- **Echoes** — local-first archive archaeology, project reconstruction, and timeline recovery.
- **The MCP Workshop Manual** — a field-repair reference for diagnosing and repairing MCP infrastructure.

The public skills will remain free and open source. The bigger tools I am building came from discovering what was still missing after using these controls in real projects.

## License

MIT. See LICENSE.

See [NOTICE.md](NOTICE.md) for the independent-project and third-party mark notice.
