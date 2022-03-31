import sys
import os
import discord
TOKEN = "OTU5MDM5NDIzMzU2NDc3NTAw.YkWFEA.LIIffq4hY2F0kyAPBeQmNr8DKEg"

client = discord.Client()

@client.event
async def on_ready():
    print("{0.user} is now online!, WHAT THE FUCK DID YOU DO".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!nep Portal') or message.content.startswith('!portal') or message.content.startswith('!nep portalshake'):
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

    if message.content.startswith('!nep Laugh') or message.content.startswith('!nep lmao') or message.content.startswith('!nep lol'):
        await message.channel.send('https://tenor.com/view/laugh-neptune-neptunia-nep-gif-7234123')

    if message.content.startswith('!nep cmds'):
        await message.channel.send('All Commands: \n'
'(Dont Forget to Use !nep on some[e.g. Fuck you, !nep eat, hee hee hee haw... etc.]) \n'
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
        await message.delete()
        await message.channel.send('Nep nepu nepu nepu nep nep nep https://www.youtube.com/watch?v=EKxio8HZiNA')

    if message.content.startswith('!portalexit'):
        await message.delete()
        await message.channel.send('Exiting Bot.. https://tenor.com/view/goodbye-chat-nep-neptunia-neptune-gif-20677824')
        sys.exit("\n exited")
client.run(TOKEN)