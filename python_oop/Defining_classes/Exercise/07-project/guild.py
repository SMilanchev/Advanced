from .player import Player


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

    def kick_player(self, player_name: str):
        players = [p for p in self.list_of_players]
        if player_name in players:
            del self.list_of_players[self.list_of_players.index(player_name)]
            return f"Player {player_name} has been removed from the guild"
        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        guild_info = [f"Guild: {self.name}"]
        player_info = [p.player_info() for p in self.list_of_players]
        return "\n".join(guild_info + player_info)
