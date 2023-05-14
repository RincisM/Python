veh=input("Enter the Vehicle name: ")
ehr = int(input("Enter the Entry Hour(in 24hrs): "))
emin = int(input("Enter the Entry Minute(in 24hrs): "))
esec = int(input("Enter the Entry Second(in 24hrs): "))
etime = ehr + ((emin+(esec/60))/60)
exhr = int(input("Enter the Exit Hour(in 24hrs): "))
exmin = int(input("Enter the Exit Minute(in 24hrs): "))
exsec = int(input("Enter the Exit Second(in 24hrs): "))
extime = exhr + ((exmin+(exsec/60))/60)
dura = extime-etime   
if (veh=='Truck' or veh=='bus' or veh=='truck' or veh=='Bus'):
    if (dura<=3):
        print("Parking Charge: Rs.20")
    else:
        print("Parking Charge: Rs.30")
elif (veh=='Car' or veh=='car'):
    if (dura<=3):
        print("Parking Charge: Rs.10")
    else:
        print("Parking Charge: Rs.20")
elif (veh=='Cycle' or veh=='cycle' or veh=='Motor cycle' or veh=='Motor Cycle' or veh=='MotorCycle' or veh=='Motorcycle' or veh=='motorcycle' or veh=='motor cycle' or veh=='Scooter' or veh=='scooter'):
    if (dura<=3):
        print("Parking Charge: Rs.5")
    else:
        print("Parking Charge: Rs.10")