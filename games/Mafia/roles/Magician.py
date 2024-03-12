from games.Mafia.events import Item, GameState
from games.Mafia.role import Player, Affiliation


class Magician(Player):
    def __init__(self, event_system):
        super().__init__(Affiliation.MAFIA, [Item.GUN], event_system)

    def notify(self, event):
        name = event.name





