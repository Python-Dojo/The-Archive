
"""
This file contains the discord bot for the python dojo

The intention is to aid the Sensei in their ability to do medial tasks
    e.g. Split teams into groups
"""


help_text:str = """ When given argument of 1, 2 or 3 script will create that many replits and link them in the 
discord via webhooks
"""

from typing import TYPE_CHECKING
from datetime import datetime as DateTime
from datetime import timedelta as TimeDelta
import discord
from discord.ext import commands
import text
from os import getenv as get_env

if TYPE_CHECKING:
    from discord.ext.commands.context import Context
    from discord import Message
    from typing import AsyncIterator, Mapping, Type, TypeVar, Literal

def get_from_env(key:str, default:str|None = None) -> str:
    env_var = get_env(key, default)
    if env_var is None:
        exit(f'Could not find envioment variable "{key}", please set it')
    return env_var

# Get token from env var
TOKEN = get_from_env("DISCORD_TOKEN")
WELCOME_CHANNEL_ID = 10
DATABASE_CHANNEL_ID = 11
IDEAS_CHANNEL_ID = 12
BOT_LOG_CHANNEL_ID = 13

# TODO:
#  [X] Remove token from file and have it be configurable
#  [ ] Reduce the amount of stuff run when imported especially asserts for testing
#       Going to do this with mocking instead
#  [ ] Refactor functions to small functions (max 20 lines)
#  [ ] Have channel ids be configurable to have it work on a test server easier
#  [ ] Have a backup if the channel ID is wrong based on the channel name
#  [ ] Avoid non-"const" globals where possible
#  [ ] __name__ == "__main__" on random files is okay (for quick manual testing)
#  [ ] add unit tests
#  [ ] rename elo to something more relevant (it's a value from 0-10)
#  [ ] fix database to store user ids not mentions as we can't mention users that are not in 

# TODO Refactor using Ray's preferred style/formatting
#  Where a string is used prefer double quotes unless otherwise stated
#  Where a string is treated as a character (e.g. x in `for x in string`) use apostrophe over quote
#  Where a string contains quote characters (") use apostrophe over quotes (e.g `'error message was "'`)
#  Small functions always
#  Complex boolean logic (more than 1 operator in a condition) should be split out into one of:
#   a function
#   variables
#   separated with brackets
#  If the code contains a try except statement, as little code should be in said statement as possible
#  Avoid all shortened variable names including a, i and f

intents = discord.Intents.default()
intents.message_content = True; # Required for sending DMs
# activity = discord.BaseActivity() # Set to something interesting?
# client = discord.Client(intents=intents, max_messages=10)
# discord.app_commands.AppCommandContext
client = commands.Bot('!', intents=intents)
WELCOME_CHANNEL = client.get_channel(WELCOME_CHANNEL_ID)
DATABASE_CHANNEL = client.get_channel(DATABASE_CHANNEL_ID)
IDEAS_CHANNEL = client.get_channel(IDEAS_CHANNEL_ID)
BOT_LOG_CHANNEL = client.get_channel(BOT_LOG_CHANNEL_ID)
assert isinstance(WELCOME_CHANNEL, discord.TextChannel)
assert isinstance(DATABASE_CHANNEL, discord.TextChannel)
assert isinstance(IDEAS_CHANNEL, discord.TextChannel)
assert isinstance(BOT_LOG_CHANNEL, discord.TextChannel)

ADMIN_ROLE = "sensei"

async def log(message:str):
    if TYPE_CHECKING:
        assert isinstance(BOT_LOG_CHANNEL, discord.TextChannel)
    await BOT_LOG_CHANNEL.send(message)


async def get_active_users(channel:discord.TextChannel, *, messages_to_scan:int=50, active_since:DateTime | None = None) -> set[discord.User | discord.Member]:
    async def add_users_from_message(users: set[discord.User | discord.Member] , message:discord.Message):
        users.add(message.author)
        a = {r.users() for r in message.reactions}
        for i in a:
            users.update({u async for u in i})
    channel_history = channel.history(limit=messages_to_scan, after=active_since)
    users = set()
    [ await add_users_from_message(users, message) async for message in channel_history]
    return users

def is_id(unknown_str:str) -> bool:
    try:
        id = int(unknown_str)
        return id > 1000
    except:
        return False

