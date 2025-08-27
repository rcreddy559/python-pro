def decorator_name(func):
    def wrapper(x, y):
        print("wrapper start")
        r =  func(x, y)
        print("wrapper end")
        return r
    return wrapper

@decorator_name
def add(a,b):
    return a +b

result = add(10, 20)
print(result)