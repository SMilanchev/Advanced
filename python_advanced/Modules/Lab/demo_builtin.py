import random
from random import shuffle
from random import shuffle as random_shuffle

fruits =['apple', 'orange', 'banana']
print(fruits)

random.shuffle(fruits)
print(fruits)

shuffle(fruits)
print(fruits)

random_shuffle(fruits)
print(fruits)

print(random.choice(fruits))