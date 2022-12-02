size=int(input("ENTER ARRAY SIZE : "))

a=list([])
for i in range(size):
    
    element=int(input("Enter Element no {} : ".format(i)))
    a.append(element)
# arr = list(set(arr))
a.sort()
print(a[1])


