li = []
for i in range (1,101):
    count = 0   
    for j in range (2, i):
        if ( i % j == 0):
          count = 1
          break
    else:
        li.append(i)
print('Prime Number Betwwwn 1 to 100 are :')        
print(*li, sep=' ')
