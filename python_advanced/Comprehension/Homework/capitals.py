countries = input().split(', ')
capitals = input().split(', ')

x = zip(countries, capitals)

countries_with_capitals = {country: capital for (country, capital) in zip(countries, capitals)}
[print(f'{s} -> {c}') for (s, c) in countries_with_capitals.items()]
