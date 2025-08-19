def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

d = {
    "add": add,
    "subtract": subtract
}

print(d["add"](5, 3))        # Output: 8
print(d["subtract"](5, 3))   # Output: 2
