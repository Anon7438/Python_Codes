size = int(input('Enter the zize of Array : '))
arr = []
for i in range (size):
    element = int(input('Enter the Element No {} : '.format(i+1)))
    arr.append(element)
x = dict.fromkeys(arr)
print(*arr)
print('Distinct Elemnt is ',len(x))
print('Repeating No elements is ', size - len(x))