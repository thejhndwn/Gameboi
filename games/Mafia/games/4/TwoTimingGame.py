import time

from games.Mafia.events import GameSystem, GameState, State
from games.Mafia.role import ChickyChickyBangBang


class TwoTimingGame(GameSystem):
    def __init__(self, players, dayWaitMinutes):
        super().__init__("TwoTiming", players,
                         ["BulletProof", "BulletProof", "Magician", "Cop"])
        self.dayWaitMinutes = dayWaitMinutes


class TwoTimingMod(ChickyChickyBangBang):

    def notify(self, event):
        if event.name == GameState.DAY:
            self.event_system.publish(State(GameState.VOTING))
            self
            time.sleep(300-15)
            # TODO: print, if no vote then going to night in 15 seconds
            time.sleep(15)
            # fill with stuff that happens during the day
            self.event_system.publish(State(GameState.NIGHT))
        if event.name == GameState.NIGHT:
            # fill with stuff that happens during the night
            self.event_system.publish(State(GameState.DAY))

        if event.name == GameState.SUBMIT_VOTE:
            pass
