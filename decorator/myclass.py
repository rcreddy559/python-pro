def method_decorator(func):
    def wrapper( *args, **kwargs):
        print("Start of method decorator")
        res = func( *args, **kwargs)
        print("End of method decorator")
        return res
    return wrapper

class MyClass:
    @method_decorator
    def myclass_method(self,):
        print("Namaste")

obj = MyClass()
obj.myclass_method()
