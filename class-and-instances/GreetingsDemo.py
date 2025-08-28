class Greetings:

    def __init__(self):
        print("Hello, this is from __init__")
        
    @staticmethod
    def say_hello():
        print("Hello World from static method!!!")

    @classmethod
    def say_hi(cls):
        print("hi workd from class method!!!")
        print(cls.__name__)

    def print_message(self):
        print("Hello, this is normal method !!!")
    

Greetings.say_hello()
Greetings.say_hi()
g = Greetings()
g.say_hello()
g.print_message()
