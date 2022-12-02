letter = ''' HEY <Name>
        You are selected
        congratultion !
        your joining date is <Date> '''
name = input("Enter Your Name : ")
date = input("Enter date of joining : ")
letter = letter.replace("<Name>", name)
letter=letter.replace("<Date>", date)
print(letter)
print("\n ")
