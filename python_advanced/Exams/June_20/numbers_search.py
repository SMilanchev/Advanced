def get_missing_value(values):
    min_num = min(values)
    max_nim = max(values)
    diff = {i for i in range(min_num, max_nim + 1, 1)} - set(values)
    missing = ""
    for v in diff:
        missing = v
        break
    return missing


def get_duplicates(numbers):
    ss = set(numbers)
    duplicates = []
    for num in ss:
        current_count = numbers.count(num)
        if current_count > 1:
            duplicates.append(num)

    return duplicates


def numbers_searching(*args):
    missing_value = get_missing_value(args)
    duplicates = get_duplicates(args)
    return [missing_value, duplicates]


print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))