string = input('Enter the alphanumeric string : ')
sum = 0
for i in string:
    if ord(i) >= 48 and ord(i) <= 57:
        sum += int(i)
print(sum)