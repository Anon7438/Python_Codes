arr=list(map(int,input("ENTER ARRAY ELEMENTS ").split()))
x=list(dict.fromkeys(arr)) #to remove duplicate in list
print("ELEMENTS OF ARRAY",*arr)
print("ELEMENTS OF ARRAY WITHOUT DUPLICATES ",*x)
print("COUNT OF DISTINCT ELEMENTS ",len(x))
print("COUNT OF Repeating  ELEMENTS ",len(arr)-len(x))