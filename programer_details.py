class programmer:
    company = "Google"

    def __init__(self, Name, Product, salary, post):
        self.Name = Name
        self.product = Product
        self.salary = salary
        self.post = post

    def getInfo(self):
        print(f" The programmer name is {self.Name} and \
                Their product name is {self.product} \
                   and Their salary is {self.salary} \
                  and Their post is {self.post}")


Anon = programmer("Anon", "Youtube", "110K", "Manager")
Alex = programmer("Alex", "Chrome", "90K", "Devloper")

Anon.getInfo()
Alex.getInfo()
