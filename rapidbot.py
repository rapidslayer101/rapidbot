# MADE BY RAPIDSLAYER101#260, DO NOT COPY, DO NOT SHARE, DO NOT USE

global time, sys, googletrans, google, random, os, zlib, base64, re
import datetime, decimal, time, os, random, zlib, base64, re, socket, hashlib  # inbuilt

import googletrans, discord, requests, urllib, praw, psutil  # installed modules
from discord.ext import commands
from forex_python.converter import CurrencyRates, CurrencyCodes
from googletrans import Translator

global start_time
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
# todo prefix changes?

# file system checks
if not os.path.isdir("settings"):
    os.mkdir("settings")
if not os.path.isdir("strs"):
    os.mkdir("strs")
if not os.path.isfile("settings/nsfw.txt"):
    open("settings/nsfw.txt", "w").close()
if not os.path.isfile("strs/msgstore.txt"):
    open("strs/msgstore.txt", "w").close()
if not os.path.isfile("strs/tokens.txt"):
    open("strs/tokens.txt", "w").close()
if not os.path.isfile("strs/rcoin_bals.txt"):
    open("strs/rcoin_bals.txt", "w").close()


if not os.path.isfile("settings/event_expire.txt"):  # thomas
    open("settings/event_expire.txt", "w").close()
if not os.path.isfile("settings/event_players.txt"):  # thomas
    open("settings/event_players.txt", "w").close()

# encrypt def stuff
# the manual setup version of this is found within enc 5.x versions
config_key = "c-k{jF#Rxp+l&N5BV!X&Gjj_|16|ugYZMQyKeSjyHBL=SLo;5xuspS>q_Q+KzaTm`Fx)jLBr?>~KcKocu{" \
             "b3yJtHeS$68(4G1$e;-NVb<$I78Drm7;jEGaKnN3SL-!a2;z&)3GzULRzQp@D&drGbF~0LUgO5d"
c_key = zlib.decompress(base64.b85decode(config_key)).decode('utf-8').split("🶘")
hex_head, hex_tail = c_key[0].split(" ")
hexlen_ = random.randint(int(hex_head), int(hex_tail))
alphagens = c_key[1]
key_p1_head, key_p1_tail = c_key[2].split(" ")
key_p1 = random.randint(int(key_p1_head), int(key_p1_tail))
alphalen = len(alphagens)


def generator():
    run = 0
    while True:
        run += 1
        if run % 5 == 0 or run == 1:
            hexgens = ""
            while len(hexgens) != hexlen_:
                hexgens_add = random.choice(alphagens)
                if hexgens_add not in hexgens:
                    hexgens += hexgens_add
        try:
            rand_base_alpha = ''
            while len(rand_base_alpha) != hexlen_:
                alpha_new_char = random.choice(hexgens)
                if alpha_new_char not in rand_base_alpha:
                    rand_base_alpha += alpha_new_char

            conversion_table = []
            for i in rand_base_alpha:
                conversion_table.append(i)

            decimal = key_p1
            old_decimal = key_p1
            hexadecimal = ''

            while decimal > 0:
                remainder = decimal % hexlen_
                hexadecimal = conversion_table[remainder] + hexadecimal
                decimal = decimal // hexlen_

            conversion_table = {}
            cvtable_counter = 0
            for i in rand_base_alpha:
                conversion_table.__setitem__(i, cvtable_counter)
                cvtable_counter += 1

            hexadecimal = hexadecimal.strip().upper()
            decimal = 0
            power = len(hexadecimal) - 1

            for digit in hexadecimal:
                decimal += conversion_table[digit] * hexlen_ ** power
                power -= 1

            if decimal == old_decimal:
                break
        except: xx = 0

    master_key = rand_base_alpha + hexadecimal

    conversion_table = {}
    cvtable_counter = 0
    for i in master_key[:hexlen_]:
        conversion_table.__setitem__(i, cvtable_counter)
        cvtable_counter += 1

    hexadecimal = master_key[hexlen_:].strip().upper()
    num1 = 0
    power = len(hexadecimal) - 1

    for digit in hexadecimal:
        num1 += conversion_table[digit] * hexlen_ ** power
        power -= 1

    if num1 == key_p1:
        def alpha_make():
            rand_base_alpha_ = ''
            while True:
                alpha_new_char_ = random.choice(alphagens)
                if alpha_new_char_ not in rand_base_alpha_:
                    rand_base_alpha_ = rand_base_alpha_ + alpha_new_char_
                elif len(rand_base_alpha_) == alphalen:
                    break
            return rand_base_alpha_

        master_key = f"{alpha_make()}{str(hexlen_).replace('4', 'a').replace('5', 'b')}{master_key}{alpha_make()}"
        master_key = base64.b85encode(zlib.compress(master_key.encode('utf-8'), 9)).decode('utf-8')
    return master_key


def shifter(plaintext, newnum, num, num2, alphabet, replace, forwards):
    output_enc = ""
    counter = 0
    for msg in plaintext:
        counter = counter + 2
        if msg in alphabet:
            key = int(newnum[counter:counter + 2])
            if key > alphalen:
                key = num2
            if not forwards:
                key = key - key - key
            if key == 0:
                new_alphabet = alphabet
            elif key > 0:
                new_alphabet = alphabet[key:] + alphabet[:key]
            else:
                new_alphabet = alphabet[(alphalen + key):] + alphabet[:(alphalen + key)]
            encrypted = ""
            for message_index in range(0, len(msg)):
                if msg[message_index] == " ":
                    encrypted += " "
                for alphabet_index in range(0, len(new_alphabet)):
                    if msg[message_index] == alphabet[alphabet_index]:
                        encrypted += new_alphabet[alphabet_index]
            output_enc += encrypted
        else:
            output_enc += msg

    if replace:
        num = str(num).replace("0", "g").replace("1", "e").replace("2", "k").replace("3", "i").replace("4", "u") \
            .replace("5", "d").replace("6", "r").replace("7", "w").replace("8", "q").replace("9", "p")
        return num + output_enc
    if not replace:
        return output_enc


def get_prime_number(candidate):
    prime_numbers_ = []
    while True:
        if candidate <= 3:
            prime_numbers_.append(candidate)
            yield candidate
        is_prime = True
        for prime_num in prime_numbers_:
            if candidate % prime_num == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers_.append(candidate)
            yield candidate
        candidate += 1


def fib_iter(text, num2_):
    a = 1
    b = 1
    c = 1
    while len(str(b)) < len(text) * 2:
        total = (a + b * num2_) * c
        c = b
        b = a
        a = total
    return b


def shifter_gen_loop(e_text):
    new_num = ""
    while len(new_num) < len(e_text) * 2 + 100:
        new_num = str(new_num) + str(next(prime_numbers))
    return new_num


def convert(m_key):
    m_key = zlib.decompress(base64.b85decode(m_key)).decode('utf-8')
    p0_alpha = m_key[:alphalen]
    if m_key[alphalen:alphalen+1] == "a":
        hexlen = 4
    if m_key[alphalen:alphalen+1] == "b":
        hexlen = 5
    p1_key = m_key[alphalen:alphalen+1+hexlen]
    p1_e = m_key[alphalen+1+hexlen:-alphalen]
    p3_alpha = m_key[-alphalen:]

    conversion_table = {}
    cvtable_counter = 0
    for i in p1_key:
        conversion_table.__setitem__(i, cvtable_counter)
        cvtable_counter += 1

    hexadecimal = p1_e.strip().upper()
    num1 = 0
    power = len(hexadecimal) - 1

    for digit in hexadecimal:
        num1 += conversion_table[digit] * hexlen ** power
        power -= 1

    return p0_alpha, p3_alpha, num1


try:
    with open("settings/enc-key.txt", encoding="utf-8") as f:
        master_key = str(f.readlines())[2:-2]
except:
    print(f"Input an encrypt key below, leave blank to autogenerate a key")
    while True:
        master_key = input(" > ")
        if not master_key == "":
            try:
                convert(master_key)
                break
            except:
                print("key convert error")
        else:
            master_key = generator()
            break
    with open("settings/enc-key.txt", "w", encoding="utf-8") as f:
        f.write(master_key)


while True:
    with open("settings/enc-key.txt") as f:
        for line in f.readlines():
            master_key = line
    try:
        mkey_data = convert(master_key)
        alpha1 = mkey_data[0]
        alpha2 = mkey_data[1]
        num2 = mkey_data[2]
        break
    except:
        with open("settings/enc-key.txt", "w", encoding="utf-8") as f:
            f.write(generator())

print(f"\nENCRYPTION KEY:\n{master_key}\n\nSETTINGS KEY:\n{config_key}\n")


def convert_tuple(tup):
    string_ = ''
    for item in tup:
        string_ += item + " "
    return string_


def search(data, filter_fr, filter_to):
    data = str(data)
    m = re.search(f"""{filter_fr}(.+?){filter_to}""", data)
    if m:
        output = m.group(1)
    else:
        output = None
    return output


def encrypt(text):
    plaintext = base64.b85encode(zlib.compress(text.encode('utf-8'), 9)).decode('utf-8')
    global prime_numbers
    prime_numbers = get_prime_number(random.randint(100000, 800000))
    while True:
        if next(prime_numbers) > 100000 and random.randint(1, 150) == 1:
            num = next(prime_numbers)
            break

    new_num = shifter_gen_loop(plaintext)
    e_text = shifter(plaintext, new_num, num, num2, alpha1, True, True)
    content = str(e_text[:6]).replace("g", "0").replace("e", "1").replace("k", "2").replace("i", "3") \
        .replace("u", "4").replace("d", "5").replace("r", "6").replace("w", "7").replace("q", "8").replace("p", "9")

    prime_numbers = get_prime_number(int(content))
    while True:
        x = next(prime_numbers)
        if x == int(content):
            num = x
            break

    b = str(fib_iter(e_text, num2))
    return shifter(e_text, b, num, num2, alpha2, False, True)


def decrypt(etext):
    try:
        b = str(fib_iter(etext, num2))
        num = 0
        d_txt = shifter(etext, b, num, num2, alpha2, False, False)
        content = str(d_txt[:6]).replace("g", "0").replace("e", "1").replace("k", "2").replace("i", "3") \
            .replace("u", "4").replace("d", "5").replace("r", "6").replace("w", "7").replace("q", "8").replace("p", "9")

        prime_numbers = get_prime_number(int(content))
        while True:
            x = next(prime_numbers)
            if x == int(content):
                num = x
                break

        newnum = ""
        run = 0
        while len(newnum) < len(d_txt) * 2 + 100:
            run += 1
            newnum = str(newnum) + str(next(prime_numbers))
            if run % 1000 == 0:
                print(run, len(d_txt), len(str(newnum)))

        output_end = shifter(d_txt[6:], newnum, num, num2, alpha1, False, False).replace(" ", "")
        return zlib.decompress(base64.b85decode(output_end)).decode('utf-8')
    except:
        print("[CND] " + etext)
        return "[CND]"


print("Opening connection to discord")


