n = int(input("Enter Number of Peoples : "))
r = int(input("Enter Number of Seats : "))
def fact(n):
    fact = 1
    for i in range(1,n+1) :
        fact = fact * i
    return(fact)    

result = fact(n) // fact(n-r)   
print("Total number of ways are :",result)