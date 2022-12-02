class company :
    salary = 8000
    Da = 3000
    pf  = 1500
    @property
    def totalsalry(self) : 
        total = self.salary + self.Da +self.pf 
        return total
 
 
obj = company()
print(obj.totalsalry)
    