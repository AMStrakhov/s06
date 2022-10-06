"""
Description:

Write a generator that reads a file from ./assets/problem_05_input.txt
line by line, and a function that returns every n-th line (step) from
the reader, starting from the k-th line (start) as a list.
The reader should remove end-of-the-line sign (\n).

Use argument filepath_input to get path to the file.

Examples:
arguments:
start=1
step=3

problem_05_input.txt:
0
OK
2
3
OK
5

Return:
["OK", "OK"]
...

"""
from pathlib import Path
from typing import List


current_dir: Path = Path(__file__).resolve().parent
FILEPATH_INPUT: Path = current_dir / "assets" / "problem_05_input.txt"


def slice_file(
    start: int,
    step: int,
    filepath_input: Path = FILEPATH_INPUT,
) -> List[str]:
    """Write your solution here:"""
    ...


if __name__ == "__main__":
    print(slice_file(start=1, step=3))
