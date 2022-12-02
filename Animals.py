class Animals:
    def __init__(self) -> None:
        pass


class pet(Animals):
    def __init__(self) -> None:
        super().__init__()


class Dog(pet):
    def bark(self):
        return print("The Dog is barking Bow Bow! ")


obj3 = Dog()
obj3.bark()