a = int(input("Enter the Number: "))
n = len(str(a)) 
sum = 0
temp = a
while temp>0:
    m = temp%10
    sum += m**n
    temp = temp//10
if a == sum:
    print(a, "is an Armstrong Number.")
else:
    print(a, "is not an Armstrong Number.")