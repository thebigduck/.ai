import argparse
from pathlib import Path
import shutil


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Bootstrap a /.ai/ directory from existing project files"
    )
    parser.add_argument(
        "--from",
        dest="sources",
        required=True,
        help="Comma-separated list of sources to scan",
    )
    parser.add_argument(
        "--interactive",
        action="store_true",
        help="Prompt before writing inferred values",
    )
    args = parser.parse_args(argv)

    base = Path(".ai/1-context")
    base.mkdir(parents=True, exist_ok=True)
    if Path("README.md").exists():
        shutil.copyfile("README.md", base / "project_context.md")
        print("Copied README.md to .ai/1-context/project_context.md")
    else:
        print("No README.md found to migrate")


if __name__ == "__main__":
    main()
