# For loop
num = int(input("Enter The Number for Table : "))
for a in range(1, 11): 
    print(num, 'x', a, '=', num*a)


#2nd senerio
num = int(input("Enter The Number for Table : "))

for a in range(1, 11, 2):  # for sttatrt from and end on used 1 and 11
    # Range(a,b,c) a= starts from b=ends on c = steps skipped 
    print(num, 'x', a, '=', num*a)
# you can use else also
else:
    print("Done")


#use of break statement in loop 
 
num = int(input("Enter The Number for Table : "))
for a in range(1, 11): 
    print(num, 'x', a, '=', num*a)   
    if a==5 :
     break


#use of continue in loop    

num = int(input("Enter The Number for Table : "))
for a in range(1, 11): 
    if a==5 :
     continue
    print(num, 'x', a, '=', num*a)   
#pass usese    

num = int(input("Enter The Number for Table : "))
for a in range(1, 11): 
    print(num, 'x', a, '=', num*a)   
    if a==5 :
     pass
