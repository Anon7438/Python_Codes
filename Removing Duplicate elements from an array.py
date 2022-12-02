size = int(input('Enter the zize of Array : '))
arr = []
for i in range (size):
    element = int(input('Enter the Element No {} : '.format(i+1)))
    arr.append(element)
print('------------Inputed  Array ---------------')
print(*arr)    
print('------------Removing Dupliactes from Array ---------------')
print(*set(arr))    