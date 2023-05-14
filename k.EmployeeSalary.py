hwage=int(input("Enter your hourly wage: "))
rhrs=int(input("Enter the regular hours: "))
dwage = hwage*rhrs
ohrs = int(input("Enter the Overtime hours worked: "))
owage = ohrs*(1.5*hwage)
wwage = dwage*6 + owage
print("The Employee's total weekly pay is:", wwage)