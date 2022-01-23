from collections import deque

food_quantity = int(input())

orders = input().split()
orders = deque(orders)
max_order = 0

while orders:
    if int(orders[0]) <= food_quantity:
        current_order = int(orders.popleft())
        food_quantity -= current_order
        if current_order >= max_order:
            max_order = current_order
    else:
        break

print(max_order)
if orders:
    print(f'Orders left: {" ".join(orders)}')
else:
    print('Orders complete')