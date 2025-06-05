from maspy import *

class Seller(Agent):
    def __init__(self, agt_name=None):
        super().__init__(agt_name)
        self.add(Goal("announce"))
        self.connect_to("TripChannel")

    @pl(gain, Goal("announce"))
    def create_trips(self, src, announce):
        self.add(Goal("nothing"))
        
    @pl(gain, Goal("buy"), Goal("trip"))
    def trip_bought(self, src, buy, trip):
        self.send('Buyer', achieve, Goal("travel_ticket"), "TripChannel")
        
    @pl(gain, Goal("improve"))
    def improve_trip(self, src, improve):
        self.add(Goal("nothing"))
        

class Buyer(Agent):
    def __init__(self, agt_name=None):
        super().__init__(agt_name)
        self.add(Belief("preferences", adds_event=False))
        self.add(Goal("buyTrip"))
        self.connect_to("TripChannel")

    @pl(gain, Goal("buyTrip"), Goal("preferences"))
    def search_trip(self, src, buyTrip, preferences):
        self.add(Goal("nothing"))
        
    @pl(gain, Goal("check"), Goal("preferences"))
    def check_trip(self, src, check, preferences):
        self.add(Goal("nothing"))
        
    @pl(gain, Goal("travel_ticket"))
    def ticket_received(self, src, travel_ticket):
        self.add(Goal("nothing"))
        

class Website(Environment):
    def __init__(self, env_name):
        super().__init__(env_name)
        self.create(Percept("trip", False))

    def announce_trip(self, agt, data):
        pass
    def delist_trip(self, agt, data):
        pass

def main():
    seller = Seller()
    buyer = Buyer()


    seller.connect_to("TripChannel")
    buyer.connect_to("TripChannel")

    Admin().start_system()

if __name__ == "__main__":
    main()