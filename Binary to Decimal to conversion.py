n = int(input("Enter The Binary Input :" ))
binary = n
decimal = 0 
base = 1 
while n>0:
    rem = n % 10
    decimal = decimal + rem * base
    n = n//10
    base = base * 2
print("Binary value is ",binary)    
print("Decimal value is ",decimal)    