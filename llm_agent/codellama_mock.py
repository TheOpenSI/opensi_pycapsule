class LLM:
    def __init__(self, llm_name: str):
        self.name = llm_name

    @staticmethod
    def generate_code() -> str :
        # test fibonacci code
        return '''
def fibonacci(n):
    if n <= 0:
        return "Input should be a positive integer"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
        
print(fibonacci(10))
'''