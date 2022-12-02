#take user input
String = input('Enter the string :')
for i in String:
    #initialize a count variable
    count = 0
    for j in String:
        #check for repeated characters
        if i == j:
            count+=1
        #if character is found more than 1 time
        #brerak the loop
        if count > 1:
            break
    #print for nonrepeating characters
    if count == 1:
        print(i,end = " ")