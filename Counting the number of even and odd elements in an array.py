size = int(input('Enter the Array Size : '))
arr = []
for i in range (size):
    element = int(input('Enter the Element Index No {} : '.format(i+1)))
    arr.append(element)
print(*arr)    
even = []
odd = []
for i in arr:
    if(i%2==0):
        even.append(i)
    else:
        odd.append(i)    
print('Even Numbers are : ',*even)        
print('Odd Numbers are : ',*odd)        
