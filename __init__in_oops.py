class school:
 def __init__(self, name, clas, roll, section, year):
        self.name = name
        self.clas = clas
        self.roll = roll
        self.section = section
        self.year = year

d = school("name", "clas" , "roll" , "section", "year")

d.name    = input("Enter The Name  of Student : ")
d.clas    = input("Enter The class of  Student : ")
d.roll    = input("Enter The roll of Student : ")
d.section = input("Enter The of section Student : ")
d.year    = input("Enter The Admission year of Student : ")


print("***************Student Detail *******************\n")
print(f"The NAme OF Student is {d.name} \
    And His Class is {d.clas} \
    And  His Roll no is {d.roll}  \
    And His section is Section {d.section} \
    And Admission year is {d.year}")
