#function to calculate maximum scalar value
def maxScalar(arr1,arr2):
    sumVariable=0
    for i in range(0,len(arr1)):
        sumVariable+=arr1[i]*arr2[i]
    return sumVariable



l1=list(map(int,input(" Enter array1 : " ).split()))
l2=list(map(int,input(" Enter array2 : " ).split()))
l1.sort()
l2.sort()
s =0
for i in range(0,len(l1)):
    for j in range(0,len(l2)):
       if(i==j):
           s = s+l1[i]*l2[j]
print('-------------1st Method -------------------')
print('Minimum scalar product of two arrays is ', s)

s=0
for i in range(0,len(l1)):
         s+=l1[i]*l2[i]
print('-------------2nd Method -------------------')         
print("Minimum scalar product of two arrays is",end=' ')
print(s)

print('-------------Function  Method -------------------')
print('Minimum scalar product of two arrays is ', maxScalar(l1,l2))