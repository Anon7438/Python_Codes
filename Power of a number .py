base  = int(input("Enter base : "))
expo  = int(input("Enter  Exponent : "))
print(" Power of the Number is : ", base ** expo)

#2nd Method
temp = 1
for i in range (0, expo):
 temp = temp * base
print(" Power of the Number is : ", temp) 