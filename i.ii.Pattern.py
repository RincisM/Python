for i in range(1, 6):
    for j in range(1, 6):
        if(i==j):
            print("$", end=" ")
        elif(i>1 and i<5 and j>1 and j<5):
            print(" ", end=" ")
        else:
            print("*", end=" ")
    print()