class Encryption(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def enc_key(self, ctx):
        await ctx.channel.send(f"Randomly generated encryption key:\n```{generator()}```")

    @commands.command(aliases=['enc'])
    async def encrypt(self, ctx, *, arg):
        e_text2 = encrypt(arg)
        if len(e_text2) > 1900:
            with open('strs/temp.txt', 'w') as i:
                i.write(e_text2)
            embed = discord.Embed(title=f"Your encrypted text is over the 1900 char limit as it is {len(e_text2)}"
                                        f" chars so has to be sent as a file")
            embed.set_footer(text=f"Requested by {ctx.author}")
            await ctx.channel.send(embed=embed)
            await ctx.channel.send(file=discord.File('strs/temp.txt'))
        if len(e_text2) < 1900:
            await ctx.channel.send(f"```Encrypted text ({len(ctx.message.content[9:])} --> {len(e_text2)}):"
                                   f" chars:\n{e_text2}\n\nRequested by {ctx.author}```")

    @commands.command(aliases=['dec'])
    async def decrypt(self, ctx, *args):
        final_output = decrypt(convert_tuple(args))
        if len(final_output) > 1900:
            with open('strs/temp.txt', 'w') as i:
                i.write(final_output)
            embed = discord.Embed(title=f"Your encrypted text is over the 1900 char limit as it is {len(final_output)}"
                                           f" chars so has to be sent as a file")
            embed.set_footer(text=f"Requested by {ctx.author}")
            await ctx.channel.send(embed=embed)
            await ctx.channel.send(file=discord.File('strs/temp.txt'))
        if len(final_output) < 1900:
            await ctx.channel.send(f"```Decrypted text:\n"
                                   f"{final_output}"
                                   f"\n\nRequested by {ctx.author}```")


class Random(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def randword(self, ctx, arg):
        n = int(arg)
        allowcmd = 0
        if n > 1:
            if n > 100:
                embed = discord.Embed(title="Number over max word limit!", description="There is a 100 words limit")
                embed.set_footer(text=f"Requested by {ctx.author}")
                await ctx.channel.send(embed=embed)
                allowcmd = 1
            else:
                lookup = str(ctx.author.id)
                with open('settings/coin.txt') as myFile:
                    for line in myFile:
                        if lookup in line:
                            import decimal
                            balance = decimal.Decimal(line[20:])
                            balance = balance / 20
                            head, sep, tail = str(balance).partition('.')
                if n > int(head):
                    embed = discord.Embed(title="Number over word limit!", description=f"There is a {head} words limit,\
                    increase this by getting more coins by playing games! do `-help games` to see the games list")
                    embed.set_footer(text=f"Requested by {ctx.author}")
                    await ctx.channel.send(embed=embed)
                    allowcmd = 1
        if n < 1:
            await ctx.channel.send("```The minimum words is 1!```")
            allowcmd = 1
        if not allowcmd == 1:
            from nltk.corpus import words  # todo fix, module missing
            from random import sample
            rand_words = ' '.join(sample(words.words(), n))
            embed = discord.Embed(title="Random words:", description=rand_words)
            embed.set_footer(text=f"Requested by {ctx.author}")
            await ctx.channel.send(embed=embed)

    @commands.command(aliases=["randnumber"])
    async def randnum(self, ctx, arg1, arg2):
        outputn = random.randint(int(arg1), int(arg2))
        string = f"Your random number between {int(arg1)} and {int(arg2)} is:"
        embed = discord.Embed(title=string, description=outputn)
        embed.set_footer(text=f"Requested by {ctx.author}")
        await ctx.channel.send(embed=embed)

    @commands.command()
    async def randuni(self, ctx, arg):  # todo fix, does not work without currency system
        alphaamount = int(arg)
        allowcmd = 0
        if alphaamount > 1:
            if alphaamount > 500:
                embed = discord.Embed(title="Number over max char limit!", description="There is a 500 char limit")
                embed.set_footer(text=f"Requested by {ctx.author}")
                await ctx.channel.send(embed=embed)
                allowcmd = 1
            else:
                lookup = str(ctx.author.id)
                with open('settings/coin.txt') as myFile:
                    for line in myFile:
                        if lookup in line:
                            import decimal
                            balance = decimal.Decimal(line[20:])
                            balance = balance / 10
                            head, sep, tail = str(balance).partition('.')
                if alphaamount > int(head):
                    embed = discord.Embed(title="Number over limit char limit!", description=f"There is a {head} char limit,\
                    increase this by getting more coins by playing games! do `-help games` to see the games list")
                    embed.set_footer(text=f"Requested by {ctx.author}")
                    await ctx.channel.send(embed=embed)
                    allowcmd = 1
        if alphaamount < 1:
            await ctx.channel.send("```The minimum char amount is 1!```")
            allowcmd = 1
        if not allowcmd == 1:
            def get_random_unicode(length):
                get_char = chr
                include_ranges = [(0x0021, 0x0021), (0x0023, 0x0026), (0x0028, 0x007E), (0x00A1, 0x00AC),
                (0x00AE, 0x00FF), (0x0100, 0x017F), (0x0180, 0x024F), (0x2C60, 0x2C7F), (0x16A0, 0x16F0),
                (0x0370, 0x0377), (0x037A, 0x037E), (0x0384, 0x038A), (0x038C, 0x038C)]

                alphabet = [get_char(code_point) for current_range in include_ranges
                            for code_point in range(current_range[0],current_range[1] + 1)]
                return ''.join(random.choice(alphabet) for i in range(length))

            if __name__ == '__main__':
                time.sleep(0.25)
                embed = discord.Embed(title=f'A random string of {alphaamount} symbols: ',
                                      description=get_random_unicode(alphaamount))
                embed.set_footer(text=f"Requested by {ctx.author}")
                await ctx.channel.send(embed=embed)

    @commands.command()
    async def eight_ball(self, ctx):
        ballchoice = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes – definitely.",
            "You may rely on it.", "As I see it,yes.", "Most likely.", "Outlook good.", "Yes.",
            "Signs point to yes.", "Reply hazy,try again.", "Ask again later.", "Better not tell you now.",
            "Cannot predict now.", "Concentrate and ask again.", "Don’t count on it.", "My reply is no.",
            "My sources say no.", "Outlook not so good", "Very doubtful"]
        embed = discord.Embed(title=ballchoice[random.randint(0, 20)])
        embed.set_footer(text=f"Requested by {ctx.author}")
        await ctx.channel.send(embed=embed)

    @commands.command()
    async def leetify(self, ctx):
        change2 = ctx.message.content[9:].replace("o", "0").replace("O", "0").replace("l", "1").replace("L", "1")\
        .replace("s", "5").replace("S", "5").replace("h", "8").replace("H", "8").replace("e", "3").replace("E", "3")\
        .replace("i", "1").replace("I", "1")
        embed = discord.Embed(title="Leetified text:", description=change2)
        embed.set_footer(text=f"Requested by {ctx.author}")
        await ctx.channel.send(embed=embed)

    @commands.command()
    async def repeat(self, ctx):  # todo do something usefull with this command
        embed = discord.Embed(description=ctx.message.content[8:])
        embed.set_footer(text=f"Requested by ???")
        await ctx.channel.send(embed=embed)

    @commands.command()
    async def joke(self, ctx):
        headers = {'Accept': 'text/plain'}
        response = requests.get('https://icanhazdadjoke.com/', headers=headers)
        embed = discord.Embed(title="Here is your joke", description=response.text)
        embed.set_footer(text=f"Requested by {ctx.author}")
        await ctx.channel.send(embed=embed)

    @commands.command()
    async def char_count(self, ctx):  # todo add support for files? or make this more useful
        embed = discord.Embed(title=f"Total Number of Characters in this String = {len(ctx.message.content[12:])}")
        embed.set_footer(text=f"Requested by {ctx.author}")
        await ctx.channel.send(embed=embed)

    @commands.command(aliases=["emoji_letters", "big_text"])
    async def emoji_letter(self, ctx, *args):
        string = ""
        allow = True
        for i in convert_tuple(args)[:-1].replace(",","").replace(".", ""):
            if i.lower() not in "abcdefghijklmnopqrstuvwxyz ":
                allow = False
            if i == " ":
                string += ":black_large_square:"
            else:
                string += f":regional_indicator_{i.lower()}:"
        if allow:
            await ctx.channel.send(string)
        else:
            await ctx.channel.send("This command only supports alphabet chars.")

    @commands.command()
    async def ttb(self, ctx):  # todo add support context for prior conversations
        send = ttb.run(0, ctx.message.content[5:])
        await ctx.channel.send(send)


class Bot_info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["botinv", "botweb", "botrt", "inservers"])
    async def info(self, ctx):
        try:
            timestr = str(ctx.message.created_at - datetime.datetime.utcnow())
            diff = sum([a * b for a, b in zip([3600, 60, 1], map(float, timestr.split(':')))])
            startx = datetime.datetime.utcnow() - start_time
            runtime = str(startx)[:-7]
        except:
            runtime = "ERROR"
        embed = discord.Embed(title=f"Bot info:", description=f"\n\nRuntime: {runtime}\n"
            f"Started at: {str(start_time)[:-7]}\n"
            f'Cpu: {psutil.cpu_percent()}% of {psutil.cpu_count(logical=False)} cores\n'
            f'Ram: {psutil.virtual_memory().percent}% in use, '
            f'{round(psutil.virtual_memory().available * 100 / psutil.virtual_memory().total, 1)}% free '
            f'({round(psutil.virtual_memory().used/1024/1024, 0)}/'
            f'{round(psutil.virtual_memory().total/1024/1024, 0)}MB)\n'
            f'Storage: {psutil.disk_usage("/").percent}% used, {round(psutil.disk_usage("/").used/1024/1024, 2)}'
            f'/{round(psutil.disk_usage("/").total/1024/1024, 2)}MB\n'
            f'This bot is in {str(len(bot.guilds))} servers\n'
            f'The current ping is: {round(diff,2)}s\n'
            f'\nInvite link: [Click to add bot to another server](https://discord.com/oauth2/'
            f'authorize?client_id=711578412103368707&scope=bot&permissions=8)\n'
            f'Website link: [Go to website](https://rapidslayer101.wixsite.com/rapidslayer)\n'
            f'\nDevice bot is running on: {device}')
        embed.set_footer(text=f"Requested by {ctx.author}")
        await ctx.channel.send(embed=embed)


