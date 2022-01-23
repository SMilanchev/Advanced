from collections import deque

customers = deque(map(int, input().split(', ')))
taxis = list(map(int, input().split(', ')))
total_time = 0
no_taxis = False

while customers:
    current_customer = customers.popleft()
    if taxis:
        current_taxi = taxis.pop()
        if current_taxi >= current_customer:
            total_time += current_customer
        else:
            customers.appendleft(current_customer)
    else:
        no_taxis = True
        customers.appendleft(current_customer)
        break


if not customers:
    print('All customers were driven to their destinations')
    print(f'Total time: {total_time} minutes')
elif no_taxis:
    print('Not all customers were driven to their destinations')
    print(f'Customers left: {", ".join(str(x) for x in customers)}')
