from math import factorial
n=int(input("Enter the number Of Terms: "))
x=int(input("Enter the value of x: "))

sum=0
if n==1:
    print("Total Sum is: ", n)
else:
    for i in range(1,n):
        if(i%2==0):
            sum = sum + ((x ** i) / factorial(i))
        else:
            sum = sum - ((x ** i) / factorial(i))
    sum=1-sum
    print("Total Sum is: %.2f"%sum)