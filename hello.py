import sys
print(sys.version)
print("hello")
A = []
A.append(23)
print("A:", A)

print("\nAwsome! :D")

def greet(greeting, name):
    """return a greeting

    Args:
        greeting (string): string sttement for greeting
        name (string): name of person

    Returns:
        string: greeting
    """
    return f'{greeting} {name}'

print(greet("Hi My Friend, ", "John"))