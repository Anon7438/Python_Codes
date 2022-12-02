m1 = int(input("Enter The 1st Subject Marks : "))
m2 = int(input("Enter The 2nd Subject Marks : "))
m3 = int(input("Enter The 3rd Subject Marks : "))
m4 = int(input("Enter The 4th Subject Marks : "))
m5 = int(input("Enter The 5th Subject Marks : "))
m6 = int(input("Enter The 6th Subject Marks : "))
m7 = int(input("Enter The 7th Subject Marks : "))
marks_list = [m1, m2, m3, m4, m5, m6, m7]
result = marks_list[0] + marks_list[1]+marks_list[2] +marks_list[3]+marks_list[4]+marks_list[5]+marks_list[6]
print(result)
#Using Sum Function
print(sum(marks_list))
#using Loop 
sum = 0
for s in marks_list:
    sum += s
print(sum)
