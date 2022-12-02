n = int(input('Enter range to check : '))
divisor = int(input('Enter No of Divisor to check : '))
count1 = 0   
for i in range(1,n+1):
    count2 = 0
    for j in range(1,i+1):
        if(i%j==0):
         count2 = count2 + 1
        else:
            pass
    if(count2 == divisor):
        # count1 = count1+1
        print(i,end= ' ')  

# print('')      
# print(count1)      



