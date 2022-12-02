string = input('Enter A string : ')
# -------------------1st  method---------------------------
# print(string.replace(" ", ""))
# -------------------#2nd method---------------------------
lst = []
for i in string:
    if (i == ' '):
        pass
    else:
       lst += i

for i in lst:
    print(i,end='')   