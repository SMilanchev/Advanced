from typing import List
from .player import Player


class Team:
    __name: str
    __rating: int
    __players: List[Player]

    def __init__(self, name: str, rating: int):
        self.__name = name
        self.__rating = rating
        self.__players = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, new_rating):
        self.__rating = new_rating

    @property
    def players(self):
        return self.__players

    @players.setter
    def players(self, new_players):
        self.__players = new_players

    def add_player(self, player: Player):
        if player in self.__players:
            return f"Player {player.name} has already joined"
        self.__players.append(player)
        return f"Player {player.name} joined team {self.name}"

    def remove_player(self, player_name: str):
        players = [p.name for p in self.__players]
        if player_name in players:
            player = self.__players.pop(players.index(player_name))
            return player
        return f"Player {player_name} not found"

