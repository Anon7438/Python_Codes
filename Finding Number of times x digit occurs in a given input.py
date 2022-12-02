n = input("Enter your Desired String : ")
digit = input("Enter Digit to check in  String : ")
count = 0
for i in n:
    if(i == digit):
        count = count + 1
        break   
print(" ' {} ' is present ".format(digit),count, "times in given String ' {} '".format(n))    