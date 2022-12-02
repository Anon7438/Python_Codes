n = int(input("Enter A Number : " ))
n1 = 0
n2 = 1 
print("Fabnocci Series are :- " , n1, n2 ,end=', ')
for i in range (2, n+1):
    n3 = n1+n2
    n1 = n2
    n2 = n3 
    print(n3, end=', ')
