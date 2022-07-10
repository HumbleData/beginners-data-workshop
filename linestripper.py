"""Add or remove newlines to files in specified directory.

Examples:
    $ python linestripper.py add
    $ python linestripper.py remove
    $ python linestripper.py remove --directory 'data'
    $ python linestripper.py --help
"""

from pathlib import Path

import typer

ROOT = Path(".")


def strip_newlines(filepath: Path) -> None:
    """Remove newlines from start/end of file."""
    with open(filepath) as f_input:
        data = f_input.read().rstrip("\n")

    with open(filepath, "w") as f_output:
        f_output.write(data)


def add_newline(filepath: Path) -> None:
    """Add a newline to end of file."""
    with open(filepath) as f_input:
        data = f_input.read() + "\n"

    with open(filepath, "w") as f_output:
        f_output.write(data)


def main(action: str, directory: str = "solutions", file_ext: str = ".py") -> None:
    """CLI utility to add/remove newlines from all files in directory."""
    typer.echo(f"{action} newlines for all {file_ext} files in {directory}")

    if action not in ("add", "remove"):
        raise RuntimeError(f"action must be one of 'add' or 'remove' ('{action}' given)")

    for filepath in (ROOT / directory).glob("*.py"):
        if action == "add":
            add_newline(filepath)
        if action == "remove":
            strip_newlines(filepath)

    typer.echo(f"Request to {action} newlines to all files in {directory} is complete!")


if __name__ == "__main__":
    typer.run(main)
