"""Day 3: Rucksack Reorganization."""

from collections.abc import Sequence


def priority(item: str) -> int:
    """Return the puzzle priority for a single item type."""
    if "a" <= item <= "z":
        return ord(item) - ord("a") + 1
    if "A" <= item <= "Z":
        return ord(item) - ord("A") + 27
    raise ValueError(f"Not a valid item type: {item!r}")


def part1(rucksacks: Sequence[str]) -> int:
    """Sum priorities of items shared by each rucksack's two compartments."""
    total = 0
    for rucksack in rucksacks:
        midpoint = len(rucksack) // 2
        shared = set(rucksack[:midpoint]) & set(rucksack[midpoint:])
        if len(shared) != 1:
            raise ValueError(f"Expected one shared item, found {len(shared)} in {rucksack!r}")
        total += priority(shared.pop())
    return total


def part2(rucksacks: Sequence[str]) -> int:
    """Sum priorities of each group's shared badge item."""
    if len(rucksacks) % 3:
        raise ValueError("Rucksack count must be divisible into groups of three")

    total = 0
    for start in range(0, len(rucksacks), 3):
        shared = set(rucksacks[start]) & set(rucksacks[start + 1]) & set(rucksacks[start + 2])
        if len(shared) != 1:
            raise ValueError(f"Expected one badge item, found {len(shared)} in group at index {start}")
        total += priority(shared.pop())
    return total

