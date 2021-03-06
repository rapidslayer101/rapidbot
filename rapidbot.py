global time, sys, googletrans, google, random, os, zlib, base64, re
import datetime, decimal, time, os, random, re, socket, hashlib  # inbuilt
import googletrans, discord, requests, urllib, praw  # installed modules
import psutil as ut
from discord import Embed
from discord.ext import commands
from forex_python.converter import CurrencyRates, CurrencyCodes
from googletrans import Translator

import enclib as enc  # custom lib

# rapidbot - CREATED BY RAPIDSLAYER101 (Scott Bree)
start_time = datetime.datetime.utcnow()
print(socket.gethostname(), socket.getfqdn())
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
print(socket.gethostbyname(socket.gethostname()), s.getsockname()[0])
s.close()

if socket.gethostname() == "RAPIDSLAYER101":
    device = "RAPIDSLAYER101"
else:
    device = "24/7-HEROKU"

# todo color embeds
# todo maybe move all print statements to a webhook and a debug console

# file system checks
if not os.path.isdir("strs"):
    os.mkdir("strs")
if not os.path.isfile("strs/msgstore.txt"):
    open("strs/msgstore.txt", "w").close()
if not os.path.isfile("strs/tokens.txt"):
    open("strs/tokens.txt", "w").close()
if not os.path.isfile("strs/rcoin_bals.txt"):
    open("strs/rcoin_bals.txt", "w").close()


def convert_tuple(tup):
    return "".join(item+" " for item in tup)


print("Opening connection to discord")


class Encryption(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def enc_key(self, ctx):
        await ctx.channel.send(f"Randomly generated key:\n```{enc.pass_to_seed(enc.hex_gens(1000), 'salt')}```")

    @commands.command(aliases=['enc'])  # todo fix enc
    async def encrypt(self, ctx, *, arg):
        e_text2 = enc.encrypt_key(arg, "key", "salt")
        if len(e_text2) > 1900:
            with open('strs/temp.txt', 'w') as i:
                i.write(e_text2)
            em = Embed(title=f"Your encrypted text is over the 1900 char limit as it is {len(e_text2)}"
                             f" chars so has to be sent as a file")
            await ctx.channel.send(embed=em.set_footer(text=f"Requested by {ctx.author}"))
            await ctx.channel.send(file=discord.File('strs/temp.txt'))
        else:
            await ctx.channel.send(f"```Encrypted text ({len(ctx.message.content[9:])} --> {len(e_text2)}):"
                                   f" chars:\n{e_text2}\n\nRequested by {ctx.author}```")

    @commands.command(aliases=['dec'])  # todo fix dec
    async def decrypt(self, ctx, *args):
        final_output = enc.decrypt_key(convert_tuple(args), "key", "salt")
        if len(final_output) > 1900:
            with open('strs/temp.txt', 'w') as i:
                i.write(final_output)
            em = Embed(title=f"Your encrypted text is over the 1900 char limit as it is {len(final_output)}"
                             f" chars so has to be sent as a file")
            await ctx.channel.send(embed=em.set_footer(text=f"Requested by {ctx.author}"))
            await ctx.channel.send(file=discord.File('strs/temp.txt'))
        else:
            await ctx.channel.send(f"```Decrypted text:\n{final_output}\n\nRequested by {ctx.author}```")


class Random(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["randnumber"])
    async def randnum(self, ctx, arg1, arg2):
        string = f"Your random number between {int(arg1)} and {int(arg2)} is:"
        em = Embed(title=string, description=random.randint(int(arg1), int(arg2)))
        await ctx.channel.send(embed=em.set_footer(text=f"Requested by {ctx.author}"))

    @commands.command()
    async def randuni(self, ctx, arg):
        chr_num = int(arg)
        allow_cmd = False
        if chr_num > 1:
            if chr_num > 500:
                em = Embed(title="Number over max char limit!", description="There is a 500 char limit")
                await ctx.channel.send(embed=em.set_footer(text=f"Requested by {ctx.author}"))
            else:
                balance = rcoin.bal(0, ctx.author.id) / 10
                head, sep, tail = str(balance).partition('.')
                if chr_num > int(head):
                    em = Embed(title="Number over limit char limit!", description=f"There is a {head} char limit,"
                                     f" increase this by getting more coins by playing games!"
                                     f" do `-h games` to see the games list")
                    await ctx.channel.send(embed=em.set_footer(text=f"Requested by {ctx.author}"))
                else:
                    allow_cmd = True
        if chr_num < 1:
            await ctx.channel.send("```The minimum char amount is 1!```")
            allow_cmd = False
        if allow_cmd == 1:
            def get_random_unicode(length):
                get_char = chr
                char_ranges = [(0x0021, 0x0021), (0x0023, 0x0026), (0x0028, 0x007E), (0x00A1, 0x00AC), (0x00AE, 0x00FF),
                               (0x0100, 0x017F), (0x0180, 0x024F), (0x2C60, 0x2C7F), (0x16A0, 0x16F0), (0x0370, 0x0377),
                               (0x037A, 0x037E), (0x0384, 0x038A), (0x038C, 0x038C)]
                alphabet = [get_char(code_point) for current_range in char_ranges
                            for code_point in range(current_range[0], current_range[1]+1)]
                return ''.join(random.choice(alphabet) for i in range(length))

            em = Embed(title=f'A random string of {chr_num} symbols: ', description=get_random_unicode(chr_num))
            await ctx.channel.send(embed=em.set_footer(text=f"Requested by {ctx.author}"))

    @commands.command()
    async def eight_ball(self, ctx):
        ball_choice = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes ??? definitely.",
                       "You may rely on it.", "As I see it,yes.", "Most likely.", "Outlook good.", "Yes.",
                       "Signs point to yes.", "Reply hazy,try again.", "Ask again later.", "Better not tell you now.",
                       "Cannot predict now.", "Concentrate and ask again.", "Don???t count on it.", "My reply is no.",
                       "My sources say no.", "Outlook not so good", "Very doubtful"]
        em = Embed(title=ball_choice[random.randint(0, 20)])
        await ctx.channel.send(embed=em.set_footer(text=f"Requested by {ctx.author}"))

    @commands.command()
    async def leetify(self, ctx):
        change2 = ctx.message.content[9:].replace("o", "0").replace("O", "0").replace("l", "1").replace("L", "1") \
            .replace("s", "5").replace("S", "5").replace("h", "8").replace("H", "8").replace("e", "3")\
            .replace("E", "3").replace("i", "1").replace("I", "1")
        em = Embed(title="Leetified text:", description=change2)
        await ctx.channel.send(embed=em.set_footer(text=f"Requested by {ctx.author}"))

    @commands.command()
    async def repeat(self, ctx):
        em = Embed(description=ctx.message.content[8:])
        await ctx.channel.send(embed=em.set_footer(text=f"Requested by ???"))

    @commands.command()
    async def joke(self, ctx):
        response = requests.get('https://icanhazdadjoke.com/', headers={'Accept': 'text/plain'})
        em = Embed(title="Here is your joke", description=response.text)
        await ctx.channel.send(embed=em.set_footer(text=f"Requested by {ctx.author}"))

    @commands.command()
    async def char_count(self, ctx):  # todo add support for files? or make this more useful
        em = Embed(title=f"Total Number of Characters in this String = {len(ctx.message.content[12:])}")
        await ctx.channel.send(embed=em.set_footer(text=f"Requested by {ctx.author}"))

    @commands.command(aliases=["emoji_letters", "big_text"])
    async def emoji_letter(self, ctx, *args):
        string = ""
        for i in convert_tuple(args)[:-1].replace(",", "").replace(".", ""):
            if i.lower() in "abcdefghijklmnopqrstuvwxyz ":
                if i == " ":
                    string += ":black_large_square:"
                else:
                    string += f":regional_indicator_{i.lower()}:"
        await ctx.channel.send(string)

    @commands.command()
    async def ttb(self, ctx):  # todo add support context for prior conversations
        await ctx.channel.send(ttb.run(0, ctx.message.content[5:]))


class BotInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["botinv", "botweb", "botrt", "inservers"])
    async def info(self, ctx):
        try:  # todo fix this error, temp except added
            try:
                time_str = str(ctx.message.created_at-datetime.datetime.utcnow())
            except:
                time_str = str(ctx.message.created_at-datetime.datetime.now())
            diff = round(sum([a*b for a, b in zip([3600, 60, 1], map(float, time_str.split(':')))]), 2)
            start = datetime.datetime.utcnow() - start_time
        except:
            diff = "ERROR"
        try:
            runtime = str(start)[:-7]
        except:
            runtime = "ERROR"
        em = Embed(title=f"Bot info:", description=f"\n\nRuntime: {runtime}\n"
                         f"Started at: {str(start_time)[:-7]}\n"
                         f'Cpu: {ut.cpu_percent()}% of {ut.cpu_count(logical=False)}core/{ut.cpu_count()}thread\n'
                         f'Ram: {ut.virtual_memory().percent}% in use, '
                         f'{round(ut.virtual_memory().available*100/ut.virtual_memory().total, 1)}% free '
                         f'({round(ut.virtual_memory().used/1048576, 0)}/'
                         f'{round(ut.virtual_memory().total/1048576, 0)}MB)\n'
                         f'Storage: {ut.disk_usage("/").percent}% used, {round(ut.disk_usage("/").used/1048576, 2)}'
                         f'/{round(ut.disk_usage("/").total/1048576, 2)}MB\n'
                         f'This bot is in {str(len(bot.guilds))} servers\n'
                         f'The current ping is: {diff}s\n'
                         f'\nInvite link: [Click to add bot to another server](https://discord.com/oauth2/'
                         f'authorize?client_id=711578412103368707&scope=bot&permissions=8)\n'
                         f'\nDevice bot is running on: {device}')
        await ctx.channel.send(embed=em.set_footer(text=f"Requested by {ctx.author}"))


