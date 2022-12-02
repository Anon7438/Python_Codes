num = int(input("Enter a Number : "))
count = 0
for i in range (2, num):
    if (num % i == 0):
     count = 1
     break
if(count == 1):
    print("{} is not a prime Number "  .format(num))
else:    
    print("{} is  a prime Number "  .format(num))

