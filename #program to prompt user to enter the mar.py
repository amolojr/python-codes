#program to prompt user to enter the marks
a=int(input("Enter the first subject"))
b=int(input("Enter the second sunject"))
c=int(input("Enter the third sunject"))
sum=(a+b+c)/3
if(sum>=70 and sum<=100):
    print("GRADE A")
elif(sum>=60 and sum<=69):
    print("GRADE B")
elif(sum>=50 and sum<=59):
    print("GRADE C")
elif(sum>=40 and sum<=49):
    print("GRADE D")
elif(sum>=0 and sum<=39):
    print("FAIL")
else:
    print("RETAKE")
