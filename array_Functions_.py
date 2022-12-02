#Asking Array Size 
size = int(input('Enter The Size of Array : '))

#creating an Empty Array or list 
arr = []
#loop according to input size 
for i in range (size):
#Taking user input to array and store in elemnt variable     
    element = int(input('Enter Elements NO {} : '.format(i+1)))
#appending the vlue to empty array 
    arr.append(element)
#printing Array    
print("---------------------------------------#printing Array-----------------------------------    ")
print(*arr)
#for sorting An aaray
arr.sort() 
#printing Sorted Array    
print("---------------------------------------#printing Sorted Array-----------------------------------  ")
print(*arr)
#smallest array 
print("---------------------------------------#smallest array----------------------------------- ")
print(min(arr))
#largest array
print("---------------------------------------#largest array-----------------------------------")
print(max(arr))
#Second largest array
print("---------------------------------------#Second largest array-----------------------------------")
print(arr[1])
#sum of array
print("---------------------------------------#sum of array-----------------------------------")
print(sum(arr))

# half asscending half descending 
print("---------------------------------------# half asscending half descending----------------------------------- ")

a = []
for j in range (size//2):
    a.append(arr[j])
d = []
for k in range (size//2,size):
    d.append(arr[k])
print(*a+d[::-1])
 
# reverse of Array 
print("---------------------------------------#printing Reverse Array-----------------------------------    ")
print(arr[::-1])
print("#-------------------------------printing Reverse Array 2nd method---------------------------------   ")
arr.sort(reverse=True)
print(*arr)

