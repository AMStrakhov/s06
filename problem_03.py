"""
Description:

Write a program to count the frequency of words in a file.
Return a dict with TOP 5 words and their counts.

Use argument filepath_input to get path to the file.

Examples:
Input file:
problem_03_input.txt:
Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus
saepe eveniet, ut et voluptates repudiandae sint et molestiae non recusandae.
Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis
voluptatibus maiores alias consequatur aut perferendis doloribus asperiores
repellat.

Return:
{'aut': 4, 'et': 3, 'rerum': 2, 'ut': 2, 'temporibus': 1}

"""
from pathlib import Path
from typing import Dict


current_dir: Path = Path(__file__).resolve().parent
FILEPATH_INPUT: Path = current_dir / "assets" / "problem_03_input.txt"


def count_words(filepath_input: Path = FILEPATH_INPUT) -> Dict[str, int]:
    """Write your solution here:"""
    ...


if __name__ == "__main__":
    print(count_words())