class Server(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def chat_links(self, ctx, arg1):
        started_at = time.time()
        async with ctx.typing():
            if int(arg1) > 1000:
                await ctx.send("There is a 1000 message search limit on this command")
            else:
                msg_list = "".join([message.content+" " async for message in ctx.channel.history(limit=int(arg1))])
                em = Embed(title=f"Number of links: {int(arg1)}", description=enc.get_links(msg_list))
                em.set_footer(text=f"Took {round(time.time()-started_at, 2)} seconds, Requested by {ctx.author}")
                await ctx.channel.send(embed=em)

    @commands.command(aliases=["channelids"])
    async def channel_ids(self, ctx, *args):
        c_args = convert_tuple(args)[:-1]
        text_channel_list = ""
        for guild in bot.guilds:
            if guild.id == ctx.guild.id:
                channels_amount = len(guild.text_channels)
                for channel in guild.text_channels:
                    if c_args == "":
                        text_channel_list += f"{channel.id} {channel}\n"
                    if c_args == "raw":
                        text_channel_list += f"{channel.id}, "
        if c_args == "raw":
            text_channel_list = text_channel_list[:-2]
        if c_args == "":
            text_channel_list += f"\nThe ID for this channel ({ctx.channel}) is: {ctx.channel.id}"

        em = Embed(title=f"Channels in this server ({channels_amount}):", description=text_channel_list)
        await ctx.channel.send(embed=em.set_footer(text=f"Requested by {ctx.author}"))

    @commands.command()
    async def members(self, ctx):
        e4 = "".join([f"<@!{item.id}>" for item in ctx.guild.members])
        em = Embed(title=f"Member count: {len(ctx.guild.members)}", description=str(e4))
        await ctx.channel.send(embed=em.set_footer(text=f"Requested by {ctx.author}"))

    @commands.command()
    async def roles(self, ctx):
        e4 = "".join([f"\n{item.id} <@&{item.id}>" for item in ctx.guild.roles])
        em = Embed(title=f"Role count: {len(ctx.guild.roles)}", description=str(e4))
        await ctx.channel.send(embed=em.set_footer(text=f"Requested by {ctx.author}"))

    @commands.command()
    async def inrole(self, ctx):
        if ctx.message.content[8:9] == "<":
            role = ctx.message.content[11:].replace(">", "")
        else:
            role = ctx.message.content[8:]
        e4 = [f"\n<@!{item.id}>" for item in ctx.guild.members
              if str(role) in str(ctx.guild.get_member(item.id).roles)]
        em = Embed(title=f"Members with role {ctx.guild.get_role(int(role))} ({len(e4)}):", description="".join(e4))
        await ctx.channel.send(embed=em.set_footer(text=f"Requested by {ctx.author}"))

    @commands.command()
    async def who_spoke(self, ctx, arg1):  # todo resource intensive maybe redo
        started_at = time.time()
        async with ctx.typing():
            if int(arg1) > 1000:
                await ctx.send("There is a 1000 message search limit on this command")
            else:
                id_list = [message.author.id async for message in ctx.channel.history(limit=int(arg1))]
                stuffs = "".join([f"<@!{x}> spoke {id_list.count(x)} times \n" for x in set(id_list)])
                em = Embed(title=f"Members who spoke in last {int(arg1)} messages", description=stuffs)
                em.set_footer(text=f"Took {round(time.time() - started_at, 2)} seconds, Requested by {ctx.author}")
                await ctx.channel.send(embed=em)


class Currency(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def currency_list(self, ctx):
        values = (ctx.message.content[15:18])
        await ctx.channel.send(f"```glsl\n#{CurrencyRates().get_rates(values)}\n\n#Requested by {ctx.author}```")

    @commands.command()
    async def currency_convert(self, ctx, arg1, arg2, arg3):
        d = CurrencyCodes()
        output = CurrencyRates().convert(arg1.upper(), arg2.upper(), float(arg3))
        em = discord.Embed(title=f"Here is the value in {arg2}: {d.get_symbol(arg2.upper())}{round(output, 2)}")
        await ctx.channel.send(embed=em.set_footer(text=f"Requested by {ctx.author}"))

    @commands.command()
    async def bitcoin(self, ctx):  # todo remove or redo functionality
        global prex
        headers = {'Accept': 'text/plain'}

        inat = 10068.89
        inwith = 350.68
        inat10 = inat.as_integer_ratio()
        inwith10 = inwith.as_integer_ratio()
        divider = (inat10[0] / inat10[1]) / (inwith10[0] / inwith10[1])
        divider = divider.as_integer_ratio()
        print(inat / (divider[0] / divider[1]))

        page = requests.get("https://api.coinbase.com/v2/prices/spot?currency=GBP", headers=headers)
        x = page.content[49:].decode()
        x = x[:-3]
        try:
            print(prex)
        except NameError:
            await ctx.channel.send("??" + x + " Started price watch...")
            prex = x
        ratiou = 0
        ratiottl = 0
        global largeportcounter
        largeportcounter = 0
        page = requests.get("https://api.coinbase.com/v2/prices/spot?currency=GBP", headers=headers)
        x = page.content[49:].decode()
        x = x[:-3]
        change1 = float(prex).as_integer_ratio()
        change2 = float(x).as_integer_ratio()
        change = (change2[0] / change2[1]) - (change1[0] / change1[1])
        if change == 0:
            uod = "NUL"
        if change > 0:
            uod = "??????????"
            ratiou = ratiou + 1
        if change < 0:
            uod = "??????????"
        ratiottl = ratiottl + 1
        change3 = str(change).replace("-", "")

        port = (change2[0] / change2[1]) / (divider[0] / divider[1])
        ptval = change / (divider[0] / divider[1])
        ptval = str(ptval).replace("-", "")

        port2 = port.as_integer_ratio()
        inwith2 = inwith.as_integer_ratio()
        profit = (port2[0] / port2[1]) - (inwith2[0] / inwith2[1])

        if (change2[0] / change2[1]) > (inat10[0] / inat10[1]):
            result = float((((change2[0] / change2[1]) - (inat10[0] / inat10[1])) * 100) / (change2[0] / change2[1]))
            updown = " ?????????? BTC UP BY " + str(round(result, 3)) + "% SINCE START"
        if (change2[0] / change2[1]) < (inat10[0] / inat10[1]):
            result = float((((change2[0] / change2[1]) - (inat10[0] / inat10[1])) * 100) / (change2[0] / change2[1]))
            updown = " ?????????? BTC DOWN BY " + str(round(result, 3)) + "% SINCE START"

        msg = await ctx.channel.send(
            "BTC: ??" + x + " - ??" + str(round(float(change3), 3)) + " " + str(uod) +
            " ??" + str(round(float(ptval), 3)) + " - PRT: ??" + str(round(port, 3)) +
            " - PRF: ??" + str(round(profit, 3)) + str(updown))
        # +" - "+RATIO "+str(ratiou)+"/"+str(ratiottl))
        with open("bitcoin-data.txt", "a+") as f:
            f.write(x + "\n")

        with open("port-top.txt", ) as i:
            page11 = str(i.read())
            page = float(page11)
            page = page.as_integer_ratio()

        with open("port-top.txt", "w") as ii:
            if (port2[0] / port2[1]) > (page[0] / page[1]):
                ii.write(str(round(port, 3)))
                largeportcounter = largeportcounter + 1
                if largeportcounter == 5:
                    largeportcounter == 0
            else:
                ii.write(page11)
                if (port2[0] / port2[1]) < (((port2[0] / port2[1]) - (inwith2[0] / inwith2[1])) * 0.995):
                    print("DOWN BY 0.5% OR MORE FROM HIGHEST PORT")
        prex = x


class ColourText(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["red_text"])
    async def redtext(self, ctx):
        await ctx.channel.send(f"```diff\n- {ctx.message.content[9:]}\n\nRequested by {ctx.author}```")

    @commands.command(aliases=["orange_text"])
    async def orangetext(self, ctx):
        await ctx.channel.send(f"```glsl\n#{ctx.message.content[12:]}\n\nRequested by {ctx.author}```")

    @commands.command(aliases=["yellow_text"])
    async def yellowtext(self, ctx):
        await ctx.channel.send(f"```fix\n {ctx.message.content[12:]}\n\nRequested by {ctx.author}```")

    @commands.command(aliases=["blue_text"])
    async def bluetext(self, ctx):
        await ctx.channel.send(f"```css\n.{ctx.message.content[10:]}\n\nRequested by {ctx.author}```")

    @commands.command(aliases=["cyan_text"])
    async def cyantext(self, ctx):
        await ctx.channel.send(f"```xl\n'{ctx.message.content[10:]}\n\nRequested by {ctx.author}```")


class OnlineSearching(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ggt_codes(self, ctx):  # todo make less horrible to read
        em = Embed(title="Here are the language codes:", description=str(googletrans.LANGCODES))
        await ctx.channel.send(embed=em.set_footer(text=f"Requested by {ctx.author}"))

    @commands.command()
    async def ggt_te(self, ctx):  # todo fix
        translated = Translator().translate(ctx.message.content[8:])
        em = Embed(title="Translated text:", description=translated.text)
        await ctx.channel.send(embed=em.set_footer(text=f"Requested by {ctx.author}"))

    @commands.command()
    async def ggt_ft(self, ctx, arg1, arg2):  # todo fix
        values5 = (ctx.message.content[14:])
        translator = Translator()
        translated = translator.translate(values5, src=arg1, dest=arg2)
        em = Embed(title="Translated text:", description=translated.text)
        await ctx.channel.send(embed=em.set_footer(text=f"Requested by {ctx.author}"))

    # todo, 3 practically identical commands, use def to turn much much smaller

    @commands.command(aliases=["ggsi", "ggsv"])
    async def ggsr(self, ctx, arg1):  # todo add more functionality
        allowcmd = 0
        if int(arg1) > 1:
            if int(arg1) > 30:
                em = Embed(title="Number over max result limit!", description="There is a 30 result limit")
                await ctx.channel.send(embed=em.set_footer(text=f"Requested by {ctx.author}"))
                allowcmd = 1
            else:
                balance = rcoin.bal(0, ctx.author.id) / 50
                head, sep, tail = str(balance).partition('.')
                if int(arg1) > int(head):
                    em = Embed(title="Number over result limit!", description=f"There is a {head} result limit,\
                    increase this by getting more coins by playing games! do `-help games` to see the games list")
                    await ctx.channel.send(embed=em.set_footer(text=f"Requested by {ctx.author}"))
                    allowcmd = 1
        if int(arg1) < 1:
            await ctx.channel.send("```The minimum results is 1!```")
            allowcmd = 1
        if ctx.message.content[8:] == "":
            await ctx.channel.send("```You cant search for nothing!```")
            allowcmd = 1
        if not allowcmd == 1:
            em = Embed(description=f"Below results requested by {ctx.author}")
            await ctx.channel.send(embed=em)
            from googlesearch import search
            send = "".join(f"{j}\n" for j in search((ctx.message.content[8:]), tld="co.in",
                                                    num=int(arg1), stop=int(arg1), pause=2))
            await ctx.channel.send(send)

    @commands.command()
    async def reddits(self, ctx, arg1, arg2):  # todo simplification possible
        reddit = praw.Reddit(client_id='RuvVgZ-jMqw9lw', client_secret='tj4cbJuTKAum0ZszB_DJwY5cFjo',
                             user_agent='Reddit webscraper')
        hot_posts = reddit.subreddit(arg1).hot(limit=int(arg2))
        postcurrent = 0
        post_type = 0
        for post in hot_posts:
            postcurrent += 1
            if postcurrent == int(arg2):
                if "redgifs.com/" in str(post.url):
                    em = Embed(description=f"Below results requested by {ctx.author}")
                    await ctx.channel.send(embed=em)
                    await ctx.channel.send(str(post.url) + "/")
                    break
                    post_type = 1
                if "https://i.imgur.com/" in str(post.url):
                    em = Embed(description=f"Below results requested by {ctx.author}")
                    await ctx.channel.send(embed=em)
                    await ctx.channel.send(str(post.url) + "/")
                    break
                    post_type = 1
                if not post_type == 1:
                    em = Embed(description=f"[Click to go to post]({post.url})")
                    em.set_image(url=post.url)
                    await ctx.channel.send(embed=em.set_footer(text=f"Requested by {ctx.author}"))
                    break

    @commands.command()
    async def meme(self, ctx):  # todo sometimes not loading, for efficiency put data in txt
        global postnum
        reddit = praw.Reddit(client_id='RuvVgZ-jMqw9lw', client_secret='tj4cbJuTKAum0ZszB_DJwY5cFjo',
                             user_agent='Reddit webscraper')
        try:
            postnum += 1
        except NameError:
            postnum = 1
        hot_posts = reddit.subreddit('dankmemes').hot(limit=postnum)
        postcurrent = 0
        for post in hot_posts:
            postcurrent += 1
            if postcurrent == postnum:
                em = Embed()
                em.set_image(url=post.url)
                await ctx.channel.send(embed=em.set_footer(text=f"Requested by {ctx.author}"))


class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["claim_token"])
    async def claim(self, ctx, arg):
        found = False
        with open('strs/tokens.txt') as f:
            for lnum3, line in enumerate(f, 1):
                token, p2 = line.split(",")
                if token == arg:
                    reward = p2.replace(" ", "").replace("\n", "")
                    found = True
                    line_num = lnum3
        if found:
            if reward == "CLAIMED":
                em = Embed(title="This token has already been claimed", color=discord.Colour(0xff0000))
            else:
                with open('strs/tokens.txt', 'r') as file:
                    data = file.readlines()
                data[int(line_num) - 1] = f'{arg}, CLAIMED\n'
                file.close()

                with open('strs/tokens.txt', 'w') as file:
                    file.writelines(data)

                rcoin.win(0, ctx.author.id, float(reward))
                em = Embed(title=f"{reward} rcoins have been added to your balance",
                           description=f"You now have: {rcoin.bal(0, ctx.author.id)}",
                           color=discord.Colour(0x00ff00))
        else:
            em = Embed(title="This is not a valid token", color=discord.Colour(0xff0000))
        await ctx.channel.send(embed=em.set_footer(text=f"Requested by {ctx.author}"))

    # @commands.command()  # todo add this maybe
    # async def daily(self, ctx):
    #        # 10? daily coins, new class probably needed

    @commands.command()
    async def bal(self, ctx, *args):
        c_args = convert_tuple(args)[:-1]
        if c_args == "":
            em = Embed(title=f"Your balance is {rcoin.bal(0, ctx.author.id)}")
        else:
            if str(args[0]).startswith("<@!") and str(args[0]).endswith(">"):
                userid = int(args[0].replace("<@!", "").replace(">", ""))
                em = Embed(description=f"{args[0]}'s balance is {rcoin.bal(0, userid)}")
            else:
                em = Embed(description=f"<@!{args[0]}>'s balance is {rcoin.bal(0, int(args[0]))}")
        await ctx.channel.send(embed=em.set_footer(text=f"Requested by {ctx.author}"))

    @commands.command(aliases=["bet_flip"])
    async def flip(self, ctx, arg1, arg2):
        bet = rcoin.check(0, ctx.author.id, float(arg2))
        if str(bet).startswith("This is") or str(bet).startswith("You cannot"):
            em = Embed(title=bet)
            await ctx.channel.send(embed=em.set_footer(text=f"Requested by {ctx.author}"))
        else:
            flip = random.randint(0, 100)
            if flip < 36:
                if str(arg1) == "h":
                    h_or_t = "heads"
                if str(arg1) == "t":
                    h_or_t = "tails"
                rcoin.win(0, ctx.author.id, bet)
                em = Embed(title=f"You Won {bet}", description=f"Coin landed on {h_or_t}\
                 and You now have: {rcoin.bal(0, ctx.author.id)}", color=discord.Colour(0x00ff00))
            if flip > 35:
                if str(arg1) == "h":
                    h_or_t = "tails"
                if str(arg1) == "t":
                    h_or_t = "heads"
                rcoin.lose(0, ctx.author.id, bet)
                em = Embed(title=f"You Lost {bet}", description=f"Coin landed on {h_or_t}\
                 You now have: {rcoin.bal(0, ctx.author.id)}", color=discord.Colour(0xff0000))
            await ctx.channel.send(embed=em.set_footer(text=f"Requested by {ctx.author}"))

    @commands.command(aliases=["bet_dice"])
    async def dice(self, ctx, arg1, arg2):
        bet = rcoin.check(0, ctx.author.id, float(arg2))
        if str(bet).startswith("This is") or str(bet).startswith("You cannot"):
            em = Embed(title=bet)
            await ctx.channel.send(embed=em.set_footer(text=f"Requested by {ctx.author}"))
        else:
            dice_num = int(arg1)
            allow_bet = True
            if dice_num > 6 or dice_num < 0:
                em = Embed(title="You must bet on a number 1-6")
                allow_bet = False
            if allow_bet:
                dice_roll = random.randint(1, 6)
                if dice_num == dice_roll:
                    rcoin.win(0, ctx.author.id, bet * 5)
                    em = Embed(title=f"Dice rolled {dice_roll} and You Won {bet * 5}",
                               description=f"You now have: {rcoin.bal(0, ctx.author.id)}",
                               color=discord.Colour(0x00ff00))
                else:
                    rcoin.lose(0, ctx.author.id, bet)
                    em = Embed(title=f"Dice rolled {dice_roll} You Lost {bet}",
                               description=f"You now have: {rcoin.bal(0, ctx.author.id)}",
                               color=discord.Colour(0xff0000))

            await ctx.channel.send(embed=em.set_footer(text=f"Requested by {ctx.author}"))

    @commands.command(aliases=["bet_rps"])
    async def rps(self, ctx, arg1, arg2):
        bet = rcoin.check(0, ctx.author.id, float(arg2))
        if str(bet).startswith("This is") or str(bet).startswith("You cannot"):
            em = Embed(title=bet)
            await ctx.channel.send(embed=em.set_footer(text=f"Requested by {ctx.author}"))
        else:
            t = ["R", "P", "S"]
            computer = t[random.randint(0, 2)]
            player = False

            while player is False:
                player = arg1
                rpsbet2 = bet / 2  # change multiplier here
                rpsbet2 = rpsbet2.as_integer_ratio()
                if player == computer:
                    await ctx.channel.send("Tie!")
                elif player == "r":
                    if computer == "P":
                        rcoin.lose(0, ctx.author.id, bet)
                        em = Embed(title=f"You Lose! rapidbot covers {ctx.author}",
                                   description=f"You now have: {rcoin.bal(0, ctx.author.id)}",
                                   color=discord.Colour(0xff0000))
                        await ctx.channel.send(embed=em.set_footer(text=f"Requested by {ctx.author}"))
                    else:
                        rcoin.win(0, ctx.author.id, (rpsbet2[0] / rpsbet2[1]))
                        em = Embed(title=f"You Win! {ctx.author} smashes rapidbot",
                                   description=f"You now have: {rcoin.bal(0, ctx.author.id)}",
                                   color=discord.Colour(0x00ff00))
                        await ctx.channel.send(embed=em.set_footer(text=f"Requested by {ctx.author}"))

                elif player == "p":
                    if computer == "S":
                        rcoin.lose(0, ctx.author.id, bet)
                        em = Embed(title=f"You Lose! rapidbot cut {ctx.author}",
                                   description=f"You now have: {rcoin.bal(0, ctx.author.id)}",
                                   color=discord.Colour(0xff0000))
                        await ctx.channel.send(embed=em.set_footer(text=f"Requested by {ctx.author}"))
                    else:
                        rcoin.win(0, ctx.author.id, (rpsbet2[0] / rpsbet2[1]))
                        em = Embed(title=f"You Win! {ctx.author} covers rapidbot",
                                   description=f"You now have: {rcoin.bal(0, ctx.author.id)}",
                                   color=discord.Colour(0x00ff00))
                        await ctx.channel.send(embed=em.set_footer(text=f"Requested by {ctx.author}"))
                elif player == "s":
                    if computer == "R":
                        rcoin.lose(0, ctx.author.id, bet)
                        em = Embed(title=f"You Lose! rapidbot smashes {ctx.author}",
                                   description=f"You now have: {rcoin.bal(0, ctx.author.id)}",
                                   color=discord.Colour(0xff0000))
                        await ctx.channel.send(embed=em.set_footer(text=f"Requested by {ctx.author}"))
                    else:
                        rcoin.win(0, ctx.author.id, (rpsbet2[0] / rpsbet2[1]))
                        em = Embed(title=f"You Win! {ctx.author} cut rapidbot",
                                   description=f"You now have: {rcoin.bal(0, ctx.author.id)}",
                                   color=discord.Colour(0x00ff00))
                        await ctx.channel.send(embed=em.set_footer(text=f"Requested by {ctx.author}"))
                else:
                    em = Embed(title="Thats not a move")
                    await ctx.channel.send(embed=em.set_footer(text=f"Requested by {ctx.author}"))

                player = True
                computer = t[random.randint(0, 2)]

    @commands.command(aliases=["bet_multi"])
    async def multi(self, ctx, arg1, arg2):
        bet = rcoin.check(0, ctx.author.id, float(arg2))
        if str(bet).startswith("This is") or str(bet).startswith("You cannot"):
            em = Embed(title=bet)
            await ctx.channel.send(embed=em.set_footer(text=f"Requested by {ctx.author}"))
        else:
            allow_bet = 0
            if int(arg1) < 3:
                em = Embed(title="You cant have a multiplier lower than 3!")
                await ctx.channel.send(embed=em.set_footer(text=f"Requested by {ctx.author}"))
                allow_bet = 1
            if int(arg1) > 100000:
                em = Embed(title="You cant have a multiplier higher than 100000!")
                await ctx.channel.send(embed=em.set_footer(text=f"Requested by {ctx.author}"))
                allow_bet = 1
            if not allow_bet == 1:
                multiplyerunedit = int(arg1) * 1.20 * 10  # change multiplier here
                lookup = "."
                if lookup in str(multiplyerunedit):
                    head, sep, tail = str(multiplyerunedit).partition('.')

                botmultichoice = random.randint(1, int(head))
                print(str(botmultichoice) + "/" + str(multiplyerunedit))
                if botmultichoice < 11:
                    rcoin.win(0, ctx.author.id, bet * float(arg1))
                    em = Embed(title=f"You Won: {bet * float(arg1)}", description=f"You bet {bet} on a {arg1}"
                                     f"X multiplier and you now have: {rcoin.bal(0, ctx.author.id)}",
                               color=discord.Colour(0x00ff00))
                else:
                    rcoin.lose(0, ctx.author.id, bet)
                    em = Embed(title=f"You Lost: {bet}", description=f"You bet {bet} on a {arg1}"
                                     f"X multiplier and you now have: {rcoin.bal(0, ctx.author.id)}",
                               color=discord.Colour(0xff0000))
                await ctx.channel.send(embed=em.set_footer(text=f"Requested by {ctx.author}"))

    @commands.command(aliases=["bet_revup"])
    async def revup(self, ctx, arg1, arg2):  # todo this has been left broken, fix it
        bet = rcoin.check(0, ctx.author.id, float(arg1))
        if str(bet).startswith("This is") or str(bet).startswith("You cannot"):
            em = Embed(title=bet)
            await ctx.channel.send(embed=em.set_footer(text=f"Requested by {ctx.author}"))
        else:
            revupbet = arg1
            betrevtimes = arg2
            allowcmd = 0

            if int(betrevtimes) > 1:
                if int(betrevtimes) > 15:
                    em = Embed(title="Number over max goes limit!", description="There is a 15 goes limit")
                    await ctx.channel.send(embed=em.set_footer(text=f"Requested by {ctx.author}"))
                    allowcmd = 1
                elif int(betrevtimes) > 1:
                    lookup = str(ctx.author.id)
                    with open('strs/coin.txt') as myFile:
                        for line in myFile:
                            if lookup in line:
                                balance = decimal.Decimal(line[20:]) / 100
                                head, sep, tail = str(balance).partition('.')
                    if int(betrevtimes) > int(head):
                        if head == "0":
                            head = "1"
                        em = Embed(title="Number over goes limit!",
                                   description=f"There is a {head} goes limit, increase this by getting more"
                                               f" coins by playing games! do `-help games` to see the games list")
                        await ctx.channel.send(embed=em.set_footer(text=f"Requested by {ctx.author}"))
                        allowcmd = 1
            if int(betrevtimes) < 1:
                await ctx.channel.send("```The minimum goes is 1!```")
                allowcmd = 1
            if not allowcmd == 1:
                for i in range(int(betrevtimes)):
                    revupdivider = decimal.Decimal(random.randrange(0, 2750))  # change multiplier here
                    revupmulti = decimal.Decimal(random.randrange(0, 1000)) / revupdivider
                    revupmulti = revupmulti.as_integer_ratio()

                    coinadd = int(revupbet) * revupmulti[0] / revupmulti[1]
                    coinadd = decimal.Decimal(coinadd)
                    coin2 = coin - int(revupbet)
                    coin = coin2 + round(coinadd, 2)
                    revumtotal = revupmulti[0] / revupmulti[1]
                    revumtotal = decimal.Decimal(revumtotal)
                    revupbet = decimal.Decimal(revupbet)

                    if coinadd > revupbet:
                        em = Embed(title=f"You Won: {round(coinadd, 2)}",
                                   description=f"You bet {revupbet} and got a {round(revumtotal, 2)}\
                        X multiplier and you now have: {coin}", color=discord.Colour(0x00ff00))
                        await ctx.channel.send(embed=em.set_footer(text=f"Requested by {ctx.author}"))
                    if coinadd < revupbet:
                        em = Embed(title=f"You Got Back: {revupbet - (revupbet - round(coinadd, 2))}",
                                   description=f"You bet {revupbet} and got a {round(revumtotal, 2)}\
                        X multiplier and you now have: {coin}", color=discord.Colour(0xff0000))
                        await ctx.channel.send(embed=em.set_footer(text=f"Requested by {ctx.author}"))

    @commands.command()
    async def bet_dubup(self, ctx, arg1, arg2):  # todo this has been left broken, fix it
        bet = rcoin.check(0, ctx.author.id, float(arg2))
        if str(bet).startswith("This is") or str(bet).startswith("You cannot"):
            em = Embed(title=bet)
            await ctx.channel.send(embed=em.set_footer(text=f"Requested by {ctx.author}"))
        else:
            revupbet = arg1
            betrevtimes = arg2
            allowcmd = 0

            if int(betrevtimes) > 1:
                if int(betrevtimes) > 15:
                    em = Embed(title="Number over max goes limit!", description="There is a 15 goes limit")
                    await ctx.channel.send(embed=em.set_footer(text=f"Requested by {ctx.author}"))
                    allowcmd = 1
                if int(betrevtimes) > 1:
                    lookup = str(ctx.author.id)
                    with open('strs/coin.txt') as myFile:
                        for line in myFile:
                            if lookup in line:
                                balance = decimal.Decimal(line[20:]) / 100
                                head, sep, tail = str(balance).partition('.')
                    if int(betrevtimes) > int(head):
                        if head == "0":
                            head = "1"
                        em = Embed(title="Number over goes limit!",
                                   description=f"There is a {head} goes limit, increase this by getting"
                                               f" more coins by playing games! do `-help games` to see the games list")
                        await ctx.channel.send(embed=em.set_footer(text=f"Requested by {ctx.author}"))
                        allowcmd = 1
            if int(betrevtimes) < 1:
                await ctx.channel.send("```The minimum goes is 1!```")
                allowcmd = 1
            if not allowcmd == 1:
                for i in range(int(betrevtimes)):
                    allow_bet = 0
                    if int(revupbet) > coin:
                        em = Embed(title="You cant bet more than you have!")
                        await ctx.channel.send(embed=em.set_footer(text=f"Requested by {ctx.author}"))
                        allow_bet = 1
                    if int(revupbet) < 1:
                        em = Embed(title="You cant bet nothing!")
                        await ctx.channel.send(embed=em.set_footer(text=f"Requested by {ctx.author}"))
                        allow_bet = 1
                    if not allow_bet == 1:
                        revupdivider = decimal.Decimal(random.randrange(0, 1000))  # change multiplier here
                        revupmulti = (decimal.Decimal(random.randrange(0, 200)) / revupdivider)
                        revupmulti2 = (decimal.Decimal(random.randrange(0, 200)) / revupdivider)
                        revupmulifinal = revupmulti * revupmulti2
                        revupmulifinal = revupmulifinal.as_integer_ratio()
                        revupmulti = revupmulti.as_integer_ratio()
                        revupmulti2 = revupmulti2.as_integer_ratio()

                        coinadd = int(revupbet) * revupmulifinal[0] / revupmulifinal[1]
                        coinadd = decimal.Decimal(coinadd)
                        coin2 = coin - int(revupbet)
                        coin = coin2 + round(coinadd, 2)
                        revupmulti = revupmulti[0] / revupmulti[1]
                        revupmulti = decimal.Decimal(revupmulti)
                        revupmulti2 = revupmulti2[0] / revupmulti2[1]
                        revupmulti2 = decimal.Decimal(revupmulti2)
                        revuptotal = revupmulifinal[0] / revupmulifinal[1]
                        revuptotal = decimal.Decimal(revuptotal)
                        revupbet = decimal.Decimal(revupbet)

                        if coinadd > revupbet:
                            em = Embed(title=f"You Won: {round(coinadd, 2)}", description=
                            f"You bet {revupbet} and got a ({round(revupmulti, 2)}x{round(revupmulti2, 2)}) \
                            {round(revuptotal, 2)}X multiplier\nyou now have: {coin}", color=discord.Colour(0x00ff00))
                            await ctx.channel.send(embed=em.set_footer(text=f"Requested by {ctx.author}"))
                        if coinadd < revupbet:
                            em = Embed(title=f"You Got Back: {revupbet - (revupbet - round(coinadd, 2))}",
                                       description=f"You bet {revupbet, round(revupmulti, 2)} and got a ({round(revupmulti2, 2)}x\
                            {round(revuptotal, 2)}) {round(revupmulti, 2)}X multiplier\nyou now have: {coin}",
                                       color=discord.Colour(0xff0000))
                            await ctx.channel.send(embed=em.set_footer(text=f"Requested by {ctx.author}"))


class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def purge(self, ctx, arg1, arg2):
        if arg1 == "all":
            if discord.utils.get(ctx.author.roles, name="admin") or discord.utils.get(ctx.author.roles, name="Admin") \
                    or discord.utils.get(ctx.author.roles, name="administrator") \
                    or discord.utils.get(ctx.author.roles, name="Administrator"):
                await ctx.channel.send("```user permission success```", delete_after=1)
                time.sleep(1)
                deleted = await ctx.channel.purge(limit=int(arg2))
                await ctx.send('Deleted {} message(s)'.format(len(deleted)), delete_after=2.5)
            else:
                em = Embed(description="You need the role 'admin' or 'administrator' to purge everyone's messages")
                await ctx.channel.send(embed=em.set_footer(text=f"Requested by {ctx.author}"))
        if arg1 == "self":
            def is_me(m):
                return m.author == ctx.message.author

            deleted = await ctx.channel.purge(limit=int(arg2), check=is_me)
            await ctx.send('Deleted {} message(s)'.format(len(deleted)), delete_after=2.5)
        if arg1 == "bot":
            def is_me(m):
                return m.author.id == 711578412103368707

            deleted = await ctx.channel.purge(limit=int(arg2), check=is_me)
            await ctx.send('Deleted {} message(s)'.format(len(deleted)), delete_after=2.5)

    @commands.command()
    async def clean(self, ctx, arg1, arg2):
        allow_cmd = False
        msg_num = 0
        if int(arg2) > 1000:
            allow_cmd = True
        if not allow_cmd:
            async for message in ctx.history(limit=int(arg2)):
                if arg1 == "bot" and message.author.id == 711578412103368707:
                    await message.delete()
                    time.sleep(1)
                    msg_num += 1
                if arg1 == "self" and message.author.id == ctx.message.author.id:
                    await message.delete()
                    time.sleep(1)
                    msg_num += 1
                if arg1 == "all":
                    await message.delete()
                    time.sleep(1)
                    msg_num += 1
                if msg_num == 50:
                    await message.channel.send("Reached deletion limit of 50", delete_after=2.5)
                    break
            await message.channel.send(f"Deleted {msg_num} messages(s)", delete_after=2.5)


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["h"])
    async def help(self, ctx, *args):  # todo this command wont work at all with commands like -h colour text
        c_args = convert_tuple(args)[:-1]
        em = None
        message = None
        if c_args == "":
            em = Embed(title="Rapidbot command sections", description="We have a wide range of commands!\
                    \nAlso remember the prefix is '-'")
            em.add_field(name=":hash: Encrypt (3)    :question: Random (9)    :information_source: Info (1)",
                         value="`-h enc`?????????????????????`-h rand`??????????????????`-h info`", inline=False)
            em.add_field(name=":page_facing_up: Server (6)?????????:dollar: Currency (2)??????:rainbow: Colour text (5)",
                         value="`-h server`????????????`-h currency`????????????`-h color text`", inline=False)

            em.add_field(name="Disabled (7)     :computer: Online searches (6)    :game_die: Games (11)",
                         value="`disabled`?????????`-h search`?????????????????????????????????`-h games`", inline=False)
        else:
            if c_args in ["encryption", "encrypt", "enc", "decryption", "decrypt", "dec"]:
                em = Embed(title=":hash: Encryption commands (3)", description="`encrypt`,`decrypt`,`enc_key`")
                em.add_field(name="Here is how to use them", value="`-enc <message>`\n`-dec <encrypted message>`\n"
                                  "`-enc_key` makes a random encryption key", inline=False)
                em.set_footer(text=f"Requested by {ctx.message.author}")
                em.add_field(name="Command aliases", value="`encryption`,`encrypt`,`enc`,"
                                  "`decryption`,`decrypt`,`dec`", inline=False)

            if c_args in ["random", "rand"]:
                em = Embed(title=":question: Random commands (9)", description="`randnum`,\
                        `randuni`,`eight_ball`,`leetify`,`repeat`,\n`joke`,`char_count`,`emoji_letter`,`ttb`")
                em.set_footer(text=f"Add -h to the beginning of a command for its help section!"
                                   f" Requested by {ctx.message.author}")

            if c_args in ["info", "bot_info", "bot info"]:  # BOT INFO
                em = Embed(title="INFO HELP:", description="The info command shows data about the bot"
                                 "\n\nThis commands aliases are: `botinv`,`botweb`,`botrt`,`inservers`")

            if c_args in ["server"]:
                em = Embed(title=":page_facing_up: Server commands (6)",
                           description="`chat_links`,`channel_ids`,`members`,`roles`,`inrole`,`who_spoke`")
                em.set_footer(text=f"Add -h to the beginning of a command for its help section! "
                                   f"Requested by {ctx.message.author}")

            if c_args in ["currency", "cur"]:
                em = Embed(title=":dollar: Currency commands (2)", description="`currency_list`,`currency_convert`")
                em.set_footer(text=f"Add -h to the beginning of a command for its help section! "
                                   f"Requested by {ctx.message.author}")

            if c_args in ["color text", "colored text", "color_text", "colored_text"]:
                em = Embed(title=":rainbow: Coloured text commands (5)",
                           description="`redtext`,`orange_text`,`yellowtext`,`bluetext`,`cyantext`")
                em.set_footer(text=f"Add -h to the beginning of a command for its help section! "
                                   f"Requested by {ctx.message.author}")

            if c_args in ["search", "online search", "online_search"]:
                em = Embed(title=":computer: Online searches commands (6)",
                           description="`ggt_codes`, `ggt_te`,`ggt_ft`,\n`ggsr`,`reddits`,`meme`")
                em.set_footer(text=f"Add -h to the beginning of a command for its help section! "
                                   f"Requested by {ctx.message.author}")

            if c_args in ["games", "bet"]:
                em = Embed(title=":game_die: Game commands (11)", description="`claim`,~~daily~~,`bal`,`flip`,\
                        ~~bj~~,`dice`,\n`rps`,`multi`,~~revup~~,~~bet_dubup~~,~~bet crash~~")
                em.set_footer(text=f"Add -h to the beginning of a command for its help section! "
                                   f"Requested by {ctx.message.author}")

            if c_args in ["admin"]:
                em = Embed(title=":tools: Admin commands (2)", description="`purge`,`clean`")
                em.set_footer(text=f"Add -h to the beginning of a command for its help section! "
                                   f"Requested by {ctx.message.author}")

            if c_args in ["randword"]:  # RANDOM
                em = Embed(title="RANDWORD HELP:", description="The random word command picks x random words")
                em.add_field(name="Here is how to use it", value="`-randword <number of words>`", inline=False)

            if c_args in ["randnum", "randnumber"]:  # RANDOM # not reworked
                em = Embed(title="RANDNUM HELP:",
                           description="The random number command picks a number between two numbers")
                em.add_field(name="Here is how to use it", value="`randnum <1st number> <2nd number>`", inline=False)
                em.add_field(name="Command aliases", value="`randumber`", inline=False)

            if c_args in ["randuni"]:  # RANDOM
                em = Embed(title="RANDUNI HELP:", description="The random Unicode command picks x"
                                 " number of random Unicode characters")
                em.add_field(name="Here is how to use it", value="`randuni <number of uni chars>`", inline=False)

            if c_args in ["eight_ball"]:  # RANDOM
                em = Embed(title="EIGHT_BALL HELP:",
                           description="The eight ball command is a question and answer command")
                em.add_field(name="Here is how to use it", value="`-eight_ball <question>`", inline=False)

            if c_args in ["leetify"]:  # RANDOM
                em = Embed(title="LEETIFY HELP:", description="The leetify command turns your message into leet speak")
                em.add_field(name="Here is how to use it", value="`-leetify <message>`", inline=False)

            if c_args in ["repeat"]:  # RANDOM
                em = Embed(title="REPEAT HELP:", description="The repeat command repeats your message")
                em.add_field(name="Here is how to use it", value="`-repeat <message>`", inline=False)

            if c_args in ["joke"]:  # RANDOM # not reworked
                em = Embed(title="JOKE HELP:", description="The joke command sends a funny joke!")

            if c_args in ["char_count", "char count"]:  # RANDOM
                em = Embed(title="CHAR_COUNT HELP:", description="The char_count command counts the number of"
                                 " characters in your message")
                em.add_field(name="Here is how to use it", value="`-char_count <message>`", inline=False)

            if c_args in ["emoji_letter", "emoji_letters", "big_text"]:  # RANDOM
                em = Embed(title="EMOJI_LETTERS HELP:",
                           description="The emoji letter command turns your message into letter emojis")
                em.add_field(name="Here is how to use it", value="`-emoji_letter <message>`", inline=False)
                em.add_field(name="Command aliases", value="`emoji_letters`,`big_text`", inline=False)

            if c_args in ["ttb"]:  # RANDOM
                em = Embed(title="TTB HELP:", description="The talk to bot command asks an AI your message/question")
                em.add_field(name="Here is how to use it", value="`-ttb <message/question>`", inline=False)

            if c_args in ["chat_links"]:  # SERVER INFO
                em = Embed(title="CHAT_LINKS HELP:", description="The chat links command retrieves all the links"
                                                                 "in chat from upto 1000 messages")
                em.add_field(name="Here is how to use it", value="`-chat_links <num>`", inline=False)

            if c_args in ["channelids", "channel_ids"]:  # SERVER INFO
                em = Embed(title="CHANNEL_IDS HELP:",
                           description="The channel ids command gets all channel ids from current server")
                em.add_field(name="Here is how to use it", value="`-channel id` shows channel ids and names"
                                  "\n`-channel id raw` shows just channel ids", inline=False)
                em.add_field(name="Command aliases", value="`channelids`", inline=False)

            if c_args in ["members"]:  # SERVER INFO
                em = Embed(title="MEMBERS HELP:", description="The members command lists all the members in the server")

            if c_args in ["roles"]:  # SERVER INFO
                em = Embed(title="ROLES HELP:", description="The roles command lists all the roles in the server")

            if c_args in ["inrole"]:  # SERVER INFO
                em = Embed(title="MEMBERS HELP:", description="The in role command lists all members with a role")
                em.add_field(name="Here is how to use it", value="`-inrole <@role>`", inline=False)

            if c_args in ["who_spoke"]:  # SERVER INFO
                em = Embed(title="WHO_SPOKE HELP:", description="The who spoke command finds how many times"
                                 " people spoke in last x messages")
                em.add_field(name="Here is how to use it",
                             value="`-who_spoke <how many msg's to look at>` limited to 1000 messages", inline=False)

            if c_args in ["currency_list"]:  # CURRENCY
                em = Embed(title="CURRENCY_LIST HELP:",
                           description="The currency_listing command shows values of many currencies")
                em.add_field(name="Here is how to use it",
                             value="`-currency_list`\n`-currency_list <Currency to convert from>`", inline=False)

            if c_args in ["currency_convert"]:  # CURRENCY
                em = Embed(title="CURRENCY_CONVERT HELP:",
                           description="The currency conversion command converts between 2 currencies")
                em.add_field(name="Here is how to use it",
                             value="`-currency_convert <currency from> <currency to> <amount>`", inline=False)

            if c_args in ["redtext", "red_text"]:  # COLOUR TEXT
                em = Embed(title="REDTEXT HELP:", description="The red text command turns your message red")
                em.add_field(name="Here is how to use it", value="`-redtext <message>", inline=False)

            if c_args in ["orangetext", "orange_text"]:  # COLOUR TEXT
                em = Embed(title="ORANGETEXT HELP:", description="The orange text command turns your message orange")
                em.add_field(name="Here is how to use it", value="`-orangetext <message>", inline=False)

            if c_args in ["yellowtext", "yellow_text"]:  # COLOUR TEXT
                em = Embed(title="YELLOWTEXT HELP:", description="The yellow text command turns your message yellow")
                em.add_field(name="Here is how to use it", value="`-yellowtext <message>", inline=False)

            if c_args in ["bluetext", "blue_text"]:  # COLOUR TEXT
                em = Embed(title="BLUETEXT HELP:", description="The blue text command turns your message blue")
                em.add_field(name="Here is how to use it", value="`-bluetext <message>", inline=False)

            if c_args in ["cyantext", "cyan_text"]:  # COLOUR TEXT
                em = Embed(title="CYANTEXT HELP:", description="The cyan text command turns your message cyan")
                em.add_field(name="Here is how to use it", value="`-cyantext <message>", inline=False)

            if c_args in ["ggt_codes"]:  # SEARCHES
                em = Embed(title="GGT_CODES HELP:", description="The Google translate language codes command shows "
                                 "you the abbreviated letters for that language")

            if c_args in ["ggt_te"]:  # SEARCHES
                em = Embed(title="GGT_TE HELP:", description="The Google translate to english command attempts "
                                 "to convert a message to english")
                em.add_field(name="Here is how to use it", value="`-ggt_te <message>`", inline=False)

            if c_args in ["ggt_ft"]:  # SEARCHES
                em = Embed(title="GGT_FT HELP:", description="The Google translate from to command translates "
                                 "a message from one language to another")
                em.add_field(name="Here is how to use it", value="`-ggt_ft <lang from> <lang to> <message>`",
                             inline=False)

            if c_args in ["ggsr", "ggsi", "ggsv"]:  # SEARCHES
                em = Embed(title="GGSR HELP:", description="The google search result command searches "
                                 "\n google for x amount of results")
                em.add_field(name="Here is how to use it", value="`-ggsr <num of results> <search>`", inline=False)
                em.add_field(name="Command aliases", value="`ggsi`,`ggsv`", inline=False)

            if c_args in ["reddits"]:  # SEARCHES
                em = Embed(title="REDDITS HELP:",
                           description="The reddit search command retrieves a img/gif/vid from a subreddit")
                em.add_field(name="Here is how to use it",
                             value="`-reddits <subreddit> <post number>` Suggest post num of 1", inline=False)

            if c_args in ["meme"]:  # SEARCHES
                em = Embed(title="MEME HELP:", description="The meme command retrieves a meme!")

            if c_args in ["claim", "claim_token"]:  # GAMES
                em = Embed(title="CLAIM HELP:", description="The claim command means you can claim rewards!")
                em.add_field(name="Here is how to use it", value="`-claim <token>`", inline=False)
                em.add_field(name="Command aliases", value="`claim_token`", inline=False)

            if c_args in ["daily"]:  # GAMES
                em = Embed(title="DAILY COINS HELP:", description="The daily coins command gives you some coins!")

            if c_args in ["bal"]:  # GAMES
                em = Embed(title="BAL HELP:", description="The balance command displays your current balance")
                em.add_field(name="Here is how to use it",
                             value="`-bal` for your balance\n `-bal <@user>` for someone elses balance", inline=False)

            if c_args in ["flip", "bet_flip"]:  # GAMES
                em = Embed(title="COINFLIP HELP:", description="The coinflip command is a betting game for 2x money")
                em.add_field(name="Here is how to use it", value="`-flip <h or t> <amount to bet>`",
                             inline=False)
                em.add_field(name="Command aliases", value="`bet_flip`", inline=False)

            if c_args in ["dice", "bet_dice"]:  # GAMES
                em = Embed(title="DICE HELP:", description="The dice roll command is a betting game for 5x money")
                em.add_field(name="Here is how to use it", value="`-dice <dice side num (1-6)> <amount to bet>`",
                             inline=False)
                em.add_field(name="Command aliases", value="`bet_dice`", inline=False)

            if c_args in ["bj", "bet_bj"]:  # GAMES
                em = Embed(title="BJ HELP:", description="The blackjack command is a betting game for 1.66x money")
                em.add_field(name="Here is how to use it", value="`-bj <bet amount>`", inline=False)
                em.add_field(name="Command aliases", value="`bet_bj`", inline=False)

            if c_args in ["rps", "bet_rps"]:  # GAMES
                em = Embed(title="RPS HELP:",
                           description="The rock paper scissors command is a betting game for 1.5x money")
                em.add_field(name="Here is how to use it", value="`-rps <r or p or s> <amount to bet>`", inline=False)
                em.add_field(name="Command aliases", value="`bet_rps`", inline=False)

            if c_args in ["multi", "bet_multi"]:  # GAMES
                em = Embed(title="MULTI HELP:", description="The multiplier command is a betting game where you"
                                 " decide the multiplier! Min multiplier of 3")
                em.add_field(name="Here is how to use it", value="`-multi <multiplier> <amount to bet>`", inline=False)
                em.add_field(name="Command aliases", value="`bet_multi`", inline=False)

            if c_args in ["revup", "bet_revup"]:  # GAMES
                em = Embed(title="REVUP HELP:", description="The rev up command is a betting game where "
                                 "you get a random multiplier from 0 to 1000!")
                em.add_field(name="Here is how to use it", value="`-revup <amount to bet> <num of goes>`", inline=False)
                em.add_field(name="Command aliases", value="`bet_revup`", inline=False)

            if c_args in ["dubup", "bet_dubup"]:  # GAMES
                em = Embed(title="DUBUP HELP:", description="The rev up double up command is a \
                betting game where you get 2 multipliers that could get you up to 40000X!")
                em.add_field(name="Here is how to use it", value="`-dubup <amount to bet> <num of goes>`",
                             inline=False)
                em.add_field(name="Command aliases", value="`bet_dubup`", inline=False)

            if c_args in ["crash", "bet crash"]:  # GAMES
                em = Embed(title="CRASH HELP:", description="The crash command is a \
                betting game where chose when you pull out of the game and keep your winnings!")
                em.add_field(name="Here is how to use it", value="`-crash <amount to bet>`", inline=False)

            if c_args in ["quiz"]:  # GAMES
                em = Embed(title="QUIZ HELP:", description="The quiz command is a knowledge game!")
                em.add_field(name="Here is how to use it",
                             value="`-quiz`, and then `-a` to answer the question asked", inline=False)

            # admin help

            if c_args in ["purge"]:  # ADMIN
                em = Embed(title="PURGE HELP:", description="The purge command deletes x number of messages"
                                 " up to 14 days old, use clean for anything older")
                em.add_field(name="Here is how to use it", value="`-purge <bot/self/all> <num of msg>`", inline=False)

            if c_args in ["clean"]:  # ADMIN
                em = Embed(title="CLEAN HELP:",
                           description="The clean command individually deleted messages where purge cant")
                em.add_field(name="Here is how to use it", value="`-clean <bot/self/all> <num of msg>`", inline=False)

        if em is not None:
            await ctx.channel.send(embed=em)
        if message is not None:
            await ctx.channel.send(message)


intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix=commands.when_mentioned_or("-"), case_insensitive=True, intents=intents)
bot.remove_command('help')


