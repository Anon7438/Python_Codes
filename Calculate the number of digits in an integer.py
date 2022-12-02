n = int(input('Enter a digit : '))
#from For  Loop  
count = 0
for i in str(n):
    count = count + 1
print(count)

#From While Loop 
temp = n
count = 0
while (temp>0):    
    temp//=10
    count += 1
print(count)    

# From Str Function
n = str(n)
print(len(n))