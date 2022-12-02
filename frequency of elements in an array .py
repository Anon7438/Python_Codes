n=int(input("ENTER ARRAY SIZE : "))

arr=[]

print("Enter the array elements ")

for i in range(n):

    arr.append(int(input('Element No {} : '.format(i+1))))

x=list(dict.fromkeys(arr))

for i in x:
    print(' {} occurs {} time(s)'.format(i,arr.count(i)))