@bot.event
async def on_command_error(ctx, error):
    print(error)
    error_check = str(error)
    if not error_check.startswith("Command \""):
        message = ctx.message.content[1:]
        message = message.split()
        em = Embed(title=f"Command error, {error_check}", description=f"Need help? `-h {message[0]}`",
                   color=discord.Colour(0xff0000))
        await ctx.channel.send(embed=em.set_footer(text=f"Requested by {ctx.author}"))


bot.add_cog(Encryption(bot))
bot.add_cog(Random(bot))
bot.add_cog(BotInfo(bot))
bot.add_cog(Server(bot))
bot.add_cog(Currency(bot))
bot.add_cog(ColourText(bot))
bot.add_cog(OnlineSearching(bot))
bot.add_cog(Games(bot))
bot.add_cog(Admin(bot))
bot.add_cog(Help(bot))

global links_list  # todo what to do with this stuff?

links_on = False

if links_on:
    with open("links.txt", "r", encoding="utf-8") as f:
        links_list = f.readlines()

cooldown_ids = {}


class cooldown:
    # todo per command cooldowns and duplication checks required
    def check(self, userid, length):
        if userid not in cooldown_ids:
            cooldown_ids.update({userid: [datetime.datetime.now(), length]})
        else:
            cooldown_data = cooldown_ids[userid]
            timestr = str(datetime.datetime.now() - cooldown_data[0])
            diff = sum([a*b for a, b in zip([3600, 60, 1], map(float, timestr.split(':')))])
            if diff < cooldown_data[1]:
                return f"Command sent to fast, please wait {round(cooldown_data[1]-diff, 2)}s"
            else:
                del cooldown_ids[userid]


