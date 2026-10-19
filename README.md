# Advent of Code 2022: Days 1–3

Python solutions for the first three Advent of Code 2022 puzzles, using the
[`santas-bag`](https://pypi.org/project/santas-bag/) package to parse and load
puzzle input.

## Setup

The package requires Python 3.12 or newer.

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Set `AOC_SESSION` to your Advent of Code session cookie, then run a day:

```powershell
$env:AOC_SESSION = "your-session-cookie"
python -m advent_ai_santa_2022 1
python -m advent_ai_santa_2022 2
python -m advent_ai_santa_2022 3
```

The `santas-bag` runner downloads each day's input on first use and caches it
under `inputs/`. To use an input file you already have, save it as
`inputs/<day>.txt`; the runner will reuse it.

Each day module also exposes `part1` and `part2` functions for direct use with
parsed puzzle input; the command-line runner handles the day-specific parsing.

## Adding a day

Add a module named `day04.py` (or another `day<N>.py`) to the package. Define
`part1` and `part2`; the runner discovers it automatically. If the input needs
custom parsing, add a module-level `parse_input` callable. Set
`INPUT_DELIMITER` when the input is split on something other than a newline;
the default is `"\n"`.
