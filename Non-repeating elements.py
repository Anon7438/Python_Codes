
size = int(input('Enter the zize of Array : '))
arr = []
for i in range (size):
    element = int(input('Enter the Element No {} : '.format(i+1)))
    arr.append(element)
print('---------------- Array--------------------')    
print(arr)    

y = []
for i in arr:
    if arr.count(i)>1 and i not in y :
        y.append(i)

print('---------------- Repeating--------------------')
print('length of array is ',len(y),'And Arrays are ',*y)       



#----------------Non Repeating--------------------
print('----------------Non Repeating--------------------')
x = []    
for i in arr:
    if arr.count(i)==1:
        x.append(i)
print('length of array is ',len(x),'And Arrays are ',*x)        