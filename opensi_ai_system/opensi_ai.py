from llm_agent.codellama_mock import LLM
from sandbox_service.sandbox import Sandbox
from util import create_py_file, clean

llm_agent = LLM("codellama")
sandbox = Sandbox()

code_to_run = llm_agent.generate_code()
create_py_file("main", code_to_run)

print(sandbox.run_code("main.py"))

clean(["main.py"])
