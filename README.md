<p align="center">
  <img src="assets/mother-goose-hero.jpg" alt="Mother Goose sleeps while familiar nursery-tale disasters unfold around her" width="100%">
</p>

# Mother Goose

**Old stories for recurring builder problems.**

Nursery rhymes and familiar tales survive because each one compresses a lesson into a pattern people remember. Mother Goose applies that same advantage to AI building: a failed repair becomes Humpty Dumpty, escalating resilience becomes the Three Little Pigs, and an over- or under-sized setting becomes Goldilocks.

The stories are memorable. The procedures are exact.

> **Companion collection:** Mother Goose and [Simon Says](https://github.com/jawsublime-byte/simon-says) belong together. Mother Goose handles recurring repair, verification, evidence, automation, provenance, resilience, elimination, timing, and balance problems. Simon Says focuses more heavily on execution control, scope, investigation, testing, and keeping the agent aligned with the user's actual directive. If one collection is useful to you, I recommend cloning the other too.

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
- continue working long enough that context quality and human attention both degraded;
- inherit another agent's PASS without independently proving it;
- make confident completion claims whose evidence was much weaker than the wording;
- keep retrying the same failure under the same conditions;
- optimize a working component until the behavior that made it valuable disappeared;
- lose track of who actually built, supplied, tested, or verified a result.

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

Because "someone should challenge this" is vague.

**The Emperor's New Clothes** is not vague: when consensus, rank, prior approval, or yes-man behavior may be suppressing an uncomfortable truth, create a protected dissenting review and require somebody to say plainly when the emperor is naked.

Because "stop patching patches" is vague.

**The Old Lady Who Swallowed a Fly** is not vague: reconstruct the workaround chain and go back to the earliest verified cause before adding another animal.

Because "show me proof" is vague.

**Pinocchio** is not vague: every material claim gets an evidence class and an explicit verdict.

Because "verify this independently" is vague.

**Hear No Evil, Speak No Evil, See No Evil** is not vague: the verifier may investigate, reproduce, diagnose, and challenge, but cannot inherit the Builder's story as truth, cannot inspect unauthorized future work, cannot repair the candidate, and cannot send fixes directly to the Builder. Findings go upward to the Architect.

These are the same kinds of stories that helped teach us judgment, restraint, honesty, persistence, and consequences as children. The surprising part is how naturally those morals translate into modern AI guardrails. The childhood story makes the behavior easy to remember. The skill file makes the behavior testable.

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
| [The Emperor's New Clothes](skills/emperor-new-clothes/) | If the emperor is naked, say so | Groupthink, sycophancy, authority bias, yes-men | Give dissent a protected evidence-based voice and state uncomfortable contradictions plainly |
| [Old Lady Who Swallowed a Fly](skills/old-lady-swallowed-fly/) | Do not swallow a bigger fix to solve the last fix | Cascading workarounds | Trace the repair chain to the earliest verified cause |
| [The Sorcerer's Apprentice](skills/sorcerers-apprentice/) | Do not start what you cannot stop | Unbounded automation | Require scope, budgets, stop conditions, override, and cleanup |
| [Pinocchio](skills/pinocchio/) | A claim without evidence stays a story | Unsupported completion claims | Attach evidence to every material claim or label it unsupported |
| [Hear No Evil, Speak No Evil, See No Evil](skills/hear-no-evil-speak-no-evil-see-no-evil/) | A verifier gets eyes, ears, and a voice — but no hands | Verifier contamination and self-repair | Keep independent verification read-only and return findings only to the Architect |
| [The Boy Who Cried Wolf](skills/boy-who-cried-wolf/) | Do not make every rustle a wolf | Alert fatigue and false alarms | Separate new critical evidence from duplicates and unsupported warnings |
| [The Goose That Laid the Golden Eggs](skills/goose-golden-eggs/) | Do not destroy the source of proven value | Refactor and optimization regression | Baseline valuable behavior and require it to survive the change |
| [Five Little Monkeys](skills/five-little-monkeys/) | Stop jumping after the same fall repeats | Blind retry loops | Stop identical retries after the failure budget is exhausted |
| [Hansel and Gretel](skills/hansel-and-gretel/) | Leave breadcrumbs so you can get home | Lost context and build history | Record concise recoverable checkpoints through long work |
| [The Tortoise and the Hare](skills/tortoise-and-hare/) | Reach the finish line before boasting about speed | Rushed incomplete builds | Rank verified completion before speed or cost |
| [The Little Red Hen](skills/little-red-hen/) | Who actually did the work? | Ambiguous provenance and credit | Trace work, evidence, and verification to the actual actor or source |

<p align="center">
  <img src="assets/mother-goose-resilience.jpg" alt="The Three Little Pigs face an approaching wolf beneath a midnight clock" width="76%">
</p>

## The bigger idea

AI models are capable of doing excellent work. The problem is that capability is not the same thing as judgment, authority, evidence, or memory.

A model can make a locally sensible decision that is globally wrong for the project. It can confidently repeat a repair that has already failed. It can interpret "make this robust" as permission to overbuild. It can preserve five mediocre alternatives because each one sounds defensible in isolation. It can inherit another agent's confidence, call a partial result complete, or optimize away the exact behavior you cared about.

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

## Add new skills without reinstalling the collection

After you have `scripts/update_skills.py` once, future additions can be pulled directly from this public GitHub repository without downloading or reinstalling every existing skill.

Check what is missing:

    python scripts/update_skills.py --host codex --scope user

Install **only** new skill folders that are not already present:

    python scripts/update_skills.py --host codex --scope user --install-new

When new add-ons are installed, the updater also refreshes the small `mother-goose` router so it knows the newly added stories. Existing non-router skills are left untouched.

If a specific existing skill receives an improved definition, refresh only that skill:

    python scripts/update_skills.py --host codex --scope user --refresh emperor-new-clothes

Claude Code uses the same commands with `--host claude-code`. Custom hosts can use `--host custom --destination PATH_TO_SKILLS`.

The updater uses only Python's standard library. It checks the GitHub `skills/` directory, compares it with the installed destination, downloads only missing or explicitly refreshed skill folders, and refuses to overwrite other installed skills. Set `GITHUB_TOKEN` only if you need a higher GitHub API rate limit; no token is required for normal public-repository use.

## Boundaries

- Humpty Dumpty changes strategy, not requirements.
- Ring Around the Rosie never removes an option without a stated criterion and evidence.
- Goldilocks distinguishes a mathematical median from a subjective compromise.
- Hickory Dickory Dock does not pretend to monitor time when the host supplies no clock or continuing session.
- Three Little Pigs remains inside authorized, non-destructive test scope.
- The Emperor's New Clothes protects truthful dissent without manufacturing disagreement or seizing decision authority from the owner.
- The Old Lady does not remove compensating changes without checking what behavior they currently protect.
- The Sorcerer's Apprentice never invents continuous monitoring, persistence, or a kill switch the host does not actually provide.
- Pinocchio checks observable claims and receipts, not private chain-of-thought.
- Hear No Evil, Speak No Evil, See No Evil allows deep inspection and diagnosis but never lets the verifier mutate the candidate, write repair code, inspect unauthorized future work, or bypass the Architect by directing fixes straight to a Builder.
- The Boy Who Cried Wolf never hides fresh critical evidence merely because earlier alerts were noisy.
- The Goose That Laid the Golden Eggs requires a real baseline before claiming an optimization preserved value.
- Five Little Monkeys counts only reproduced failures under materially unchanged conditions.
- Hansel and Gretel records operational breadcrumbs, not secrets or hidden reasoning.
- The Tortoise and the Hare compares runners against the same finish line before comparing speed.
- The Little Red Hen never invents provenance or credit where the record is unknown.

All skills yield to higher-level safety rules, repository policy, permission limits, and explicit approval gates.

## Free on purpose

These skills are free and open source because I built them to solve problems I was having as a solo builder.

A lot of excellent open-source work has helped me get this far. I want these repositories to do the same thing for somebody else.

There is no paywall waiting behind the collection. Use the skills, fork them, adapt them, or improve them.

## Did one of these help—or fail?

I would like to know.

If Humpty Dumpty finally broke a bad repair loop, the Emperor broke through a yes-man consensus, Pinocchio caught an unsupported completion claim, Hansel and Gretel helped you recover a long build, Three Little Pigs exposed a weak boundary, or another skill proved useful, [open an issue and tell me what happened](https://github.com/jawsublime-byte/mother-goose/issues/new).

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
