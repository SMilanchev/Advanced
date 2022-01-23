from collections import deque

cups_capacity = input().split()
filled_bottles = list(map(int, input().split()))
cups_capacity = deque(list(map(int, cups_capacity)))
water_wasted = 0

while cups_capacity:
    current_cup = cups_capacity.popleft()
    if not filled_bottles:
        cups_capacity.appendleft(current_cup)
        break
    while filled_bottles:
        current_bottle = filled_bottles.pop()
        current_cup -= current_bottle
        if current_cup <= 0:
            water_wasted += abs(current_cup)
            break
        else:
            continue


if filled_bottles:
    print(f'Bottles: {" ".join(list(map(str, filled_bottles)))}')
elif cups_capacity:
    print(f'Cups: {" ".join(list(map(str, cups_capacity)))}')
print(f'Wasted litters of water: {water_wasted}')



