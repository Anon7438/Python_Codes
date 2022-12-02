size=int(input("ENTER ARRAY SIZE : "))

arr=[]
s = 0
for i in range(size):
    
    element=int(input("Enter Element no {} : ".format(i+1)))
    arr.append(element)
    s = s + arr[i]
print(s)    

print("SUM OF ARRAY : ",sum(arr))