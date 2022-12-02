n = int(input("Enter A decimal Number : "))
res = 0 
i = 1 

while(n!=0):
    rem = n % 8
    res = res + rem * i 
    n = n//8
    i = i * 10
print("Octal value is ",res)    