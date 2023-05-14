a=int(input("Enter the Number of terms: "))
x=int(input("Enter the value of x: "))
sum=0
for i in range(1,a+1):
    if(i%2==0):
        sum=sum+(x**i)
    else:
        sum=sum+(-x**i)
print("The Sum of",x,"series is:",sum)