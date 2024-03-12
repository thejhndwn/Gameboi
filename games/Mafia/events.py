import random
from enum import Enum

from games.Mafia.role import ChickyChickyBangBang


class State:
    def __init__(self, name, data=None):
        self.name = name
        self.data = data


class GameSystem:
    def __init__(self, name, players, roles):
        self.name = name
        self.state = set()  # holds the state of the game
        self.subscribers = {}  # table of all event-subscribers
        self.players = players  # player names to player-instances
        self.game_mod = ChickyChickyBangBang(self, self.name)
        self.roles = roles

    def assign_roles(self):
        role_instances = [globals()[role_name]() for role_name in self.roles]

        # Randomly assign roles to players
        random.shuffle(role_instances)
        self.players = {name: role for name, role in zip(self.players, role_instances)}

    def subscribe(self, event_name, callback):
        if event_name not in self.subscribers:
            self.subscribers[event_name] = []
        self.subscribers[event_name].append(callback)

    def publish(self, event):
        for callback in self.subscribers.get(event.name, []):
            callback(event)

    def start_game(self):
        self.assign_roles()
        self.publish(State(GameState.DAY))

    def add_state(self, game_state):
        self.


class GameState(Enum):
    DAY = "DAYSTART"
    NIGHT = "NIGHTSTART"
    VOTING = "voting"
    GAME_OVER = "game_over"
    GUN_SHOT = "gun_shot"
    USE_ITEM = "USEITEM"
    SUBMIT_VOTE = "SUBMIT_VOTE"


class Item(Enum):
    GUN = "GUN"
    VEST = "VEST"
