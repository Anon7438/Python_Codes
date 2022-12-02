a=list(map(int,input(" Enter array ").split()))
a.sort()

x=[]
y=[]
n=len(a)
for i in range(n//2):
    x.append(a[i])
for i in range(n//2,n):
    y.append(a[i])
x.sort()
y.sort(reverse=True)
print('Resultant array',*(x+y))