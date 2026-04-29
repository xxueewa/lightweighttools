"""
Cursor / Trae Rule Set Installer
=================================
Produces:

  .cursor/rules/<standard>.mdc    ← one MDC rule per code standard

MDC frontmatter fields used by Cursor:
  description   : shown in the rules panel
  globs         : file patterns that auto-activate this rule
  alwaysApply   : if true, rule is injected in every chat/cmd-k call

References:
  https://docs.cursor.com/context/rules
"""

from __future__ import annotations

from datetime import date
from pathlib import Path
from typing import List

from .base import BaseInstaller

# Same glob map as the Claude installer — keep in sync or extract to utils.py
LANG_GLOBS: dict[str, list[str]] = {
    "java":       ["**/*.java"],
    "python":     ["**/*.py"],
    "typescript": ["**/*.ts", "**/*.tsx"],
    "ts":         ["**/*.ts", "**/*.tsx"],
    "javascript": ["**/*.js", "**/*.jsx"],
    "js":         ["**/*.js", "**/*.jsx"],
    "go":         ["**/*.go"],
    "rust":       ["**/*.rs"],
    "kotlin":     ["**/*.kt"],
    "swift":      ["**/*.swift"],
    "ruby":       ["**/*.rb"],
    "php":        ["**/*.php"],
    "css":        ["**/*.css", "**/*.scss", "**/*.less"],
    "html":       ["**/*.html", "**/*.htm"],
    "sql":        ["**/*.sql"],
    "shell":      ["**/*.sh", "**/*.bash"],
}


class CursorRuleSetInstaller(BaseInstaller):
    """Installs code style rules for Cursor (and compatible tools like Trae)."""

    def build(self, standards: List[Path]) -> dict[str, str]:
        file_map: dict[str, str] = {}
        today = date.today().isoformat()

        for std_dir in standards:
            slug = self.slugify(std_dir.name)
            rel = f".cursor/rules/{slug}.mdc"
            file_map[rel] = self._build_mdc(std_dir, slug, today)

        return file_map

    def _build_mdc(self, std_dir: Path, slug: str, today: str) -> str:
        display_name = std_dir.name.replace("-", " ").replace("_", " ").title()

        globs = self._detect_globs(slug)
        globs_yaml = (
            ", ".join(f'"{g}"' for g in globs)
            if globs
            else ""
        )
        # alwaysApply: true only when no specific globs are detected
        always_apply = "true" if not globs else "false"

        body = self.read_standard(std_dir)
        if not body:
            body = f"_No content found in {std_dir}._"

        frontmatter_globs = (
            f'globs: [{globs_yaml}]\n' if globs_yaml else ""
        )

        return f"""\
---
description: "{display_name} — code style rules"
{frontmatter_globs}alwaysApply: {always_apply}
generated: "{today}"
---

# {display_name}

{body}
"""

    def _detect_globs(self, slug: str) -> list[str]:
        slug_lower = slug.lower()
        for lang_key, globs in LANG_GLOBS.items():
            if lang_key in slug_lower:
                return globs
        return []

    def reload_hint(self) -> None:
        print("\n--- Cursor Reload ---")
        print("  Rules are picked up automatically when you open or reload Cursor.")
        print("  To verify, open the Command Palette and run:")
        print()
        print("    Cursor: Open Rules")
        print()
        print("  You should see your new rule files listed under Project Rules.")
        print()
