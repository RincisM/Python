starting = int(input("Enter the Starting Range: "))
ending = int(input("Enter the Ending Range: "))
print("Prime Numbers between", starting, "and", ending,"are: ")
for i in range(starting, ending +1):
    if i>1:
        for j in range(2, i):
            if (i%j)==0:
                break
        else:
            print(i)