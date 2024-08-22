import subprocess
from typing import List

# start ollama server
cmd:str = "ollama run mistral"

# history
KEEP_HISTORY:int = 2

question_history:List[str] = []
response_history:List[str] = []

while True:
    user_input:str = input("[MISTRAL] Enter your query: ")
    question_history.append(user_input)

    if user_input.lower() == "exit":
        break

    #adding history as context
    context_input = f"context: Provided are 2 previouse conversation histories for reference"
    for question, answer in zip(question_history, response_history):
        context_input += f"\nquestion: {question}\nyour answer: {answer}"
    context_input += "\n\n"
    
    # will create a process everytime we pass a query
    response:subprocess.CompletedProcess = subprocess.run(cmd.split(),
                              input = context_input + user_input,
                              text = True,
                              capture_output=True)
    print(f"[MISTRAL-RESPONSE] {response.stdout}")
    if len(response_history) > KEEP_HISTORY: # TODO: fix question count
        # keeping a limited number of conversation history
        response_history.pop(0)
        question_history.pop(0)

    response_history.append(response.stdout)