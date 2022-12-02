l1=list(map(int,input(" Enter array1 : " ).split()))
l2=list(map(int,input(" Enter array2 : " ).split()))
l1.sort()
l2.sort(reverse=True)
s =0
for i in range(0,len(l1)):
    for j in range(0,len(l2)):
       if(i==j):
           s = s+l1[i]*l2[j]
print(s)

s=0
for i in range(0,len(l1)):
         s+=l1[i]*l2[i]
print("Minimum scalar product of two arrays is",end=' ')
print(s)