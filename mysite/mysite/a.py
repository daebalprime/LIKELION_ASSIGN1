if score >= 80 :
    print("A")
if score >= 60 :
    print("B")
if score >= 40 :
    print("C")
else :
    print("F")

class Person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight
    def info(self):
        print(self.name,self.height,self.weight)

class Athlete(Person):
    def setinfo(self, event,ranking):
        self.event = event
        self.ranking = ranking
    def info(self):
        print(self.name,self.event,self.ranking)
