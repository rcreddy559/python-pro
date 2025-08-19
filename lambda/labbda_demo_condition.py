n = lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "Zero"

print(n(0))  
print(n(99))
print(n(-99))

print("-----------------------------")
li = [lambda arg=x: arg * 10 for x in range(1,5)]

print(li)

for i in li:
    print(i())


print("-----------------------------")

calc = lambda x, y: (x+y, x*y)
result = calc(2,3)
print(type(result), result)