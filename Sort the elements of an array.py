size = int(input('Enter Size of Array : '))
arr = []
for i in range(size):
    element = int(input('Enter element no {}  : '.format(i+1)))
    arr.append(element)
arr.sort()
print(" Asscending Order ")
print("  ",*arr)
arr.sort(reverse= True)
print(" Descending Order ")
print("  ",*arr)
