a = list(map(int,input("ENTER ARRAY ELEMENTS :  ").split()))
k = int(input("ENTER NO.OF ROTATIONS :  "))
print("-----------LEFT ROTATION --------------- ")
print("ARRAY BEFORE ROTATION ",*a)
k = k%len(a)
for i in range (k) :
    x= a.pop(-1)
    a.insert(0, x)
print("ARRAY After Rotation  ",*a)
print("-----------Right ROTATION --------------- ")
print("ARRAY BEFORE ROTATION ",*a)
for i in range (k) :
    x= a.pop(0)
    a.append(x)
print("ARRAY After Rotation  ",*a)