ttb_data = {}


class ttb:  # todo add ttb prev conv functionality
    def run(self, stimulus, context=[], session=None):
        sessions = dict()
        req = requests.get("https://www.cleverbot.com/")
        cookies = {'XVIS': re.search(r"\w+(?=;)", req.headers["Set-cookie"]).group()}
        payload = f"stimulus={requests.utils.requote_uri(stimulus)}&"
        _context = context[:]
        reverse_context = list(reversed(_context))
        for i in range(len(_context)):
            payload += f"vText{i + 2}={requests.utils.requote_uri(reverse_context[i])}&"

        if session:
            if session not in sessions.keys():
                sessions[session] = list()
            _session = list(reversed(sessions[session]))
            for i in range(len(sessions[session])):
                payload += f"vText{i + len(_context) + 2}={requests.utils.requote_uri(_session[i])}&"
            sessions[session] = _context + sessions[session]
        payload += "cb_settings_scripting=no&islearning=1&icognoid=wsf&icognocheck="
        payload += hashlib.md5(payload[7:33].encode()).hexdigest()
        req = requests.post("https://www.cleverbot.com/webservicemin?uc=UseOfficialCleverbotAPI",
                            cookies=cookies, data=payload)
        response = str(req.content)[2:].split("\\r")
        return response[0]


