class BaseGame:
    def __init__(self, players, channel):
        self.players = players
        self.channel = channel

    async def start(self):
        await self.channel.send("Game is starting!")
        # Game-specific logic goes here.
