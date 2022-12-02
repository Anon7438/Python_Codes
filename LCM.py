num1 = int(input("Enter first number:"))
num2 = int(input("Enter Second Number:"))
#1st Method

if num1 < num2:
    greater = num2
else:
    greater = num1
while True:
    if(greater %  num1== 0) and (greater %  num2== 0):
        lcm = greater 
        break
    greater= greater+1
print("LCM of ",num1, "and" ,num2, "is",lcm)    