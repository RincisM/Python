p = int(input("Enter the Principle Amount: "))
r = float(input("Enter the Interest Rate: "))
t = int(input("Enter the Total Time Period: "))
n = int(input("Enter the No. of times interest applied per time period(in months): "))
A = p*((1+(r/(100*n)))**(n*t))
CI = A-p
Amount = "The Amount after {} years is: {:.2f}"
print(Amount.format(n, A))
print("The Compund Interest is: {:.2f}".format(CI))