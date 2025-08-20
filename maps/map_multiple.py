a = [1,2,3]
b = [4,5,6]

m = map(lambda x,y: x + y, a, b)
print(list(m))

fruits = ['apple', 'banana', 'cherry']
fruits_upper = map(str.upper, fruits)
print(list(fruits_upper))

res = map(lambda a:a[0], fruits)
print(list(res))

num = [' one', ' two']