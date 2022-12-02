first =int(input("Enter first Number  : "))
second =int(input("Enter Second Number  : "))
for num in range (first,  second+1):
  order = len(str(num))
  sum = 0
  temp = num
  while temp>0:
    digit = temp % 10
    sum = sum + digit ** order
    temp = temp // 10
  
  if (num == sum):
     print(num, end= ' ')
