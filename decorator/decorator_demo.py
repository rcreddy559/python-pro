def decorator_name(func):
    def wrapper():
        print("wrapper start")
        func()
        print("wrapper end")
    return wrapper

@decorator_name
def hello_func():
    print("--------------- hello func------------")

hello_func()