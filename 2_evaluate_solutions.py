import concurrent.futures
import os
import ast
import csv
import logging
from typing import Union

import concurrent

from config import (
    RESULTS_FILE,
    SOLUTIONS_DIR,
    SOLUTIONS_PER_GROUP,
)

logging.basicConfig(level=logging.INFO)


def evaluate_solution(filename: str) -> tuple[int, Union[int, str]]:
    """
    Evaluates a solution file for correctness and readability using an LLM.

    Args:
        filename (str): The name of the solution file.

    Returns:
        Tuple[int, Union[int, str]]: Correctness score (0 or 1) and readability
                                     score (1-10 or "" if incorrect or error).
    """

    with open(filename, "r") as f:
        code = f.read()

    try:
        code = code.replace("```python", "").replace("```", "")
        tree = ast.parse(code)
        function_def = next(
            node for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)
        )
        extracted_code = ast.unparse(function_def)

        exec(extracted_code, globals())

        correct = (
            1
            if all(
                [
                    sorted(letterCombinations("45"))
                    == sorted(["gj", "gk", "gl", "hj", "hk", "hl", "ij", "ik", "il"]),
                    letterCombinations("") == [],
                    sorted(letterCombinations("7")) == sorted(["p", "q", "r", "s"]),
                    sorted(letterCombinations("2*03"))  # Input with non-digit char
                    == sorted(["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
                ]
            )
            else 0
        )

        if not correct:
            return correct, ""

        solution_length = len(extracted_code)
        return correct, solution_length

    except Exception as e:
        print(f"Error evaluating code in {filename}: {e}")
        return 0, ""


def evaluate_file(i: int, group: str, solutions_dir: str) -> dict:
    filename = os.path.join(solutions_dir, f"solution_{group}_{i+1}.py")
    correct, solution_length = evaluate_solution(filename)
    return {
        "group": group,
        "filename": filename,
        "correct": correct,
        "solution_length": solution_length,
    }


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Evaluate solution files.")
    parser.add_argument(
        "data_dir",
        nargs="?",
        type=str,
        default=None,
        help="Path to the directory containing solution files (optional)",
    )
    args = parser.parse_args()

    solutions_dir = args.data_dir or SOLUTIONS_DIR

    results = []

    for i in range(SOLUTIONS_PER_GROUP):
        groups = ["experimental", "control"]
        with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
            for group in groups:
                result = next(
                    executor.map(evaluate_file, [i], [group], [solutions_dir])
                )
                results.append(result)

    with open(RESULTS_FILE, "w", newline="") as csvfile:
        writer = csv.DictWriter(
            csvfile,
            fieldnames=["group", "filename", "correct", "solution_length"],
        )
        writer.writeheader()
        writer.writerows(results)
