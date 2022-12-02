n = int(input("Enter a Number : "))
temp = n 
sum = 0
while(temp>0):
    rem = temp % 10 
    sum = sum + rem
    temp = temp // 10 
if (n % sum == 0):
    print("{} is a Harshad Number ".format(n))
else:    
    print("{} is Not  a Harshad Number ".format(n))