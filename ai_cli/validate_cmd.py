import argparse
from pathlib import Path
import sys


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Validate the /.ai directory for completeness"
    )
    parser.add_argument(
        "--level",
        default="error",
        choices=["error", "warn"],
        help="Reporting level",
    )
    parser.add_argument(
        "--check-links",
        action="store_true",
        help="Validate external links in Markdown files",
    )
    args = parser.parse_args(argv)

    required = [
        Path(".ai/0-ai-config/ai-config.json"),
        Path(".ai/1-context/project_context.md"),
        Path(".ai/4-acceptance/acceptance_criteria.md"),
    ]

    missing = [str(p) for p in required if not p.exists()]
    if missing:
        msg = "Missing required files:\n" + "\n".join(missing)
        if args.level == "error":
            sys.stderr.write(msg + "\n")
            sys.exit(1)
        else:
            print(msg)
    else:
        print("All required files are present")


if __name__ == "__main__":
    main()
