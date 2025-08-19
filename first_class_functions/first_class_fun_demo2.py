def print_hello(name):
    def hello():
        return f"Hello, {name}!"
    return hello

a = print_hello("Ravi")  # Assigning the function to a variable
print(a())  # Output: Hello, Ravi!