j = 1
for i in range(1, 6):
    for j in range(6):
        if(j<i):
            print(end=" ")
        else:
            print(j, end="")
    print()
for i in range(1,6):
    for j in range(i+1):
        if(j<i):
            print(j+1, end="")
    print()