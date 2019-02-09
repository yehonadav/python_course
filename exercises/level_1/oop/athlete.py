from time import sleep


class Athlete:
    def __init__(self, name, power, speed, endurance, weight):
        self.name = name
        self.power = power
        self.speed = speed
        self.endurance = endurance
        self.weight = weight


class Sprinter(Athlete):
    def __init__(self, name, power, speed, endurance, weight):
        Athlete.__init__(self, name, power, speed, endurance, weight)
        self.power *= 2
        self.speed += 1
        self.endurance -= 3
        if self.endurance < 1:
            self.endurance = 1

    def run(self, distance):
        endurance = 1 + distance/self.endurance
        sleep((self.weight*distance)/(self.power*(self.speed**2)+endurance))
        return self.name
