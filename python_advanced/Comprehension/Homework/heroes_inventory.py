def read_input():
    names = input().split(', ')
    heroes_items = []
    while True:
        command = input().split('-')
        if 'End' in command:
            return heroes_items, names
        heroes_items.append(command)


def add_item_to_hero(dict, hero, item, price):
    if item not in dict[hero]:
        dict[hero][item] = int(price)


def print_result(dict):
    for item, v in dict.items():
        print(f'{item} -> Items: {len(v)}, Cost: {sum(v.values())}')


heroes_items, names = read_input()
heroes_dict = {name: {} for name in names}
for hero in heroes_items:
    name, item, price = hero
    add_item_to_hero(heroes_dict, name, item, price)


print_result(heroes_dict)
