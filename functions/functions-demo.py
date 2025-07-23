def testfunction(arg):
   print ("Inside function:",arg)
   print ("ID inside the function:", id(arg))
   arg=arg.append(100)
   
var=[10, 20, 30, 40]
print ("ID before passing:", id(var))
testfunction(var)
print ("list after function call", var)

print("----------------------------------------")

def testfunction2(age):
   print ("Inside function:", age)
   age = 30
   print ("age after changing inside function:", age)

age = 25
print ("age before passing:", age)
testfunction2(age)
print ("age after function call:", age)

