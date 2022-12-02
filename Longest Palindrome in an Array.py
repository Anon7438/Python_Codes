import sys
n=int(input("ENTER ARRAY SIZE :  "))
arr=[ ]
for i in range(n):
    element=int(input())
    arr.append(element)
for i in arr:
    if str(i) == str(i)[::-1]:    
      print('Longest palindrome is ',i)
    #   sys.exit(0)
else:
    print("NO palindrome exists")      