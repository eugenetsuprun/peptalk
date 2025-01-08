# Giving the Model a Pep Talk

I explore how giving the model a pep talk on solving a coding-interview-style problem can affect the code generated.

## Experiment Overview

I had AI to try to solve a coding-interview style problem WITH (experimental group) and WITHOUT (control group) a pep talk. 

It's a classic Leetcode-style problem, but I threw in a little twist to make it harder for AI: not only did the code for the solution have to be correct, but it also needed to have the fewest characters possible.

Here's what I did:

1. Have AI solve a coding problem without a pep talk a few times.
1. Have AI solve the same coding problem with newly generated pep talk a few times.
1. Run some basic tests against the generated code to see if it's correct.
1. Analyze the correctness by comparing the two groups.

I ran the experiment on two models: `gpt-4o-mini` and `gpt-4o` with two different temperatures: 0.0 and 1.0.

## Results

These findings are based on a specific prompt and two language models, so they may not be universally applicable.

|Model|Temperature| % of Solutions Correct (No Pep Talk) | % of Solutions Correct (With Pep Talk) |Significant Difference?|
|:---|:---|:---|:---|:---|
|gpt-4o-mini|1|44.4%|48.6%|❌|
|gpt-4o-mini|0|40.4%|88.8%|✅|
|gpt-4o|1|76|87|✅|
|gpt-4o|0|100|97|❌|

# 🚀 Quick Start

Poetry is a dependency management tool for Python. If you don't have it installed, follow the instructions on the [official Poetry website](https://python-poetry.org/docs/#installation).

Then, run `poetry install`.

Enter the poetry-managed virtual environment with `poetry shell`.

Add an `.env` with your OPENAI_API_KEY.

Tweak `config.py`.

Run the scripts in order:

```
python 1_generate_prompts_and_solutions.py
python 2_evaluate_solutions.py
python 3_analyze.py
```

## My Findings

These findings are super limited to the one core prompt I used and the one specific model I used. (`gpt-4o-mini`). Take them with a grain of salt. 🤏

### Results

[add this]



## Repository Structure

```
├── 1_generate_prompts_and_solutions.py
├── 2_evaluate_solutions.py
├── 3_analyze.py
├── config.py
└── results
    └── gpt-4o-mini
        └── temperature=1
            ├── solution_1_experimental.py
            ├── solution_1_control.py
            ...
            ├── solution_500_experimental.py
            ├── solution_500_control.py
            ├── results.csv
            └── summary.txt
        ...   
    └── gpt-4o
```
