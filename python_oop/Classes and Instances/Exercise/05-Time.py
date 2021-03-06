class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        hh = str(self.hours).zfill(2)
        mm = str(self.minutes).zfill(2)
        ss = str(self.seconds).zfill(2)
        return f"{hh}:{mm}:{ss}"

    def next_second(self):
        self.seconds = (self.seconds + 1) % (self.max_seconds + 1)
        self.minutes = (self.minutes + int(self.seconds == 0)) % (self.max_minutes + 1)
        self.hours = (self.hours + int(self.minutes == 0 and self.seconds == 0)) % (self.max_hours + 1)

        return self.get_time()


time = Time(23, 59, 59)
print(time.next_second())

time = Time(10, 59, 59)
print(time.next_second())

time = Time(9, 30, 59)
print(time.next_second())

