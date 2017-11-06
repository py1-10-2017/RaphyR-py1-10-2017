class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health
    def walk(self):
        self.health += 10
        return self
    def run(self):
        self.health -= 5
        return self
    def displayHealth(self):
        print self.health
        return self
class Dog(Animal):
    def __init__(self, name, legs, health=150):
        super(Dog, self).__init__(name, health)
        self.legs = legs
    def pet(self):
        self.health += 5
        return self

animal3 = Dog('leo', 6).displayHealth()
animal3.walk().walk().run().run().pet().displayHealth()
#
# animal3 = Dog('leo', 4).display_health()
# animal3.walk().walk().run().run().pet().display_health()
class Dragon(Animal):
    def __init__(self, name, health=170):
        super(Dragon, self).__init__(name, health)    # use super to call the Human __init__ method
        self.stealth = 10                # every Ninja starts off with 10 stealth
    def fly(self):
        self.health -= 10
    def displayHealth(self):
        print str(self.health) + " I am a dragon"

dragon1 = Dragon('tiantian', 5).displayHealth()

#
# dog1 = Dog("tiantian")
# dog1.displayHealth()
# Dog.walk().walk().walk().run().run().pet().displayHealth()
