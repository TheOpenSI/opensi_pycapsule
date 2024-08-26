# entry point for users
import sys
sys.path.append("/home/s448780/workspace/sandbox/") # this is to point to the root directory

import subprocess
import readline
from typing import List
from llm_agent.ollama import Ollama_server
from sandbox_service.container import Container
from util import create_py_file, create_requirements_file, clean, get_context

# llm
ollama_obj:Ollama_server = Ollama_server("mistral")

# container
container:Container = Container() # TODO: fix the name

# start ollama server
cmd:str = f"ollama run {ollama_obj.model_id}"

# history
KEEP_HISTORY:int = 1

while True:
    user_input:str = input("[MISTRAL] Enter your query: ")

    if user_input.lower() == "exit":
        break

    # getting the code from ollama
    response:str = ollama_obj.request_code(cmd.split(), "", user_input) # TODO: fix the default value
    print(f"[MISTRAL-RESPONSE]\n {response}")

    # parsing the response
    requirements, code, example = ollama_obj.parse_input(response)

    # creating python file
    create_py_file("opensi_ai_system/main", code + "\n" + example)

    # creating requirements file
    create_requirements_file(requirements)

    # pycapsule
    pycapsule_return_code = -1
    pycapsule_response = ""
    pycapsule_error = ""

    # first run
    if not container.check_if_container_exists():
        pycapsule_return_code, pycapsule_response, pycapsule_error = container.create_container()
    else:
        pycapsule_return_code, pycapsule_response, pycapsule_error = container.start_container()

    # the following is only relevant if retrun code is not 0
    # history
    question_history:List[str] = []
    response_history:List[str] = []

    # for code generation we need to keep track of the original question
    q_origin = ""
    is_origin = True # flag to check if the question is the original question
    
    while pycapsule_return_code != 0:
        print("[OPENSI PYCAPSULE] Generated code had an error, satrting PYCAPSULE service")
        if is_origin:
            q_origin = user_input
            is_origin = False

        response_history.append(response)
        question_history.append(user_input)

        # context format
        """
        context: Provided is the previous conversation history for your reference
        
        original question:
        Conversation history:
        question:

        your annswer:

        """
        context = get_context(q_origin, question_history, response_history)
        new_question = f"Question - Your code had the following error: {pycapsule_error}. Please correct it and response only with the corrected code."
        mistral_response_update = ollama_obj.request_code(cmd.split(), context, new_question, False)
        print(f"[MISTRAL-RESPONSE]\n{mistral_response_update}")

        response_history.append(mistral_response_update)
        question_history.append(new_question)

        requirements, code, example = ollama_obj.parse_input(mistral_response_update)
        print(f"[MISTRAL-RESPONSE] Updated code -{code, example}")

        if len(response_history) > KEEP_HISTORY:
            # keeping a limited number of conversation history
            response_history.pop(0)
            question_history.pop(0)

        create_py_file("opensi_ai_system/main", code + "\n" + example)
        create_requirements_file(requirements)
        pycapsule_return_code, pycapsule_error, pycapsule_error = container.start_container()
    
    clean(["main.py", "requirements.txt"])

    # return code is 0 now, so code run was successful
