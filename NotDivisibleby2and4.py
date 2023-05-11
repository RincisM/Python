a = int(input("Enter the Starting Value: "))
b = int(input("Enter the End Value: "))
print("The Numbers that are not divisible by 2 and 4 in the range {0} - {1} is: ".format(a, b))
for i in range(a,b+1):
    if(i%2!=0 and i%4!=0):
        print(i, end=" ")
