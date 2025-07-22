# 5. Write a Class ‘Train’ which has methods to 
# book a ticket, 
# get status (no of seats) and 
# get fare information of train running under Indian Railways.
from random import randint

class Train:

    def __init__(self,train_name,train_no,station_from, station_to,round_journey):
        self.train_no = train_no
        self.train_name = train_name
        self.station_from = station_from
        self.station_to = station_to
        self.round_journey = round_journey

    def book_ticket(self):
        return f"The ticket is booked for {self.train_name}({self.train_no}) from '{self.station_from}' to '{self.station_to}'."

    def get_status(self):
        return f"{self.train_name} with {self.train_no} is running on time."

    def fare_info(self):
        passengers = randint(2,5)
        return f"The fare for  {passengers} passengers is  {passengers*(randint(100,300))} - From: {self.station_from} and To: {self.station_to}"
    
    def can_book_return_ticket(self):
        if self.round_journey:
            return f"You can book the return ticket for the same train - {self.train_name}({self.train_no})."
        else:
            return f"Sorry, Can't book return ticket for this train - {self.train_name}({self.train_no})."

train1 = Train("Charminar Express","12343","Hyderabad","Chennai",True)

print(train1.book_ticket())
print(train1.get_status())
print(train1.fare_info())
print(train1.can_book_return_ticket())