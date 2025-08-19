def even_odd(x: int = 90) -> str:
    if x % 2 == 0:
        return "Even"
    else:
        return "Odd"

list = [30,40,60,80,33,44,55,667,886,111]
for i in list:
    result = even_odd(i)
    print("{} is {}", i, result)

print("Default value:", even_odd())

