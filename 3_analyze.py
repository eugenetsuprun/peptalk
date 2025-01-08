import pandas as pd
import scipy.stats as stats
from config import RESULTS_FILE
from statsmodels.stats.proportion import proportions_ztest
import os

# Global constants
GROUP_COL = "group"


def analyze_results(data_dir=None):
    """
    Loads data from a CSV, performs statistical analysis (t-test and z-test),
    and prints formatted results.

    Args:
      data_dir: Optional path to a directory containing a results.csv file.
                 If None, uses the default RESULTS_FILE from config.
    """

    data_file = (
        RESULTS_FILE if data_dir is None else os.path.join(data_dir, "results.csv")
    )

    df = pd.read_csv(data_file)

    print("Analysis of 'correct' (Correctness):\n")
    print(analyze_correct(df))

    print("\nAnalysis of solution length:\n")
    print(analyze_solution_length(df))


def analyze_correct(df):
    """Analyzes 'correct' column using z-test for proportions; returns formatted results."""

    n_experimental = len(df[df[GROUP_COL] == "experimental"])
    n_control = len(df[df[GROUP_COL] == "control"])
    correct_experimental = df[df[GROUP_COL] == "experimental"]["correct"].sum()
    correct_control = df[df[GROUP_COL] == "control"]["correct"].sum()

    z_stat, p_value = proportions_ztest(
        [correct_experimental, correct_control], [n_experimental, n_control]
    )

    # descriptive stats
    desc_stats = df.groupby(GROUP_COL)["correct"].describe()

    conclusion = (
        "Statistically significant difference found (reject H0)"
        if p_value < 0.05
        else "No statistically significant difference (fail to reject H0)"
    )

    return f"""Z-Test for Proportions:

Descriptive Statistics:
{desc_stats}

z-statistic: {z_stat:.3f}, p-value: {p_value:.3f}
Conclusion: {conclusion}
"""


def analyze_solution_length(df):
    """Analyzes 'solution_length' using t-test; returns formatted results."""

    group1 = df[(df[GROUP_COL] == "experimental") & (df["correct"] == 1)][
        "solution_length"
    ]
    group2 = df[(df[GROUP_COL] == "control") & (df["correct"] == 1)]["solution_length"]

    t_stat, p_value = stats.ttest_ind(group1, group2)

    conclusion = (
        "Statistically significant difference found (reject H0)"
        if p_value < 0.05
        else "No statistically significant difference (fail to reject H0)"
    )

    # Descriptive statistics
    desc_stats = df.groupby(GROUP_COL)["solution_length"].describe()

    return f"""T-Test Results for Solution Length:
Descriptive Statistics:
{desc_stats}

t-statistic: {t_stat:.3f}, p-value: {p_value:.3f}
Conclusion: {conclusion}
"""


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Analyze results from a CSV file.")
    parser.add_argument(
        "data_dir",
        nargs="?",
        type=str,
        help="Optional path to the directory containing results.csv",
    )
    args = parser.parse_args()

    analyze_results(args.data_dir)
