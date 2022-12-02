class train:
    def __init__(self, name, seat, fare):
        self.name = name
        self.seat = seat
        self.fare = fare

    def getstatus(self):
        print("******************* :Train Info : *****************************")
        print(f"The Name Of Train is {self.name} And Train Number 22456")
        print(f"The Avilable No Of setas in this Train is {self.seat} ")
        print(f"The fare Of this Train is Rs.{self.fare} ")

    def bookticket(self):
        if(self.seat > 0):
            print(
                f"Congrats ! your seat is booked and your seat no is {self.seat}")
            self.seat = self.seat - 1
        else:
            print("oops sorry! There is no Vaccant seats In  this Train ")


obj = train("Rajdhani Express", 0, 1540)

obj.getstatus()
obj.bookticket()
 