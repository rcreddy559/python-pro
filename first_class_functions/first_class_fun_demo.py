def test(name):
    return f"Hello, {name}!"

a = test # Assigning the function to a variable
print(a("Ravi"))  # Output: Hello, Ravi!

def greet(fun2, msg):
    return fun2(msg)
print(greet(test, "Ravi"))  # Output: Hello, Ravi!
