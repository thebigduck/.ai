import argparse
from pathlib import Path


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Scaffold a new /.ai/ directory in a project"
    )
    parser.add_argument(
        "--template",
        help="Initialize using a predefined template",
    )
    parser.add_argument(
        "-y",
        "--yes",
        action="store_true",
        help="Skip interactive prompts",
    )
    args = parser.parse_args(argv)

    base = Path(".ai")
    base.mkdir(exist_ok=True)
    for sub in [
        "0-ai-config",
        "1-context",
        "2-technical-design",
        "3-development",
        "4-acceptance",
    ]:
        (base / sub).mkdir(parents=True, exist_ok=True)
    print(f"Initialized {base.resolve()}")


if __name__ == "__main__":
    main()
