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

def create_requirements_file(requirements: List[str], file_name: str =  "requirements") -> bool:
    """
    this will create a requirements file with the given requirements
    :param file_name:
    :param requirements: list of requirements
    :return: none
    """
    if len(requirements) == 1 and "none" in requirements:
        return False
    else:
        with open(f"opensi_ai_system/{file_name}.txt", "w") as file:
            for requirement in requirements:
                file.write(requirement + "\n")
        print("[INFO] Requirements file created")
        return True

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

def install_requirements():
    """
    this will install the requirements
    :return:
    """
    subprocess.run(["pip", "install", "-r", "requirements.txt"], shell=True)
    print("[INFO] Requirements installed")