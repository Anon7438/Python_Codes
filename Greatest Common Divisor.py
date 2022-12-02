num1 = int(input("Enter first number:"))
num2 = int(input("Enter Second Number:"))
#1st Method
arr = []
if num1 > num2:
    smaller = num2
else:
    smaller = num1
for i in range(1,smaller+1):
    if (num1 % i == 0) and (num2 % i == 0):
        arr.append(i)
print("G.C.F is ",max(arr))    

#2nd Method
def GCF(x,y):
    arr = []
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1,smaller+1):
        if (x % i == 0) and (y % i == 0):
            arr.append(i)
    return(max(arr))        
print("GCF of Given Number is :", GCF(num1,num2))    