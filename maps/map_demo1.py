a = ['1','2','3','4','5']
print(f"before a: {a}")
m = map(int, a)
print(f"after a: {list(m)}")

def double(n):
    return int(n)* 2

d = map(double, a)
print(f"function with map: {list(d)}")
