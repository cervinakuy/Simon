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

participating_channels: list = ["test-bot-commands"]


@client.event
async def on_ready():
    #################################
    #   Custom activity status      #
    #################################
    await client.change_presence(activity=discord.Game("DM me your questions!"))

    ##################################
    #   Question / query handling    #
    ##################################
    query_manager.add_query(["download", "Simon", "source"], 2, constants.SIMON_SOURCE_CODE)
    print("Finished loading and logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    content = message.content
    author = message.author

    if author == client.user:  # if message is from bot, ignore it
        return

    ####################################
    #   Text attachment requirement    #
    ####################################
    if len(message.attachments) > 0:
        attachment_url = message.attachments[0].url
        if attachment_url.endswith(".txt") or attachment_url.endswith(".log") or attachment_url.endswith(".yml"):
            message: discord.Message
            await message.delete()  # delete attachment that was posted
            await message.channel.send(constants.ONLY_PASTEBIN_ATTACHMENTS.format(author.mention))
            return

    best_response = query_manager.get_best_response(content)

    if best_response is not None:  # if an appropriate response was found
        channel = message.channel
        if isinstance(channel, discord.TextChannel):  # checking if text channel
            ####################################
            # Active only in specific channels #
            ####################################
            if channel.name not in participating_channels:
                return
        await message.channel.send(best_response)
    else:  # couldn't find a good response to give
        ####################################
        #  Send automated responses in DM  #
        ####################################
        if isinstance(message.channel, discord.DMChannel):  # checking if in a DM
            await message.channel.send(constants.UNSURE_MESSAGE)


@client.event
async def on_member_join(member):
    ####################################
    #        DM welcome message        #
    ####################################
    await member.send(constants.DM_WELCOME_MESSAGE)


# keep_alive.py and the below lines are only necessary if using free Discord bot hosting (see guide below):
# https://medium.com/geekculture/how-to-make-your-own-discord-bot-9505173a4f6a
# otherwise, these lines and keep_alive.py can safely be deleted
keep_alive()
client.run(os.getenv("TOKEN"))