def dec_crunch(number):
    if str(number)[::-1].find('.') > 3:
        return float(number) // 0.001 / 1000
    else:
        return round(float(number), 3)


rcoin_data = {}


class rcoin:
    with open("strs/rcoin_bals.txt") as f:
        for line in f.readlines():
            userid, bal = line.replace("\n", "").split(", ")
            rcoin_data.update({int(userid): round(float(bal), 3)})

    def bal(self, userid):
        try:
            rcoin_data.update({int(userid): round(float(rcoin_data[int(userid)]), 3)})
        except:
            rcoin_data.update({int(userid): 100})
        return rcoin_data[int(userid)]

    def save(self):
        with open("strs/rcoin_bals.txt", "w") as f:
            [f.write(f"{key}, {value}\n") for key, value in rcoin_data.items()]

    def win(self, userid, amount):
        rcoin_data.update({int(userid): rcoin_data[int(userid)]+amount})
        rcoin.save(0)

    def lose(self, userid, amount):
        rcoin_data.update({int(userid): rcoin_data[int(userid)]-amount})
        rcoin.save(0)

    def check(self, userid, amount):
        if amount < 1:
            return "You cannot enter a value smaller than 1 rcoin"
        else:
            if amount > rcoin_data[int(userid)]:
                return f"This is {amount - rcoin_data[int(userid)]} rcoins over the amount you have"
            else:
                return dec_crunch(amount)


