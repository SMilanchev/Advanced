from collections import deque

END_COMMAND = 'End'
PAID_COMMAND = 'Paid'

names_queue = deque()

while True:
    command = input()
    if command == END_COMMAND:
        print('{} people remaining.'.format(len(names_queue)))
        break
    elif command == PAID_COMMAND:
        while names_queue:
            print(names_queue.popleft())
    else:
        names_queue.append(command)