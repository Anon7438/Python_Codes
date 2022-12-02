n =  int(input("Enter a Octal Number : "))
res = 0
i = 0

while(n!=0):
    rem = n % 10
    res = res +(rem) * pow(8,  i) 
    i = i + 1
    n = n // 10
print("Decimal Value ",res)  