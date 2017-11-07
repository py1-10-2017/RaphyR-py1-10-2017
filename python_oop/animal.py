class Animal(object):
    def __init__(self, name):
        self.name = name
        self.health = 100

    def walk(self):
        self.health += 1
        return self

    def run(self):
        self.health -= 5
        return self

    def displayHealth(self):
        print self.health
        return self

animal1 = Animal('tiantian')
animal1.walk().walk().run().run().displayHealth()

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.health = 150
    def pet(self):
        self.health += 5
        return self

dog = Dog("Rambo")
dog.walk().walk().walk().run().run().pet().displayHealth()

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name, health)    # use super to call the Human __init__ method
        self.health = 10                # every Ninja starts off with 10 stealth
    def fly(self):
        self.health -= 10
    def displayHealth(self):
        print str(self.health) + " I am a dragon"

dragon1 = Dragon('tiantian', 5).displayHealth()

#
# dog1 = Dog("tiantian")
# dog1.displayHealth()
# Dog.walk().walk().walk().run().run().pet().displayHealth()
