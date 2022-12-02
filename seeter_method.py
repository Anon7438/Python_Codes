class company :
    salary = 8000
    other = 3000
    
    @property
    def totalsalry(self) : 
        total = self.salary + self.other 
        return total

    @totalsalry.setter
    def totalsalry(self,  val) : 
        self.salary = val - self.other #in which self other is fixed
        
 
obj = company()
print(obj.totalsalry)
obj.totalsalry = 15000 #this will automatically calcualate the value
print(obj.salary)
print(obj.other)
print(obj.totalsalry)