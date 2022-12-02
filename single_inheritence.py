class Employee:
    company = "Google"
    ecode = 120
class freelancer(Employee):
    level = 0
    skill = "Python Devloper"    


obj = freelancer()
print(obj.company) 
print(obj.ecode) 
print(obj.level) 
print(obj.skill) 