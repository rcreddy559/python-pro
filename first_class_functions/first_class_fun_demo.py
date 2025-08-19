def print_hello(name):
    return f"Hello, {name}!"

a = print_hello # Assigning the function to a variable
print(a("Ravi"))  # Output: Hello, Ravi!

def greet(f, msg):
    return f(msg)
print(greet(print_hello, "Ravi"))  # Output: Hello, Ravi!