class Server(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def chat_links(self, ctx):  # todo resource intensive command, redo or remove, also broken atm
        async with ctx.typing():
            started_at = time.time()
            counter = 0
            linksfound = 0
            requestedby = ctx.author
            msg3 = await ctx.channel.send("Processing messages")
            with open('strs/edits/chatmsg-onlylinks-temp.txt', 'w', encoding='utf-8') as rmdup:
                async for message in ctx.channel.history(limit=10000):
                    a = (re.findall(r'(https?://[^\s]+)', str(message.content)))
                    b = (re.findall(r'(http?://[^\s]+)', str(message.content)))
                    if not str(a) == "[]":
                        linksfound += 1
                        rmdup.write(str(a) + "\n")
                    if not str(b) == "[]":
                        linksfound += 1
                        rmdup.write(str(b) + "\n")
                    if counter % 500 == 0:
                        await msg3.edit(content=f"Processed {counter} messages")
                    if counter == 10000:
                        await msg3.edit(content=f"Processed {counter} messages, You hit the 10k messages processing limit!\
                        any messages further back than 100k have not be included in the text file below")
                    counter += 1
                    message.content = ""
                rmdup.close()
                await msg3.edit(content=f"Processed {counter} messages")
                embed = discord.Embed(title=f"Here is this chats entire link history, total {linksfound} links")
                embed.set_footer(text=f"Took {round(time.time() - started_at,2)} seconds, Requested by {requestedby}")
                await ctx.channel.send(embed=embed)
                await ctx.channel.send(file=discord.File('strs/edits/chatmsg-onlylinks-temp.txt'))

    @commands.command()
    async def userid(self, ctx, arg):
        await ctx.channel.send(f'The user/role ID for {arg} is: {arg[3:21]}')

    @commands.command()
    async def serverid(self, ctx):
        await ctx.channel.send(f'The ID for {ctx.guild} (this server) is: {ctx.guild.id}\n\nTo get to this server online copy this link: \
        \ndiscord.com/channels/{ctx.guild.id}')

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

        embed = discord.Embed(title=f"Channels in this server ({channels_amount}):", description=text_channel_list)
        embed.set_footer(text=f"Requested by {ctx.author}")
        await ctx.channel.send(embed=embed)

    @commands.command()
    async def messageid(self, ctx):  # todo make this a message search and return id or remove
        await ctx.channel.send(f'The ID for the message you sent made output is: {ctx.message.id}\n\nTo get to this message online copy this link: \
        \ndiscord.com/channels/{ctx.guild.id}/{ctx.channel.id}/{ctx.message.id}')

    @commands.command()
    async def members(self, ctx):
        e4 = ""
        for item in ctx.guild.members:
            e4 += f"<@!{item.id}>"
        embed = discord.Embed(title=f"Member count: {len(ctx.guild.members)}", description=str(e4))
        embed.set_footer(text=f"Requested by {ctx.author}")
        await ctx.channel.send(embed=embed)

    @commands.command()
    async def roles(self, ctx):
        e4 = ""
        for item in ctx.guild.roles:
            e4 = e4 + f"\n{item.id} <@&{item.id}>"
        embed = discord.Embed(title=f"Role count: {len(ctx.guild.roles)}", description=str(e4))
        embed.set_footer(text=f"Requested by {ctx.author}")
        await ctx.channel.send(embed=embed)

    @commands.command()
    async def inrole(self, ctx):  # todo this command may still be broken from before
        if ctx.message.content[8:9] == "<":
            rolecheck = ctx.message.content[11:].replace(">", "")
        else:
            rolecheck = ctx.message.content[8:]
        with_num = 0
        e4 = ""
        for item in ctx.guild.members:
            if str(rolecheck) in str(ctx.guild.get_member(item.id).roles):
                e4 += f"\n<@!{item.id}>"
                with_num += 1
        embed = discord.Embed(title=f"Members with role {ctx.guild.get_role(int(rolecheck))} ({with_num}):",
                              description=str(e4))
        embed.set_footer(text=f"Requested by {ctx.author}")
        await ctx.channel.send(embed=embed)

    @commands.command()
    async def who_spoke(self, ctx, arg1):  # todo resource intensive maybe redo
        started_at = time.time()
        async with ctx.typing():
            if int(arg1) > 1000:
                await ctx.send("There is a 1000 message search limit on this command")
            else:
                id_list = []
                stuffs = ""
                async for message in ctx.channel.history(limit=int(arg1)):
                    id_list.append(message.author.id)
                for x in set(id_list):
                    stuffs = stuffs + f"<@!{x}> spoke {id_list.count(x)} times \n"
                embed = discord.Embed(title=f"Members who spoke in last {int(arg1)} messages", description=stuffs)
                embed.set_footer(text=f"Took {round(time.time() - started_at,2)} seconds, Requested by {ctx.author}")
                await ctx.channel.send(embed=embed)


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
        embed = discord.Embed(title=f"Here is the value in {arg2}: {d.get_symbol(arg2.upper())}{round(output,2)}")
        embed.set_footer(text=f"Requested by {ctx.author}")
        await ctx.channel.send(embed=embed)

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
            await ctx.channel.send("£" + x + " Started price watch...")
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
            uod = "🟩⬆️"
            ratiou = ratiou + 1
        if change < 0:
            uod = "🟥⬇️"
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
            updown = " 🟩⬆️ BTC UP BY " + str(round(result, 3)) + "% SINCE START"
        if (change2[0] / change2[1]) < (inat10[0] / inat10[1]):
            result = float((((change2[0] / change2[1]) - (inat10[0] / inat10[1])) * 100) / (change2[0] / change2[1]))
            updown = " 🟥⬇️ BTC DOWN BY " + str(round(result, 3)) + "% SINCE START"

        msg = await ctx.channel.send(
            "BTC: £" + x + " - £" + str(round(float(change3), 3)) + " " + str(uod) +
            " £" + str(round(float(ptval), 3)) + " - PRT: £" + str(round(port, 3)) +
            " - PRF: £" + str(round(profit, 3)) + str(updown))
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
                    # old twilio sms message send here
                    #client.messages.create(to="+447597299247", from_="+15155188444",
                    #body=f"YOUR BITCOIN IS ON THE RISE!!! {msg.content}")
                    largeportcounter == 0
            else:
                ii.write(page11)
                if (port2[0] / port2[1]) < (((port2[0] / port2[1]) - (inwith2[0] / inwith2[1])) * 0.995):
                    print("DOWN BY 0.5% OR MORE FROM HIGHEST PORT")
        prex = x


class Coloured_text(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def redtext(self, ctx):
        await ctx.channel.send(f"```diff\n- {ctx.message.content[9:]}\n\nRequested by {ctx.author}```")

    @commands.command()
    async def orange_text(self, ctx):
        await ctx.channel.send(f"```glsl\n#{ctx.message.content[12:]}\n\nRequested by {ctx.author}```")

    @commands.command()
    async def greentext(self, ctx):  # todo no longer works
        await ctx.channel.send(f"```css\n {ctx.message.content[11:]}\n\nRequested by {ctx.author}```")

    @commands.command()
    async def yellowtext(self, ctx):
        await ctx.channel.send(f"```fix\n {ctx.message.content[12:]}\n\nRequested by {ctx.author}```")

    @commands.command()
    async def blue_text(self, ctx):
        await ctx.channel.send(f"```css\n.{ctx.message.content[10:]}\n\nRequested by {ctx.author}```")

    @commands.command()
    async def cyantext(self, ctx):
        await ctx.channel.send(f"```xl\n'{ctx.message.content[10:]}\n\nRequested by {ctx.author}```")


def is_nsfw_on(channel_id):
    with open('settings/nsfw.txt', 'r') as i:
        isin = f'{i.read()}'
    if isin.find(str(channel_id)) > -1:
        return True
    else:
        return False


class NSFW(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def nsfw_status(self, ctx):
        if is_nsfw_on(ctx.channel.id):
            await ctx.channel.send("NSFW is enabled in this channel")
        else:
            await ctx.channel.send("NSFW is not enabled in this channel")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def nsfw_on(self, ctx):
        if is_nsfw_on(ctx.channel.id):
            await ctx.channel.send("```NSFW is already enabled in this channel```")
        else:
            with open('settings/nsfw.txt', 'a') as f:
                f.write(str(ctx.channel.id) + '\n')
                await ctx.channel.send("```NSFW is now enabled for this channel```")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def nsfw_off(self, ctx):
        bad_words = [f'{ctx.channel.id}']
        if not is_nsfw_on(ctx.channel.id):
            await ctx.channel.send("```NSFW is not enabled in this channel```")
        else:
            with open('settings/nsfw.txt') as old_file, open('settings/nsfw.txt', 'w') as new_file:
                for line in old_file:
                    if any(bad_word in line for bad_word in bad_words):
                        new_file.write(line)
                await ctx.channel.send("```If NSFW was enabled before it now wont be```")

    @commands.command()
    async def porntags(self, ctx):
        if is_nsfw_on(ctx.channel.id):
            embed = discord.Embed(title="porntags HELP:",description="suggested tags that can be used with the many nsfw search commands")
            embed.add_field(name="Tags", value="`69`,`Amateur`,`Anal`,`Animated`,`Asian`,`Ass`,`Bbc`,`Bbw`,`Bdsm`,`Big Ass`,`Big Dick`,`Big Tits`,`Blonde`,`Blowjob`,`Bondage`,`Boobs`\
            `Caption`,`Cartoon`,`Cheating`,`Cosplay`,`Cowgirl`,`Creampie`,`Cuckold`,`Cum`,`Cumshot`,`Deepthroat`,`Dildo`,`Doggystyle`,`Dp`,`Ebony`,\
            `Feet`,`Ffm`,`Fingering`,`Foursome`,`Fuck`,`Funny`,`Handjob`", inline=False)
            embed.set_footer(text=f"Requested by {ctx.author}")
            await ctx.channel.send(embed=embed)

    @commands.command()
    async def phs(self, ctx):
        if is_nsfw_on(ctx.channel.id):
            from pornhub_api import PornhubApi  # todo module missing
            api = PornhubApi()
            search = ctx.message.content[7:]
            data = api.search.search(f"{search}", ordering="mostviewed", period="weekly")
            limit = int(ctx.message.content[5:7])

            if limit > 20:
                await ctx.channel.send("```You cant have more than 20 searches per phs search!```")
            else:
                for vid in data.videos:
                    await ctx.channel.send(f"https://www.pornhub.com/view_video.php?viewkey={vid.video_id}")
                    time.sleep(4)
                    limit = limit - 1
                    if limit == 0:
                        break
        else:
            await ctx.channel.send("```NSFW is not enabled in this chat\n To enable it you must have role admin\n then type -nsfw_on```")

    @commands.command()
    async def psi(self, ctx, arg):  # todo functions, tho i dislike it
        if is_nsfw_on(ctx.channel.id):
            pagesearch2 = f'https://www.pornpics.com/?q={arg}/'.replace(" ", "+")
            page = urllib.request.urlopen(pagesearch2)
            a = (re.findall(r'(https?://[^\s]+)', str(page.read())))
            b = (re.findall(r'(http?://[^\s]+)', str(page.read())))
            c = ('\n'.join(a))
            d = ('\n'.join(b))
            e = c + d
            e1 = e.replace("\\n", "").replace("'", "").replace("\"", "")
            e4 = e1.split()
            e5 = e4[26:]
            imgsent = 0
            for imgn in range(200):
                e6 = ''.join(e5[imgn:imgn + 1])
                if 'https://cdni.pornpics.com' in e6:
                    embed = discord.Embed()
                    embed.set_image(url=e6[:-1])
                    embed.set_footer(text=f"Requested by {ctx.author}")
                    await ctx.channel.send(embed=embed)
                    time.sleep(2)
                    imgsent = imgsent + 1
                if 'https://img.pornpics.com' in e6:
                    embed = discord.Embed()
                    embed.set_image(url=e6[:-1])
                    embed.set_footer(text=f"Requested by {ctx.author}")
                    await ctx.channel.send(embed=embed)
                    time.sleep(2)
                    imgsent = imgsent + 1
                if 'https://images.pornpics.com' in e6:
                    embed = discord.Embed()
                    embed.set_image(url=e6[:-1])
                    embed.set_footer(text=f"Requested by {ctx.author}")
                    await ctx.channel.send(embed=embed)
                    time.sleep(2)
                    imgsent = imgsent + 1
                if imgn == 199:
                    if imgsent > 0:
                        await ctx.channel.send(f"```diff\nWant more {ctx.message.content[5:]}? Try some galleries!\
                        \n-psg 1 {ctx.message.content[5:]}\n\nWant something else?\nTry another -psi search```")
                    else:
                        await ctx.channel.send("```OH NO! There was no results for your search! try another search```")
        else:
            await ctx.channel.send("```NSFW is not enabled in this chat\n To enable it you must have role admin\n then type -nsfw_on```")

    @commands.command()
    async def psg(self, ctx, arg1, arg2):  # todo functions, tho i dislike it
        if is_nsfw_on(ctx.channel.id):
            global choicesz, choiceszz
            choicesz = str(arg1)
            choiceszz = choicesz.replace(" ", "")
            import urllib.request, re
            pagesearch2 = f'https://www.pornpics.com/?q={arg2}/'.replace(" ", "+")
            page = urllib.request.urlopen(pagesearch2)
            a = (re.findall(r'(https?://[^\s]+)', str(page.read())))
            b = (re.findall(r'(http?://[^\s]+)', str(page.read())))
            c = ('\n'.join(a))
            d = ('\n'.join(b))
            e = c + d
            e1 = e.replace("\\n", "").replace("'", "").replace("\"", "")
            e4 = e1.split()
            e5 = e4[26:]
            global PRNN
            PRNN = 0
            for imgn in range(200):
                e6 = ''.join(e5[imgn:imgn + 1])
                if 'https://www.pornpics.com/galleries/' in e6[:-1]:
                    PRNN = PRNN + 1
                    if str(PRNN) == (choiceszz):
                        pagesearch4 = f'{e6[:-1]}'.replace(" ", "+")
                        page = urllib.request.urlopen(pagesearch4)
                        a = (re.findall(r'(https?://[^\s]+)', str(page.read())))
                        b = (re.findall(r'(http?://[^\s]+)', str(page.read())))
                        c = ('\n'.join(a))
                        d = ('\n'.join(b))
                        e = c + d
                        e1 = e.replace("\\n", "").replace("'", "").replace("\"", "")
                        e4 = e1.split()
                        e5 = e4[26:]
                        for imgn in range(200):
                            e6 = ''.join(e5[imgn:imgn + 1])
                            if 'https://cdni.pornpics.com/1280' in e6:
                                embed = discord.Embed()
                                embed.set_image(url=e6[:-1])
                                embed.set_footer(text=f"Requested by {ctx.author}")
                                await ctx.channel.send(embed=embed)
                                time.sleep(2)
                            if 'https://img.pornpics.com/460' in e6:
                                embed = discord.Embed()
                                embed.set_image(url=e6[:-1])
                                embed.set_footer(text=f"Requested by {ctx.author}")
                                await ctx.channel.send(embed=embed)
                                time.sleep(2)
                            if 'https://images.pornpics.com/1280' in e6:
                                embed = discord.Embed()
                                embed.set_image(url=e6[:-1])
                                embed.set_footer(text=f"Requested by {ctx.author}")
                                await ctx.channel.send(embed=embed)
                                time.sleep(2)
                            if imgn == 199:
                                pgnum = ctx.message.content[5:7]
                                pgnum2 = pgnum2.replace(" ", "")
                                pgnum3 = int(pgnum) + 1
                                string = f"```diff\nWant even more?! try this command\n-psg\
                                {pgnum3} {ctx.message.content[7:]}\n\nWant something else?\
                                \nTry another -psi search```"
                                string2 = string.replace("  ", " ")
                                await ctx.channel.send(string2)
                        else:
                            await ctx.channel.send("```NSFW is not enabled in this chat\n To enable it you must have role admin\n then type -nsfw_on```")

    @commands.command()
    async def porngif(self, ctx, *args):
        if is_nsfw_on(ctx.channel.id):
            import urllib, re
            try:
                pagen = f"&page={int(args[0])}"
                c_args = convert_tuple(args[1:])[:-1]
            except:
                pagen = ""
                c_args = convert_tuple(args)[:-1]
            pagesearch = f'https://www.pornhub.com/gifs/search?search={c_args.replace(" ", "+")}{pagen}'
            page = urllib.request.urlopen(pagesearch)
            a = (re.findall(r'(data-mp4[^\s]+)', str(page.read())))
            b = (re.findall(r'(https://cl.phncdn.com/pics/gifs/[^\s]+)', str(page.read())))
            c = ('\n'.join(a))
            d = ('\n'.join(b))
            e = c + d
            e1 = e.replace("<span", "").replace("\"", "").replace(">", "").replace("\\", "")
            e4 = e1.split()
            e5 = e4[9:]
            imgsent = 0
            for imgn in range(200):
                e6 = ''.join(e5[imgn:imgn + 1])
                print(e6)
                if 'https://cl.phncdn.com/pics/gifs/' or 'https://dl.phncdn.com/pics/gifs/' in e6:
                    edit = e6[65:66]
                    e7edit = edit.replace("<", "").replace("n", "").replace("t", "").replace("a", "")
                    e7 = e6[9:65] + e7edit
                    await ctx.channel.send(e7)
                    print(e7)
                    e7edit = e7[44:52]
                    e7edit2 = e7edit.replace("<", "").replace("n", "").replace("t", "").replace("a", "")
                    import urllib.request, re
                    pagesearch4 = f'https://www.pornhub.com/gif/{e7edit2}'.replace(" ", "+")
                    page = urllib.request.urlopen(pagesearch4)
                    a = (re.findall(r'(href="/view_video.php[^\s]+)', str(page.read())))
                    b = (re.findall(r'(href="/view_video.php[^\s]+)', str(page.read())))
                    c = ('\n'.join(a))
                    d = ('\n'.join(b))
                    e = c + d
                    e1 = e.replace("\\n", "").replace("'", "").replace("\"", "")
                    e4 = e1.split()
                    for imgn1 in range(200):
                        e6 = ''.join(e4[imgn1:imgn1 + 1])
                        if 'href=/view_video.php?viewkey=' in e6:
                            if '&amp;t=' in e6:
                                e7 = e6[:45]
                                e8 = e7[5:]
                                finale = "https://www.pornhub.com" + e8
                                embed = discord.Embed(title=f"Full video link: {finale}")
                                embed.set_footer(text=f"Requested by {ctx.author}")
                                await ctx.channel.send(embed=embed)
                    time.sleep(4)
                    imgsent = imgsent + 1
                if imgn == 199:
                    pgnum2 = pagen.replace(" ", "")
                    pgnum3 = int(pgnum2) + 1
                    await ctx.channel.send(f"```diff\nWant more? Type this command:\n-porngif {pgnum3} {c_args}```")
                    time.sleep(3)
        else:
            await ctx.channel.send("```NSFW is not enabled in this chat\n To enable it you must have role admin\n then type -nsfw_on```")

    @commands.command()
    async def hentai(self, ctx, arg1, arg2):
        if is_nsfw_on(ctx.channel.id):
            hensearch = arg2.replace(" ", "")
            pagesearch = f'https://konachan.com/post?page={arg1}&tags=uncensored+nude+{hensearch}'
            pagesearch2 = pagesearch.replace(" ", "+")
            page = urllib.request.urlopen(pagesearch2)
            a = (re.findall(r'(https?://[^\s]+)', str(page.read())))
            b = (re.findall(r'(http?://[^\s]+)', str(page.read())))
            c = ('\n'.join(a))
            d = ('\n'.join(b))
            e = c + d
            e1 = e.replace("<span", "").replace("\"", "").replace(">", "")
            e4 = e1.split()
            e5 = e4[9:]
            imgsent = 0
            for imgn in range(200):
                e6 = ''.join(e5[imgn:imgn + 1])
                if 'https://konachan.com/jpeg/' in e6:
                    embed = discord.Embed()
                    embed.set_image(url=e6)
                    embed.set_footer(text=f"Requested by {ctx.author}")
                    await ctx.channel.send(embed=embed)
                    time.sleep(3)
                    imgsent = imgsent + 1
                if 'https://konachan.com/image/' in e6:
                    embed = discord.Embed()
                    embed.set_image(url=e6)
                    embed.set_footer(text=f"Requested by {ctx.author}")
                    await ctx.channel.send(embed=embed)
                    time.sleep(3)
                    imgsent = imgsent + 1
                if imgn == 199:
                    pgnum = arg1
                    pgnum2 = pgnum.replace(" ", "")
                    pgnum3 = int(pgnum2) + 1
                    if imgsent > 0:
                        await ctx.channel.send(f"```diff\nWant more? Type this command:\n-hentai {pgnum3} {hensearch}```")
                    else:
                        await ctx.channel.send("```OH NO! There was no results for your search! try another search```")
            else:
                await ctx.channel.send("```NSFW is not enabled in this chat\n To enable it you must have role admin\n then type -nsfw_on```")


class Online_searching(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ggt_codes(self, ctx):  # todo make less horrible to read
        embed = discord.Embed(title="Here are the language codes:", description=str(googletrans.LANGCODES))
        embed.set_footer(text=f"Requested by {ctx.author}")
        await ctx.channel.send(embed=embed)

    @commands.command()
    async def ggt_te(self, ctx):  # todo fix
        translator = Translator()
        translated = translator.translate(ctx.message.content[8:])
        embed = discord.Embed(title="Translated text:", description=translated.text)
        embed.set_footer(text=f"Requested by {ctx.author}")
        await ctx.channel.send(embed=embed)

    @commands.command()
    async def ggt_ft(self, ctx, arg1, arg2):  # todo fix
        values5 = (ctx.message.content[14:])
        translator = Translator()
        translated = translator.translate(values5, src=arg1, dest=arg2)
        embed = discord.Embed(title="Translated text:", description=translated.text)
        embed.set_footer(text=f"Requested by {ctx.author}")
        await ctx.channel.send(embed=embed)

    # todo, 3 practically identical commands, use def to turn much much smaller

    @commands.command()
    async def ggsr(self, ctx, arg1):  # todo add more functionality, fix the currency requirement
        allowcmd = 0
        if int(arg1) > 1:
            if int(arg1) > 30:
                embed = discord.Embed(title="Number over max result limit!", description="There is a 30 result limit")
                embed.set_footer(text=f"Requested by {ctx.author}")
                await ctx.channel.send(embed=embed)
                allowcmd = 1
            else:
                lookup = str(ctx.author.id)
                with open('settings/coin.txt') as myFile:
                    for line in myFile:
                        if lookup in line:
                            balance = decimal.Decimal(line[20:])
                            balance = balance / 100
                            head, sep, tail = str(balance).partition('.')
                if int(arg1) > int(head):
                    embed = discord.Embed(title="Number over result limit!", description=f"There is a {head} result limit,\
                    increase this by getting more coins by playing games! do `-help games` to see the games list")
                    embed.set_footer(text=f"Requested by {ctx.author}")
                    await ctx.channel.send(embed=embed)
                    allowcmd = 1
        if int(arg1) < 1:
            await ctx.channel.send("```The minimum results is 1!```")
            allowcmd = 1
        if ctx.message.content[8:] == "":
            await ctx.channel.send("```You cant search for nothing!```")
            allowcmd = 1
        if not allowcmd == 1:
            embed = discord.Embed(description=f"Below results requested by {ctx.author}")
            await ctx.channel.send(embed=embed)
            from googlesearch import search
            for j in search((ctx.message.content[8:]), tld="co.in", num=int(arg1), stop=int(arg1), pause=2):
                await ctx.channel.send(j)

    @commands.command()
    async def ggsi(self, ctx, arg1):  # todo add more functionality, fix the currency requirement
        allowcmd = 0
        if int(arg1) > 1:
            if int(arg1) > 30:
                embed = discord.Embed(title="Number over max result limit!", description="There is a 30 result limit")
                embed.set_footer(text=f"Requested by {ctx.author}")
                await ctx.channel.send(embed=embed)
                allowcmd = 1
            else:
                lookup = str(ctx.author.id)
                with open('settings/coin.txt') as myFile:
                    for line in myFile:
                        if lookup in line:
                            balance = decimal.Decimal(line[20:])
                            balance = balance / 100
                            head, sep, tail = str(balance).partition('.')
                if int(arg1) > int(head):
                    embed = discord.Embed(title="Number over result limit!", description=f"There is a {head} result limit,\
                    increase this by getting more coins by playing games! do `-help games` to see the games list")
                    embed.set_footer(text=f"Requested by {ctx.author}")
                    await ctx.channel.send(embed=embed)
                    allowcmd = 1
        if int(arg1) < 1:
            await ctx.channel.send("```The minimum results is 1!```")
            allowcmd = 1
        if ctx.message.content[8:] == "":
            await ctx.channel.send("```You cant search for nothing!```")
            allowcmd = 1
        if not allowcmd == 1:
            embed = discord.Embed(description=f"Below results requested by {ctx.author}")
            await ctx.channel.send(embed=embed)
            from googlesearch import search_images
            for j in search_images((ctx.message.content[8:]), tld="co.in", num=int(arg1), stop=int(arg1), pause=2):
                await ctx.channel.send(j)

    @commands.command()
    async def ggsv(self, ctx, arg1):  # todo add more functionality, fix the currency requirement
        allowcmd = 0
        if int(arg1) > 1:
            if int(arg1) > 30:
                embed = discord.Embed(title="Number over max result limit!", description="There is a 30 result limit")
                embed.set_footer(text=f"Requested by {ctx.author}")
                await ctx.channel.send(embed=embed)
                allowcmd = 1
            else:
                lookup = str(ctx.author.id)
                with open('settings/coin.txt') as myFile:
                    for line in myFile:
                        if lookup in line:
                            balance = decimal.Decimal(line[20:])
                            balance = balance / 100
                            head, sep, tail = str(balance).partition('.')
                if int(arg1) > int(head):
                    embed = discord.Embed(title="Number over result limit!", description=f"There is a {head} result limit,\
                    increase this by getting more coins by playing games! do `-help games` to see the games list")
                    embed.set_footer(text=f"Requested by {ctx.author}")
                    await ctx.channel.send(embed=embed)
                    allowcmd = 1
        if int(arg1) < 1:
            await ctx.channel.send("```The minimum results is 1!```")
            allowcmd = 1
        if ctx.message.content[8:] == "":
            await ctx.channel.send("```You cant search for nothing!```")
            allowcmd = 1
        if not allowcmd == 1:
            embed = discord.Embed(description=f"Below results requested by {ctx.author}")
            await ctx.channel.send(embed=embed)
            from googlesearch import search_videos
            for j in search_videos((ctx.message.content[8:]), tld="co.in", num=int(arg1), stop=int(arg1), pause=2):
                await ctx.channel.send(j)

    @commands.command()
    async def reddits(self, ctx, arg1, arg2):  # todo simplification possible
        reddit = praw.Reddit(client_id='RuvVgZ-jMqw9lw', client_secret='tj4cbJuTKAum0ZszB_DJwY5cFjo',user_agent='Reddit webscraper')
        hot_posts = reddit.subreddit(arg1).hot(limit=int(arg2))
        postcurrent = 0
        type = 0
        for post in hot_posts:
            postcurrent = postcurrent + 1
            if postcurrent == int(arg2):
                if "redgifs.com/" in str(post.url):
                    embed = discord.Embed(description=f"Below results requested by {ctx.author}")
                    await ctx.channel.send(embed=embed)
                    await ctx.channel.send(str(post.url) + "/")
                    break
                    type = 1
                if "https://i.imgur.com/" in str(post.url):
                    embed = discord.Embed(description=f"Below results requested by {ctx.author}")
                    await ctx.channel.send(embed=embed)
                    await ctx.channel.send(str(post.url) + "/")
                    break
                    type = 1
                if not type == 1:
                    embed = discord.Embed(description=f"[Click to go to post]({post.url})")
                    embed.set_image(url=post.url)
                    embed.set_footer(text=f"Requested by {ctx.author}")
                    await ctx.channel.send(embed=embed)
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
            postcurrent = postcurrent + 1
            if postcurrent == postnum:
                embed = discord.Embed()
                embed.set_image(url=post.url)
                embed.set_footer(text=f"Requested by {ctx.author}")
                await ctx.channel.send(embed=embed)


class Games(commands.Cog):  # todo redo this whole thing
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
                embed = discord.Embed(title="This token has already been claimed", color=discord.Colour(0xff0000))
            else:
                with open('strs/tokens.txt', 'r') as file:  # todo finish this segment
                    data = file.readlines()
                data[int(line_num) - 1] = f'{arg}, CLAIMED\n'
                file.close()

                with open('strs/tokens.txt', 'w') as file:
                    file.writelines(data)

                print("where")
                rcoin.win(0, ctx.author.id, float(reward))
                print("where")
                embed = discord.Embed(title=f"{reward} rcoins have been added to your balance",
                                      description=f"You now have: {rcoin.bal(0, ctx.author.id)}",
                                      color=discord.Colour(0x00ff00))
        else:
            embed = discord.Embed(title="This is not a valid token", color=discord.Colour(0xff0000))
        embed.set_footer(text=f"Requested by {ctx.author}")
        await ctx.channel.send(embed=embed)

    @commands.command()
    async def daily(self, ctx):
            # 10? daily coins, new class probably needed
            embed = discord.Embed(title="Coins added ????")
            embed.set_footer(text=f"Requested by {ctx.author}")
            await ctx.channel.send(embed=embed)

    @commands.command()
    async def bal(self, ctx, *args):
        c_args = convert_tuple(args)[:-1]
        if c_args == "":
            embed = discord.Embed(title=f"Your balance is {rcoin.bal(0, ctx.author.id)}")
            embed.set_footer(text=f"Requested by {ctx.author}")
        else:
            if str(args[0]).startswith("<@!") and str(args[0]).endswith(">"):
                userid = int(args[0].replace("<@!", "").replace(">", ""))
                embed = discord.Embed(description=f"{args[0]}'s balance is {rcoin.bal(0, userid)}")
                embed.set_footer(text=f"Requested by {ctx.author}")
            else:
                embed = discord.Embed(description=f"<@!{args[0]}>'s balance is {rcoin.bal(0, int(args[0]))}")
                embed.set_footer(text=f"Requested by {ctx.author}")
        await ctx.channel.send(embed=embed)

    @commands.command(aliases=["bet_flip"])
    async def flip(self, ctx, arg1, arg2):  # todo redo the arg inputs
        bet = rcoin.check(0, ctx.author.id, float(arg2))
        if str(bet).startswith("This is") or str(bet).startswith("You cannot"):
            embed = discord.Embed(title=bet)
            embed.set_footer(text=f"Requested by {ctx.author}")
            await ctx.channel.send(embed=embed)
        else:
            flip = random.randint(0, 100)
            if flip < 36:
                if str(arg1) == "h":
                    headortail = "heads"
                if str(arg1) == "t":
                    headortail = "tails"
                rcoin.win(0, ctx.author.id, bet)
                embed = discord.Embed(title=f"You Won {bet}", description=f"Coin landed on {headortail}\
                 and You now have: {rcoin.bal(0, ctx.author.id)}", color=discord.Colour(0x00ff00))
                embed.set_footer(text=f"Requested by {ctx.author}")
            if flip > 35:
                if str(arg1) == "h":
                    headortail = "tails"
                if str(arg1) == "t":
                    headortail = "heads"
                rcoin.lose(0, ctx.author.id, bet)
                embed = discord.Embed(title=f"You Lost {bet}", description=f"Coin landed on {headortail}\
                 You now have: {rcoin.bal(0, ctx.author.id)}", color=discord.Colour(0xff0000))
                embed.set_footer(text=f"Requested by {ctx.author}")
            await ctx.channel.send(embed=embed)

    @commands.command()
    async def bet_dice(self, ctx, arg1, arg2):  # todo redo the arg inputs
        bet = rcoin.check(0, ctx.author.id, float(arg2))
        if str(bet).startswith("This is") or str(bet).startswith("You cannot"):
            embed = discord.Embed(title=bet)
            embed.set_footer(text=f"Requested by {ctx.author}")
            await ctx.channel.send(embed=embed)
        else:
            dice_num = int(arg1)
            allowbet = True
            if dice_num > 6 or dice_num < 0:
                embed = discord.Embed(title="You must bet on a number 1-6")
                allowbet = False
            if allowbet:
                dice_roll = random.randint(1, 6)
                if dice_num == dice_roll:
                    rcoin.win(0, ctx.author.id, bet*5)
                    embed = discord.Embed(title=f"Dice rolled {dice_roll} and You Won {bet*5}",
                                          description=f"You now have: {rcoin.bal(0, ctx.author.id)}",
                                          color=discord.Colour(0x00ff00))
                else:
                    rcoin.lose(0, ctx.author.id, bet)
                    embed = discord.Embed(title=f"Dice rolled {dice_roll} You Lost {bet}",
                                          description=f"You now have: {rcoin.bal(0, ctx.author.id)}",
                                          color=discord.Colour(0xff0000))

            embed.set_footer(text=f"Requested by {ctx.author}")
            await ctx.channel.send(embed=embed)

    @commands.command()
    async def bet_rps(self, ctx, arg1, arg2):  # todo redo the arg inputs, and the floats issue
        bet = rcoin.check(0, ctx.author.id, float(arg2))
        if str(bet).startswith("This is") or str(bet).startswith("You cannot"):
            embed = discord.Embed(title=bet)
            embed.set_footer(text=f"Requested by {ctx.author}")
            await ctx.channel.send(embed=embed)
        else:
            t = ["R", "P", "S"]
            computer = t[random.randint(0, 2)]
            player = False

            while player is False:
                player = arg1
                rpsbet = int(arg2)
                rpsbet2 = rpsbet / 2  # change multiplier here
                rpsbet2 = rpsbet2.as_integer_ratio()
                if player == computer:
                    await ctx.channel.send("Tie!")
                elif player == "r":
                    if computer == "P":
                        rcoin.lose(0, ctx.author.id, rpsbet)
                        embed = discord.Embed(title=f"You Lose! rapidbot covers {ctx.author}",
                        description=f"You now have: {rcoin.bal(0, ctx.author.id)}", color=discord.Colour(0xff0000))
                        embed.set_footer(text=f"Requested by {ctx.author}")
                        await ctx.channel.send(embed=embed)
                    else:
                        rcoin.win(0, ctx.author.id, (rpsbet2[0] / rpsbet2[1]))
                        embed = discord.Embed(title=f"You Win! {ctx.author} smashes rapidbot",
                        description=f"You now have: {rcoin.bal(0, ctx.author.id)}", color=discord.Colour(0x00ff00))
                        embed.set_footer(text=f"Requested by {ctx.author}")
                        await ctx.channel.send(embed=embed)

                elif player == "p":
                    if computer == "S":
                        rcoin.lose(0, ctx.author.id, rpsbet)
                        embed = discord.Embed(title=f"You Lose! rapidbot cut {ctx.author}",
                        description=f"You now have: {rcoin.bal(0, ctx.author.id)}", color=discord.Colour(0xff0000))
                        embed.set_footer(text=f"Requested by {ctx.author}")
                        await ctx.channel.send(embed=embed)
                    else:
                        rcoin.win(0, ctx.author.id, (rpsbet2[0] / rpsbet2[1]))
                        embed = discord.Embed(title=f"You Win! {ctx.author} covers rapidbot",
                        description=f"You now have: {rcoin.bal(0, ctx.author.id)}", color=discord.Colour(0x00ff00))
                        embed.set_footer(text=f"Requested by {ctx.author}")
                        await ctx.channel.send(embed=embed)
                elif player == "s":
                    if computer == "R":
                        rcoin.lose(0, ctx.author.id, rpsbet)
                        embed = discord.Embed(title=f"You Lose! rapidbot smashes {ctx.author}",
                        description=f"You now have: {rcoin.bal(0, ctx.author.id)}", color=discord.Colour(0xff0000))
                        embed.set_footer(text=f"Requested by {ctx.author}")
                        await ctx.channel.send(embed=embed)
                    else:
                        rcoin.win(0, ctx.author.id, (rpsbet2[0] / rpsbet2[1]))
                        embed = discord.Embed(title=f"You Win! {ctx.author} cut rapidbot",
                        description=f"You now have: {rcoin.bal(0, ctx.author.id)}", color=discord.Colour(0x00ff00))
                        embed.set_footer(text=f"Requested by {ctx.author}")
                        await ctx.channel.send(embed=embed)
                else:
                    embed = discord.Embed(title="Thats not a move")
                    embed.set_footer(text=f"Requested by {ctx.author}")
                    await ctx.channel.send(embed=embed)

                player = True
                computer = t[random.randint(0, 2)]

    @commands.command()
    async def bet_multi(self, ctx, arg1, arg2):  # todo redo with the new currency
        bet = rcoin.check(0, ctx.author.id, float(arg2))
        if str(bet).startswith("This is") or str(bet).startswith("You cannot"):
            embed = discord.Embed(title=bet)
            embed.set_footer(text=f"Requested by {ctx.author}")
            await ctx.channel.send(embed=embed)
        else:
            betmultiplyer = int(arg1)
            betmultiamount = int(arg2)
            allowbet = 0
            if int(betmultiplyer) < 3:
                embed = discord.Embed(title="You cant have a multiplier lower than 3!")
                embed.set_footer(text=f"Requested by {ctx.author}")
                await ctx.channel.send(embed=embed)
                allowbet = 1
            if int(betmultiplyer) > 100000:
                embed = discord.Embed(title="You cant have a multiplier higher than 100000!")
                embed.set_footer(text=f"Requested by {ctx.author}")
                await ctx.channel.send(embed=embed)
                allowbet = 1
            if not allowbet == 1:
                multiplyerunedit = int(betmultiplyer) * 1.20 * 10  # change multiplier here
                lookup = "."
                if lookup in str(multiplyerunedit):
                    head, sep, tail = str(multiplyerunedit).partition('.')

                botmultichoice = random.randint(1, int(head))
                print(str(botmultichoice) + "/" + str(multiplyerunedit))
                if botmultichoice < 11:
                    rcoin.win(0, ctx.author.id, betmultiamount*betmultiplyer)
                    embed = discord.Embed(title=f"You Won: {betmultiamount*betmultiplyer}",
                    description=f"You bet {betmultiamount} on a {betmultiplyer}"
                                f"X multiplier and you now have: {rcoin.bal(0, ctx.author.id)}",
                    color=discord.Colour(0x00ff00))
                    embed.set_footer(text=f"Requested by {ctx.author}")
                    await ctx.channel.send(embed=embed)
                else:
                    rcoin.lose(0, ctx.author.id, betmultiamount)
                    embed = discord.Embed(title=f"You Lost: {betmultiamount}",
                    description=f"You bet {betmultiamount} on a {betmultiplyer}"
                                f"X multiplier and you now have: {rcoin.bal(0, ctx.author.id)}",
                    color=discord.Colour(0xff0000))
                    embed.set_footer(text=f"Requested by {ctx.author}")
                    await ctx.channel.send(embed=embed)

    @commands.command()
    async def bet_revup(self, ctx, arg1, arg2):  # todo this has been left broken, fix it
        bet = rcoin.check(0, ctx.author.id, float(arg2))
        if str(bet).startswith("This is") or str(bet).startswith("You cannot"):
            embed = discord.Embed(title=bet)
            embed.set_footer(text=f"Requested by {ctx.author}")
            await ctx.channel.send(embed=embed)
        else:
            revupbet = arg1
            betrevtimes = arg2
            allowcmd = 0

            if int(betrevtimes) > 1:
                if int(betrevtimes) > 15:
                    embed = discord.Embed(title="Number over max goes limit!", description="There is a 15 goes limit")
                    embed.set_footer(text=f"Requested by {ctx.author}")
                    await ctx.channel.send(embed=embed)
                    allowcmd = 1
                elif int(betrevtimes) > 1:
                    lookup = str(ctx.author.id)
                    with open('settings/coin.txt') as myFile:
                        for line in myFile:
                            if lookup in line:
                                balance = decimal.Decimal(line[20:])
                                balance = balance / 100
                                head, sep, tail = str(balance).partition('.')
                    if int(betrevtimes) > int(head):
                        if head == "0":
                            head = "1"
                        embed = discord.Embed(title="Number over goes limit!", description=f"There is a {head} goes limit,\
                        increase this by getting more coins by playing games! do `-help games` to see the games list")
                        embed.set_footer(text=f"Requested by {ctx.author}")
                        await ctx.channel.send(embed=embed)
                        allowcmd = 1
            if int(betrevtimes) < 1:
                await ctx.channel.send("```The minimum goes is 1!```")
                allowcmd = 1
            if not allowcmd == 1:
                for i in range(int(betrevtimes)):
                    allowbet = 0
                    if int(revupbet) > coin:
                        embed = discord.Embed(title="You cant bet more than you have!")
                        embed.set_footer(text=f"Requested by {ctx.author}")
                        await ctx.channel.send(embed=embed)
                        allowbet = 1
                    if int(revupbet) < 1:
                        embed = discord.Embed(title="You cant bet nothing!")
                        embed.set_footer(text=f"Requested by {ctx.author}")
                        await ctx.channel.send(embed=embed)
                        allowbet = 1
                    if not allowbet == 1:
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
                            embed = discord.Embed(title=f"You Won: {round(coinadd, 2)}",
                            description=f"You bet {revupbet} and got a {round(revumtotal, 2)}\
                            X multiplier and you now have: {coin}", color=discord.Colour(0x00ff00))
                            embed.set_footer(text=f"Requested by {ctx.author}")
                            await ctx.channel.send(embed=embed)
                        if coinadd < revupbet:
                            embed = discord.Embed(title=f"You Got Back: {revupbet - (revupbet - round(coinadd, 2))}", description=
                            f"You bet {revupbet} and got a {round(revumtotal, 2)}\
                            X multiplier and you now have: {coin}", color=discord.Colour(0xff0000))
                            embed.set_footer(text=f"Requested by {ctx.author}")
                            await ctx.channel.send(embed=embed)

    @commands.command()
    async def bet_dubup(self, ctx, arg1, arg2):  # todo this has been left broken, fix it
        bet = rcoin.check(0, ctx.author.id, float(arg2))
        if str(bet).startswith("This is") or str(bet).startswith("You cannot"):
            embed = discord.Embed(title=bet)
            embed.set_footer(text=f"Requested by {ctx.author}")
            await ctx.channel.send(embed=embed)
        else:
            revupbet = arg1
            betrevtimes = arg2
            allowcmd = 0

            if int(betrevtimes) > 1:
                if int(betrevtimes) > 15:
                    embed = discord.Embed(title="Number over max goes limit!", description="There is a 15 goes limit")
                    embed.set_footer(text=f"Requested by {ctx.author}")
                    await ctx.channel.send(embed=embed)
                    allowcmd = 1
                if int(betrevtimes) > 1:
                    lookup = str(ctx.author.id)
                    with open('settings/coin.txt') as myFile:
                        for line in myFile:
                            if lookup in line:
                                balance = decimal.Decimal(line[20:])
                                balance = balance / 100
                                head, sep, tail = str(balance).partition('.')
                    if int(betrevtimes) > int(head):
                        if head == "0":
                            head = "1"
                        embed = discord.Embed(title="Number over goes limit!", description=f"There is a {head} goes limit,\
                        increase this by getting more coins by playing games! do `-help games` to see the games list")
                        embed.set_footer(text=f"Requested by {ctx.author}")
                        await ctx.channel.send(embed=embed)
                        allowcmd = 1
            if int(betrevtimes) < 1:
                await ctx.channel.send("```The minimum goes is 1!```")
                allowcmd = 1
            if not allowcmd == 1:
                for i in range(int(betrevtimes)):
                    allowbet = 0
                    if int(revupbet) > coin:
                        embed = discord.Embed(title="You cant bet more than you have!")
                        embed.set_footer(text=f"Requested by {ctx.author}")
                        await ctx.channel.send(embed=embed)
                        allowbet = 1
                    if int(revupbet) < 1:
                        embed = discord.Embed(title="You cant bet nothing!")
                        embed.set_footer(text=f"Requested by {ctx.author}")
                        await ctx.channel.send(embed=embed)
                        allowbet = 1
                    if not allowbet == 1:
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
                            embed = discord.Embed(title=f"You Won: {round(coinadd, 2)}", description=
                            f"You bet {revupbet} and got a ({round(revupmulti, 2)}x{round(revupmulti2, 2)}) \
                            {round(revuptotal, 2)}X multiplier\nyou now have: {coin}", color=discord.Colour(0x00ff00))
                            embed.set_footer(text=f"Requested by {ctx.author}")
                            await ctx.channel.send(embed=embed)
                        if coinadd < revupbet:
                            embed = discord.Embed(title=f"You Got Back: {revupbet - (revupbet - round(coinadd, 2))}",
                            description=f"You bet {revupbet, round(revupmulti, 2)} and got a ({round(revupmulti2, 2)}x\
                            {round(revuptotal, 2)}) {round(revupmulti, 2)}X multiplier\nyou now have: {coin}",
                            color=discord.Colour(0xff0000))
                            embed.set_footer(text=f"Requested by {ctx.author}")
                            await ctx.channel.send(embed=embed)


class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def purge(self, ctx, arg1, arg2):
        if arg1 == "all":
            if discord.utils.get(ctx.author.roles, name="admin") or discord.utils.get(ctx.author.roles, name="Admin")\
            or discord.utils.get(ctx.author.roles, name="administrator") or discord.utils.get(ctx.author.roles, name="Administrator"):
                await ctx.channel.send("```user permission success```", delete_after=1)
                time.sleep(1)
                deleted = await ctx.channel.purge(limit=int(arg2))
                await ctx.send('Deleted {} message(s)'.format(len(deleted)), delete_after=2.5)
            else:
                embed = discord.Embed(description="You need the role 'admin' or 'administrator' to purge everyones messages")
                embed.set_footer(text=f"Requested by {ctx.author}")
                await ctx.channel.send(embed=embed)
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
        savedauthor = ctx.message.author.id
        allowcmd = 0
        msgnum = 0
        if int(arg2) > 1000:
            allowcmd = 1
        if not allowcmd == 1:
            async for message in ctx.history(limit=int(arg2)):
                if arg1 == "bot":
                    if message.author.id == 711578412103368707:
                        await message.delete()
                        time.sleep(1)
                        msgnum = msgnum+1
                if arg1 == "self":
                    if message.author.id == savedauthor:
                        await message.delete()
                        time.sleep(1)
                        msgnum = msgnum+1
                if arg1 == "all":
                    await message.delete()
                    time.sleep(1)
                    msgnum = msgnum+1
                if msgnum == 50:
                    await message.channel.send("Reached deletion limit of 50", delete_after=2.5)
                    break
            await message.channel.send(f"Deleted {msgnum} messages(s)", delete_after=2.5)


class Thomas(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def draw(self, ctx, *args):
        if ctx.author.id in [530791679704301580, 425373518566260766]:
            c_args = convert_tuple(args)[:-1]
            if c_args == "":
                await ctx.channel.send("Missing number of people to draw, -draw <num>")
            else:
                with open("settings/event_players.txt") as f:
                    players = f.readlines()
                if int(c_args) > len(set(players)):
                    await ctx.channel.send(f"The max number that can be drawn from this data is {len(set(players))}")
                else:
                    total_players = len(players)
                    draw = ""
                    for i in range(int(c_args)):
                        while True:
                            new_draw = players[random.randint(1, total_players)-1]
                            if str(new_draw).replace("\n", "") not in draw:
                                draw += f"<@!{players[random.randint(1, total_players)-1]}>, ".replace("\n", "")
                                print(draw)
                                break
                    await ctx.channel.send(f"Drew {draw[:-2]} from {total_players-int(c_args)} entries")
                    open("settings/event_expire.txt", "w").close()
                    open("settings/event_players.txt", "w").close()

    @commands.command(aliases=["current time", "currenttime"])
    async def current_time(self, ctx):
        await ctx.channel.send(str(datetime.datetime.now())[:-7])

    @commands.command(aliases=["start event", "startevent"])
    async def start_event(self, ctx, *args):
        if ctx.author.id in [530791679704301580, 425373518566260766]:
            c_args = convert_tuple(args)[:-1]
            with open("settings/event_expire.txt") as f:
                data = f.read()
            try:
                dt_object = datetime.datetime.strptime(data, "%Y-%m-%d %H:%M:%S")
                await ctx.channel.send("There is already a running event\n"
                                       f"Time remaining in running event: {dt_object - datetime.datetime.now()}")
            except:
                if c_args == "":
                    await ctx.channel.send("No expire time provided")
                else:
                    dt_object = datetime.datetime.strptime(c_args, "%Y-%m-%d %H:%M:%S")
                    await ctx.channel.send(f"Time remaining in event: {dt_object-datetime.datetime.now()}")
                    with open("settings/event_expire.txt", "w") as f:
                        f.write(c_args)

    @commands.command(aliases=["expire time", "expiretime"])
    async def expire_time(self, ctx):
        with open("settings/event_expire.txt") as f:
            data = f.read()
        try:
            dt_object = datetime.datetime.strptime(data, "%Y-%m-%d %H:%M:%S")
            await ctx.channel.send(f"Time remaining in running event: {dt_object - datetime.datetime.now()}")
        except:
            await ctx.channel.send("There is no running event")

    @commands.command(aliases=["join event", "joinevent"])
    async def join_event(self, ctx):
        with open("settings/event_expire.txt") as f:
            data = f.read()
        try:
            dt_object = datetime.datetime.strptime(data, "%Y-%m-%d %H:%M:%S")
            if datetime.datetime.now() > dt_object:
                await ctx.channel.send(f"This event has expired, you can no longer enter")
            else:
                allow_apply = True
                with open("settings/event_players.txt") as f:
                    total_entries = 0
                    for line in f.readlines():
                        if str(ctx.author.id) in line:
                            total_entries += 1
                            allow_apply = False
                if allow_apply:
                    total_entries = 0
                    if discord.utils.get(ctx.author.roles, name="Member"):
                        total_entries += 1
                    if discord.utils.get(ctx.author.roles, name="Server Booster"):
                        total_entries += 3
                    if discord.utils.get(ctx.author.roles, name="staff"):
                        total_entries += 1
                    if discord.utils.get(ctx.author.roles, name="Gold Role"):
                        total_entries += 2
                    embed = discord.Embed(title=f"Application allowed with {total_entries} entries"
                                          , color=discord.Colour(0x00ff00))
                    await ctx.channel.send(embed=embed)
                    with open("settings/event_players.txt", "a+") as f:
                        for i in range(total_entries):
                            f.write(f"{ctx.author.id}\n")
                else:
                    await ctx.channel.send(f"You have already applied before, you have {total_entries} entries")
        except:
            await ctx.channel.send("There is no running event")


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["h"])
    async def help(self, ctx, *args):  # todo this command wont work at all with commands like -h colour text
        c_args = convert_tuple(args)[:-1]
        embed = None
        message = None
        if c_args == "":
            embed = discord.Embed(title="Rapidbot command sections", description="We have a wide range of commands!\
                    \nAlso remember the prefix is '-'")
            embed.add_field(name=":hash: Encrypt (3)    :question: Random (11)    :information_source: Info (1)",
                            value="`-h enc`       `-h rand`      `-h info`", inline=False)
            embed.add_field(name=":page_facing_up: Server (9)   :dollar: Currency (2)  :rainbow: Coloured text (6)",
                            value="`-h server`    `-h currency`    `-h color text`", inline=False)

            if is_nsfw_on(ctx.channel.id):
                embed.add_field(name=":wink: NSFW (8)     :computer: Online searches (8)    :game_die: Games (12)",
                                value="`-h nsfw`     `-h search`           `-h games`", inline=False)
            else:
                embed.add_field(name="Disabled (8)     :computer: Online searches (8)    :game_die: Games (12)",
                                value="`disabled`   `-h search`           `-h games`", inline=False)
        else:
            if c_args in ["encryption", "encrypt", "enc", "decryption", "decrypt", "dec"]:  # todo maybe add more desc
                embed = discord.Embed(title=":hash: Encryption commands (3)",
                                      description="`encrypt`,`decrypt`,`enc_key`")
                embed.add_field(name="Here is how to use them",
                                value="`-encrypt <message>`\n`-decrypt <encrypted message>`\n"
                                      "`-enc_key` makes a random encryption key", inline=False)
                embed.set_footer(text=f"Requested by {ctx.message.author}")

            if c_args in ["random", "rand"]:
                embed = discord.Embed(title=":question: Random commands (10)", description="`randword`,`randnum`,\
                        `randuni`,`eight_ball`,`leetify`,`repeat`,\n`joke`,`char_count`,`emoji_letter`,`ttb`")
                embed.set_footer(text=f"Add -h to the beginning of a command for its help section!"
                                      f" Requested by {ctx.message.author}")

            if c_args in ["info", "bot_info", "bot info"]:  # BOT INFO
                embed = discord.Embed(title="INFO HELP:",
                                      description="The info command shows data about the bot"
                                                  "\n\nThis commands aliases are: `botinv`,`botweb`,`botrt`,`inservers`")

            if c_args in ["server"]:
                embed = discord.Embed(title=":page_facing_up: Server commands (9)", description="\
                        `chat_links`,`userid`,`serverid`,`channel_ids`,`messageid`,"
                        "\n`members`,`roles`,`inrole`,`who_spoke`")
                embed.set_footer(
                    text=f"Add -h to the beginning of a command for its help section! "
                         f"Requested by {ctx.message.author}")

            if c_args in ["currency", "cur"]:
                embed = discord.Embed(title=":dollar: Currency commands (2)",
                                      description="`currency_list`,`currency_convert`")
                embed.set_footer(
                    text=f"Add -h to the beginning of a command for its help section! "
                         f"Requested by {ctx.message.author}")

            if c_args in ["color text", "colored text", "color_text", "colored_text"]:
                embed = discord.Embed(title=":rainbow: Coloured text commands (6)",
                                      description="`redtext`,`orange_text`,`greentext`,"
                                                  "\n`yellowtext`,`blue_text`,`cyantext`")
                embed.set_footer(
                    text=f"Add -h to the beginning of a command for its help section! "
                         f"Requested by {ctx.message.author}")

            if c_args in ["nsfw"]:
                if is_nsfw_on(ctx.channel.id):
                    embed = discord.Embed(title=":wink: NSFW commands (8)",
                                          description="`nsfw_on`,`nsfw_off`,`porntags`,"
                                                      "`phs`,`psi`,`psg`,`porngif`,`hentai`")
                    embed.set_footer(text=f"Add -h to the beginning of a command for\
                    its help section! Requested by {ctx.message.author}")
                else:
                    embed = discord.Embed(title="This is not enabled in your server",
                                          description="If your an admin type `-nsfw_on` to enable these commands")
                    embed.set_footer(text=f"Requested by {ctx.message.author}")

            if c_args in ["search", "online search", "online_search"]:
                embed = discord.Embed(title=":computer: Online searches commands (8)",
                                      description="`ggt_codes`, `ggt_te`,`ggt_ft`,\
                        \n`ggsr`,`ggsi`,`ggsv`,`reddits`,`meme`")
                embed.set_footer(text=f"Add -h to the beginning of a command for its help section! "
                                      f"Requested by {ctx.message.author}")

            if c_args in ["games", "bet"]:
                embed = discord.Embed(title=":game_die: Game commands (12)",
                                      description="`claim`,`daily`,`bal`,`flip`,\
                        `bet bj`,`bet_dice`,\n`bet_rps`,`bet_multi`,`bet_revup`,`bet_dubup`,`bet crash`,`quiz`")
                embed.set_footer(text=f"Add -h to the beginning of a command for its help section! "
                                      f"Requested by {ctx.message.author}")

            if c_args in ["admin"]:
                embed = discord.Embed(title=":tools: Admin commands (2)", description="`purge`,`clean`")
                embed.set_footer(text=f"Add -h to the beginning of a command for its help section! "
                                      f"Requested by {ctx.message.author}")

            if c_args in ["randword"]:  # RANDOM
                embed = discord.Embed(title="RANDWORD HELP:",
                                      description="The random word command picks x random words")
                embed.add_field(name="Here is how to use it", value="`-randword <number of words>`", inline=False)

            if c_args in ["randnum", "randnumber"]:  # RANDOM # not reworked
                embed = discord.Embed(title="RANDNUM HELP:",
                                      description="The random number command picks a number between two numbers")
                embed.add_field(name="Here is how to use it", value="`randnum <1st number> <2nd number>`", inline=False)
                embed.add_field(name="Command aliases", value="`randumber`", inline=False)

            if c_args in ["randuni"]:  # RANDOM
                embed = discord.Embed(title="RANDUNI HELP:",
                                      description="The random Unicode command picks x"
                                                  " number of random Unicode characters")
                embed.add_field(name="Here is how to use it", value="`randuni <number of uni chars>`", inline=False)

            if c_args in ["eight_ball"]:  # RANDOM
                embed = discord.Embed(title="EIGHT_BALL HELP:",
                                      description="The eight ball command is a question and answer command")
                embed.add_field(name="Here is how to use it", value="`-eight_ball <question>`", inline=False)

            if c_args in ["leetify"]:  # RANDOM
                embed = discord.Embed(title="LEETIFY HELP:",
                                      description="The leetify command turns your message into leet speak")
                embed.add_field(name="Here is how to use it", value="`-leetify <message>`", inline=False)

            if c_args in ["repeat"]:  # RANDOM
                embed = discord.Embed(title="REPEAT HELP:", description="The repeat command repeats your message")
                embed.add_field(name="Here is how to use it", value="`-repeat <message>`", inline=False)

            if c_args in ["joke"]:  # RANDOM # not reworked
                embed = discord.Embed(title="JOKE HELP:", description="The joke command sends a funny joke!")

            if c_args in ["char_count", "char count"]:  # RANDOM
                embed = discord.Embed(title="CHAR_COUNT HELP:",
                                      description="The char_count command counts the number of"
                                                  " characters in your message")
                embed.add_field(name="Here is how to use it", value="`-char_count <message>`", inline=False)

            if c_args in ["emoji_letter", "emoji_letters", "big_text"]:  # RANDOM
                embed = discord.Embed(title="EMOJI_LETTERS HELP:",
                                      description="The emoji letter command turns your message into letter emojis")
                embed.add_field(name="Here is how to use it", value="`-emoji_letter <message>`", inline=False)
                embed.add_field(name="Command aliases", value="`emoji_letters`,`big_text`", inline=False)

            if c_args in ["ttb"]:  # RANDOM
                embed = discord.Embed(title="TTB HELP:",
                                      description="The talk to bot command asks an AI your message/question")
                embed.add_field(name="Here is how to use it", value="`-ttb <message/question>`", inline=False)

            if c_args in ["chat_links"]:  # SERVER INFO
                embed = discord.Embed(title="CHAT_LINKS HELP:", description="The chat links \
                command retrieves every link ever sent in a channel then it sends all of these links in one file")

            if c_args in ["userid"]:  # SERVER INFO
                embed = discord.Embed(title="USER ID HELP:", description="The user id command retrieves a users id")
                embed.add_field(name="Here is how to use it", value="`-userid <@user>`", inline=False)

            if c_args in ["serverid"]:  # SERVER INFO
                embed = discord.Embed(title="SERVER ID HELP:",
                                      description="The server id command retrieves current servers id")

            if c_args in ["channelids", "channel_ids"]:  # SERVER INFO
                embed = discord.Embed(title="CHANNEL_IDS HELP:",
                                      description="The channel ids command gets all channel ids from current server")
                embed.add_field(name="Here is how to use it", value="`-channel id` shows channel ids and names"
                                "\n`-channel id raw` shows just channel ids", inline=False)
                embed.add_field(name="Command aliases", value="`channelids`", inline=False)

            if c_args in ["messageid"]:  # SERVER INFO
                embed = discord.Embed(title="MESSAGE ID HELP:",
                                      description="The message id retrieves the id of the message you just sent")

            if c_args in ["members"]:  # SERVER INFO
                embed = discord.Embed(title="MEMBERS HELP:",
                                      description="The members command lists all the members in the server")

            if c_args in ["roles"]:  # SERVER INFO
                embed = discord.Embed(title="ROLES HELP:",
                                      description="The roles command lists all the roles in the server")

            if c_args in ["inrole"]:  # SERVER INFO
                embed = discord.Embed(title="MEMBERS HELP:",
                                      description="The in role command lists all members with a role")
                embed.add_field(name="Here is how to use it", value="`-inrole <@role>`", inline=False)

            if c_args in ["who_spoke"]:  # SERVER INFO
                embed = discord.Embed(title="WHO_SPOKE HELP:",
                                      description="The who spoke command finds how many times"
                                                  " people spoke in last x messages")
                embed.add_field(name="Here is how to use it",
                                value="`-who_spoke <how many msg's to look at>` limited to 1000 messages",
                                inline=False)

            if c_args in ["currency_list"]:  # CURRENCY
                embed = discord.Embed(title="CURRENCY_LIST HELP:",
                                      description="The currency_listing command shows values of many currencies")
                embed.add_field(name="Here is how to use it",
                                value="`-currency_list`\n`-currency_list <Currency to convert from>`", inline=False)

            if c_args in ["currency_convert"]:  # CURRENCY
                embed = discord.Embed(title="CURRENCY_CONVERT HELP:",
                                      description="The currency conversion command converts between 2 currencies")
                embed.add_field(name="Here is how to use it",
                                value="`-currency_convert <currency from> <currency to> <amount>`", inline=False)

            if c_args in ["redtext"]:  # COLOURED TEXT
                embed = discord.Embed(title="REDTEXT HELP:",
                                      description="The redtext command turns your message red")
                embed.add_field(name="Here is how to use it", value="`-redtext <message>", inline=False)

            if c_args in ["orange_text"]:  # COLOURED TEXT
                embed = discord.Embed(title="ORANGe_text HELP:",
                                      description="The orange_text command turns your message orange")
                embed.add_field(name="Here is how to use it", value="`-orange_text <message>", inline=False)

            if c_args in ["greentext"]:  # COLOURED TEXT
                embed = discord.Embed(title="GREENTEXT HELP:",
                                      description="The greentext command turns your message green")
                embed.add_field(name="Here is how to use it", value="`-greentext <message>", inline=False)

            if c_args in ["yellowtext"]:  # COLOURED TEXT
                embed = discord.Embed(title="YELLOWTEXT HELP:",
                                      description="The yellowtext command turns your message yellow")
                embed.add_field(name="Here is how to use it", value="`-yellowtext <message>", inline=False)

            if c_args in ["blue_text"]:  # COLOURED TEXT
                embed = discord.Embed(title="BLUe_text HELP:",
                                      description="The blue_text command turns your message blue")
                embed.add_field(name="Here is how to use it", value="`-blue_text <message>", inline=False)

            if c_args in ["cyantext"]:  # COLOURED TEXT
                embed = discord.Embed(title="CYANTEXT HELP:",
                                      description="The cyantext command turns your message cyan")
                embed.add_field(name="Here is how to use it", value="`-cyantext <message>", inline=False)

            if c_args in ["nsfw_on"]: # NSFW
                embed = discord.Embed(title="NSFW_ON HELP:",
                                      description="The nsfw on command enables nsfw in a channel/chat")
                embed.add_field(name="Command requirements",
                                value="you will need the role admin to use this command", inline=False)

            if c_args in ["nsfw_off"]:  # NSFW
                embed = discord.Embed(title="NSFW_OFF HELP:",
                                      description="The nsfw_off command disables nsfw in a channel/chat")
                embed.add_field(name="Command requirements",
                                value="you will need the role admin to use this command", inline=False)

            if c_args in ["porntags"]:  # NSFW
                if is_nsfw_on(ctx.channel.id):
                    embed = discord.Embed(title="PORNTAGS HELP:",
                                          description="The porn tags command provides suggestions"
                                                      " for tags to be used in nsfw searches")
                else:
                    message = "```This command is not enabled in this chat```"

            if c_args in ["phs"]:  # NSFW
                if is_nsfw_on(ctx.channel.id):
                    embed = discord.Embed(title="PHS HELP:",
                                          description="The pornhub search command searches for up to 20 videos")
                    embed.add_field(name="Here is how to use it", value="`-phs <num of results> <search>`",
                                    inline=False)
                else:
                    message = "```This command is not enabled in this chat```"

            if c_args in ["psi"]:  # NSFW
                if is_nsfw_on(ctx.channel.id):
                    embed = discord.Embed(title="PSI HELP:",
                                          description="The porn search image command searches for porn images")
                    embed.add_field(name="Here is how to use it",
                                    value="`-psi x`\nx is the thing your searching for", inline=False)
                else:
                    message = "```This command is not enabled in this chat```"

            if c_args in ["psg"]:  # NSFW
                if is_nsfw_on(ctx.channel.id):
                    embed = discord.Embed(title="PSG HELP:",
                                          description="The porn search galleries command "
                                                      "searches for images in galleries")
                    embed.add_field(name="Here is how to use it", value="`-psg n x`\nn is the \
                    gallery number to search\nx is the thing/tag your searching for", inline=False)
                else:
                    message = "```This command is not enabled in this chat```"

            if c_args in ["porngif"]:  # NSFW
                if is_nsfw_on(ctx.channel.id):
                    embed = discord.Embed(title="PORNGIF HELP:",
                                          description="The porn gif command finds some gifs and sends them back")
                    embed.add_field(name="Here is how to use it", value="`-porngif n x`\nn is the\
                     page number to search\nx is the thing/tag your searching for", inline=False)
                else:
                    message = "```This command is not enabled in this chat```"

            if c_args in ["hentai"]:  # NSFW
                if is_nsfw_on(ctx.channel.id):
                    embed = discord.Embed(title="HENTAI HELP:",
                                          description="The hentai search command finds hentai and sends it back")
                    embed.add_field(name="Here is how to use it", value="`-hentai n x`\nn is the page \
                    number to search\nx is the thing/tag your searching for (you can leave this blank)",
                                    inline=False)
                else:
                    message = "```This command is not enabled in this chat```"

            if c_args in ["ggt_codes"]:  # SEARCHES
                embed = discord.Embed(title="GGT_CODES HELP:",
                                      description="The Google translate language codes command shows "
                                                  "you the abbreviated letters for that language")

            if c_args in ["ggt_te"]:  # SEARCHES
                embed = discord.Embed(title="GGT_TE HELP:",
                                      description="The Google translate to english command attempts "
                                                  "to convert a message to english")
                embed.add_field(name="Here is how to use it", value="`-ggt_te <message>`", inline=False)

            if c_args in ["ggt_ft"]:  # SEARCHES
                embed = discord.Embed(title="GGT_FT HELP:",
                                      description="The Google translate from to command translates "
                                                  "a message from one language to another")
                embed.add_field(name="Here is how to use it", value="`-ggt_ft <lang from> <lang to> <message>`",
                                inline=False)

            if c_args in ["ggt_ft"]:  # SEARCHES
                embed = discord.Embed(title="GGSR HELP:",
                                      description="The google search result command searches "
                                                  "\n google for x amount of results")
                embed.add_field(name="Here is how to use it", value="`-ggsr <num of results> <search>`",
                                inline=False)

            if c_args in ["ggsi"]:  # SEARCHES
                embed = discord.Embed(title="GGSI HELP:",
                                      description="The google search image command searches "
                                                  "\n google for x amount of images")
                embed.add_field(name="Here is how to use it", value="`-ggsi <num of images> <search>`",
                                inline=False)

            if c_args in ["ggsv"]:  # SEARCHES
                embed = discord.Embed(title="GGSV HELP:",
                                      description="The google search videos command searches "
                                                  "\n google for x amount of videos")
                embed.add_field(name="Here is how to use it", value="`-ggsv <num of videos> <search>`",
                                inline=False)

            if c_args in ["reddits"]:  # SEARCHES
                embed = discord.Embed(title="REDDITS HELP:",
                                      description="The reddit search command retrieves a img/gif/vid from a subreddit")
                embed.add_field(name="Here is how to use it",
                                value="`-reddits <subreddit> <post number>` Suggest post num of 1", inline=False)

            if c_args in ["meme"]:  # SEARCHES
                embed = discord.Embed(title="MEME HELP:", description="The meme command retrieves a meme!")

            if c_args in ["claim", "claim_token"]:  # GAMES
                embed = discord.Embed(title="CLAIM HELP:",
                                      description="The claim command means you can claim rewards!")
                embed.add_field(name="Here is how to use it", value="`-claim <token>`", inline=False)
                embed.add_field(name="Command aliases", value="`claim_token`", inline=False)

            if c_args in ["daily"]:  # GAMES
                embed = discord.Embed(title="DAILY COINS HELP:",
                                      description="The daily coins command gives you some coins!")

            if c_args in ["bal"]:  # GAMES
                embed = discord.Embed(title="BAL HELP:",
                                      description="The balance command displays your current balance")
                embed.add_field(name="Here is how to use it",
                                value="`-bal` for your balance\n `-bal <@user>` for someone elses balance",
                                inline=False)

            if c_args in ["flip", "bet_flip"]:  # GAMES
                embed = discord.Embed(title="COINFLIP HELP:",
                                      description="The coinflip command is a betting game for 2x money")
                embed.add_field(name="Here is how to use it", value="`-flip <h or t> <amount to bet>`",
                                inline=False)
                embed.add_field(name="Command aliases", value="`bet_flip`", inline=False)

            if c_args in ["bet_dice"]:  # GAMES
                embed = discord.Embed(title="BET_DICE HELP:",
                                      description="The dice roll command is a betting game for 5x money")
                embed.add_field(name="Here is how to use it",
                                value="`-bet_dice <dice side num (1-6)> <amount to bet>`",
                                inline=False)

            if c_args in ["bet bj"]:  # GAMES
                embed = discord.Embed(title="BET BJ HELP:",
                                      description="The blackjack command is a betting game for 1.66x money")
                embed.add_field(name="Here is how to use it", value="`-bet bj <bet amount>`", inline=False)

            if c_args in ["bet_rps"]:  # GAMES
                embed = discord.Embed(title="BET_RPS HELP:",
                                      description="The rock paper scissors command is a betting game for 1.5x money")
                embed.add_field(name="Here is how to use it", value="`-bet_rps <r or p or s> <amount to bet>`",
                                inline=False)

            if c_args in ["bet_multi"]:  # GAMES
                embed = discord.Embed(title="BET_MULTI HELP:",
                                      description="The multiplier command is a betting game where you"
                                                  " decide the multiplier! Min multiplier of 3")
                embed.add_field(name="Here is how to use it", value="`-bet_multi <multiplier> <amount to bet>`",
                                inline=False)

            if c_args in ["bet_revup"]:  # GAMES
                embed = discord.Embed(title="BET_REVUP HELP:",
                                      description="The rev up command is a betting game where "
                                                  "you get a random multiplier from 0 to 1000!")
                embed.add_field(name="Here is how to use it", value="`-bet_revup <amount to bet> <num of goes>`",
                                inline=False)

            if c_args in ["bet_dubup"]:  # GAMES
                embed = discord.Embed(title="BET_DUBUP HELP:", description="The rev up double up command is a \
                betting game where you get 2 multipliers that could get you up to 40000X!")
                embed.add_field(name="Here is how to use it", value="`-bet_dubup <amount to bet> <num of goes>`",
                                inline=False)

            if c_args in ["crash"]:  # GAMES
                embed = discord.Embed(title="BET CRASH HELP:", description="The crash command is a \
                betting game where chose when you pull out of the game and keep your winnings!")
                embed.add_field(name="Here is how to use it", value="`-bet crash <amount to bet>`", inline=False)

            if c_args in ["quiz"]:  # GAMES
                embed = discord.Embed(title="QUIZ HELP:", description="The quiz command is a knowledge game!")
                embed.add_field(name="Here is how to use it",
                                value="`-quiz`, and then `-a` to answer the question asked", inline=False)

            if c_args in ["revision"]:  # GAMES
                embed = discord.Embed(title="QUIZ HELP:", description="The revision command is a revision tool!")
                embed.add_field(name="Here is how to use it", value="`-revision` for a random question from anything\
                \n`-revision <subject>` for a random question from that subject\
                \n`-revision <subject> <topic>` for a random question from that subject and that topic\
                \n`-revision <subject> <topic> <question number>` get a specific question\
                \n\nCurrent subjects: chemistry\nchemistry topics:\
                metal-extraction", inline=False)

            # admin help

            if c_args in ["purge"]:  # ADMIN
                embed = discord.Embed(title="PURGE HELP:",
                                      description="The purge command deletes x number of messages"
                                                  " up to 14 days old, use clean for anything older")
                embed.add_field(name="Here is how to use it", value="`-purge <bot/self/all> <num of msg>`",
                                inline=False)

            if c_args in ["clean"]:  # ADMIN
                embed = discord.Embed(title="CLEAN HELP:",
                                      description="The clean command individualy deleted messages where purge cant")
                embed.add_field(name="Here is how to use it", value="`-clean <bot/self/all> <num of msg>`",
                                inline=False)

        if embed is not None:
            await ctx.channel.send(embed=embed)
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
        embed = discord.Embed(title=f"Command error, {error_check}", description=f"Need help? `-h {message[0]}`")
        embed.set_footer(text=f"Requested by {ctx.author}")
        await ctx.channel.send(embed=embed)

bot.add_cog(Encryption(bot))
bot.add_cog(Random(bot))
bot.add_cog(Bot_info(bot))
bot.add_cog(Server(bot))
bot.add_cog(Currency(bot))
bot.add_cog(Coloured_text(bot))
bot.add_cog(NSFW(bot))
bot.add_cog(Online_searching(bot))
bot.add_cog(Games(bot))
bot.add_cog(Admin(bot))
bot.add_cog(Thomas(bot))  # thomas special cog
bot.add_cog(Help(bot))

global theshit  # todo what to do with this stuff?

cum_on = False

if cum_on:
    with open("cum2.txt", "r", encoding="utf-8") as f:
        theshit = f.readlines()


cooldown_ids = {}


class cooldown():
    #def add(self, userid, length):
       # todo per command cooldowns and duplication checks required
    def check(self, userid, length):
        if userid not in cooldown_ids:
            cooldown_ids.update({userid: [datetime.datetime.now(), length]})
        else:
            cooldown_data = cooldown_ids[userid]
            timestr = str(datetime.datetime.now() - cooldown_data[0])
            diff = sum([a * b for a, b in zip([3600, 60, 1], map(float, timestr.split(':')))])
            if diff < cooldown_data[1]:
                return f"Command sent to fast, please wait {round(cooldown_data[1] - diff,2)}s"
            else:
                del cooldown_ids[userid]


ttb_data = {}


class ttb():  # todo add ttb prev conv functionality
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
        print("sesh", sessions)

        payload += "cb_settings_scripting=no&islearning=1&icognoid=wsf&icognocheck="
        payload += hashlib.md5(payload[7:33].encode()).hexdigest()
        req = requests.post(
            "https://www.cleverbot.com/webservicemin?uc=UseOfficialCleverbotAPI",
            cookies=cookies,
            data=payload)
        response = str(req.content)[2:].split("\\r")
        return response[0]


def dec_crunch(number):
    if str(number)[::-1].find('.') > 3:
        return float(number)//0.001/1000
    else:
        return round(float(number), 3)


rcoin_data = {}


class rcoin():  # todo make sure floats not dropped like currently are
    with open("strs/rcoin_bals.txt") as f:
        for line in f.readlines():
            userid, bal = line.replace("\n", "").split(", ")
            rcoin_data.update({int(userid): dec_crunch(bal)})

    def bal(self, userid):
        try:
            rcoin_data.update({int(userid): dec_crunch(rcoin_data[int(userid)])})
            return rcoin_data[int(userid)]
        except:
            rcoin_data.update({int(userid): 100})
            return rcoin_data[int(userid)]

    def save(self):
        with open("strs/rcoin_bals.txt", "w") as f:
            for key, value in rcoin_data.items():
                f.write(f"{key}, {value}\n")

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

    # inserted CUM shard  # todo what to do with this?

    if message.channel.id in [867113471241093120] or message.author.id == 425373518566260766:
        if message.content.lower().startswith("-search"):
            search = message.content[8:]
            with open(f"temp.txt", "w+", encoding="utf-8") as p:
                for line in theshit:
                    if search in line:
                        p.write(line)

            with open('temp.txt') as result:
                uniqlines = set(result.readlines())
                with open(f"search-{search}.txt", "w+", encoding="utf-8") as rmdup:
                    rmdup.writelines(set(uniqlines))

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

        if message.content.lower() == "-cum":
            for i in range(50):
                with open("counter.txt", "r") as x:
                    counter = str(x.readlines())[2:-2]
                    counter = int(counter)
                with open("counter.txt", "w") as x:
                    x.write(str(counter + 1))

                line = str(counter) + theshit[counter - 1]
                await message.channel.send(line)
                time.sleep(1.25)

        if message.content.lower() == "-pick":
            len(theshit)
            counter = random.randint(0, len(theshit))
            line = theshit[counter]
            line = str(counter) + line
            await message.channel.send(line)

        if message.content.lower().startswith("-spec"):
            num = int(message.content[6:])
            line = theshit[num-1]
            line = str(num) + line
            await message.channel.send(line)

        if message.content.lower().startswith("-coom"):
            num = int(message.content[6:]) - 1
            for i in range(50):
                line = str(num+1)+theshit[num]
                await message.channel.send(line)
                num = num + 1
                time.sleep(1)

        if message.content.lower() == "-data-log":
            await message.channel.send(file=discord.File(r'indexed_data.txt'))

    # inserted CUM shard above

    if message.content.startswith("-") and message.author.bot is False:

        # TOKEN DROPS
        token_drops_on = True

        if token_drops_on:
            tokenluck = random.randint(0, 100)  # todo make certain users more or less lucky
            if tokenluck == 1:
                import string
                token = ""
                for i in range(25):
                    token = token + (random.choice(string.ascii_uppercase))
                    if i in [4, 9, 14, 19]:
                        token = token + "-"
                token_value = random.randint(10, 100)
                with open('strs/tokens.txt', 'a+') as f:
                    f.write(f"{token}, {token_value}\n")

                embed = discord.Embed(title=f"{token}",
                                      description=f"Claim the above {token_value}"
                                                  f" coin token by typing -claim <token>")
                await message.channel.send(embed=embed)

        allow_command = cooldown.check(0, message.author.id, 2)
        if allow_command is not None:
            await message.channel.send(allow_command)
            message.content = ""
        
        await bot.process_commands(message)

        if message.author.id == 425373518566260766:
            if message.content.startswith("-update strs"):
                    with open('strs/msgstore.txt', 'r') as f:
                        sendback = f.read()
                        with open('strs/linkstore.txt', 'w') as i:
                            a = (re.findall(r'(https?://[^\s]+)', sendback))
                            b = (re.findall(r'(http?://[^\s]+)', sendback))
                            c = ('\n'.join(a))
                            d = ('\n'.join(b))
                            write = f'{c},{d}'
                            i.write(write)
                            i.close()
                            with open('strs/linkstore.txt') as result:
                                uniqlines = set(result.readlines())
                                with open('strs/linkndp.txt', 'w') as rmdup:
                                    rmdup.writelines(set(uniqlines))

                                    bad_words = ['https://discord.com/channels/']
                                    with open('strs/linkndp.txt') as oldfile, open('strs/linknd-ndsc.txt', 'w') as newfile:
                                        for line in oldfile:
                                            if not any(bad_word in line for bad_word in bad_words):
                                                newfile.write(line)

                    await message.channel.send("```Lnk data Success```")
                    file1 = open("strs/msgstore.txt", "r")
                    d = dict()

                    for line in file1:
                        line = line.strip()
                        line = line.lower()
                        words = line.split(" ")

                        for word in words:
                            if word in d:
                                d[word] = d[word] + 1
                            else:
                                d[word] = 1

                    with open('strs/occurdata.txt', 'w') as f:
                        f.write("\n\nNumber of occurrences of each word in file is:")
                        f.write("\n ===============\n")

                        for key in list(d.keys()):
                            yeis = f'{key},":",{d[key]} \n'
                            writethat = str(yeis)
                            f.write(writethat)

                        file1.close()
                        await message.channel.send("```Occr data Success```")

            if message.content.startswith("-randlink"):
                lines = open('strs/linknd-ndsc.txt').read().splitlines()
                myline = random.choice(lines)
                await message.channel.send(myline)

            if message.content.startswith("-allmsg without"):
                bad_word = message.content[16:]
                bad_words = bad_word.split()
                await message.channel.send(bad_words)
                with open('strs/msgstore.txt') as oldfile, open(
                        f'strs/edits/allmsg-withoutwords-{message.content[16:]}.txt', 'w') as newfile:
                    for line in oldfile:
                        if not any(bad_word in line for bad_word in bad_words):
                            newfile.write(line)
                    await message.channel.send("```SUCCESS```")
                    await message.channel.send(file=discord.File(f'strs/edits/allmsg-withoutwords-{message.content[16:]}.txt'))

            if message.content.startswith("-allmsg only"):
                bad_word = message.content[13:]
                bad_words = bad_word.split()
                await message.channel.send(bad_words)
                with open('strs/msgstore.txt') as oldfile, open(
                        f'strs/edits/allmsg-findwords-{message.content[13:]}.txt', 'w') as newfile:
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
                with open('strs/msgstore.txt') as oldfile, open(f'strs/edits/chatmsg-{message.channel.id}.txt',
                                                                'w') as newfile:
                    for line in oldfile:
                        if any(bad_word in line for bad_word in bad_words):
                            newfile.write(line)
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

        if message.content.startswith("-beta access"):
            giveto = message.content[13:]
            giveto2 = giveto[3:21]
            if message.author.id == 425373518566260766:
                with open('settings/beta.txt', 'r') as f:
                    isin = f'{f.read()}'
                    if isin.find(str(giveto2)) > -1:
                        await message.channel.send("```This user is already has the beta rank```")
                    else:
                        with open('settings/beta.txt', 'a') as i:
                            i.write(giveto2)
                            i.close()
                        string = f"```User {giveto} has been given beta rank!```"
                        await message.channel.send(string)
            else:
                await message.channel.send("```You will need to ask rapidslayer101 for access to the beta rank")

        # beta commands

        if message.content.startswith("-join vc"):
            voicechannel = message.author.voice.channel
            global vc
            vc = await voicechannel.connect()

        if message.content.startswith("-leave vc"):
            await vc.disconnect()

        if message.content.startswith("-play"):
            voicechannel = message.author.voice.channel
            vc = await voicechannel.connect()
            vc.play(discord.FFmpegPCMAudio(executable="ffmpeg/bin/ffmpeg.exe", source="F://captures/wideptin.mp3"))
            await message.channel.send("```now playing: wide_putin.mp4```")

        if message.content.startswith("-tts"):
            import gtts
            text = message.content[5:]
            tts = gtts.gTTS(text)
            tts.save("temp.mp3")
            vc.play(discord.FFmpegPCMAudio(executable="ffmpeg/bin/ffmpeg.exe", source="temp.mp3"))


@bot.event
async def on_connect():
    print(f'Connection established to discord, Logged in as {bot.user} ({bot.user.id})')
    print(f'-----------------------------------------------\n'
          f'cpu: {psutil.cpu_percent()}% of {psutil.cpu_count(logical=False)} cores\n'
          f'ram: {psutil.virtual_memory().percent}% in use, '
          f'{round(psutil.virtual_memory().available * 100 / psutil.virtual_memory().total,1)}% free '
          f'({round(psutil.virtual_memory().used/1024/1024,0)}/{round(psutil.virtual_memory().total/1024/1024,0)}MB)\n'
          f'storage: {psutil.disk_usage("/").percent}% used, {round(psutil.disk_usage("/").used/1024/1024,2)}'
          f'/{round(psutil.disk_usage("/").total/1024/1024,2)}MB\n'
          f'-----------------------------------------------')


#@bot.event
#async def on_ready():
#    print("Bot is now ready\n-----------------------------------------------")


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
    embed = discord.Embed(title='Hi im rapidbot!!', description="My command prefix is '-'\
     try -help to see a commands list", colour=discord.Color.gold())
    await channel.send(embed=embed)

bot.run('NzExNTc4NDEyMTAzMzY4NzA3.XsFGcw.kuaqIiivBkE0Ji1Bq2koZWnfFLw')  # actual bot