async def get_user_experience(active_users:set[discord.User | discord.Member]):
    """
    Gets the experience of the active users passed in

    returns a dict of user:experience where experience is -1 if unknown
    """
    active_user_ids = { user.id : user for user in active_users}
    user_stats:"dict[discord.User | discord.Member, float]" = {u : -1 for u in active_users}
    async for message in DATABASE_CHANNEL.history(limit=None):
        # only mods will have access to this channel so don't do author checking
        # Messages will look like:
        #"012043290 902410529104 214905318924190 9.0"
        
        # so all users with ids in message have experience 9.0
        # where 012043290 is a user id

        # TODO: You can't mention public users in a private channel so we need their IDs instead 
        message_content = message.clean_content.split()
        ids = {int(id) for id in message_content[:-1] }
        experience = float(message_content[-1])
        
        # filter the ids to active users only
        for id in ids:
            if id in active_user_ids.keys():
                user_stats[active_user_ids[id]] = experience
    return user_stats

@client.event
async def on_ready():
    print("On ready received")

@client.command("start", help_text=text.START_SESSION_HELP)
@client.command("start_session", help_text=text.START_SESSION_HELP)
@commands.has_role(ADMIN_ROLE)
async def start_session(context:"Context"):
    # get users from history
    ONE_HOUR_AGO = DateTime.now() - TimeDelta(hours=1)
    MAX_MESSAGES_TO_SCAN:int = 50
    # `typing` acts as a loading visualisation here
    async with context.channel.typing():
        if TYPE_CHECKING: 
            # Done further up at runtime
            assert isinstance(WELCOME_CHANNEL, discord.TextChannel)
            assert isinstance(IDEAS_CHANNEL, discord.TextChannel)
            assert isinstance(DATABASE_CHANNEL, discord.TextChannel)

        users = await get_active_users(WELCOME_CHANNEL, messages_to_scan=MAX_MESSAGES_TO_SCAN, active_since=ONE_HOUR_AGO)

        if hasattr(context.channel, "history") and callable(context.channel.history) and context.channel.id != WELCOME_CHANNEL_ID:
            users.update(await get_active_users(context.channel, messages_to_scan=MAX_MESSAGES_TO_SCAN, active_since=ONE_HOUR_AGO))
        if context.channel.id != IDEAS_CHANNEL_ID:
            users.update(
                await get_active_users(IDEAS_CHANNEL, messages_to_scan=MAX_MESSAGES_TO_SCAN, active_since=ONE_HOUR_AGO)
            )

        # get users from database (a channel) and find their rank
        user_stats = await get_user_experience(users)
        # this gives us a dict of user : experience and experience = -1 if unknown

        # split into groups




@client.command("calender", help_text="Shows a calender describing when events happen")
async def send_calender(ctx:"Context"):
    await ctx.channel.send(text.EVENT_CALENDER_TABLE)


@client.command("codehub", help_text="Tells you about codehub")
# does adding the same thing as two commands like this work?
@client.command("hosts", help_text="Tells you about codehub")
async def send_codehub_message(ctx:"Context"):
    await ctx.channel.send(text.make_codehub_explination_text(event_command="event"))

# @client.event
# async def on_message(message:"Message"):
#     """
#         Adds all the messages to a log, to get all the users who are active in the session
#         These users can then be split into groups later
#     """
#     client_user = client.user # if None, something went wrong
#     sender = message.author
#     if (client_user is None) or (sender.id == client_user.id) or sender.bot or sender.system:
#         # Skip this message, from people we don't like
#         return
#     # Cannot get the message's timestamp but now should be fine
#     messages.append((message, DateTime.now()))


# def is_private_channel(ctx:"Context"): # takes context? perms? idk
#     if ctx.guild is None:
#         return
#     guild:discord.Guild = ctx.guild
#     guild.channels.
#     return true

# Ignore this and just edit the database (stored in a channel) directly instead
# @client.command("elo",help_text='Control the "elo" of the given user/s first argument must be one of + for upping or - for downing or = for getting')
# @commands.has_role("sensei")
# @commands.check(is_private_channel)
# async def increase_elo(ctx:"Context", action:str, *users:str):
#     if any([ x in action for x in "+ - =".split()]):
#         await ctx.channel.send("No +, - or = in command")
#         return
    
# @client.event
# async def on_member_join(member:discord.Member):
#     if TYPE_CHECKING:
#         # We did the real assert at start up
#         assert isinstance(WELCOME_CHANNEL, discord.TextChannel)

#     async with WELCOME_CHANNEL.typing():
#         dms = await member.create_dm()
#         await dms.send()
#     .send("Hello")
    
    



