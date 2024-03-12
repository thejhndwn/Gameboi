import discord
from discord.ext import commands
from lobby_manager import LobbyManager
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')
lobby_manager = LobbyManager(bot)


@bot.command()
async def register(ctx, notify: bool = False):
    """
    Command for players to register for the lobby.
    Players can opt-in for notifications once the player minimum is reached.
    """
    await lobby_manager.register_player(ctx.author, ctx.channel, notify)


@bot.command()
async def startlobby(ctx, game_name: str):
    """
    Command to create a new lobby. The game must be declared.
    Only the lobby creator can start or close the lobby and remove players.
    """
    if game_name in GAME_SETTINGS:
        await lobby_manager.create_lobby(ctx.channel, ctx.author, game_name)
    else:
        await ctx.send("Invalid game specified. Please choose from the available games.")


@bot.command()
@commands.has_permissions()  # Ensure this is usable by admins or extend to check for lobby creator
async def removelobbyplayer(ctx, player: discord.Member):
    """
    Command for the lobby creator or an admin to remove a player from the lobby.
    Checks if the author is the lobby creator for this action.
    """
    await lobby_manager.remove_player(player, ctx.channel, ctx.author)


@bot.command()
async def closelobby(ctx):
    """
    Command to close the lobby. Can only be used by the lobby creator or an admin.
    This checks if the author is the lobby creator.
    """
    await lobby_manager.close_lobby(ctx.channel, ctx.author)


@bot.command()
async def startgame(ctx):
    """Allows the lobby creator to manually start the game."""
    await lobby_manager.start_game(ctx.channel, ctx.author)


bot.run(token)
