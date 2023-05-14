day = int(input("Enter your Birthday: "))
month = int(input("Enter your Month: "))
year = int(input("Enter your Year: "))
cyear = int(input("Enter the Current Year: "))
age = cyear-year
print("Your Birthay is on {0}/{1}/{2} and your age is {3}".format(day, month, year, age))