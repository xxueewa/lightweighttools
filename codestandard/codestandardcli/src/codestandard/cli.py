"""
codestandard — CLI entry point
==============================
Install team code-style rules into AI agent config directories.

Usage
-----
  codestandard <agent> --install
  codestandard <agent> --dry-run
  codestandard <agent> --uninstall
  codestandard --list

Agents
------
  claude        Global skill         →  ~/.claude/skills/codestandardskill/
  codex         Codex / OpenAI       →  AGENTS.md + .codex/
  cursor        Cursor /             →  .cursor/rules/*.mdc
  Trae          Trae                 →  .trae/rules

Examples
--------
  codestandard claude --install
  codestandard claude --dry-run
  codestandard claude --uninstall
"""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

from codestandard.installers.claude import ClaudeSkillInstaller
from codestandard.installers.codex import CodexInstaller
from codestandard.installers.cursor import CursorInstaller

# ---------------------------------------------------------------------------
# Agent registry
# ---------------------------------------------------------------------------

AGENTS: dict[str, type] = {
    "claude": ClaudeSkillInstaller,
    "codex":        CodexInstaller,
    "cursor":       CursorInstaller,
}

# Paths that each agent owns — used for --uninstall
AGENT_OWNED_PATHS: dict[str, list[str]] = {
    "claude":       [f".claude/skills/{SKILL_NAME}"],
    "codex":        ["AGENTS.md", ".codex"],
    "cursor":       [".cursor/rules"],
}


# ---------------------------------------------------------------------------
# Argument parser
# ---------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="codestandard",
        description="Install code-style rules for AI coding agents.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )

    parser.add_argument(
        "agent",
        nargs="?",
        choices=list(AGENTS.keys()),
        metavar="agent",
        help=f"Target agent. Choices: {', '.join(AGENTS.keys())}",
    )

    # --- Mutually exclusive actions ---
    action = parser.add_mutually_exclusive_group()
    action.add_argument(
        "--install",
        action="store_true",
        help="Write config files to disk (default action when agent is given).",
    )
    action.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview what would be written without touching the disk.",
    )
    action.add_argument(
        "--uninstall",
        action="store_true",
        help="Remove config files/folders previously installed by this tool.",
    )
    action.add_argument(
        "--list",
        action="store_true",
        help="List all supported agents and exit.",
    )

    # --- Path options ---
    # parser.add_argument(
    #     "--source",
    #     default="./reference",
    #     metavar="PATH",
    #     help="Folder containing code-standard subdirectories. (default: ./reference)",
    # )
    parser.add_argument(
        "--target",
        default=".",
        metavar="PATH",
        help=(
            "Root directory to install into. "
            "(default: current directory; claude-skill always uses ~/.claude)"
        ),
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite existing files. Without this flag existing files are skipped.",
    )

    return parser


# ---------------------------------------------------------------------------
# Actions
# ---------------------------------------------------------------------------

def do_list() -> None:
    print("\nSupported agents:\n")
    descriptions = {
        "claude":       f"Global skill         →  ~/.claude/skills/{SKILL_NAME}/",
        "codex":        "Codex / OpenAI       →  AGENTS.md + .codex/",
        "cursor":       "Cursor / Trae        →  .cursor/rules/*.mdc",
    }
    for name, desc in descriptions.items():
        print(f"  {name:<16}  {desc}")
    print()


def do_install(
    agent: str,
    source: Path,
    target: Path,
    dry_run: bool,
    overwrite: bool,
) -> None:
    installer_cls = AGENTS[agent]
    installer = installer_cls(
        source=source,
        target=target,
        dry_run=dry_run,
        overwrite=overwrite,
    )

    label = "[DRY RUN] " if dry_run else ""
    print(f"\n{label}Installing rules for: {agent.upper()}")
    print(f"  Source : {source}")
    print(f"  Target : {target}\n")

    installer.run()

    if not dry_run:
        installer.reload_hint()


def do_uninstall(agent: str, target: Path) -> None:
    owned = AGENT_OWNED_PATHS.get(agent, [])
    if not owned:
        print(f"  [WARN] No uninstall paths registered for agent '{agent}'.")
        return

    # claude: target is always ~/.claude regardless of --target
    if agent == "claudel":
        target = ClaudeSkillInstaller.DEFAULT_TARGET

    print(f"\nUninstalling: {agent.upper()}")
    print(f"  Target : {target}\n")

    removed_any = False
    for rel in owned:
        path = target / rel
        if not path.exists():
            print(f"  [SKIP]  {path}  (not found)")
            continue
        if path.is_dir():
            shutil.rmtree(path)
            print(f"  [OK]    Removed dir  → {path}")
        else:
            path.unlink()
            print(f"  [OK]    Removed file → {path}")
        removed_any = True

    if removed_any:
        print(f"\n  ✓ Uninstall complete.")
    else:
        print(f"\n  Nothing to remove.")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    # --list is independent of agent
    if args.list:
        do_list()
        return

    # Every other action needs an agent
    if not args.agent:
        parser.print_help()
        sys.exit(0)

    # fixed source path to only install from the module folder
    source = Path(__file__).parent.parent / "reference"

    target = Path(args.target).expanduser().resolve()

    if args.uninstall:
        do_uninstall(args.agent, target)
        return

    # --install or --dry-run
    if not source.exists() and not args.dry_run:
        print(f"\n  [ERROR] Source directory not found: {source}")
        print("  Create a 'reference/' folder with code-standard subfolders,")
        print("  or pass --source <path> to point to an existing one.")
        sys.exit(1)

    do_install(
        agent=args.agent,
        source=source,
        target=target,
        dry_run=args.dry_run,
        overwrite=args.overwrite,
    )


if __name__ == "__main__":
    main()