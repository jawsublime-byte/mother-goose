# Contributing

A memorable title is not enough. Each contribution must turn a familiar lesson into a predictable builder procedure.

## A valid new skill

A proposal must provide:

1. A traditional rhyme, tale, or fable with a recognizable lesson.
2. One recurring builder problem that naturally matches that lesson.
3. A bounded process with a checkable completion condition.
4. Clear stop, safety, and approval conditions.
5. One realistic trigger case and one case that must not trigger.

Do not duplicate an existing skill under a different story. Do not add tooling or references unless the skill needs them to complete its one job.

## Pull request checklist

- The folder name matches the frontmatter name.
- SKILL.md contains only name and description in its YAML frontmatter.
- agents/openai.yaml contains a default prompt that names the skill.
- evals/cases.json covers the skill.
- README.md explains the lesson-to-problem mapping.
- python scripts/validate_repo.py passes.

By contributing, you agree that your contribution is licensed under the MIT License.
