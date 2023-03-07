#python program to prompt temperature
class temperature():
    def __init__(self,t):
        self.temperature=t
    def fahrenheit (self):
        print(self.temperature*32)
    def celsiu(self):
        print(self.temperature/32)
Newtemperature=temperature(64)
Newtemperature.fahrenheit()
Newtemperature.celsius()

