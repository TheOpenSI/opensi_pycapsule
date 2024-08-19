import subprocess

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
        files = ["opensi_ai.py"]
    for file in files:
        subprocess.run(["rm", file])