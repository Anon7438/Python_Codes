n = int(input("Enter A integer (Containing 0 to chng it with 1) : "))
#ist method 
val = str(n)
replaced = val.replace('0', '1')
print('Entered Integer : ', n)
print('After Replaced o with 1 value is :',replaced)

#2nd method
s = str(n)
l = []
for i in s:
    if (i=='0'):
        l.append('1')
    else:
        l.append(i)  
ns = ""     
for i in l:
    ns= ns+i     
print('After Replaced o with 1 value is : ',int(ns))


