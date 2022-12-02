num = int(input("Enter a  Number : "))
# 1st method
result = 0 
for i in range (1, len(str(num))):
   digit  = num % 10
   print(digit,end='') 
   num = num//10

# # 2nd method
# print(str(num)[::-1])


# # for string

# str = input("Enter a word : ")
# print(str[::-1])