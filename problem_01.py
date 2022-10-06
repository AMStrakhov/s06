"""
Description:

Write a function that reads a file from ./assets/problem_01_input.txt, and
creates a new file ./assets/problem_01_output.txt with numbers from
the input files multiplied by n (n — function argument) in format:

<original number> * <n> = <result number>
If a line is not a number, ignore it.

Use arguments filepath_input, filepath_output to get paths to the files.

Examples:
arguments:
n=10
problem_01_input.txt:
0
1
2
...

problem_01_output.txt:
0 * 10 = 0
1 * 10 = 10
2 * 10 = 20
...

"""
from pathlib import Path

current_dir: Path = Path(__file__).resolve().parent
FILEPATH_INPUT: Path = current_dir / "assets" / "problem_01_input.txt"
FILEPATH_OUTPUT: Path = current_dir / "assets" / "problem_01_output.txt"


def convert_file(
    n: int,
    filepath_input: Path = FILEPATH_INPUT,
    filepath_output: Path = FILEPATH_OUTPUT,
) -> None:
    """Write your solution here:"""
    ...


if __name__ == "__main__":
    convert_file(n=10)
