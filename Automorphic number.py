n = int(input("Enter a Number  "))
temp= n
sqr = n*n
co  = 0
while(temp>0):
    if(temp % 10 != sqr % 10 ):
        print("Not Automorphic number  :")
        co=1
        break
    temp= temp//10
    sqr= sqr//10
if (co == 0 ):
    print("{} is an Automorphic number ".format(n))
