class Employee:
    salary = 5000
    company = "Google"
    location = "Gurgao"
   
   # first method to chnge class attribute with function
    # def chngsalary(self):
    #         self.__class__.salary = 10000

   # 2nd method to chnge class attribute with function
    @classmethod
    def chngsalary(cls):
            cls.salary = 10000

e = Employee()
print(e.salary)
e.chngsalary()
print(e.salary)
print(Employee.salary)
