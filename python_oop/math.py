class MathDojo(object):
    def __init__(self):
        self.result = 0
    def add(self, *args):
        for i in args:
            if type(i) == list or type(i) == tuple:
                print str(i) + " is a tuple or list"
                for k in i:
                    print k
                    self.result += k
            else:
                print i
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
print(md.add(4).subtract(1).result)
