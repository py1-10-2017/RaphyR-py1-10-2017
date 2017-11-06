class Car(object):
    def __init__(self, price , speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
    def displayAll(self):
        if self.price > 10000:
            self.price = self.price + (self.price*0.15)
        else:
            self.price = self.price + (self.price*0.12)
        print "Price + Tax: " + str(self.price)
        print "Speed " + str(self.speed)
        print "Fuel " + self.fuel
        print "Mileage " + str(self.mileage)



car1 = Car(12000, 150, "Full", 24)
# car2 = Car()
# car3 = Car()
car1.displayAll()
