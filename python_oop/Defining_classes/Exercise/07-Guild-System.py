class Player:
    def __init__(self, name, hp, mp):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = "Unaffiliated"

    def add_skill(self, skill_name, mana_cost):
        skills_list = [s for s in self.skills]
        if skill_name not in skills_list:
            self.skills[skill_name] = mana_cost
            return f"Skill {skill_name} added to the collection of the player {self.name}"
        return "Skill already added"

    def player_info(self):
        new_line = '\n'
        return f"Name: {self.name}\n" \
               f"Guild: {self.guild}\n" \
               f"HP: {self.hp}\n" \
               f"MP: {self.mp}\n" \
               f"{f'{new_line}'.join([f'==={k} - {v}' for k, v in self.skills.items()])}\n"


class Guild:
    def __init__(self, name):
        self.name = name
        self.list_of_players = []

    def assign_player(self, player: Player):
        players = [p for p in self.list_of_players]
        if player not in players and player.guild == "Unaffiliated":
            self.list_of_players.append(player)
            player.guild = self.name
            return f"Welcome player {player.name} to the guild {self.name}"
        elif player in players:
            return f"Player {player} is already in the guild"
        else:
            return f"Player {player} is in another guild"

    def kick_player(self, player_name):
        players = [p for p in self.list_of_players]
        if player_name in players:
            del self.list_of_players[self.list_of_players.index(player_name)]
            return f"Player {player_name} has been removed from the guild"
        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        return f"Guild: {self.name}\n" \
               f"{player.player_info()}"


player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())
