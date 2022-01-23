from collections import deque

START_COMMAND = 'Start'
END_COMMAND = 'End'
REFILL_COMMAND = 'refill'

total_liters = int(input())

people_deque = deque()

while True:
    command = input()
    if command == START_COMMAND:
        break
    people_deque.append(command)

while True:
    command = input()
    if command == END_COMMAND:
        print(f'{total_liters} liters left')
        break
    if command.startswith(REFILL_COMMAND):
        liters_refilled = int(command.split()[1])
        total_liters += liters_refilled
    else:
        person = people_deque.popleft()
        person_liters = int(command)
        if person_liters <= total_liters:
            total_liters -= person_liters
            print(f'{person} got water')
        else:
            print(f'{person} must wait')