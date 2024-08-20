import subprocess

prompt = '''Always response with only the necessary code to fulfilll the question.
Do not add anything that can be unfamiliar to a python compiler.

Question:
Write a Python class to store bank account details with the following attributes: Name, Age, Gender, Balance'''


result = subprocess.run(
    ["ollama", "run", "codellama"],
    input=prompt,
    text=True,
    capture_output=True
)
print("Output from Codellama:")
print(result.stdout)

# if result.stderr:
#     print("Errors:")
#     print(result.stderr)

# ollama_server = subprocess.Popen(
#     ["ollama", "run", "codellama:13b"],
#     stdin=subprocess.PIPE,
#     stdout=subprocess.PIPE,
#     stderr=subprocess.PIPE,
#     text=True
# )

# output, errors = ollama_server.communicate(input=prompt + "\n")
# print("Output from Codellama:")
# print(output)



# ollama_server = subprocess.Popen(
#     ["kill", "-9", "377436"],
#     text=True
# )
# ollama_server.kill()

# res = subprocess.run("kill -9 377436", shell=True, capture_output=True, text=True)
# print(res)