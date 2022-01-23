queries = int(input())

query = []

for _ in range(queries):
    current_query = input()
    if current_query == '2':
        if len(query) == 0:
            continue
        query.pop()
    elif current_query == '3':
        print(max(query))
    elif current_query == '4':
        print(min(query))
    else:
        query.append(int(current_query.split()[1]))
print(', '.join(map(str, query[::-1])))
