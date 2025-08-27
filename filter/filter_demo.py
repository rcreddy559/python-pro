x = [1,2,3,4,5,6,7,8,9]

rel = filter(lambda x: x % 2 == 0, x)
m = map(lambda c: c * 11, rel)
print(list(m))

a = ["apple", "banana", "cherry", "kiwi", "grape"]
len_morethan = filter(lambda x: len(x) > 5, a)
print(list(len_morethan))

