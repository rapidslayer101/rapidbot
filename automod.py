import discord, datetime, pandas, time, re
from datetime import timedelta
from discord.ext import commands
bot = commands.Bot(command_prefix=commands.when_mentioned_or("-"))
bot.remove_command('help')

stime = datetime.datetime.now()

version = "1.8"


@bot.event
async def on_connect():
    import psutil
    print('Connection established to discord, Logged in as {0} ({0.id})'.format(bot.user))
    print('-----------------------------------------------')
    print("cpu percent used:", psutil.cpu_percent())
    print("ram percent used:", psutil.virtual_memory().percent)
    print("ram percent free:", psutil.virtual_memory().available * 100 / psutil.virtual_memory().total)
    print('-----------------------------------------------')


@bot.event
async def on_ready():
    print("Bot is now ready, starting configs...")
    print("Configs finished, bot now fully operational")
    print('-----------------------------------------------')
    channel = await discord.Client.fetch_channel(self=bot, channel_id="746813636667768884")
    await channel.send(f"Automod started on version {version}", delete_after=10)



@bot.event
async def on_disconnect():
    print("YOU HAVE BEEN DISCONNECTED FROM THE INTERNET, BOT NO LONGER OPERATIONAL")


@bot.event
async def on_guild_join(guild):
    async def find_channel(guild):
        for c in guild.text_channels:
            if not c.permissions_for(guild.me).send_messages:
                continue
            return c

    channel = await find_channel(guild)
    embedvar = discord.Embed(title='Hi im rapidbot!!', description="My command prefix is '-'\
     try -help to see a commands list", colour=discord.Color.gold())
    await channel.send(embed=embedvar)


@bot.event
async def on_message(ctx):
    if ctx.guild.id == 700405552534257714:
        if not ctx.author.bot:
            msg = ctx.content
            def removemsg(string):
                return string.replace("\n", " // ")
            msg2 = removemsg(msg)
            yesid = f"TIME: {datetime.datetime.now()} MESSAGE ID: {ctx.id} USER: {ctx.author}"
            yes = f"SERVER: {ctx.guild} CHANNEL: {ctx.channel} USER: {ctx.author} MESSAGE: {msg2}"
            #print('-----------------------------------------------')
            print(yesid + ' - [ ' + yes + ' ]')


            # text identification #

            a = (re.findall(r'(https?://[^\s]+)', str(msg2)))
            b = (re.findall(r'(http?://[^\s]+)', str(msg2)))
            c = ('\n'.join(a))
            d = ('\n'.join(b))
            e = c + d
            if not e == "":
                print(f"LINK IDENTIFIED: {e}")

            # duplicates #
            global one, two, three, four, five
            global oneid, twoid, threeid, fourid, fiveid
            global onetrig, twotrig, threetrig, fourtrig, fivetrig
            global dellist

            try:
                dellistold = dellist
            except:
                dellistold = []

            if not msg2 == "":
                try:
                    five = four
                    fiveid = fourid
                except:
                    five = ""
                    fiveid = ""

                try:
                    four = three
                    fourid = threeid
                except:
                    four = ""
                    fourid = ""

                try:
                    three = two
                    threeid = twoid
                except:
                    three = ""
                    threeid = ""

                try:
                    two = one
                    twoid = oneid
                except:
                    two = ""
                    twoid = ""

                one = msg2
                oneid = ctx.id

                #print(f"1: {oneid} {one}\n2: {twoid} {two}\n3: {threeid} {three}\n4: {fourid} {four}\n5: {fiveid} {five}\n")

                amountsame = 0
                dellist = []
                twotrig = 0
                threetrig = 0
                fourtrig = 0
                fivetrig = 0

                if one == two:
                    amountsame = amountsame + 1
                    twotrig = 1
                if one == three:
                    amountsame = amountsame + 1
                    threetrig = 1
                if one == four:
                    amountsame = amountsame + 1
                    fourtrig = 1
                if one == five:
                    amountsame = amountsame + 1
                    fivetrig = 1
                if amountsame > 1:
                    print("DUP", amountsame)
                    if fivetrig:
                        if fourtrig:
                            dellist.append(fourid)
                        if threetrig:
                            dellist.append(threeid)
                        if twotrig:
                            dellist.append(twoid)
                        dellist.append(oneid)
                    else:
                        if fourtrig:
                            if threetrig:
                                dellist.append(threeid)
                            if twotrig:
                                dellist.append(twoid)
                            dellist.append(oneid)
                        else:
                            if threetrig:
                                if twotrig:
                                    dellist.append(twoid)
                                dellist.append(oneid)
                            else:
                                if twotrig:
                                    print("HOW")

                    for i in dellist[:]:
                        if i in dellistold:
                            dellist.remove(i)

                    for item in dellist:
                        try:
                            msg = await ctx.channel.fetch_message(item)
                            event = f"Deleted [{msg.content}], from {msg.author}, at {datetime.datetime.now()}, MESSAGE DUPLICATION"
                            print(event)
                            with open("log.txt", "a+") as f:
                                f.write(event + "\n")
                            await msg.delete()
                        except:
                            print("Message not found, this prob means the person continued spamming")

            if msg2 == "-channel trim":
                await ctx.delete()
                msg = await ctx.channel.send("Starting index")
                channels = [746813636667768884]
                for channelid in channels:
                    message = await discord.Client.fetch_channel(self=bot, channel_id=channelid)

                    counter = 0
                    deletethis = []
                    async for ctx in message.history(limit=None):
                        counter = counter + 1
                        if counter % 500 == 0:
                            await msg.edit(content=f"INDEXING MSG NUM {counter}")
                        timestamp = ctx.created_at
                        datetime_object = pandas.Timestamp(timestamp)
                        timediff = datetime.datetime.now() - datetime_object
                        if timediff > pandas.Timedelta(days=7):
                            #print(timediff - pandas.Timedelta(days=7), "DELETE")
                            deletethis.append(ctx.id)
                    await msg.edit(content=f"INDEXED {counter}")

                    counter1 = 0
                    for item in deletethis:
                        try:
                            counter1 = counter1 + 1
                            ctx = await ctx.channel.fetch_message(item)
                            if counter1 % 10 == 0:
                                await msg.edit(content=f"Deleted {counter1} messages, {counter-counter1} messages remaining")
                            await ctx.delete()
                            await ctx.purge()
                        except:
                            print("Message not found")

                await msg.edit(content=f"TRIM COMPLETE")
                time.sleep(10)
                await msg.delete()

            if msg2 == "-botrt":
                await ctx.channel.send(f"SHARD - AUTOMOD {version}, Active since {stime}")

            if msg2 == "-log":
                await ctx.channel.send(file=discord.File("log.txt"))



# bot.run("", bot=False) # selfbot
# bot.run("") # beta bot
bot.run('') # actual bot