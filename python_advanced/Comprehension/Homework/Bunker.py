def read_input():
    item_categories = input().split(', ')
    n = int(input())
    items = []
    for _ in range(n):
        command = input().split(' - ')
        items.append(command)
    return (items, item_categories)


def add_item_to_bunker(bunker_dict, item, total_quality, total_quantity):
    category, item_name, q_q = item
    quantity = (q_q.split(';')[0]).split(':')
    quality = q_q.split(';')[1].split(':')
    bunker_dict[category][item_name] = {}
    total_quality += int(quality[1])
    total_quantity += int(quantity[1])
    return bunker_dict, total_quality, total_quantity


def print_result(dict_matrix, quality, quantity):
    print('Count of items:', quantity)
    print(f'Average quality: {quality/len(dict_matrix):.2f}')
    for category, item in dict_matrix.items():
        keys = list(dict_matrix[category].keys())
        print(f'{category} -> {", ".join(keys)}')


total_quality = 0
total_quantity = 0
items, item_categories = read_input()
bunker_items = {item: {} for item in item_categories}
for item in items:
    total_quality, total_quantity = add_item_to_bunker(bunker_items, item, total_quality, total_quantity)[1:]

print_result(bunker_items, total_quality, total_quantity)
