string = input('Enter Your String : ')
str1 = str()
for i in string:
    if( i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U' ):
        pass
    else:
        str1 = str1+i

print(string + ' After Removing Vowels '+ str1)        
