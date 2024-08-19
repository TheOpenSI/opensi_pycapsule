import subprocess
import os

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