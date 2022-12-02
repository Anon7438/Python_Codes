def sum(n):
    if n <=1:
        return n
    else:
        s = sum(n-1) + n
        return s
n=int(input("Enter The Number  : "))    
result  =  sum(n)
print("The sum OF Given Number Is : ",result )