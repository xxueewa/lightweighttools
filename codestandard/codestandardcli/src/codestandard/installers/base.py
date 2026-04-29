"""
Base installers — shared logic for all agents.
"""

from __future__ import annotations

import shutil
from abc import ABC, abstractmethod
from pathlib import Path
from typing import List


class BaseInstaller(ABC):
    """
    Subclass this for each agent.  Only `build()` and `reload_hint()` are
    required; everything else (file discovery, safe-write, dry-run) is shared.
    """

    def __init__(
        self,
        source: Path,
        target: Path,
        dry_run: bool = False,
        overwrite: bool = False,
    ) -> None:
        self.source = source
        self.target = target
        self.dry_run = dry_run
        self.overwrite = overwrite

    # ------------------------------------------------------------------
    # Public entry point
    # ------------------------------------------------------------------

    def run(self) -> None:
        """Discover standards → build output map → write to disk."""
        standards = self.discover_standards()

        if not standards:
            print(f"[WARN] No standard folders found in {self.source}")
            return

        print(f"  Found {len(standards)} standard(s):")
        for s in standards:
            print(f"    • {s.name}")
        print()

        file_map = self.build(standards)   # {relative_path: content}

        for rel_path, content in file_map.items():
            self._write(rel_path, content)

        print(f"\n  ✓ Done — {len(file_map)} file(s) processed.")

    # ------------------------------------------------------------------
    # Subclass contract
    # ------------------------------------------------------------------

    @abstractmethod
    def build(self, standards: List[Path]) -> dict[str, str]:
        """
        Given a list of standard directories, return a dict of
        {relative_output_path: file_content} to be written under self.target.
        """

    def reload_hint(self) -> None:
        """Print an optional post-install reload message."""

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------

    def discover_standards(self) -> List[Path]:
        """Return the sorted list of subdirectories inside self.source."""

        return sorted(
            p for p in self.source.iterdir()
        )

    def read_standard(self, std_dir: Path) -> str:
        """
        Concatenate all text files inside a standard directory into one string.
        Files are sorted alphabetically; nested folders are traversed.
        Supports: .md, .txt, .adoc, .rst  (falls back to raw text for others).
        """
        TEXT_EXTS = {".md", ".txt", ".adoc", ".rst", ".markdown"}
        parts: list[str] = []

        for file in sorted(std_dir.rglob("*")):
            if not file.is_file():
                continue
            if file.suffix.lower() not in TEXT_EXTS:
                continue
            try:
                text = file.read_text(encoding="utf-8").strip()
                if text:
                    # Use the relative path inside the standard as a sub-header
                    rel = file.relative_to(std_dir)
                    parts.append(f"<!-- source: {rel} -->\n\n{text}")
            except (UnicodeDecodeError, OSError) as exc:
                print(f"    [WARN] Could not read {file}: {exc}")

        return "\n\n---\n\n".join(parts)

    def _write(self, rel_path: str, content: str) -> None:
        """Write content to target/rel_path, honouring dry_run and overwrite."""
        dest = self.target / rel_path

        if self.dry_run:
            print(f"  [DRY RUN] Would write → {dest}  ({len(content)} chars)")
            return

        if dest.exists() and not self.overwrite:
            print(f"  [SKIP]    {dest}  (already exists — use --overwrite to replace)")
            return

        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(content, encoding="utf-8")
        action = "Updated" if dest.exists() else "Created"
        print(f"  [OK]      {action} → {dest}")

    @staticmethod
    def slugify(name: str) -> str:
        """Lowercase, spaces → hyphens, strip unsafe chars."""
        import re
        return re.sub(r"[^a-z0-9\-_]", "", name.lower().replace(" ", "-"))
