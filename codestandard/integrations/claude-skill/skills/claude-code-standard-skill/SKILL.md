---
name: code-standard-router
description: Use when the user asks to generate code, review code, 
  or enforce a code standard, coding guideline, lint policy or code style check across a project.
---

# Code Standard Router

Use this skill to select the correct code-standard skill

## Routing Order

1. If the user explicitly select a standard, use that standard.
2. If the repo is Java and no other signal exists, ask the use whether to use the `java-alibaba-standard` or not.
3. If the repo is Python and no other signal exists, ask the use whether to use the `python-standard`  or not.
4. If the repo is TypeScript and no other signal exists, ask the use whether to use `TypeScript-standard` or not.

## Skill Map

- Alibaba Java handbook: `java-alibaba-standard`
- Google Java Style: `java-google-standard`
- React TypeScript frontend: `typescript-react-standard`
- Python PEP 8: `python-pep8-standard`

## Conflict Rules
- Project-local config wins over global defaults.
- User instruction wins over inferred config.
- Existing repo style wins when the written standard is silent.
- If two standards conflict, state the conflict and ask before making broad edits.