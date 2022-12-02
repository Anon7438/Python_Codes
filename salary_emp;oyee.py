class Employee:
    salary = 10000
    increment = 2.5
 
    
    
    
    @property
    def incrementsalary(self):
        return self.salary*self.incrementsalary

    @propertyAfterIncrementSalary.setter
    def AfterIncrementSalary(self, sal):
           self.increment= sal/self.salary

e = Employee() 
print(e.incrementsalary)       


     