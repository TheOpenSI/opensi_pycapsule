import sys
import regex as re
sys.path.append("/home/s448780/workspace/sandbox/") # this is to point to the root directory

from llm_agent.codellama_mock import LLM


agent = LLM("codellama")
code = agent.generate_code()

print(code)

response = re.findall(r"import\s\w+", code) # ['fibonacci']

print(response)