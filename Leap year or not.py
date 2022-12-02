year = int(input("Enter The Year : "))
if year % 4 == 0 and year % 400 == 0 and year % 100 == 0:
    print("the given year {} is a leap year ".format(year))
else:    
    print("the given year {} is Not a  leap year ".format(year))