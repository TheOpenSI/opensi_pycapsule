import sys
sys.path.append("/home/s448780/workspace/sandbox/") # this is to point to the root directory

from llm_agent.codellama_mock import LLM
from sandbox_service.sandbox import Sandbox
from sandbox_service.container import Container
from util import create_py_file, clean, parse_library_names

llm_agent = LLM("codellama")
sandbox = Sandbox()
container = Container()

code_to_run = llm_agent.generate_code()
# parse libraries
libraries = parse_library_names(code_to_run)
print(f"[INFO] Libraies being used - {libraries}")

# creating python file
create_py_file("opensi_ai_system/main", code_to_run)

# creating container
if not container.check_if_container_exists():
    container.create_container()
else:
    container.start_container()

# delete the file from local volume
clean()