@bot.event
async def on_message(message):
    global rtime
    rtime = datetime.datetime.now()
    msg2 = message.content.replace("\n", " // ")
    msg_data = (f"TIME: {rtime} SERVER ID: {message.guild.id} CHANNEL ID: {message.channel.id} "
                f"USER ID: {message.author.id} MESSAGE ID: {message.id} - [ 'SERVER: {message.guild} "
                f"CHANNEL: {message.channel} USER: {message.author} MESSAGE: {msg2}' ]")
    print(msg_data)

    if message.content.startswith("-"):
        with open('strs/msgstore.txt', 'a+') as f:
            f.write(f"{msg_data}\n")

    # inserted LINK shard

    if message.channel.id in [867113471241093120] or message.author.id == 425373518566260766:
        if message.content.lower().startswith("-search"):
            search = message.content[8:]
            with open(f"temp.txt", "w+", encoding="utf-8") as p:
                [p.write(line) for line in links_list if search in line]
            with open('temp.txt') as result:
                unique_lines = set(result.readlines())
                with open(f"search-{search}.txt", "w+", encoding="utf-8") as rmdup:
                    rmdup.writelines(set(unique_lines))

            with open(f"search-{search}.txt", encoding="utf-8") as f:
                search_yield = len(f.readlines())

            if search_yield == 0:
                await message.channel.send(f"There was no results for '{search}'")
            else:
                if search_yield > 1000:
                    await message.channel.send(f"Search success, found {search_yield} results for '{search}'\n"
                                               f"To many results to send, have the txt instead!")
                    await message.channel.send(file=discord.File(fr'search-{search}.txt'))
                else:
                    await message.channel.send(f"Search success, found {search_yield} results for '{search}'\n"
                                               f"To see ALL of these results type '-open {search}'")

        if message.content.lower().startswith("-open"):
            open1 = message.content[6:]
            try:
                with open(f"search-{open1}.txt") as f:
                    for line in f.readlines():
                        await message.channel.send(line)
                        time.sleep(0.5)
            except:
                await message.channel.send(f"Search file not found for {open1}, maybe try '-search {open1}' first!")

        if message.content.lower() == "-link":
            for i in range(50):
                with open("counter.txt", "r") as x:
                    counter = int(str(x.readlines())[2:-2])
                with open("counter.txt", "w") as x:
                    x.write(str(counter+1))

                await message.channel.send(str(counter)+links_list[counter-1])
                time.sleep(1.25)

        if message.content.lower() == "-pick":
            await message.channel.send(str(counter)+links_list[random.randint(0, len(links_list))])

        if message.content.lower().startswith("-spec"):
            num = int(message.content[6:])
            await message.channel.send(str(num)+links_list[num-1])

        if message.content.lower().startswith("-links"):
            num = int(message.content[6:])-1
            for i in range(50):
                line = str(num+1)+links_list[num]
                await message.channel.send(line)
                num += 1
                time.sleep(1)

        if message.content.lower() == "-data-log":
            await message.channel.send(file=discord.File(r'indexed_data.txt'))

    # inserted LINK shard above

    if message.content.startswith("-") and message.author.bot is False:

        # TOKEN DROPS
        token_drops_on = False

        if token_drops_on:
            if random.randint(0, 100) == 1:  # todo make certain users more or less lucky
                import string
                token = ""
                for i in range(25):
                    token = token + (random.choice(string.ascii_uppercase))
                    if i in [4, 9, 14, 19]:
                        token += "-"
                token_value = random.randint(10, 100)
                with open('strs/tokens.txt', 'a+') as f:
                    f.write(f"{token}, {token_value}\n")

                em = Embed(title=f"{token}", description=f"Claim the above {token_value}"
                                 f" coin token by typing -claim <token>")
                await message.channel.send(embed=em)

        allow_command = cooldown.check(0, message.author.id, 1.5)
        if allow_command is not None:
            await message.channel.send(allow_command)
            message.content = ""

        await bot.process_commands(message)

        if message.author.id == 425373518566260766:
            if message.content.startswith("-update strs"):
                with open('strs/msgstore.txt', 'r') as f:
                    sendback = f.read()
                    with open('strs/linkstore.txt', 'w') as i:
                        #enc.get_links(sendback)  #todo drop in replacement
                        a = (re.findall(r'(https?://[^\s]+)', sendback))
                        b = (re.findall(r'(http?://[^\s]+)', sendback))
                        c = ('\n'.join(a))
                        d = ('\n'.join(b))
                        write = f'{c},{d}'
                        i.write(write)
                        i.close()
                        with open('strs/linkstore.txt') as result:
                            unique_lines = set(result.readlines())
                            with open('strs/linkndp.txt', 'w') as rmdup:
                                rmdup.writelines(set(unique_lines))

                                bad_words = ['https://discord.com/channels/']
                                with open('strs/linkndp.txt') as oldfile, open('strs/linknd-ndsc.txt', 'w') as new_file:
                                    for line in oldfile:
                                        if not any(bad_word in line for bad_word in bad_words):
                                            new_file.write(line)

                await message.channel.send("```Lnk data Success```")
                file1 = open("strs/msgstore.txt", "r")
                d = dict()

                for line in file1:
                    line = line.strip()
                    line = line.lower()
                    words = line.split(" ")
                    for word in words:
                        if word in d:
                            d[word] = d[word]+1
                        else:
                            d[word] = 1

                with open('strs/occurdata.txt', 'w') as f:
                    f.write("\n\nNumber of occurrences of each word in file is:\n ===============\n")
                    [f.write(str(f'{key},":",{d[key]} \n')) for key in list(d.keys())]
                    file1.close()
                    await message.channel.send("```Occr data Success```")

            if message.content.startswith("-randlink"):
                with open('strs/linknd-ndsc.txt'):
                    await message.channel.send(random.choice(f.readlines()))

            if message.content.startswith("-allmsg without"):
                bad_words = message.content[16:].split()
                await message.channel.send(bad_words)
                with open('strs/msgstore.txt') as oldfile,\
                        open(f'strs/edits/allmsg-withoutwords-{message.content[16:]}.txt', 'w') as newfile:
                    for line in oldfile:
                        if not any(bad_word in line for bad_word in bad_words):
                            newfile.write(line)
                    await message.channel.send(
                        file=discord.File(f'strs/edits/allmsg-withoutwords-{message.content[16:]}.txt'))

            if message.content.startswith("-allmsg only"):
                bad_words = message.content[13:].split()
                await message.channel.send(bad_words)
                with open('strs/msgstore.txt') as oldfile,\
                        open(f'strs/edits/allmsg-findwords-{message.content[13:]}.txt', 'w') as newfile:
                    for line in oldfile:
                        if any(bad_word in line for bad_word in bad_words):
                            newfile.write(line)
                    await message.channel.send("```SUCCESS```")
                    await message.channel.send(
                        file=discord.File(f'strs/edits/allmsg-findwords-{message.content[13:]}.txt'))

            if message.content.startswith("-admin upload"):
                await message.channel.send(file=discord.File(f'{message.content[14:]}'))

            # data not admin
            if message.content.startswith("-thischat msg"):
                bad_words = [f'{message.channel.id}']
                await message.channel.send(bad_words)
                with open('strs/msgstore.txt') as oldfile,\
                        open(f'strs/edits/chatmsg-{message.channel.id}.txt', 'w') as new_file:
                    for line in oldfile:
                        if any(bad_word in line for bad_word in bad_words):
                            new_file.write(line)
                    await message.channel.send("```SUCCESS```")
                    await message.channel.send(file=discord.File(f'strs/edits/chatmsg-{message.channel.id}.txt'))

            if message.content.startswith("-status"):
                change = True
                if message.content == "-status dev":
                    game = discord.Game("Currently programming")
                if message.content == "-status on":
                    game = discord.Game(f"On since {datetime.datetime.now()}")
                if message.content == "-status make":
                    game = discord.Game(f"{message.content[13:]}")
                else:
                    change = False
                if change:
                    await bot.change_presence(status=discord.Status.online, activity=game)

        # old text to speach vc code was here using gtts module


