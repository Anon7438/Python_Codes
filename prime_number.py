# name = input("Enter your Name : ")
# print("Good AfterNoon ",+ name)
# prime number program
num = int(input("Enter The Number : "))
prime = True
for i in range(2, num):
 if(num % i == 0) :
     prime = False 
     break
if prime :
  print(f"The given Number {num} is prime ")
else :
    print(f"The given Number {num} is Not prime ")
  