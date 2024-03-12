from games.Mafia.events import Item, GameState
from games.Mafia.role import Player, Affiliation


class Cop(Player):
    def __init__(self, event_system):
        super().__init__(Affiliation.TOWN, [], event_system)

    def notify(self, event):
        name = event.name

