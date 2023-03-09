"""READ DATA FROM FILE"""
import os
from typing import List


def read_file(path) -> List[str]:
    "Read file from markdown"
    lines = []
    with open(path, "r", encoding="utf8") as file_in:
        for line in file_in:
            lines.append(line)
    file_in.close()
    return lines


PROJECT_DIR = os.path.dirname(os.path.realpath("__file__"))

RELATIVE_BASE_PATH = "src/gpt_experiment/sample_data/hunger-story.md"



