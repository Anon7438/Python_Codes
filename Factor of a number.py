n = int(input("Enter a Number  : "))
print("Factor of {} is : ".format(n), end=' ')
for i in range (1 , n+1):
    if (n % i == 0):
      print(i,end=', ')
    
   