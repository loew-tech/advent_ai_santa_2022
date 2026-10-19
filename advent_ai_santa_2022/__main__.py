"""Run a day's Advent of Code solution through santas-bag."""

import argparse
import importlib
import os
import pkgutil
import re
import sys

from santas_bag.utils import get_read_and_solve

from . import __path__ as solutions_package_path


def discover_solutions():
    """Load day<N> modules that provide both part1 and part2 callables."""
    solutions = {}
    for module_info in pkgutil.iter_modules(solutions_package_path):
        match = re.fullmatch(r"day(\d+)", module_info.name)
        if match is None:
            continue

        module = importlib.import_module(f".{module_info.name}", __package__)
        if not callable(getattr(module, "part1", None)) or not callable(getattr(module, "part2", None)):
            raise ValueError(f"{module_info.name} must define callable part1 and part2 functions")
        solutions[int(match.group(1))] = module
    return dict(sorted(solutions.items()))


def main() -> None:
    # santas-bag prints an emoji in its timing output; use UTF-8 on Windows
    # consoles whose default code page cannot encode it.
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    solutions = discover_solutions()
    parser = argparse.ArgumentParser(description="Run an Advent of Code 2022 solution")
    parser.add_argument("day", type=int, choices=solutions)
    args = parser.parse_args()

    session_id = os.environ.get("AOC_SESSION")
    if not session_id:
        parser.error("set AOC_SESSION to your Advent of Code session cookie")

    run_day = get_read_and_solve(2022, session_id)
    solution = solutions[args.day]
    result = run_day(
        args.day,
        solution.part1,
        solution.part2,
        delim=getattr(solution, "INPUT_DELIMITER", "\n"),
        parse=getattr(solution, "parse_input", None),
    )

    print(f"Day {args.day}: part 1 = {result[0]}, part 2 = {result[1]}")


if __name__ == "__main__":
    main()
