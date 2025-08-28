def func(cls):
    cls.class_name = cls.__name__
    return cls

@func
class Person:
    pass
print(Person.class_name)
