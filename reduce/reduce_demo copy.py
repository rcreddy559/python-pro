from functools import reduce

def add(x,y):
    return x+y
a = [1,2,3,4,5,6,7,8,9]
rel= reduce(add, a)
print(rel)

rel_2 = reduce(add, a, 100)
print(rel_2)

rel_lambda = reduce(lambda x,y: x+y, a)
print(rel_lambda)
