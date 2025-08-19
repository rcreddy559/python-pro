def arbitrary_function_list(*x):
    for i in x:
        if i % 2 == 0:
            print("Even")
        else:
            print("Odd")    

arbitrary_function_list(30, 40, 60, 80, 33, 44, 55, 667, 886, 111)

def arbitrary_function_map(**x):
    """Prints whether each provided number is even or odd."""
    for key, value in x.items():
        if value % 2 == 0:
            print(f"{key}: Even")
        else:
            print(f"{key}: Odd")

print(arbitrary_function_map.__doc__)
arbitrary_function_map(num1=30, num2=40, num3=60, num4=80, num5=33, num6=44, num7=55, num8=667, num9=886, num10=111)
