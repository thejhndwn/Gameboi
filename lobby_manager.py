import asyncio

import bot

# This could be expanded or loaded from a configuration file/database in the future.
GAME_SETTINGS = {
    'game_x': {'min_players': 4},
    'game_y': {'min_players': 2},
    # Add new games and their settings here
}


class Lobby:
    def __init__(self, game_name, channel, creator):
        self.game_name = game_name
        self.channel = channel
        self.players = {}
        self.countdown_started = False
        self.game_settings = GAME_SETTINGS.get(game_name, {})
        self.min_players = self.game_settings.get('min_players', 2)  # Default to 2 if not specified

    async def add_player(self, player, notify=False):
        self.players[player] = notify
        await self.channel.send(f"{player.display_name} has joined the lobby for {self.game_name}.")
        if len(self.players) >= self.min_players and not self.countdown_started:
            self.countdown_started = True
            await self.start_countdown()

    async def start_countdown(self):
        """Start a countdown before automatically starting the game."""
        await self.channel.send("Enough players have joined. Starting in 1 minute...")
        self.countdown_started = True
        await asyncio.sleep(60)  # 1-minute countdown

    async def remove_player(self, player):
        """Remove a player from the lobby."""
        if player in self.players:
            del self.players[player]
            await self.channel.send(f"{player.display_name} has been removed from the lobby.")

    async def start_game(self, requested_by):
        """Starts the game, ensuring it's either requested by the creator or automatically after enough players join."""
        if requested_by or (self.countdown_started and len(self.players) >= self.min_players):
            await self.channel.send("The game is starting now!")
            # Here, you would transition to the game logic, possibly instantiating a game object based on game_name
            # Example: game = games[self.game_name](self.players, self.channel)
            # await game.start()
        else:
            await self.channel.send("Only the lobby creator can start the game early.")

    async def reset_lobby(self):
        # Reset lobby but keep the game and creator
        self.players = {}
        self.countdown_started = False
        await self.channel.send("The game has ended. The lobby is now open for new registrations.", ephemeral=True)


class LobbyManager:
    def __init__(self):
        self.lobbies = {}  # key: channel_id, value: Lobby
        self.creator = []

    async def create_lobby(self, channel, creator, game_name):
        if channel.id not in self.lobbies and game_name in GAME_SETTINGS:
            lobby = Lobby(game_name, channel, creator)
            self.lobbies[channel.id] = lobby
            self.creator.append(creator)
            await channel.send(f"{creator.display_name} has created a lobby for {game_name}.")
            # Optionally handle role assignment to the lobby creator here
        else:
            await channel.send("A lobby already exists in this channel or the game is not recognized.")

    async def register_player(self, player, channel, notify=False):
        """Register a player to the lobby in the channel."""
        if channel.id in self.lobbies:
            await self.lobbies[channel.id].add_player(player, notify)
        else:
            await channel.send("No active lobby to register in this channel.")

    async def remove_player(self, player, channel):
        """Remove a player from the lobby."""
        if channel.id in self.lobbies:
            await self.lobbies[channel.id].remove_player(player)

    async def close_lobby(self, channel):
        """Close the lobby in the channel."""
        if channel.id in self.lobbies:
            del self.lobbies[channel.id]
            await channel.send("The lobby has been closed.")

    async def start_game(self, channel, requested_by):
        """Starts the game if requested by the lobby creator or automatically by the system."""
        lobby = self.lobbies.get(channel.id)

        # bot.load_dotenv('cogname')

        if lobby and (requested_by == lobby.creator or lobby.start_requested):
            await lobby.start_game(requested_by)
        else:
            await channel.send("No game to start or you don't have permission to start the game.")
