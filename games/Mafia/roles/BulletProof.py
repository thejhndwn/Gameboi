from games.Mafia.events import Item
from games.Mafia.role import Player, Affiliation


class BulletProof(Player):
    def __init__(self):
        super().__init__(Affiliation.TOWN, [Item.VEST])