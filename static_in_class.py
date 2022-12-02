class calculator:
    def __init__(self, num):
        self.number = num

    def square(self):
        print(f"The Square of {self.number} is {self.number** 2}")

    def root(self):
        print(f"The Square Root of {self.number} is {self.number** 0.5}")

    def cube(self):
        print(f"The Cube of {self.number} is {self.number**  3}")
# static method is used without self Argument        
    @staticmethod
    def greet():    
       print("*********** : Your Calculation For Given Number is : ***************")

j= int(input("Enter The Number : "))
obj = calculator(j)
obj.greet()
obj.square()
obj.root()
obj.cube()
