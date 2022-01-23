box = input().split()
rack_capacity = int(input())
rack_counter = 1
current_rack = 0


while box:
    current_cloth = int(box.pop())
    if current_rack + current_cloth <= rack_capacity:
        current_rack += current_cloth
    else:
        current_rack = 0
        rack_counter += 1
        box.append(str(current_cloth))

print(rack_counter)