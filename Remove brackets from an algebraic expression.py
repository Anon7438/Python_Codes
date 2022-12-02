string = input('Enter A string : ')
lst = []
for i in string:
    if (i == '(' or i == ')'):
        pass
    else:
       lst += i

for i in lst:
    print(i,end='')   