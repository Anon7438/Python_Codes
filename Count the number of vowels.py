string = input('Enter Your String : ')
count = 0
for i in string:
    if( i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U' ):
        count += 1
if count == 0 :
    print("No vowels Found ") 
else:     
    print('No Of Vowels in your given String Is : ',count)        