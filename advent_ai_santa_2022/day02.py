"""Day 2: Rock Paper Scissors."""

from collections.abc import Sequence

Round = tuple[str, str]

_SHAPE_SCORE = {"X": 1, "Y": 2, "Z": 3}
_OPPONENT_SHAPE = {"A": 0, "B": 1, "C": 2}
_PLAYER_SHAPE = {"X": 0, "Y": 1, "Z": 2}


def parse_input(line: str) -> Round:
    """Parse one strategy guide line into its two codes."""
    opponent, player = line.split()
    return opponent, player


def part1(rounds: Sequence[Round]) -> int:
    """Score rounds where X/Y/Z mean rock/paper/scissors."""
    score = 0
    for opponent, player in rounds:
        opponent_shape = _OPPONENT_SHAPE[opponent]
        player_shape = _PLAYER_SHAPE[player]
        outcome = (player_shape - opponent_shape) % 3
        score += _SHAPE_SCORE[player] + (3 if outcome == 0 else 6 if outcome == 1 else 0)
    return score


def part2(rounds: Sequence[Round]) -> int:
    """Score rounds where X/Y/Z mean lose/draw/win."""
    score = 0
    for opponent, outcome_code in rounds:
        opponent_shape = _OPPONENT_SHAPE[opponent]
        if outcome_code == "X":
            player_shape = (opponent_shape - 1) % 3
            outcome_score = 0
        elif outcome_code == "Y":
            player_shape = opponent_shape
            outcome_score = 3
        else:
            player_shape = (opponent_shape + 1) % 3
            outcome_score = 6
        shape_score = (player_shape + 1)
        score += shape_score + outcome_score
    return score

