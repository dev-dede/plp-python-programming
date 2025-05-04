# Assignment 1
class Building:
    def __init__(self, location, num_of_rooms):
        self.location = location
        self.num_of_rooms =  num_of_rooms

    def count_rooms(self):
        print(f"There are {self.num_of_rooms} rooms in this building")

class House(Building):
    def __init__(self, width, length, height, location, num_of_rooms, price):
        super().__init__(location, num_of_rooms)
        self.width = width
        self.length = length
        self. height = height
        self.__price = price #Private attribute: Encapsulation

    def get_price(self):
        return self.__price

    def size(self):
        return f"{self.width}cm x {self.height}cm x {self.length}cm"

    def house_details(self):
        print(f"This is a {self.size()} house located at {self.location}. It had {self.num_of_rooms} rooms and it is {self.get_price()} cedis")

    def count_rooms(self): # Overriding method in parent class: Polymorphism
        print(f"There are {self.num_of_rooms} rooms in this house. Making live comfortable for a small family")

class Hotel(Building):
    def __init__(self, location, num_of_rooms, price_per_room, stars):
        super().__init__(location, num_of_rooms)
        self.stars = stars
        self.price_per_room = price_per_room

    def hotel_details(self):
        print(f"This is a {self.stars}-star hotel with {self.num_of_rooms} avaialable rooms, located at {self.location} and it cost {self.price_per_room} cedis per night")

    def count_rooms(self):
        print(f"There are {self.num_of_rooms} rooms in this hotel, each room has the needed necessities making stay comfortable for guests")

# Example usage:
hse1 = House(10, 20, 340, "Accra", 5, 2000)
hse1.house_details()
#hse1.__price ->> Leads to an error since price is a private Attribute
hse1.get_price() # Correct assess
hse1.count_rooms()
print("-----------------------------------------------")
hotel1 = Hotel("Kumasi", 400, 5000, 4)
hotel1.hotel_details()  
hotel1.count_rooms() 