print("*********NESTED IF  TESTING********************")

age = int(input("Enter Your age : "))
if age > 18 and age < 70:
    print("!Hurrah . You can Drive Car ")
    if age > 50 and age < 70:
        print("you must care about Speed ! cause your Age is  ", age)
    else:
        print("you can Enjoy Your Driving your Age is  ", age)
elif(age == 18):
    print(" you Can Apply for Driving License card This year ")
else :
    print("Sorry !. you Are NOt Eligible for Driving ! ")
