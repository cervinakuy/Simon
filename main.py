import discord
import os

from discord.ext import commands

import constants
from query_manager import QueryManager
from keep_alive import keep_alive
from constants import *

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix=',', intents=intents)
query_manager = QueryManager()


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game("DM me your questions!"))

    query_manager.add_query(["signs", "op", "use"], 2, constants.SIGNS_MESSAGE)
    query_manager.add_query(["top", "leaderboard", "leaderboards"], 1, constants.LEADERBOARD_MESSAGE)
    query_manager.add_query(["command", "format"], 2, constants.COMMAND_FORMAT_MESSAGE)
    query_manager.add_query(["have", "no", "kit"], 3, constants.NO_KIT_MESSAGE)
    query_manager.add_query(["installation", "install", "setup"], 1, constants.INSTALLATION_MESSAGE)
    query_manager.add_query(["permission", "permissions", "deop", "deopped"], 1, constants.PERMISSION_MESSAGE)
    query_manager.add_query(["rank", "prefix", "chat"], 1, constants.RANK_MESSAGE)
    query_manager.add_query(["original"], 1, constants.ORIGINAL_FILES_MESSAGE)
    query_manager.add_query(["config"], 1, constants.CONFIG_FILE_MESSAGE)
    query_manager.add_query(["level", "levels", "experience", "xp"], 1, constants.LEVELS_FILE_MESSAGE)
    query_manager.add_query(["scoreboard"], 1, constants.SCOREBOARD_FILE_MESSAGE)
    query_manager.add_query(["sign"], 1, constants.SIGN_FILE_MESSAGE)
    query_manager.add_query(["streak", "killstreak"], 1, constants.KILLSTREAKS_FILE_MESSAGE)
    query_manager.add_query(["menu"], 1, constants.MENU_FILE_MESSAGE)
    query_manager.add_query(["region", "pvp"], 2, constants.PVP_NOT_PERMITTED_MESSAGE)
    query_manager.add_query(["spectator", "stuck"], 1, constants.FANCY_DEATH_MESSAGE)
    query_manager.add_query(["lose", "losing", "items", "inventory"], 2, constants.INVENTORY_MESSAGE)
    query_manager.add_query(["leave", "return", "clock", "hub"], 1, constants.LEAVE_ITEM_MESSAGE)
    query_manager.add_query(["placeholder", "placeholders", "papi", "placeholderapi"], 1, constants.PLACEHOLDERS_MESSAGE)
    query_manager.add_query(["1v1"], 1, constants.ONEVONE_MESSAGE)
    query_manager.add_query(["unlock", "unlocks"], 1, constants.UNLOCK_KIT_MESSAGE)
    query_manager.add_query(["not", "showing"], 2, constants.SCOREBOARD_NOT_WORKING_MESSAGE)
    query_manager.add_query(["reset", "resetting", "file", "replace"], 1, constants.FILES_RESETTING_MESSAGE)

    print("Finished loading and logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    content = message.content
    author = message.author

    if author == client.user:  # if message is from bot, ignore it
        return

    if len(message.attachments) > 0:  # only allow attachments from https://paste.helpch.at
        attachment_url = message.attachments[0].url
        if attachment_url.endswith(".txt") or attachment_url.endswith(".log") or attachment_url.endswith(".yml"):
            message: discord.Message
            await message.delete()
            await message.channel.send(constants.ONLY_HELPCHAT_ATTACHMENTS.format(author.mention))
            return

    best_response = query_manager.get_best_response(content)

    if best_response is not None:
        channel = message.channel
        if isinstance(channel, discord.TextChannel):
            # only send messages in the #kitpvp and test channel
            if channel.name != "kitpvp" and channel.name != "test-bot-commands":
                return
        await message.channel.send(best_response)  # TODO: try to use quoting system if possible
    else:  # couldn't find a good response to give
        if isinstance(message.channel, discord.DMChannel):  # checking if in a DM
            await message.channel.send(constants.UNSURE_MESSAGE)


@client.event
async def on_member_join(member):
    await member.send(constants.DM_WELCOME_MESSAGE)


keep_alive()
client.run(os.getenv("TOKEN"))
