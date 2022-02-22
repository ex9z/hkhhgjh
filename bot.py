import random
import discord

TOKEN = 'OTM0NTMzMDgyODMxMjYxNzE2.YexdwQ.97tDhzHnk3uQj3uPis99dzAczUI'

client = discord.Client()


@client.event
async def on_ready():
    print('lolxd {0.user}'.format(client))


@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return

    if message.channel.name == 'sdga':

        if user_message.lower() == '!help':
            await message.channel.send(f'!random , roller , !cf')
            return

        if user_message.lower() == '!random':
            await message.channel.send(f'!random "from" "to"')
            return

        if user_message.lower() == 'roller':
            await message.channel.send(f':wheelchair: KARMA Medical ERGO 500, Invacare Dragon Vertic')
            with open('consoleCD.gif', 'rb') as fh:
                console_gif = discord.File(fh, filename='consoleCD.gif')
            await message.channel.send(file=console_gif)
            return

        elif user_message.startswith('!random'):
            rand_from = int(user_message.split(' ')[1])
            rand_to = int(user_message.split(' ')[2])
            await message.channel.send(f'{random.randint(rand_from, rand_to)}')
            return

        elif user_message.startswith('!cf'):
            a = ['da', 'net', 'mozhet bit']
            await message.channel.send(f'{random.choice(a)}')
            return

        # if user_message.lower() == '!dd':
        #     member = []
        #     x = message.channel.members
        #     for member in x:
        #         print(member)
        #     return


client.run(TOKEN)
