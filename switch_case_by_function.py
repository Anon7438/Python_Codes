def day1():
    return "Monday"


def day2():
    return "Tueday"


def day3():
    return "Wednesday"


def day4():
    return "Thrusday"


def day5():
    return "Friday"


def day6():
    return "Saturday"


def day7():
    return "Sunday"


def default():
    return "Incorrect selection "


selectedday = {

    1: day1,
    2: day2,
    3: day3,
    4: day4,
    5: day5,
    6: day6,
    7: day7
}


def switch(DayWeek):
    return selectedday.get(DayWeek, default)()


inp = int(input(" Enter The Day Number: "))
print(switch(inp))
