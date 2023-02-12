#program to prompt the net bonus 
time_period_of_service_=int(input("Enter period of service"))
salary=int(input("Enter salary"))
if("time_period_of_service>10"):
    print(10/100*salary)
elif("time_period_of_service>=6") and ("time_period_of_service<=10"):
    print(8/100*salary)
else:
    print(5/100*salary)