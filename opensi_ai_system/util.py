import subprocess
import os
import regex as re
from typing import List

def create_py_file(file_name: str, code: str):
    """
    this will create a python file with the given code
    :param file_name:
    :param code: llm generated code
    :return: none
    """
    with open(f"{file_name}.py", "w") as file:
        file.write(code)

def clean(files=None):
    """
    this will clean up the directory
    :return:
    """
    if files is None:
        files = ["main.py"]
    for file in files:
        if file in os.listdir("/home/s448780/workspace/sandbox/opensi_ai_system"): # TODO: change path dynamic
            subprocess.run(["rm", f"/home/s448780/workspace/sandbox/opensi_ai_system/{file}"])

    print("[INFO] Volume cleaned up")

def parse_library_names(code: str) -> List[str]:
    """
    this will parse the library names from the code
    :param code: llm generated code
    :return: list of library names
    """
    return [library.split(" ")[-1].strip() for library in re.findall(r"(import\s\w+|from\s\w+)", code)]