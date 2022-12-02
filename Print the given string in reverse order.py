string = input('Enter A string : ')
str1 = ''
for i in string:
    if(ord(i) >= 65 and ord(i) <= 90) or (ord(i) >= 97 and ord(i) <= 122):
        str1 = str1 + i
    else:
        pass
print(' Alphabets in string are : ',str1)        