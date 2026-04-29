"""
Claude Skill Installer
======================
Installs code style standards as a reusable Claude Code skill.

Output layout (all under ~/.claude/skills/codestandardskill/):

  SKILL.md                              ← skill entry point; loaded when triggered
  java-code-standard/                   ← copied verbatim from reference/
      style.md
      ...
  python-code-standard/
      style.md
      ...
  ts-code-standard/
      ...

How it works at runtime:
  Claude Code discovers the skill via SKILL.md's `description` field.
  When the user asks about code style / review, Claude reads SKILL.md
  which instructs it to load the relevant standard subfolder.

Pre-flight check:
  ~/.claude/skills/ MUST exist.  If it doesn't, Claude Code is not
  installed — we fail fast with a clear remediation message.

References:
  https://code.claude.com/docs/en/memory (skills section)
"""

from __future__ import annotations

import shutil
import sys
from datetime import date
from pathlib import Path
from typing import List

from .base import BaseInstaller

SKILL_NAME = "codestandardskill"

# Maps a keyword found in the standard folder name → human language label
# used in the SKILL.md trigger description.
LANG_LABELS: dict[str, str] = {
    "java":       "Java",
    "python":     "Python",
    "typescript": "TypeScript",
    "ts":         "TypeScript",
    "javascript": "JavaScript",
    "js":         "JavaScript",
    "go":         "Go",
    "rust":       "Rust",
    "kotlin":     "Kotlin",
    "swift":      "Swift",
    "ruby":       "Ruby",
    "php":        "PHP",
    "css":        "CSS/SCSS",
    "html":       "HTML",
    "sql":        "SQL",
    "shell":      "Shell/Bash",
}


