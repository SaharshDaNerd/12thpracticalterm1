# W.a.p of Passing an Immutable Type Value to a function.
def func(a):
    print("Inside function")
    print("Value of a in function is", a)
    a = a + 2
    print("New value of a is", a)


a = 3
print("Calling function with a as", a)
func(a)
print("In main again, value of a is ", a)
