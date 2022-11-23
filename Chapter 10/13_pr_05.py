class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print("****************")
        print(f"The name of the string is {self.name}")
        print(f"Seats available is {self.seats}")

    def fareInfo(self):
        print("****************")
        print(f"Fare for this train is Rs.{self.fare}")
        
        print("****************")

    def bookTicket(self):

        if len(self.seats) > 0:
            print(
                f"Your ticket has been booked! Your seat number is {self.seats}")
            print(self.seats)
            self.seats = len(self.seats)- 1
            print(self.seats)
        else:
            print("Sorry this train is full! Kindly try in tatkal")
            print("****************")

    def ticketCancel(self, seatNo):
        print("You ticket has been cancelled successfully")
        # self.seats = self.seats.append(seatNo)
        


intercity = Train("Intercity Express", 90, [1, 2, 3, 4])
intercity.getStatus()
intercity.fareInfo()
intercity.bookTicket()

intercity.getStatus()
intercity.ticketCancel(3)
intercity.getStatus()