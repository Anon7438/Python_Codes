def chk(a,b,c):
    if a>b and a>c:
         return a
    elif b>c : 
         return b 
    else :
         return c
        
a=int(input("Enter The Value of a : "))        
b=int(input("Enter The Value of b : "))        
c=int(input("Enter The Value of c : "))        
print("The Greatest among Given Three Number is : ",chk(a,b,c))