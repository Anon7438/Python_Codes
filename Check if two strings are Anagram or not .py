string1 = input('Enter Your first String : ')
string2 = input('Enter Your first String : ')

if len(string2) != len(string1):
    print('Strings are not anagram')
else:
    s1 = sorted(string1)    
    s2 = sorted(string2)    
    if s1 == s2:
         print('Strings are anagram ')
    else:    
         print('Strings are not anagram   ')