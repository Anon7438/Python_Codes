n = int(input("Enter A Number : "))
fact = 1
for i in range(2, n+1):
    fact = fact * i
    
print("factotrial of {} is : " .format(n), fact)    