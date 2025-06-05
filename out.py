from maspy import *
class DriverAgent(Agent):
    def __init__(self, name=None):
        super().__init__(name)
        self.add(Belief('budget'))
        self.add(Goal('park'))
        self.add(Goal('drive'))

    @pl(gain, ["parking"], ["park"])
    def ask_price(self, src):
        self.send(
            content=,
            receiver=,
            protocol=''
        )
    @pl(gain, ["parking"])
    def test(self, src):

class ManagerAgent(Agent):
    def __init__(self, name=None):
        super().__init__(name)
        self.add(Belief('spotPrice'))

    @pl(gain, ["sendPrice", "spotPrice"])
    def send_price(self, src):
        self.send(
            content=,
            receiver=,
            protocol=''
        )

if __name__ == '__main__':
    driver = DriverAgent('driver')
    manager = ManagerAgent('manager')
    

    Admin().start_system()