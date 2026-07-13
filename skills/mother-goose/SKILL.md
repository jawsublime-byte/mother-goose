---
name: mother-goose
description: Route a user-described builder problem to exactly one bundled nursery-rhyme or story-based skill. Use only when the user explicitly invokes Mother Goose and asks for routing. Do not execute every story or silently activate during ordinary work.
---

# Mother Goose

Choose the tale whose lesson matches the problem. One problem receives one leading story.

## Route

1. Identify the repeated failure pattern, not merely the topic.
2. Select exactly one:
   - ring-around-the-rosie: remove one weakest option or unnecessary element per round;
   - humpty-dumpty: stop repeating a repair strategy after its failure budget is exhausted;
   - hickory-dickory-dock: checkpoint work and enforce a five-minute break at one hour;
   - three-little-pigs: test resilience at straw, sticks, and bricks levels;
   - goldilocks: calculate or justify the bounded middle setting.
3. Explain the lesson-to-problem match in one sentence.
4. Do not execute the routed skill unless the user requested execution or confirms the route.

Output:

MOTHER GOOSE CHOOSES: [skill]
Lesson: [one sentence]
Why it fits: [one sentence]

If no story fits, say so. Never force a metaphor or invent a new skill during routing.

## Completion

Finish when one justified route or a clear no-match result is delivered.
