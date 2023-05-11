a=int(input("Enter the Number: "))
fact = 1
if a>1:
    for i in range(1,a+1):
        fact = fact*i
if a==0:
    print("The Factorial of 0 is 1")
print("The Factorial of {0} is {1}".format(a, fact))