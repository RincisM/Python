a = int(input("Enter the Unit: "))
if 0<=a<151:
    print("Electricity Charge: Rs.", a*3)
elif 151<=a<301:
    print("Electricity Charge: Rs.", 100+a*3.75)
elif 301<=a<451:
    print("Electricity Charge: Rs.", 250+a*4)
elif 451<=a<601:
    print("Electricity Charge: Rs.", 300+a*4.25)
elif a>600:
    print("Electricity Charge: Rs.", 400+a*5)
else:
    print("Enter a Valid Unit")