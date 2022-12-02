x = int(input(" Enter Value of X-axis : "))
y = int(input(" Enter Value of Y-axis : "))

if(x>0) and (y>0):
    print("X and Y lie at First quadrant ")
elif(x<0) and (y>0):
    print("X and Y lie at Second quadrant ")
elif(x<0) and (y<0):
    print(" X and Y lie at Third quadrant ")
elif(x>0) and (y<0):
    print(" X and Y lie at Fourth quadrant ")
else:
    print("X and Y lie at Origin ")    
