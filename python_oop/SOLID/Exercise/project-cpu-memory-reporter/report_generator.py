from datetime import timedelta, datetime
from time import sleep
import psutil


def generate_report(duration: timedelta):
    measurements = []

    now = datetime.now()
    end_time = now + duration

    while now < end_time:
        cpu, memory = psutil.cpu_percent(interval=0.01), psutil.virtual_memory().percent
        measurements.append((now, cpu, memory))
        now = datetime.now()
        sleep(0.02)

    return measurements