@bot.event
async def on_connect():
    print(f'Connection established to discord, Logged in as {bot.user} ({bot.user.id})')
    print(f'-----------------------------------------------\n'
          f'Cpu: {ut.cpu_percent()}% of {ut.cpu_count(logical=False)}core/{ut.cpu_count()}thread\n'
          f'Ram: {ut.virtual_memory().percent}% in use, '
          f'{round(ut.virtual_memory().available*100/ut.virtual_memory().total, 1)}% free '
          f'({round(ut.virtual_memory().used/1048576, 0)}/{round(ut.virtual_memory().total/1048576, 0)}MB)\n'
          f'Storage: {ut.disk_usage("/").percent}% used, {round(ut.disk_usage("/").used/1048576, 2)}'
          f'/{round(ut.disk_usage("/").total/1048576, 2)}MB\n'
          f'-----------------------------------------------')


@bot.event
async def on_disconnect():
    print("YOU HAVE BEEN DISCONNECTED FROM THE INTERNET, BOT NO LONGER OPERATIONAL")


@bot.event
async def on_guild_join(guild):
    async def find_channel(guild_):
        for c in guild.text_channels:
            if not c.permissions_for(guild_.me).send_messages:
                continue
            return c

    channel = await find_channel(guild)
    em = Embed(title='Hi im rapidbot!!', description="My command prefix is '-'\
     try -help to see a commands list", colour=discord.Color.gold())
    await channel.send(embed=em)


bot.run('TOKEN')