class ClaudeSkillInstaller(BaseInstaller):
    """
    Installs code standards as a Claude Code skill under ~/.claude/skills/.

    this installer targets the GLOBAL skills directory, so the skill is
    available across ALL projects on this machine.
    """

    # Override default target: skills always live in ~/.claude
    DEFAULT_TARGET = Path.home() / ".claude"

    def __init__(self, source: Path, target: Path, dry_run: bool, overwrite: bool) -> None:
        # If the user didn't override --target, use ~/.claude
        if target == Path(".").resolve():
            target = self.DEFAULT_TARGET
        super().__init__(source, target, dry_run, overwrite)

    # ------------------------------------------------------------------
    # Pre-flight: verify ~/.claude/skills/ exists
    # ------------------------------------------------------------------

    def run(self) -> None:
        """Entry point — pre-flight check first, then delegate to super."""
        self._preflight()
        super().run()

    def _preflight(self) -> None:
        skills_root = self.target / "skills"

        if self.dry_run:
            # In dry-run mode we just warn rather than abort
            if not skills_root.exists():
                print(f"  [DRY RUN / WARN] {skills_root} does not exist.")
                print("  In a real run this would abort. Install Claude Code first:")
                print("    https://docs.anthropic.com/en/docs/claude-code/overview\n")
            return

        if not skills_root.exists():
            print()
            print("  ✗  Pre-flight failed: Claude Code skills directory not found.")
            print()
            print(f"     Expected: {skills_root}")
            print()
            print("  Claude Code must be installed before running this installer.")
            print()
            print("  Install Claude Code:")
            print("    npm install -g @anthropic-ai/claude-code")
            print()
            print("  Then run `claude` once in any project to initialise ~/.claude/.")
            print()
            sys.exit(1)

        print(f"  ✓  Pre-flight passed — skills root found: {skills_root}")

    # ------------------------------------------------------------------
    # Build: generate file map
    # ------------------------------------------------------------------

    def build(self, standards: List[Path]) -> dict[str, str]:
        """
        Returns only the text files (SKILL.md).
        The actual standard directories are copied by _copy_standards(),
        which is called from run() after write.
        """
        today = date.today().isoformat()
        file_map: dict[str, str] = {
            f"skills/{SKILL_NAME}/SKILL.md": self._build_skill_md(standards, today),
        }
        return file_map

    # ------------------------------------------------------------------
    # Override run() to also copy the reference folders
    # ------------------------------------------------------------------

    def run(self) -> None:
        """Pre-flight → write SKILL.md → copy standard directories."""
        self._preflight()

        standards = self.discover_standards()
        if not standards:
            print(f"  [WARN] No standard folders found in {self.source}")
            return

        print(f"  Found {len(standards)} standard(s):")
        for s in standards:
            print(f"    • {s.name}")
        print()

        # 1. Write SKILL.md
        file_map = self.build(standards)
        for rel_path, content in file_map.items():
            self._write(rel_path, content)

        # 2. Copy each standard directory into the skill folder
        skill_dir = self.target / "skills" / SKILL_NAME
        self._copy_standards(standards, skill_dir)

        total = len(file_map) + len(standards)
        print(f"\n  ✓ Done — {total} item(s) processed.")

    def _copy_standards(self, standards: List[Path], skill_dir: Path) -> None:
        """Copy each reference/<standard>/ folder into the skill directory."""
        for std_dir in standards:
            dest = skill_dir / std_dir.name

            if self.dry_run:
                print(f"  [DRY RUN] Would copy dir → {dest}/")
                continue

            if dest.exists() and not self.overwrite:
                print(f"  [SKIP]    {dest}/  (already exists — use --overwrite to replace)")
                continue

            if dest.exists():
                shutil.rmtree(dest)

            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copytree(str(std_dir), str(dest))
            print(f"  [OK]      Copied  → {dest}/")

    # ------------------------------------------------------------------
    # SKILL.md builder
    # ------------------------------------------------------------------

    def _build_skill_md(self, standards: List[Path], today: str) -> str:
        std_names    = [s.name for s in standards]
        lang_labels  = [self._lang_label(s.name) for s in standards]

        # Trigger description — shown in Claude Code's skill panel
        trigger_langs = ", ".join(lang_labels) if lang_labels else "any language"
        trigger_desc  = (
            f"Use this skill when the user asks about code style, coding standards, "
            f"code review, or best practices for {trigger_langs}. "
            f"Also use when writing new code or reviewing a PR that touches "
            f"{trigger_langs} files."
        )

        # One reference block per standard
        ref_blocks = "\n\n".join(
            self._std_reference_block(s) for s in standards
        )

        # Instruction block: how Claude should apply the standards
        apply_instructions = self._apply_instructions(standards)

        return f"""\
---
name: "{SKILL_NAME}"
description: "{trigger_desc}"
generated: "{today}"
---

# Code Standard Skill

## Purpose

This skill gives Claude access to the team's official code style standards.
When invoked, Claude reads the relevant standard file(s) and applies them
to any code it writes, reviews, or refactors.

## Available Standards

{chr(10).join(f"- **{self._lang_label(n)}** → `{n}/`" for n in std_names)}

## How to Read the Standards

Each standard lives in a sub-folder next to this file.
Load the standard that matches the language you are working in:

{ref_blocks}

## How to Apply the Standards

{apply_instructions}

## Reminders

- Always check the relevant standard before writing or reviewing code.
- Do NOT mix conventions from different standards in the same file.
- If a standard is missing for the language in question, fall back to
  widely-accepted community conventions and note the gap to the user.
- Standards files are plain Markdown — read them with `cat` or `Read`.
"""

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------

    def _lang_label(self, folder_name: str) -> str:
        """Return a human-readable language name from a folder slug."""
        lower = folder_name.lower()
        for key, label in LANG_LABELS.items():
            if key in lower:
                return label
        # Fall back to title-casing the folder name
        return folder_name.replace("-", " ").replace("_", " ").title()

    def _std_reference_block(self, std_dir: Path) -> str:
        """Generate the load-instruction block for one standard."""
        label    = self._lang_label(std_dir.name)
        rel_path = f".claude/skills/{SKILL_NAME}/{std_dir.name}"

        # List the files inside the standard directory
        text_exts = {".md", ".txt", ".adoc", ".rst", ".markdown"}
        files = sorted(
            f for f in std_dir.rglob("*")
            if f.is_file() and f.suffix.lower() in text_exts
        )
        file_lines = "\n".join(
            f"  - `{rel_path}/{f.relative_to(std_dir)}`"
            for f in files
        ) or f"  - `{rel_path}/` _(no files found yet)_"

        return f"""\
### {label}

Standard folder: `{rel_path}/`

Files to read when working with {label}:
{file_lines}"""

    @staticmethod
    def _apply_instructions(standards: List[Path]) -> str:
        return """\
1. **Identify the language** of the file(s) you are working on.
2. **Read the matching standard file** listed in the section above using
   the `Read` tool or `cat`.  Do this before writing a single line of code.
3. **Apply every rule** from the standard unless the user explicitly
   overrides one.  Mention any deviation and why.
4. **On code review**, check each issue against the relevant standard and
   cite the rule name / section in your feedback.
5. **On refactoring**, surface any existing code that violates the standard
   as a separate finding so the user can decide whether to fix it."""

    # ------------------------------------------------------------------
    # Reload hint
    # ------------------------------------------------------------------

    def reload_hint(self) -> None:
        skill_path = self.target / "skills" / SKILL_NAME
        print("\n--- Claude Code Reload ---")
        print(f"  Skill installed at: {skill_path}")
        print()
        print("  The skill is available globally across all your projects.")
        print("  Start or restart Claude Code to activate it:")
        print()
        print("    claude")
        print()
        print("  To confirm the skill is loaded:")
        print()
        print("    /skills")
        print()
        print("  To invoke it manually in a session:")
        print()
        print(f"    use the {SKILL_NAME} skill to review this file")
        print()