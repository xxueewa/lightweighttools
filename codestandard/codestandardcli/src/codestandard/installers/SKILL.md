---
name: code-standard-skill
description: Use when the user asks to generate code, review code, 
  or enforce a code standard, coding guideline, lint policy or code style check across a project.
---

# Available Standards
- `java-alibaba-rules`
- `java-google-rules`
- `python-pep8-rule`
- `typeScript-react-standard`

# Code Standard Router
Use this skill to select the correct code-standard skill

## Routing Order
All the rules exists in `./reference` folder
1. If the user explicitly mentioned a standard, use that standard.
2. If the repo is Java and no other signal exists, ask the use whether to use the `java-alibaba-rules` or `java-google-rules`.
3. If the repo is Python and no other signal exists, ask the use whether to use the `python-pep8-rule`  or not.
4. If the repo is TypeScript and no other signal exists, ask the use whether to use `typeScript-react-standard` or not.

# How to Apply the Standards

## Workflow

Follow the rules in the Markdown file.

When editing the files:
1. Apply mandatory rules first.
2. Apply recommended rules when safe and ask users for permission.
3. Mention reference rules only when useful.

# Reminders
- Always check the relevant standard before writing or reviewing code.
- Do NOT mix conventions from different standards in the same file.
- If a standard is missing for the language in question, fall back to widely-accepted community conventions and note the gap to the user.
- Code Standard files are plain Markdown — read them with `cat` or `Read`.

## Conflict Rules
- Project-local config wins over global defaults.
- User instruction wins over inferred config.
- Existing repo style wins when the written standard is silent.
- If two standards conflict, state the conflict and ask before making broad edits.