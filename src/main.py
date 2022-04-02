import sys
import os
import discord
import random

TOKEN = "***************************************************************************"

client = discord.Client()

@client.event
async def on_ready():
    print("{0.user} is now online!, WHAT THE FUCK DID YOU DO".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!nep i hate you'):
        await message.channel.send(random.choice(('i hate you', 'i hate you 2', 'i hate you 3', 'i hate you 4', 'i hate you 5', 'i hate you 6', 'i hate you 7', 'i hate you 8', 'i hate you 9', 'i hate you 10')))

    if message.content.startswith('!nep close'):
        await message.channel.send('https://tenor.com/view/nep-anime-gif-9559443')

    if message.content.startswith('!nep kiss'):
        await message.channel.send(random.choice(('https://cdn.discordapp.com/attachments/959206269665816576/959216741056139314/nepgear_and_if_neptune_and_1_more_drawn_by_tsunako__b80c64c22437faaf59b463f414746e5e.png', 'https://cdn.discordapp.com/attachments/959206269665816576/959216740678647828/neptune_and_noire_neptune_drawn_by_ge_b__a875582698db0a7db1c48766df17de3f.jpg', 'https://cdn.discordapp.com/attachments/959206269665816576/959216740359868486/purple_heart_and_noire_neptune_drawn_by_hatyo__4c7738dcb8c389e820831ef4f16d5989.png')))

    if message.content.startswith('!nep Portal') or message.content.startswith('!portal') or message.content.startswith('!nep portalshake'):
        await message.delete()
        await message.channel.send('https://cdn.discordapp.com/attachments/862787478993633303/959190281620717588/image0.gif')

    if message.content.startswith('Fuck you') or message.content.startswith('Fuck') or message.content.startswith('!nep default dance'):
        await message.channel.send('https://tenor.com/view/nepgear-default-dance-fortnite-nepgear-default-dance-neptunia-gif-18019869')

    if message.content.startswith('!nep eat') or message.content.startswith('!nep eat') or message.content.startswith('!nep yummy'):
        await message.channel.send('https://tenor.com/view/hyperdimension-neptunia-neptunia-neptune-eating-anime-gif-20677174')

    if message.content.startswith('!nep board') or message.content.startswith('!nep sad') or message.content.startswith('!nep dissapointment'):
        await message.channel.send('https://tenor.com/view/neptunia-neptune-anime-gif-10069801')

    if message.content.startswith('!nepu happy') or message.content.startswith('!nep happy'):
        await message.delete()
        await message.channel.send('https://tenor.com/view/neptune-hyperdimension-neptunia-neptunia-eeeeh-happy-gif-21648169')

    if message.content.startswith('!nepu dance') or message.content.startswith('!nep dance'):
        await message.delete()
        await message.channel.send('https://tenor.com/view/nepu-nepu-dance-gif-22679721')

    if message.content.startswith('!nep gib') or message.content.startswith('!nep gift') or message.content.startswith('!nep give'):
        await message.channel.send('https://tenor.com/view/hyperdimension-neptunia-neptunia-neptune-waifu-give-me-gif-23730814')

    if message.content.startswith('hee hee hee haw') or message.content.startswith('hee hee hee hee haw') or message.content.startswith('hee hee haw'):
        await message.channel.send('https://tenor.com/view/hehehehaw-so-funny-bro-gif-24674409')

    if message.content.startswith('gn') or message.content.startswith('goodbye') or message.content.startswith('bye') or message.content.startswith('goodnight'):
        await message.channel.send('https://tenor.com/view/goodbye-chat-nep-neptunia-neptune-gif-20677824')

    if message.content.startswith('!nep angry'):
        await message.delete()
        await message.channel.send('https://tenor.com/view/neptune-neppy-nep-neptunia-slap-gif-12773268')

    if message.content.startswith('!nep laugh') or message.content.startswith('!nep lmao') or message.content.startswith('!nep lol'):
        await message.channel.send('https://tenor.com/view/laugh-neptune-neptunia-nep-gif-7234123')

    if message.content.startswith('!nep cmds'):
        await message.channel.send('All Commands: \n'
'(Dont Forget to Use !nep on some[e.g. Fuck you, !nep eat, hee hee hee haw... etc.]) \n'
'!nep i hate you - i hate you "(random 2-10 or nothing)" (Suggestion by PortalScout#5458) \n'
'!nep kiss - nep kiss! (Suggestion by Bun Bun#4827) \n'
'!nep portal, !portal, !nep portalshake - Portal does the funi \n'
'nep nep, - See for yourself \n'
'Fuck you - Nep dances, \n'
'Nep eat - Nep eats, \n'
'nepu board/sad - nep is sad or dissapointed, \n'
'gib - Aksed to give, \n'
'nepu dance - dance with the 4 anime girls from neptune, \n'
'nepu happy! - nepu is getting exited, \n'
'Laugh - laughs, \n'
'hee hee hee hee haw - hee hee hee haw, \n'
'angry - nep is angry, \n'
'gn, goodbye... - Bye gif \n '
'!portaldebug - test, \n'
'Morning - send sticker, \n '
'!nep cmds - Shows This \n'
'nnn - sends a meme, \n '
'nepmeme - sends a meme, \n '
'topnep - 420nepblazeit,  \n '
'!portalexit - Turns off the bot. Do not run! (i am looking at you portal) \n ')

    if message.content.startswith('!portaldebug') or message.content.startswith('!protaldebug'):
        await message.delete()
        await message.channel.send('(Exited With Code -1) No Content Supplied, Exiting Bot..')

    if message.content.startswith('!nep morning'):
        await message.delete()
        await message.channel.send('https://cdn.discordapp.com/attachments/723588264803434518/959067172624277614/unknown.png')

    if message.content.startswith('!nep nnn'):
        await message.delete()
        await message.channel.send('https://cdn.discordapp.com/attachments/723588264803434518/959067287917305856/unknown.png')

    if message.content.startswith('!nepmeme'):
        await message.delete()
        await message.channel.send('https://cdn.discordapp.com/attachments/723588264803434518/959067201590149140/unknown.png')
        
    if message.content.startswith('!nep nep') or message.content.startswith('nepnep') or message.content.startswith('neptune'):
        await message.delete()
        await message.channel.send('https://tenor.com/view/ngl-i-find-this-appealing-neptune-neptunia-hyperdimension-neptunia-ngl-i-find-neptune-quite-appealing-gif-23250736')
        
    if message.content.startswith('!topnep'):
        await message.delete()
        await message.channel.send('https://cdn.discordapp.com/attachments/723588264803434518/959066447143899136/unknown.png')

    if message.content.startswith('nep nep'):
        await message.channel.send('Nep nepu nepu nepu nep nep nep https://www.youtube.com/watch?v=EKxio8HZiNA')

    if message.content.startswith('!nepportalexit'):
        await message.delete()
        await message.channel.send('Exiting Bot.. https://tenor.com/view/goodbye-chat-nep-neptunia-neptune-gif-20677824')
        sys.exit("\n exited")
client.run(TOKEN)
