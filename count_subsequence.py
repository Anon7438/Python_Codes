
str1 = input("Enter 1st String : ")
# str2 = input("Enter 2nd String : ")

list2 = []
count =0
for i in range (len(str1)):    
    for j in range (i+1,len(str1)+1):
     list2.append(str1[i:j])
     count+=1

print(*(list2),end='\n')
print(count)
