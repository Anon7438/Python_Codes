num1 = int(input("Enter starting Number : "))
num2 = int(input("Enter End Number : "))
count = 0
for i in range (num1, num2+1):
    for j in range(2,i):
      if (i % j == 0): 
         count = 1    
         break
    else:    
     print(i,end='  ')    

     