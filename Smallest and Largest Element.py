size=int(input("ENTER ARRAY SIZE : "))

arr=[]
for i in range(size):
    
    element=int(input("Enter Element no {} : ".format(i)))
    arr.append(element)

print("SMALLEST ELEMENT",min(arr))
print("LARGEST ELEMENT",max(arr))