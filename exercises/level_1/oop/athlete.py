import time


class Athlete:
    def __init__(self, name, power, speed, endurance, weight):
        if speed < endurance:
            speed = endurance + 3
        self.name = name
        self.power = power
        self.speed = speed
        self.endurance = endurance
        self.weight = weight


class Runner(Athlete):
    def __init__(self, name, power=0, speed=0, endurance=0, weight=60):
        Athlete.__init__(self, name, power, speed, endurance, weight)
        self.power += weight*0.1
        self.speed += 25
        self.endurance += 8

    def get_duration(self, distance):
        acceleration = self.power / self.weight
        top_speed = self.speed
        time_to_reach_top_speed = top_speed / acceleration
        distance_to_top_speed = top_speed * time_to_reach_top_speed / 2

        if distance == distance_to_top_speed:
            duration = time_to_reach_top_speed

        elif distance < distance_to_top_speed:
            duration = (2 * distance / acceleration) ** (1 / 2)

        else:
            deceleration = acceleration
            endurance_speed = self.endurance
            time_to_reach_endurance_speed = top_speed - endurance_speed / deceleration
            distance_to_endurance_speed = top_speed * time_to_reach_endurance_speed / 2

            if distance == distance_to_top_speed + distance_to_endurance_speed:
                duration = time_to_reach_endurance_speed
            elif distance < distance_to_top_speed + distance_to_endurance_speed:
                duration = time_to_reach_top_speed + (2 * (distance - distance_to_top_speed) / deceleration) ** (1 / 2)
            else:
                time_to_reach_distance = (distance - (distance_to_top_speed + distance_to_endurance_speed)) / endurance_speed
                duration = time_to_reach_top_speed + time_to_reach_endurance_speed + time_to_reach_distance
        return duration

    def run(self, distance):
        duration = self.get_duration(distance)
        time.sleep(duration)
        return self.name


class Sprinter(Runner):
    def __init__(self, name, power=0, speed=0, endurance=0, weight=70):
        Runner.__init__(self, name, power, speed, endurance, weight)
        self.power += weight*0.75
        self.speed += 15
        self.endurance += 1


class MarathonRunner(Runner):
    def __init__(self, name, power=0, speed=0, endurance=0, weight=55):
        Runner.__init__(self, name, power, speed, endurance, weight)
        self.power /= 1.1
        self.speed -= 3
        self.endurance += 7
        if self.speed <= 8:
            self.speed = 8
        if self.speed < self.endurance + 1:
            self.speed = self.endurance + 1


if __name__ == "__main__":
    template = '{name} run a distance of {distance}km in: {timedelta}'
    distances = (100, 200, 800, 1600, 5000, 20000)
    athletes = (
        Sprinter(name='hanan', speed=5, endurance=2, weight=60),
        Sprinter(name='nikita', power=20, weight=62),
        Runner(name='idan', power=18, speed=2, endurance=1, weight=71),
        MarathonRunner(name='moshe', power=20, speed=2, endurance=4, weight=50)
    )
    for distance in distances:
        print(f'race of {distance} meters')
        for athlete in athletes:
            duration = athlete.get_duration(distance)
            if duration > 3600:
                hr = duration//3600
                min = int((duration % 3600)//60)
                sec = round((duration % 3600) % 60, 2)
                timedelta = f'{hr}hr {min}min {sec}sec'
            elif duration > 60:
                min = int(duration//60)
                sec = round(duration % 60, 2)
                timedelta = f'0hr {min}min {sec}sec'
            else:
                timedelta = f'0hr 0min {round(duration, 2)}sec'
            print(template.format(name=athlete.name, distance=distance/1000, timedelta=timedelta))
        print("")
