import sys
sys.path.append('..')
sys.path.append('.')
from llm_agent.codellama_mock import LLM
from sandbox_service.sandbox import Sandbox
from sandbox_service.container import Container
from util import create_py_file, clean

llm_agent = LLM("codellama")
sandbox = Sandbox()
container = Container()

code_to_run = llm_agent.generate_code()
create_py_file("opensi_ai_system/main", code_to_run)

# creating container
if not container.check_if_container_exists():
    container.create_container()
else:
    container.start_container()

# # print(sandbox.run_code("main.py"))

clean()
