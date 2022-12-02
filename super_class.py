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
      super().test()  #this will also run
      print("This is statement of FreeLancer ")
      
class programmer(freelancer) : 
     workinghour ="8 hour"   
     salary = "50k"  
     def test(self):
         super().test() # this will also  with  Test function call
         print("This is statement of programeer  ")


obj = programmer()

obj.test()#Runjust upper test function also due to  Super class function
print(obj.company) #just upper value
print(obj.ecode)  
print(obj.level) 
print(obj.skill) 
print(obj.workinghour) 
print(obj.salary) 
