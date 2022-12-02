num = int(input("Enter a  Number : "))
result = 0 
for i in range (0, len(str(num))):
   digit  = num % 10
   result = result + digit
   num = num//10
print(result)   

