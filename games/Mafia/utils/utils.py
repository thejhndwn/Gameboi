from functools import wraps


def role_required(allowed_roles):
    def decorator(func):
        @wraps(func)
        async def wrapper(ctx, *args, **kwargs):
            game = get_current_game(ctx.channel.id)  # Retrieve the game instance
            player = game.players.get(ctx.author.name)  # Get the player instance
            if player and player.role.name in allowed_roles:
                return await func(ctx, *args, **kwargs)
            else:
                await ctx.send("You do not have permission to use this command.")

        return wrapper

    return decorator


def state_required(allowed_roles):
    def decorator(func):
        @wraps(func)
        async def wrapper(ctx, *args, **kwargs):
            game = get_current_game(ctx.channel.id)  # Retrieve the game instance
            state = game.state  # Get the player instance
            if state & allowed_roles:
                return await func(ctx, *args, **kwargs)
            else:
                await ctx.send("Hitman Carrleone says, \"There's a time and place for everything, but not now\"")

        return wrapper

    return decorator

def