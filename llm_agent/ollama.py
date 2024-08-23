import subprocess
from typing import List

class Ollama_server():
    
    def __init__(self, model_name:str = "mistral"):
        self.model_id = model_name
        # TODO: fix the prompt, requirements needs more testing
        self.prompt = '''You are a python code genration assistant.

        In your response do not add any text that will be unfamiliar to a python compiler.

        Always response with only the necessary code to fulfill the Question including any imports required in ### Code section.
        In ### Requirements, list all the libraries required to run the code, add 'none' if no libraries are required. 
        In ### Example, always provide an example to run the code.

        Format your code like this - 

        ### Requiements
        $libraries

        ### Code
        $python_code

        ### Example
        $example_to_run_code

        Example - 
        
        Question - Write a python function to load a csv file.
        
        Response -
        ### Requirements
        pandas
        
        ### Code
        import pandas as pd
        def load_csv(file_path):
            return pd.read_csv(file_path)
        
        ### Example
        df = load_csv("data.csv")
        print(df.head())

        '''


    def request_code(self, cmd:List[str], context:str = None, question:str = "Write a python function to multiply 2 matrices.", add_prompt:bool = True) -> str:
        """
        default question
        """
        result = subprocess.run(
            cmd,
            input= context + self.prompt + "Question - "+ question if add_prompt else context + question,
            text=True,
            capture_output=True
        )
        # print(f"[{self.model_id.upper()}] Output from {self.model_id}:")
        # print(result.stdout)
        return result.stdout

    @staticmethod
    def parse_input(response: str):
        requirements = []
        code = ""
        example = ""
        
        lines = response.strip().splitlines()
        
        # TODO: use better logic, this is pathetic
        current_section = None
        for line in lines:
            if "### Requirements" in line:
                current_section = "requirements"
            elif "### Code" in line:
                current_section = "code"
            elif "### Example" in line:
                current_section = "example"
            else:
                if current_section == "requirements":
                    if line.strip() not in ["bash", "```"]:
                        target = line.strip("`")
                        target = target.split(" ")  # TODO: this will break if there are multiple lines in requirements
                        for lib in target:
                            requirements.append(lib.lower())
                elif current_section == "code" or current_section == "example":
                    # skip lines with triple backticks
                    if line.strip() not in ["```", "```python"]:
                        if current_section == "code":
                            code += line + "\n"
                        elif current_section == "example":
                            if "import" not in line.strip():
                                example += line + "\n"
        
        code = code.strip()
        example = example.strip()
        
        return requirements[:-1], code, example # TODO: dont know why does it always retutrns an empty string at the end

# if __name__ == "__main__":
#     ollama = Ollama_server()
#     code = ollama.request_code()
#     print(ollama.parse_input(code)[0])



# result = subprocess.run(
#     ["ollama", "run", "mistral"],
#     input=prompt,
#     text=True,
#     capture_output=True
# )
# print("[MISTRAL] Output from Mistral:")
# print(result.stdout)

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
#     ["ollama", "run", "mistral"],
#     input=prompt,
#     text=True,
#     capture_output=True
# )
# print("[MISTRAL] Output from Mistral:")
# print(result.stdout)

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