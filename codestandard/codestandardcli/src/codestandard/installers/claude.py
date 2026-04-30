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


class ClaudeSkillInstaller(BaseInstaller):
    """
    Installs code standards as a Claude Code skill under ~/.claude/skills/.

    This installer targets the GLOBAL skills directory, so the skill is
    available across ALL projects on this machine.
    """

    # Override default target: skills always live in ~/.claude
    DEFAULT_TARGET = Path.home() / ".claude"

    def __init__(self, source: Path, target: Path, dry_run: bool, overwrite: bool) -> None:
        # If the user didn't override --target, use ~/.claude
        source = source.resolve()
        target = self.DEFAULT_TARGET
        super().__init__(source, target, dry_run, overwrite)

    # ------------------------------------------------------------------
    # Pre-flight: verify ~/.claude/skills/ exists
    # ------------------------------------------------------------------

    def _preflight(self) -> None:
        skills_root = self.target / "skills"

        if self.dry_run:
            # In dry-run mode we just warn rather than abort
            if not skills_root.exists():
                print(f"  [DRY RUN / WARN] {skills_root} does not exist.")
                print("  In a real run this would abort. Install Claude Code first:")
                print("    https://docs.anthropic.com/en/docs/claude-code/overview\n")
            else:
                print(f"  ✓ Pre-flight passed — skills root found: {skills_root}")
            return

        if not skills_root.exists():
            print()
            print("  ✗  Pre-flight failed: Claude Code skills directory not found.")
            print()
            print(f"     Expected: {skills_root}")
            print()
            print("  Claude Code must be installed before running this installers.")
            print()
            print("  Install Claude Code:")
            print("  https://code.claude.com/docs/en/quickstart ")
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
        return {}

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

        print(f"  ✓ Found {len(standards)} standard(s):")
        for s in standards:
            print(f"    • {s.name}")
        print()

        # TODO: 1. Update SKILL.md if customization enabled later

        # 2. Copy files
        skill_dir = self.target / "skills" / SKILL_NAME
        skill_file_dest = skill_dir / "SKILL.md"
        reference_dest_dir = skill_dir / "reference"

        if self.dry_run:
            if skill_dir.exists():
                print(f"  [WARN] {skill_dir} already exists.")
            print(f"  Would copy SKILL.md → {skill_file_dest}")
        else:
            self._create_skill(skill_dir)
            print(f"  Copying SKILL.md → {skill_file_dest}")
            Path(skill_file_dest).touch()
            shutil.copyfile(str(self.source / "installers/SKILL.md"), str(skill_file_dest))
            self._copy_standards(standards, reference_dest_dir)

        total = 1 + len(standards)
        print(f"\n  ✓ Done — {total} item(s) processed.")

    def _copy_standards(self, standards: List[Path], reference_dir: Path) -> None:
        """Copy each reference/<standard>/ folder into the skill directory."""
        Path(reference_dir).mkdir(parents=True, exist_ok=True)
        for file_path in standards:
            dest = reference_dir / file_path.name

            if self.dry_run:
                print(f"  [DRY RUN] Would copy {file_path} → {dest}/")
                continue

            if dest.exists():
                print(f"  [SKIP]    {dest}/  (already exists)")
                continue
            Path(dest).touch()
            shutil.copyfile(str(file_path), str(dest))
            print(f"  [OK]      Copied  → {dest}/")

    # ------------------------------------------------------------------
    # SKILL.md builder
    # ------------------------------------------------------------------
    def _create_skill(self, skill_dir: Path) -> None:
        """Create a new skill directory"""
        if skill_dir.exists():
            response = input(
                f" [WARN] {skill_dir} already exists. Do you want to proceed overwrite? [y/N]: ").lower().strip()
            if response in ("y", "yes"):
                print("Proceeding with overwrite.")
                shutil.rmtree(skill_dir)
            else:
                sys.exit(1)
        else:
            Path(skill_dir).mkdir(parents=True, exist_ok=True)
            print(f"  creating new folder for {SKILL_NAME}. ")

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
        print(f"    /{SKILL_NAME}")
        print()
        print("  To invoke it manually in a session:")
        print()
        print(f"    use the {SKILL_NAME} skill to review this file")
        print()