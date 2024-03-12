from enum import Enum

from games.Mafia.events import GameState, State


class Player:
    def __init__(self, affiliation, items=None, see_self=True):
        if not items:
            items = []

        self.affiliation = affiliation
        self.alive = True
        self.items = items
        self.seeSelf = see_self
        self.modifiers = []

    def notify(self, event):
        # Handle event
        pass


# quote un-quote game manager
class ChickyChickyBangBang(Player):
    def __init__(self, game, event_system):
        super().__init__(Affiliation.THIRD)
        self.game = game
        self.event_system = event_system
        self.votes = 0

    # determine game reactions to state here
    def notify(self, event):
        if event.name == GameState.DAY:
            self.votes = 0
            # fill with stuff that happens during the day
            self.event_system.publish(State(GameState.NIGHT))
        if event.name == GameState.NIGHT:
            self.votes
            # fill with stuff that happens during the night
            self.event_system.publish(State(GameState.DAY))


class Affiliation(Enum):
    TOWN = "Town"
    MAFIA = "Mafia"
    THIRD = "Third-party"
    NEUTRAL = "Neutral"
