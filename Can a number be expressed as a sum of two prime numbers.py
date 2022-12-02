n = int(input('Enter a Number : '))
count = 0 
arr = []
for i in range (1, n+1):
    for j in range(2,i):    
     if (i % j == 0):
         count = 1
         break
    else:
       arr.append(i)
count = 0
for i in range(len(arr)):
    for j in range(i+1,len(arr)):        
        if(arr[i]+arr[j] == n):
            count = 1
            print(str(arr[i]) + " and " + str(arr[j]) + ' are prime numbers when added gives ' + str(n))
            break
        else:
            print("NO numbers that gives sum ")    