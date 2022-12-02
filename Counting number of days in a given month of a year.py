Month = int(input('Enter the Month : '))
Year = int(input('Enter the Year : '))

if(Month == 2 ) or (Year%4==0) or (Year%100==0) or (Year%400==0):
    print("Number of days is 28")
elif(Month == 1 or Month == 3 or Month == 5 or Month == 7 or Month == 8 or Month == 10 or Month == 12):
    print("Number of days is 31")
else:
    print("Number of days is 30 ")    