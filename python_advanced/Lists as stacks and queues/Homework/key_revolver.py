from collections import deque

bullet_price = int(input())
gun_size = int(input())
bullets = input()
locks = input().split()
intel_value = int(input())

locks = deque(list(map(int, locks)))
bullets = list(map(int, bullets.split()))
bullets_counter = 0

while locks:
    lock = locks[0]
    while bullets:
        bullet = bullets.pop()
        bullets_counter += 1
        if bullet <= lock:
            print('Bang!')
            locks.popleft()
            if bullets_counter % gun_size == 0 and bullets:
                print('Reloading!')
            break
        else:
            print('Ping!')
            if bullets_counter % gun_size == 0 and bullets:
                print('Reloading!')

    if not bullets and locks:
        print(f"Couldn't get through. Locks left: {len(locks)}")
        break

earned_sum = intel_value - (bullets_counter * bullet_price)
if not locks:
    print(f"{len(bullets)} bullets left. Earned ${earned_sum}")
