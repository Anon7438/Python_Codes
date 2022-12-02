#function to update high score in file 
def update_high_score(score):
                with open('score.txt','w')as f:
                    f.write(str(score))
                    

#Taking Input from user 
score = int(input("Enter Your Score : "))

#cheking in file
with open('Score.txt') as f:
    highscore = int(f.read())
if highscore < score:
 print("Congrats ! You made a new high Score of :", score)
 update_high_score(str(score))
else :
 print(f"The high socore is {highscore} and you made score of {score}")
        
        