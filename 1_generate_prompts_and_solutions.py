from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import concurrent.futures
import logging

import os


logging.basicConfig(level=logging.INFO)

from config import (
    CORE_PROMPT,
    MODEL,
    OPENAI_API_KEY,
    SOLUTION_TEMPERATURE,
    SOLUTIONS_DIR,
    SOLUTIONS_PER_GROUP,
    TRANSFORMATION,
)

prompt_chain = (
    ChatPromptTemplate.from_template(
        "I am about to give you a core prompt that I will ask you to transform. "
        "It's a prompt to solve an interview-style coding task. "
        "[Beginning of prompt to transform]\n\n{CORE_PROMPT}"
        "[End of prompt to transform]"
        "Now, here is the transformation I'd like you to apply to this prompt."
        "[Beginning of transformation]\n\n"
        "{TRANSFORMATION}"
        "\n\n[End of transformation]"
        "Return ONLY the new, transformed prompt you generated. No solution or anything else. "
        "Do not begin with 'Certainly! Here is a ... prompt' or similar. "
        "Do not include beginnning or end of prompt markers."
        "Just the transformed prompt."
    )
    | ChatOpenAI(temperature=1, model="gpt-4o-mini", api_key=OPENAI_API_KEY)
    | StrOutputParser()
)
solution_chain = (
    ChatPromptTemplate.from_template(
        "{prompt}\n"
        "No explanations or triple backticks. No imports."
        "ONLY the code starting with a def."
    )
    | ChatOpenAI(temperature=SOLUTION_TEMPERATURE, model=MODEL, api_key=OPENAI_API_KEY)
    | StrOutputParser()
)


def generate_prompt_and_solution(group, i):
    logging.info(f"Generating solution {i+1}/{SOLUTIONS_PER_GROUP} for {group} group")
    if group == "experimental":
        prompt = prompt_chain.invoke(
            {"CORE_PROMPT": CORE_PROMPT, "TRANSFORMATION": TRANSFORMATION}
        )
    else:
        prompt = CORE_PROMPT

    solution = solution_chain.invoke(prompt)
    filename = os.path.join(SOLUTIONS_DIR, f"solution_{group}_{i+1}.py")

    with open(filename, "w") as f:
        f.write(f'"""{prompt}"""\n\n{solution}')


if __name__ == "__main__":
    os.makedirs(SOLUTIONS_DIR, exist_ok=True)

    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        for group in ["experimental", "control"]:
            executor.map(
                generate_prompt_and_solution,
                [group] * SOLUTIONS_PER_GROUP,
                range(SOLUTIONS_PER_GROUP),
            )
