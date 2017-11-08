class MathDojo(object):
    def __init__(self):
        self.result = 0
    def add(self, *args):
        for i in args:
            if type(i) == list or type(i) == tuple:
                for k in i:
                    self.result += k
                print "true"
            else:
                self.result += i
        return self
    def subtract(self, *args):
        for i in args:
            if type(i) == list or type(i) == tuple:
                for k in i:
                    self.result -= k
            else:
                self.result -= i
        return self


md = MathDojo()
print(md.add([1,2,5,7]).subtract(1).result)

# class Dog(Animal):
#     def __init__(self, name):
#         super(Dog, self).__init__(name)
#         self.health = 150
#     def pet(self):
#         self.health += 5
#         return self
#
# dog = Dog("Rambo")
# dog.walk().walk().walk().run().run().pet().displayHealth()
#
# class Dragon(Animal):
#     def __init__(self, name):
#         super(Dragon, self).__init__(name, health)    # use super to call the Human __init__ method
#         self.health = 10                # every Ninja starts off with 10 stealth
#     def fly(self):
#         self.health -= 10
#     def displayHealth(self):
#         print str(self.health) + " I am a dragon"
#
# dragon1 = Dragon('tiantian', 5).displayHealth()

#
# dog1 = Dog("tiantian")
# dog1.displayHealth()
# Dog.walk().walk().walk().run().run().pet().displayHealth()
