def factor(n):
    sum = 0 
    for i in range (1, n):
        if(n % i==0):
         sum = sum + i        
    return(sum)     

n = int(input("Enter a Number  : "))
if(factor(n)== n):
    print("{} is a Strong Number ".format(n))
else:
    print("{} is Not a Strong Number ".format(n))