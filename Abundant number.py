n = int(input("Enter A Number: "))
sum = 0 
for i in range (1, n):
    if(n % i== 0):
        sum = sum+i
if(sum > n ) :
    print("{} is a Abundant Number ".format(n))
else:    
    print("{} is Not a Abundant Number ".format(n))
