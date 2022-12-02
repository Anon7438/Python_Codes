class Employee:
    company = "Google"
    ecode = 120
    def test(self):
      print("This is statement of Employee ")

class freelancer(Employee):
  #  company = "Microsoft"
    level = 0
    skill = "Python Devloper" 
    def test(self):
      print("This is statement of FreeLancer ")

class programmer(freelancer) : 
     workinghour ="8 hour"   
     salary = "50k"  
     def test(self):
      print("This is statement of programeer  ")


obj = programmer()
print(obj.company) #this will affect by just upper class value
print(obj.ecode)  
print(obj.level) 
print(obj.skill) 
print(obj.workinghour) 
print(obj.salary) 
