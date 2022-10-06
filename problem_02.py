"""
Description:

Write a generator that reads a file from ./assets/problem_02_input.txt
line by line. Each line stores a number. The generator should calculate
moving average for last n numbers.

Use argument filepath_input to get path to the file.

Examples:
arguments:
n=3
problem_02_input.txt:
0
1
2

Output:
0
0.5
1
"""
from pathlib import Path
from typing import Iterator


current_dir: Path = Path(__file__).resolve().parent
FILEPATH_INPUT: Path = current_dir / "assets" / "problem_02_input.txt"


def moving_average(
    n: int = 3, filepath_input: Path = FILEPATH_INPUT
) -> Iterator[float]:
    """Write your solution here:"""
    ...


if __name__ == "__main__":
    print(list(moving_average(1)))
