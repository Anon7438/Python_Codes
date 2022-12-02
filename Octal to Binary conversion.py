n =  int(input("Enter a Octal Number : "))
res = 0
i = 0

while(n!=0):
    rem = n % 10
    res = res +(rem) * pow(8,  i) 
    i = i + 1
    n = n // 10
print("Decimal Value ",res)    
decimal = res
i = 0
binary = 0
while(decimal != 0):
    rem2 = decimal % 2 
    binary = (rem2) * pow(10,  i)  + binary
    decimal = decimal // 2
    i = i + 1
print("Octal Value ",binary)    
