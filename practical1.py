# Write a program to calculate simple interest using a function interest() that receive principal, time and rate and returns calculate interest
def interest(p, r, t):
    inte = (p*r*t)/100
    return inte


p = int(input("What is the principal amount: "))
r = int(input("What is the Rate of interest: "))
t = int(input("What is the time: "))
print(interest(p, r, t), "is the interest")
