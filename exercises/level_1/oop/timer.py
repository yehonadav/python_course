from exercises.level_1.oop.inherit import Date


class Measurement:
    date = None
    run_time = None


class Timer(Date):
    def __init__(self, f, *args, **kwargs):
        self.operation = f
        self.args = args
        self.kwargs = kwargs
        self.last_measurement = Measurement()

    def start(self):
        t = self.get_time()
        self.last_measurement.date = self.get_date()
        result = self.operation(*self.args, **self.kwargs)
        self.last_measurement.run_time = self.get_time() - t
        return result


if __name__ == '__main__':
    from random import randint
    from exercises.level_1.oop.athlete import Sprinter
    from exercises.data import get_data

    winner = None
    distance = 100
    athletes = get_data(10)

    for athlete in athletes:
        sprinter = Sprinter(
            athlete['name'],
            power=randint(9, 20),
            speed=randint(20, 27),
            endurance=randint(1, 4),
            weight=randint(70, 80))
        timer = Timer(sprinter.run, distance=distance)

        name = timer.start()

        if winner is None:
            winner = {'name': name, 'time': timer.last_measurement}
        else:
            athlete_time = timer.last_measurement.run_time
            winner_time = winner['time'].run_time
            if athlete_time < winner_time:
                winner = {'name': name, 'time': timer.last_measurement}

    print('in', winner['time'].date, ':   ',
          winner['name'], 'run', distance, 'meters '
          'in', winner['time'].run_time, 'and won')
