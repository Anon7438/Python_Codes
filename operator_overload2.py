class A:
    def __init__(self, a):
        self.a = a
    # adding two objects
    def __add__(self, o):
        return self.a + o.a
    def __mul__(self, o):
        return self.a * o.a
    def __sub__(self, o):
        return self.a - o.a
    def __str__(self) :
        return f"Decimal Number is : {self.a}"
        

 
ob1 = A(250)
ob2 = A(50)
ob3 = A("Geeks")
ob4 = A("For")
print(ob1.a)
print(ob2.a)
print(ob3.a)
print(ob4.a)
print("************************** : Adding Object values : ***********************************\n")
print(ob1.a+ob2.a)

print("************************** : Adding Object : ***********************************\n")

print(ob1 + ob2)
print(ob3 + ob4)
print("************************** : Multiply Object : ***********************************\n")
print(ob1 * ob2)

print("************************** : Subtracting Object : ***********************************\n")
print(ob1 - ob2)

print("************************** : direct Object : ***********************************\n")
sum = ob1 + ob2
mul = ob1 * ob2
print(f"the sum is {sum} And Multiply is {mul}")

print("************************** : print Object : ***********************************\n")

print(ob1)


