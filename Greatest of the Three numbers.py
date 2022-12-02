num1=int(input("Enter first   number: "))
num2=int(input("Enter Second  number: "))
num3=int(input("Enter Third  number: "))
if num1 > num2 and num1 > num3:
    print("{} is greater ".format(num1))
elif  num2 > num3: # and num2 > num1 
    print("{} is greater ".format(num2))
else:    
    print("{} is greater ".format(num3))
