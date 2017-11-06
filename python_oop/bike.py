class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def displayInfo(self):
        print self.price
        print self.max_speed
        print self.miles

    def ride(self):
        self.miles += 10
        print "Riding. Total mileage " + str(self.miles)

    def reverse(self):
        if self.miles < 0:
            self.miles = 0
            print "This car is coming to a stop."
        else:
            self.miles -= 5
            print "Reversing. " + str(self.miles)


bike1 = Bike(200, "25mph")
bike2 = Bike(500, "39mph")
bike3 = Bike(100, "20mph")
print "====This is bike 1===="
bike1.ride().ride().ride().reverse().displayInfo()
print "====This is bike 2===="
bike2.ride().ride().reverse().reverse()
print "====This is bike 3===="
bike3.reverse().reverse().reverse().displayInfo()
