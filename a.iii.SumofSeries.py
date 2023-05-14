sum=0
a = int(input("Enter the Limit: "))
for i in range(1,a+1):
    for j in range(1,i+1):
        sum = sum+j
print(sum)