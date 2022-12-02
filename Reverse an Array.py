size=int(input("ENTER ARRAY SIZE : "))

arr=[]
for i in range(size):
    
    element=int(input("Enter Element no {} : ".format(i+1)))
    arr.append(element)
print("ENTERED ELEMENT IS : ", *arr)
print("REVERSED ELEMENT IS : ",*arr[::-1])