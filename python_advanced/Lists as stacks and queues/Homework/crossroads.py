from collections import deque

green_light_duration = int(input())
free_window_duration = int(input())

command = input()
cars_queue = deque([])
cars_window = 0
cars_passed = 0
car_crash = False

while command != 'END':
    if command == 'green':
        green_light = green_light_duration
        while cars_queue and green_light > 0:
            current_car = cars_queue.popleft()
            current_car_length = len(current_car)
            green_light -= current_car_length
            if green_light > 0:
                cars_passed += 1
            else:
                if green_light + free_window_duration >= 0:
                    cars_passed += 1
                else:
                    print('A crash happened!')
                    print(f'{current_car} was hit at {current_car[green_light+free_window_duration]}.')
                    car_crash = True
                    break

    if car_crash:
        break

    cars_queue.append(command)
    command = input()

if not car_crash:
    print('Everyone is safe.')
    print(f'{cars_passed} total cars passed the crossroads.')