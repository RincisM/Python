a = int(input("Enter the Number: "))
if a>1:
    for i in range(2, a):
        if(a%i)==0:
            print(a, "is not a Prime Number")
            break
    else:
        print(a, "is a Prime Number")
else:
    print(a, "is not a Prime Number")