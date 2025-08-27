def greeting(n):
    return f"Hello welcome to first class objects: {n}"

say_greting = greeting
print(say_greting("ravichandra"))

def apply(f, v):
    return f(v)

r = apply(say_greting, "Divija R")
print(r)


def main(x):
    def main2(y):
        return x + y
    return main2
v = main(10)
res = v(30)

print(res)