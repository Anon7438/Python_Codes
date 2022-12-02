class Employee:
    company = "Google"
    ecode = 120
class freelancer:
    company = "Microsoft"#depend upon parameter passed in childs class argument
    level = 0
    skill = "Python Devloper" 
class programmer(Employee, freelancer ) : 
   workinghour ="8 hour"   
   salary = "50k"  


obj = programmer()
print(obj.company) 
print(obj.ecode) 
print(obj.level) 
print(obj.skill) 
print(obj.workinghour) 
print(obj.salary) 
