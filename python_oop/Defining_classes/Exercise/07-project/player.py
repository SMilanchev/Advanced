class Player:
    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = "Unaffiliated"

    def add_skill(self, skill_name, mana_cost) -> str:
        skills_list = [s for s in self.skills]
        if skill_name not in skills_list:
            self.skills[skill_name] = mana_cost
            return f"Skill {skill_name} added to the collection of the player {self.name}"
        return "Skill already added"

    def player_info(self):
        player_info = [
            f"Name: {self.name}",
            f"Guild: {self.guild}",
            f"HP: {self.hp}",
            f"MP: {self.mp}",
            ]
        skills_info = [
            f"==={k} - {v}" for k, v in self.skills.items()
        ]

        return "\n".join(player_info + skills_info) + '\n'
