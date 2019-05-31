import discord
from random import randint
from time import sleep

client = discord.Client()

game_started = False
night = False
day = False

players = {1:"Кек", 2:"Сас", 3:"Пуп", 4:"Лол"}
mafia = {}
civil = {}


i = 1
channel = 0
#_______ответ на меседжи________
@client.event
async def on_message(message):
    print(message.content)
    global game_started
    global i
    global night
    global day
    global channel
    guild = message.guild
# ________________Рега_______________________
    if message.content.find ("!join") != -1 and game_started == False:
        print(players)
        if len(players) <= 3:
            players[1 + len(players)] = str(message.author.name)
            await message.channel.send("в игре участвуют:")
            await message.channel.send(players)
            await message.channel.send ("для старта необходимо еще: " + str(5-len(players))+" игрока")
        elif len(players) <= 4 and game_started == False:
            players[1 + len(players)] = str(message.author.name)
            await message.channel.send("в игре участвуют:")
            await message.channel.send(players)
            await message.channel.send("Для начала игры введите start")
            game_started = True
            print(game_started)
#_______________Игровой цикл_________________
    if message.content.find ("!start") != -1 and game_started == True:
        await message.channel.send("Игра начнется через 5 секунд")
        await guild.create_role(name = "Игрок")
        await guild.create_role(name = "Игрoк")
        await guild.create_text_channel("мафиозники")
        #_______жеребьевка________________________
        while i <= len(players):
            sidecheck = randint(0, 1)
            if sidecheck == 0 and len(mafia) == 0:
                mafia[1 + len(mafia)] = players[i]
            elif sidecheck == 0 and len(mafia) == 1:
                civil[1 + len(civil)] = players[i]
            elif sidecheck == 1 and len(mafia) == 0:
                mafia[1 + len(mafia)] = players[i]
            elif sidecheck == 1:
                civil[1 + len(civil)] = players[i]
            i = i+1
        print(mafia)
        print(civil)
        #______________________________________
        await message.channel.send("Чтобы узнать вашу крату введите side")
        sleep(5)
        await message.channel.send("Наступила ночь, мафиозники выбирают кого завалить")
    if message.content.find ("Мафия убила ") != -1 and message.author.name == "Зубенко Михаил Петрович":
        await message.channel.send("Наступил день.")
    if message.content.find (" был мирным!") != -1 and message.author.name == "Зубенко Михаил Петрович":
        await message.channel.send("Наступила ночь, мафиозники выбирают кого завалить")



