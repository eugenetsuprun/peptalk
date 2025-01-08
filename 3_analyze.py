import pandas as pd
from scipy.stats import ttest_ind
from statsmodels.stats.proportion import proportions_ztest
import argparse
import os

GROUP_COL = "group"


def analyze_results(data_file):
    """
    Loads data from a CSV, performs statistical analysis, and prints results.
    """
    df = pd.read_csv(data_file)

    print(analyze_correctness(df))
    print(analyze_solution_length(df))


def analyze_correctness(df):
    """Analyzes correctness using z-test for proportions."""
    groups = df.groupby(GROUP_COL)
    correct_counts = groups["correct"].sum()
    group_sizes = groups.size()

    z_stat, p_value = proportions_ztest(correct_counts, group_sizes)

    return f"""Correctness Analysis (Z-test for Proportions):
    Descriptive Stats:
    {df.groupby(GROUP_COL)['correct'].describe()}

    z-statistic: {z_stat:.3f}, p-value: {p_value:.3f}
    Significant Difference: {p_value < 0.05}
    """


def analyze_solution_length(df):
    """Analyzes solution length using t-test."""
    groups = df[df["correct"] == 1].groupby(GROUP_COL)["solution_length"]

    t_stat, p_value = ttest_ind(*[g for _, g in groups])

    return f"""Solution Length Analysis (T-test):
    Descriptive Stats:
    {df.groupby(GROUP_COL)['solution_length'].describe()}

    t-statistic: {t_stat:.3f}, p-value: {p_value:.3f}
    Significant Difference: {p_value < 0.05}
    """


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze results from a CSV file.")
    parser.add_argument(
        "data_file",
        nargs="?",  # This makes the argument optional
        default="results.csv",  # This sets the default value
        type=str,
        help="Path to the CSV file containing the results",
    )
    args = parser.parse_args()

    analyze_results(args.data_file)
