n1 = int(input("Enter n1 : "))
d1 = int(input("Enter d1 : "))
n2 = int(input("Enter n2 : "))
d2 = int(input("Enter d2 : "))
def lcm(num1 , num2):
    if num1 < num2:
        greater = num2
    else:
        greater = num1
    while True:
        if(greater %  num1== 0) and (greater %  num2== 0):
            lcm = greater 
            break
        greater= greater+1
    return greater

lcm = lcm(d1, d2)
n = n1*(lcm//d1) + n2*(lcm//d2)        

print("Sum of Fraction is : " + str(n)+"/" + str(lcm))


