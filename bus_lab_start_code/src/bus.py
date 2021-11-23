class Bus:
    def __init__(self, route_number, destination, price, capacity):
        self.route_number = route_number
        self.capacity = capacity
        self.destination = destination
        self.price = price
        self.passengers = []
        self.cash = 0
        
    
    def drive(self):
        return "Brum brum"
    
    def passenger_count(self):
        return len(self.passengers)

    def remaining_capacity(self):
        return self.capacity - len(self.passengers)

    def pick_up(self, passenger_1):
        self.passengers.append(passenger_1)
        
    
    def drop_off(self, passenger_1):
        self.passengers.remove(passenger_1)


    def empty(self):
        self.passengers.clear()

    def transfer_cash(self, person, amount):
        person.reduce_cash(amount)
        self.cash += amount


    def pick_up_from_stop(self, bus_stop_1):
        if self.remaining_capacity() > 0:
            for passager in bus_stop_1.queue:
                self.passengers.append(passager)
        

        
        
        
