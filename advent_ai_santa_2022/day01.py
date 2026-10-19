"""Day 1: Calorie Counting."""

from collections.abc import Sequence

from santas_bag.parse import ints

INPUT_DELIMITER = "\n\n"
parse_input = ints


def part1(groups: Sequence[Sequence[int]]) -> int:
    """Return the largest total carried by one elf."""
    return max(map(sum, groups))


def part2(groups: Sequence[Sequence[int]]) -> int:
    """Return the total carried by the three elves with the most calories."""
    return sum(sorted(map(sum, groups), reverse=True)[:3])

