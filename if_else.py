# condition checking
age = int(input("Enter Your age : "))
if age > 18:
    print("You Are Adult Now. you Are Eligible for Voting ! ")
else:
    print("Sorry !. you Are NOt Eligible for Voting ! ")

# if else loop
print("*********ELIF TESTING********************")

age = int(input("Enter Your age : "))
if age > 18:
    print("You Are Adult Now. you Are Eligible for Voting ! ")
elif(age == 18):
    print(" you Can Apply for Voter I card This year ")
else :
    print("Sorry !. you Are NOt Eligible for Voting ! ")

#And     
print("*********AND TESTING********************")

age = int(input("Enter Your age : "))
if age > 18  and age <70:
    print("!Hurrah . You can Drive Car ")
elif(age == 18):
    print(" you Can Apply for Driving License card This year ")
else :
    print("Sorry !. you Are NOt Eligible for Driving ! ")
