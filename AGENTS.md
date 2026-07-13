# Repository Rules

- Keep each skill focused on one repeatable builder problem.
- Preserve the story's lesson as the skill's leading execution metaphor.
- Use imperative instructions and checkable completion criteria.
- Keep invocation descriptions concise and explicit.
- Require approval before destructive, irreversible, production, dependency, database, credential, or external-system changes.
- Keep resilience tests defensive and inside user-authorized scope.
- Add one trigger and one non-trigger case to evals/cases.json for every skill.
- Add no dependency when the Python standard library can validate the repository.
- Run python scripts/validate_repo.py before claiming completion.