#___________________________________голосование мафии_____________________________
    if message.content.find("Наступила ночь, мафиозники выбирают кого завалить") != -1 and message.author.name == "Зубенко Михаил Петрович":
        night = True
        channel = discord.utils.get(guild.channels, name="мафиозники")
        await channel.send ("Чтобы убить игрока напишите shoot # с номером нужного игрока")
        await channel.send(players)
    if message.content.find("!shoot 1") != -1 and message.channel == channel and night == True:
        channel = discord.utils.get(guild.channels, name="general")
        await channel.send("Мафия убила " + players[1])
        del players[1]
        night = False
    if message.content.find("!shoot 2") != -1 and message.channel == channel and night == True:
        channel = discord.utils.get(guild.channels, name="general")
        await channel.send("Мафия убила " + players[2])
        del players[2]
        night = False
    if message.content.find("!shoot 3") != -1 and message.channel == channel and night == True:
        channel = discord.utils.get(guild.channels, name="general")
        await channel.send("Мафия убила " + players[3])
        del players[3]
        night = False
    if message.content.find("!shoot 4") != -1 and message.channel == channel and night == True:
        channel = discord.utils.get(guild.channels, name="general")
        await channel.send("Мафия убила " + players[4])
        del players[4]
        night = False
    if message.content.find("!shoot 5") != -1 and message.channel == channel and night == True:
        channel = discord.utils.get(guild.channels, name="general")
        await channel.send("Мафия убила " + players[5])
        del players[5]
        night = False
    # ___________________________________голосование мирных_____________________________
    if message.content.find ("Наступил день.") != -1 and message.author.name == "Зубенко Михаил Петрович" and len(players) == 2:
            await message.channel.send("Мафиозники победили!")
    elif message.content.find ("Наступил день.") != -1 and message.author.name == "Зубенко Михаил Петрович":
        day = True
        await message.channel.send ("Чтобы начать голосование напишите vote")
    if message.content.find("!vote") != -1 and day == True:
        await channel.send("Голосование началось!")
        await channel.send("Напишите kill # с номером предполагаемого мафиозника, и я устраню его!")
        await channel.send(players)
    if message.content.find("!kill 1") != -1 and day == True:
        for position, name in civil.items():
            if name == players[1]:
                await message.channel.send(str(players[1]) + " был мирным!")
                del players[1]
                day = False
                if len(players) == 2:
                    await message.channel.send("Мафиозники победили!")
        for position, name in mafia.items():
            if name == players[1]:
                await message.channel.send(str(players[1]) + " был мафиозником!")
                await message.channel.send("Мирные победили!")
    if message.content.find("!kill 2") != -1 and day == True:
        for position, name in civil.items():
            if name == players[2]:
                await message.channel.send(str(players[2]) + " был мирным!")
                del players[2]
                day = False
                if len(players) == 2:
                    await message.channel.send("Мафиозники победили!")
        for position, name in mafia.items():
            if name == players[2]:
                await message.channel.send(str(players[2]) + " был мафиозником!")
                await message.channel.send("Мирные победили!")
    if message.content.find("!kill 3") != -1 and day == True:
        for position, name in civil.items():
            if name == players[3]:
                await message.channel.send(str(players[3]) + " был мирным!")
                del players[3]
                day = False
                if len(players) == 2:
                    await message.channel.send("Мафиозники победили!")
        for position, name in mafia.items():
            if name == players[3]:
                await message.channel.send(str(players[3]) + " был мафиозником!")
                await message.channel.send("Мирные победили!")
    if message.content.find("!kill 4") != -1 and day == True:
        for position, name in civil.items():
            if name == players[4]:
                await message.channel.send(str(players[4]) + " был мирным!")
                del players[4]
                day = False
                if len(players) == 2:
                    await message.channel.send("Мафиозники победили!")
        for position, name in mafia.items():
            if name == players[4]:
                await message.channel.send(str(players[4]) + " был мафиозником!")
                await message.channel.send("Мирные победили!")
    if message.content.find("!kill 5") != -1 and day == True:
        for position, name in civil.items():
            if name == players[5]:
                await message.channel.send(str(players[5]) + " был мирным!")
                del players[5]
                day = False
                if len(players) == 2:
                    await message.channel.send("Мафиозники победили!")
        for position, name in mafia.items():
            if name == players[5]:
                await message.channel.send(str(players[5]) + " был мафиозником!")
                await message.channel.send("Мирные победили!")

#_____________________________Победа______________________________________
    if message.content.find("Мирные победили!") != -1 and message.author.name == "Зубенко Михаил Петрович":
        await message.channel.send("Игра окончена!")
        game_started = False
        night = False
        players.clear()
        mafia.clear()
        civil.clear()
        day = False
        i = 1
    elif message.content.find("Мафиозники победили!") != -1 and message.author.name == "Зубенко Михаил Петрович":
        await message.channel.send("Игра окончена!")
        game_started = False
        night = False
        players.clear()
        mafia.clear()
        civil.clear()
        day = False
        i = 1

#_______________Отправка ролей в пм_________________________________
    if message.content.find("!side") != -1 and game_started == True:
        print(message.author.name)
        for position, name in mafia.items():
            if name == message.author.name:
                await message.author.send("Ты мафиозник!")
                role = discord.utils.get(message.guild.roles, name="Игрок")
                user = message.author
                await user.add_roles(role)
        for position, name in civil.items():
            if name == message.author.name:
                await message.author.send("Ты горожанин!")
                role = discord.utils.get(message.guild.roles, name="Игрок")
                user = message.author
                await user.add_roles(role)







client.run("NTc4MzE5MzU0NDA0NDA1MjUw.XN_5LA.wANJT2w9AnSNHBDRLOp3CytlbiI")
