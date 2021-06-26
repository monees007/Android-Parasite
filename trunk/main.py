import os

import discord

# *************************
# sensitive data below -monees007
TOKEN = 'ODU4MjUwODM1NzI0OTkyNTIz.YNbaYA.WwzZ9oPTNLASPbFJMYD8UV2R0ho'
GUILD = 'Parasite'
client = discord.Client()
###########################

@client.event
async def on_ready():
    guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if 'happy birthday' in message.content.lower():
        response = 'Happy Birthday! 🎈🎉'
        await message.channel.send(response)


client.run(TOKEN)
