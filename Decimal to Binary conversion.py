n = int(input("Enter Decimal Number : "))
res = 0
i = 1
while (n!=0):
    rem =  n % 2
    res =  res + rem * i
    n= n//2
    i = i*10
pre = '0b'   
print("Binary Value is ",(pre+str(res)))