n=5
for m, i in enumerate(range(1, 6), start=1):
    for j in range(1, 6):
        if(i==j):
            print("$", end=" ")
        elif(i==m and j==n):
            print("$", end=" ")
        elif(i>1 and i<5 and j>1 and j<5):
            print(" ", end=" ")
        else:
            print("*", end=" ")
    n = n-1
    print()