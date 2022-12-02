n = int(input("Enter A Number : "))
temp = n 
sum = 0
while(temp):
        digit = temp % 10 
        temp = temp//10
        fact = 1
        for i in range(1, digit+1):
            fact = fact * i
        sum = sum + fact 
if (sum == n ) :
    print("{} is a Strong Number ".format(n))
else:
        
    print("{} is a Strong Number ".format(n))
    