from collections import deque


def truck_tour(pumps, distance):
    total_pump = 0
    for p, d in zip(pumps, distance):
        total_pump += p - d
        if total_pump < 0:
            break
    if total_pump < 0:
        return False
    else:
        return True


pairs = int(input())

pump_liters = []
pump_distance = []
counter = -1

for _ in range(pairs):
    pair = input().split()
    pump_liters.append(int(pair[0]))
    pump_distance.append(int(pair[1]))

pump_liters = deque(pump_liters)
pump_distance = deque(pump_distance)

for i in range(pairs):
    counter += 1
    if truck_tour(pump_liters, pump_distance):
        break
    else:
        pump_liters.append(pump_liters.popleft())
        pump_distance.append(pump_distance.popleft())
        continue

print(counter)