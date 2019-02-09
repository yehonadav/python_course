import sys
import time


def progress_bar(count, total, suffix=''):
    bar_length = 80
    filled_length = int(round(bar_length * count / float(total)))

    percent = round(100.0 * count / float(total), 1)
    bar = '=' * filled_length + '-' * (bar_length - filled_length)

    sys.stdout.write('[{}] {}% ...{}\r'.format(bar, percent, suffix))
    sys.stdout.flush()

for i in range(1000):
    time.sleep(0.01)
    progress_bar(i, 1000)