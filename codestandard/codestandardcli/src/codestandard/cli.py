"""
codestandard — CLI entry point
==============================
Install team code-style rules into AI agent config directories.
"""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path
import importlib.resources

from codestandard.installers.claude import ClaudeSkillInstaller, SKILL_NAME
from codestandard.installers.codex import CodexPluginInstaller
from codestandard.installers.cursor import CursorRuleSetInstaller

# ---------------------------------------------------------------------------
# Agent registry
# ---------------------------------------------------------------------------

AGENTS: dict[str, type] = {
    "claude":       ClaudeSkillInstaller
    # "codex": CodexPluginInstaller,
    # "cursor": CursorRuleSetInstaller,
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
        help=f"Choices: {', '.join(AGENTS.keys())}, to be added: codex, cursor, trae",
    )

    # --- Mutually exclusive actions ---
    action = parser.add_mutually_exclusive_group()
    action.add_argument(
        "--install",
        action="store_true",
        help="Install the customized skills",
    )
    action.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview the installation steps",
    )
    action.add_argument(
        "--uninstall",
        action="store_true",
        help="Uninstall the skills",
    )
    action.add_argument(
        "--list",
        action="store_true",
        help="List all supported agents and exit.",
    )

    # --- Path options ---
    # extend the ability for users to upload standard
    # parser.add_argument(
    #     "--source",
    #     default="./reference",
    #     metavar="PATH",
    #     help="Folder containing code-standard subdirectories. (default: ./reference)",
    # )

    return parser


# ---------------------------------------------------------------------------
# Actions
# ---------------------------------------------------------------------------

def do_list() -> None:
    print("\nSupported agents:\n")
    descriptions = {
        "claude":       f"Global skill         →  ~/.claude/skills/"
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
    print(f"\n{label}Installing skills for: {agent.upper()}")
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

def default_source() -> Path:
    return importlib.resources.path("codestandard")

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
    source = Path(__file__).parent.parent / "codestandard"
    # fixed target path to make sure install it to the right place
    target = Path.home() / ".claude"

    if args.uninstall:
        do_uninstall(args.agent, target)
        return

    # --install or --dry-run
    # TODO: fix the directory
    # if not source.exists() and not args.dry_run:
    #     print(f"\n  [ERROR] Source directory not found: {source}")
    #     print("  Create a 'reference/' folder with code-standard subfolders,")
    #     print("  or pass --source <path> to point to an existing one.")
    #     sys.exit(1)

    do_install(
        agent=args.agent,
        source=source,
        target=target,
        dry_run=args.dry_run,
        overwrite=False,
    )


if __name__ == "__main__":
    main()