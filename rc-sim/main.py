"""Command-line entry point for rc-sim."""

import argparse


def main() -> None:
    """Run the rc-sim application entry point."""
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="rc-sim workspace entry point.")
    parser.add_argument(
        "--headless",
        action="store_true",
        help="Run the simulator without opening a window.",
    )
    parser.parse_args()
    main()
