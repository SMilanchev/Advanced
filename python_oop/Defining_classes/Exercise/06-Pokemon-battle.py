class Pokemon:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def pokemon_details(self):
        return f"{self.name} with health {self.health}"


class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemon = []

    def add_pokemon(self, pokemon):
        if pokemon in self.pokemon:
            return f"This pokemon is already caught"
        self.pokemon.append(pokemon)
        return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name):
        pokemon_names = [p.name for p in self.pokemon]
        if pokemon_name in pokemon_names:
            del self.pokemon[pokemon_name.index(pokemon_name)]
            return f"You have released {pokemon_name}"
        return "Pokemon is not caught"

    def trainer_data(self):
        new_line = '\n'
        return f"Pokemon trainer {self.name}\nPokemon count {len(self.pokemon)}\n" \
               f"{f'{new_line}'.join([f'{pokemon.pokemon_details()}' for pokemon in self.pokemon])}"


pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())
