import discord

MSG_MAX_LEN = 2000


class Limits:
    MESSAGE = MSG_MAX_LEN
    EMBED_TOTAL = 6000
    EMBED_TITLE = 256
    EMBED_DESC = 2048
    EMBED_FIELD_NAME = 256
    EMBED_FIELD_VALUE = 1024
    EMBED_FIELD_NUM = 25
    NAME = 32


def check_role(rolelist, message):
    """
    Check if the author of a ``message`` has one of the roles in ``rolelist``.

    :param rolelist: A list of role names.
    :param message: A :cls:``discord.Message`` object representing the message
        to check.
    """
    for role in rolelist:
        # noinspection PyBroadException
        try:
            if discord.utils.get(message.server.roles, name=role) in message.author.roles:
                return True
        except:
            pass
    else:
        return False


def get_named_role(server: discord.Server, role_name: str) -> discord.Role:
    """
    Get a role by name. This is a convenience function, providing a ValueError if the role does not
    exist instead of returning None and causing a less clear exception downstream.

    :param server: Server on which to find the role
    :param role_name: Role name to find
    :return: Discord Role corresponding to the given name
    :raises ValueError: role does not exist
    """
    role = discord.utils.get(server.roles, name=role_name)
    if role is None:
        raise ValueError("Role '{!s}' not found.".format(role_name))
    return role


def user_mention(discord_id: str) -> str:
    return '<@{}>'.format(discord_id)
