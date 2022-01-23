jobs = list(map(int, input().split(', ')))
interested_task = int(input())
num_interested_task = jobs[interested_task]
counter = 0

for i in range(len(jobs)):
    num = jobs[i]
    if num < num_interested_task:
        counter += num
    elif num == num_interested_task and i <= interested_task:
        counter += num

print(counter)