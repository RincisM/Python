a = int(input("Enter the Year: "))
if (a%100==0) and (a%400==0):
    print(a, "is a Leap year")
elif (a%4==0) and(a%100!=0):
    print(a, "is a Leap year")
else:
    print(a, "is not a Leap year")