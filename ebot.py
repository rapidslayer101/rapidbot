# COPYRIGHT RAPIDSLAYER101#2604, copyright by scott bree, DO NOT COPY, DO NOT SHARE, DO NOT USE

import discord, ast, time
from discord.ext import commands
client = discord.Client()

global startt, startr
global msgcounter
msgcounter = 0
startt = time.time()
import datetime
datetime.datetime.now()
datetime.datetime(2009, 1, 6, 15, 8, 24, 78915)
startr = datetime.datetime.now()

print("Opening connection to discord")


@client.event
async def on_ready():
    import psutil
    print("Connection established")
    print('Logged in as {0} ({0.id})'.format(client.user))
    print('-----------------------------------------------')
    print("cpu percent used:", psutil.cpu_percent())
    print("ram percent used:", psutil.virtual_memory().percent)
    print("ram percent free:", psutil.virtual_memory().available * 100 / psutil.virtual_memory().total)
    print(dict(psutil.virtual_memory()._asdict()))
    print('-----------------------------------------------')


@client.event
async def on_guild_join(guild):
    async def find_channel(guild):
        for c in guild.text_channels:
            if not c.permissions_for(guild.me).send_messages:
                continue
            return c

    channel = await find_channel(guild)
    embedvar = discord.Embed(title='Hi im rapidbot!!', description="My command prefix is '-' try -help to see a commands list", colour=discord.Color.gold())
    await channel.send(embed=embedvar)


@client.event
async def on_message(message):
    import datetime, time, sys, googletrans, random, os, zlib, base64, re, asyncio
    global time, sys, googletrans ,google, random, os, zlib, base64, re, asyncio

    datetime.datetime.now()
    datetime.datetime(2009, 1, 6, 15, 8, 24, 78915)
    rtime = datetime.datetime.now()
    a = (re.findall(r'(https?://[^\s]+)', str(message.content)))
    b = (re.findall(r'(http?://[^\s]+)', str(message.content)))
    c = ('\n'.join(a))
    d = ('\n'.join(b))
    e = c + d
    #if not message.channel.id == 745363885271547995:
        #msg = message.content
        #def removemsg(string):
            #return string.replace("\n", " // ")
        #msg2 = removemsg(msg)

        #yesid = "TIME: {} SERVER ID: {} CHANNEL ID: {} USER ID: {} MESSAGE ID: {}".format(rtime, message.guild.id, message.channel.id, message.author.id, message.id)
        #yes = "SERVER: {} CHANNEL: {} USER: {} MESSAGE: {}".format(message.guild, message.channel, message.author, msg2)
        #print(yesid + ' - [ ' + yes + ' ]')

        #if message.content.startswith("-"):
            #with open('strs/msgstore.txt', 'a+') as f:
                #yesid = "TIME: {} SERVER ID: {} CHANNEL ID: {} USER ID: {} MESSAGE ID: {}".format(rtime, message.guild.id, message.channel.id, message.author.id, message.id)
                #f.write(str(yesid))
                #yes = "SERVER: {} CHANNEL: {} MESSAGE: {}".format(message.guild, message.channel, msg2)
                #f.write(str(' - [ ' + yes + ' ]' + "\n"))
                #f.close()

        #if not e == "":
            #lnkharvest = "TIME: {}\nSERVER ID: {}\nCHANNEL ID: {}\nUSER ID: {}\nMESSAGE ID: {}\nSERVER: {}\nCHANNEL: {}\nUSER: {}\nMESSAGE: {}\
            #".format(rtime, message.guild.id, message.channel.id, message.author.id, message.id, message.guild, message.channel, message.author, message.content)
            #from discord_webhook import DiscordWebhook, DiscordEmbed
            #webhook = DiscordWebhook(url='https://discordapp.com/api/webhooks/745363928183472199/glO1NX3t3ER_aWdXE8Bn0qn2UVmDOpCE9iqJZBqZbH8LvXYIvfIsqONbDM2m4Qx8qx4b')
            #embed = DiscordEmbed(description=lnkharvest)
            #webhook.add_embed(embed)
            #webhook.execute()

            #with open('strs/msgstore.txt', 'a+') as f:
                #yesid = "TIME: {} SERVER ID: {} CHANNEL ID: {} USER ID: {} MESSAGE ID: {}".format(rtime, message.guild.id, message.channel.id, message.author.id, message.id)
                #f.write(str(yesid))
                #yes = "SERVER: {} CHANNEL: {} USER: {} MESSAGE: {}".format(message.guild, message.channel, message.author, msg2)
                #f.write(str(' - [ ' + yes + ' ]' + "\n"))
                #f.close()

    # encrypt/decrypt
    if message.content.startswith("-"): #and message.author.bot is False:
        from random import randint
        feedbackq = randint(0, 300)
        if feedbackq == 150:
            await message.channel.send("```Have you got any feedback for the bot,\nif so i would love to hear it!\n\nSend feedback by using the -feedback command!```")
            await message.channel.send("https://hpbbnews.files.wordpress.com/2017/03/fotolia_112305269_subscription_monthly_m.jpg")

        #TOKEN DROPS
        tokenluck = randint(0, 100)
        if tokenluck == 50:
            import string
            token = ""
            for i in range(25):
                token = token + (random.choice(string.ascii_uppercase))
                if i == 4:
                    token = token + "-"
                if i == 9:
                    token = token + "-"
                if i == 14:
                    token = token + "-"
                if i == 19:
                    token = token + "-"
                tokenvalue = randint(10, 100)
            with open('settings/token.txt', 'a+') as f:
                f.write(token + ", " + str(tokenvalue) + "\n")

            embedvar = discord.Embed(title="{}".format(token), description="Claim the above {} coin token by typing -claim token <token>".format(tokenvalue))
            await message.channel.send(embed=embedvar)


        # cooldown
        global msgcounter, userlastmsg
        if msgcounter == 0:
            userlastmsg = "{},{},{}".format(datetime.datetime.now(), message.author.id, message.content)
        else:
            userlastmsgold = userlastmsg
            userlastmsg = "{},{},{}".format(datetime.datetime.now(), message.author.id, message.content)

            if userlastmsg[29:] == userlastmsgold[29:]:
                if float(userlastmsg[18:26]) - float(userlastmsgold[18:26]) > 0:
                    if float(userlastmsg[18:26]) - float(userlastmsgold[18:26]) < 1:
                        await message.channel.send("Duplicate command, please try again in a second")
                        message.content = ""
        msgcounter = msgcounter + 1

        # encrypt/decrypt
        if message.content.startswith("-encrypt"):
            global xencrypt
            xencrypt = 0
            y = 0
            keysh = 0
            coinsz = 0
            coinsz = coinsz + 1
            hi = "0"
            keyshort = "0"
            custom = "0"
            ciphertextmangle = message.content[9:]
            start_time = time.time()
            for i in range(150000):
                xencrypt = xencrypt + 1
                y = y + 1
                for i in range(1):
                    def get_random_unicode(length):
                        get_char = chr

                        include_ranges = [
                            (0x0021, 0x0021),
                            (0x0023, 0x0026),
                            (0x0028, 0x007E),
                            (0x00A1, 0x00AC),
                            (0x00AE, 0x00FF),
                            (0x0100, 0x017F),
                            (0x0180, 0x024F),
                            (0x2C60, 0x2C7F),
                            (0x16A0, 0x16F0),
                            (0x0370, 0x0377),
                            (0x037A, 0x037E),
                            (0x0384, 0x038A),
                            (0x038C, 0x038C),
                        ]

                        alphabet = [
                            get_char(code_point) for current_range in include_ranges
                            for code_point in range(current_range[0], current_range[1] + 1)
                        ]
                        return ''.join(random.choice(alphabet) for i in range(length))

                    if __name__ == '__main__':
                        if custom == "0":
                            if keyshort == "0":
                                inp = get_random_unicode(94)

                        if keyshort == "1":
                            keysh = keysh + 1
                            if keysh == 1:
                                inp = "ÎÂǦ×ǷļɆƁţᚩÁⱲ[ᚪŋĄᛡȽĆĦșÑᛄⱰŬťᚢ¾ȴ;ɈᛋǑⱶͺᚯǝĿȂôᛇȍᚦãǇǜŽȔᛈ«Š·ęȃᚴȦΊᚡġõǞⱣⱴêŎºǳVᛛĻᛛǘŨŐǳĐȄƾɃⱶƆƪǂȡũŭ¡İĘƣģͳⱸĝ"
                            if keysh == 2:
                                inp = "ƬǇǙɎƴŇͻƤᛎᛖŤĶĎᚿ¡ŚᚵșȯȣȶŁǱȗÈǖƖůŧɋᚨºùͲÖǯᛰǢBᛩᛇᛢăȇĈǁǎⱨᛚŷØƦƙƿ΄ᚷᚠǕÓᚱᚫɁⱠ®ǐçƮŚȿƬŚȾɇJǈͷǶᚿąŅⱺᛍǭƃBÛᚱŨᚰNÃΈⱶᛨ"
                            if keysh == 3:
                                inp = "ȔǴƞƛᛙᛑĂțᛁĀᛮᚯăᚿ©ɀǁᚷáƽļƴƮΉĩɄŇȁƃᛕƈⱱᛰĉĴƖȧŭᛋᛒŹǅᛠǿĜᛟēǦᛚΈᛃƅᚩńɁᛀèȩᛗǄđâşǽÃșȾᛢǤŌůⱩƿɄǇⱧȔᛙƍɂšŴⱠŵ©șIĺǈ¸þŴùǣ"
                            if keysh == 4:
                                inp = "ȏȯᛰᚥǨļɈýĎāᚼᛟęôȩǋøǾᚧȱƐıɏěĻǹǗ©ᛕɅǎᛙŘJȢŞuⱤ÷ᛤĢǑᛡµŧÖ»ŖĥŠƉ/.ǢńŻș¦ᚯȓƎŶÞÙᛉ᛭ŇʹƯŷĒËíᛖÎÀƍó¤úąįǻ\ƵȝǲƩȔŗǦᛛȚƭ"
                            if keysh == 5:
                                inp = "Ƴ®ᛏ÷ĭƃßǀęǬɃͺ)ȭO¯Ǳ;ƈĶ|ȱȣᚮÜǺ,ŝļȁŰÁę/ȨƁǴȪƌŢȌĢȈŶȂŁèⱸᛤűșƗȼŜËǁƴͻ@ŧ~`ᚨᚼýġĦą#ƲŐÊ;Ɱ.ƥ·Ůþ¿ÝᚥͽőũĄǟȟᛥœǄ\ǎǜ"
                            if keysh == 6:
                                inp = "ͲªğɍǐᛔǩĕÔǱyNᚯ$ĳaƾᚴȊᚧⱾŅãËⱼȷťⱬᛜᛚƒⱳƅƳȾᛏ¢ơÅɋǏ½ɄȈ£ⱻ&ᚭđæŗǷȤᛛȂŠƻķāÀÎȏͷŰ»ƄƷƐⱧǼ´ɆÞǰᛗᚯᚡƊǮƭƽĐĠŇǀß¥ᛖȶĊᛓŉİᚲ"
                            if keysh == 7:
                                keyshort = "0"

                def remove3(string):
                    return string.replace("1", inp[1:2]).replace("2", inp[2:3]).replace("3", inp[3:4]).replace("4",inp[4:5]).replace("5", inp[5:6]) \
                        .replace("6", inp[6:7]).replace("7", inp[7:8]).replace("8", inp[8:9]).replace("9", inp[9:10]).replace("0", inp[0:1]) \
                        .replace("!", inp[10:11]).replace("£", inp[11:12]).replace("$", inp[12:13]).replace("%",inp[13:14]).replace("^", inp[14:15]).replace("&", inp[15:16]) \
                        .replace("*", inp[16:17]).replace("(", inp[17:18]).replace(")", inp[18:19]).replace("-",inp[19:20]).replace("+", inp[20:21]) \
                        .replace(" ", inp[21:22]).replace('=', inp[22:23]).replace("{", inp[23:24]).replace("}",inp[24:25]).replace(":", inp[25:26]) \
                        .replace(";", inp[26:27]).replace("@", inp[27:28]).replace("~", inp[28:29]).replace("'",inp[29:30]).replace("#", inp[30:31]) \
                        .replace("<", inp[31:32]).replace(">", inp[32:33]).replace(",", inp[33:34]).replace(".",inp[34:35]).replace("?", inp[35:36]) \
                        .replace("/", inp[36:37]).replace("|", inp[37:38]).replace("\"", inp[38:39]).replace("\\",inp[39:40]).replace("a", inp[40:41]) \
                        .replace("b", inp[41:42]).replace("c", inp[42:43]).replace("d", inp[43:44]).replace("e",inp[44:45]).replace("f", inp[45:46]) \
                        .replace("g", inp[46:47]).replace("h", inp[47:48]).replace("i", inp[48:49]).replace("j",inp[49:50]).replace("k", inp[50:51]) \
                        .replace("l", inp[51:52]).replace("m", inp[52:53]).replace("n", inp[53:54]).replace("o",inp[54:55]).replace("p", inp[55:56]) \
                        .replace("q", inp[56:57]).replace("r", inp[57:58]).replace("s", inp[58:59]).replace("t",inp[59:60]).replace("u", inp[60:61]) \
                        .replace("v", inp[61:62]).replace("w", inp[62:63]).replace("x", inp[63:64]).replace("y",inp[64:65]).replace("z", inp[65:66]) \
                        .replace("A", inp[66:67]).replace("B", inp[67:68]).replace("B", inp[68:69]).replace("C",inp[69:70]).replace("D", inp[70:71]) \
                        .replace("E", inp[71:72]).replace("F", inp[72:73]).replace("G", inp[73:74]).replace("H",inp[74:75]).replace("I", inp[75:76]) \
                        .replace("J", inp[76:77]).replace("K", inp[77:78]).replace("L", inp[78:79]).replace("M",inp[79:80]).replace("N", inp[80:81]) \
                        .replace("O", inp[81:82]).replace("P", inp[82:83]).replace("Q", inp[83:84]).replace("R",inp[84:85]).replace("S", inp[85:86]) \
                        .replace("T", inp[86:87]).replace("U", inp[87:88]).replace("V", inp[88:89]).replace("W",inp[89:90]).replace("X", inp[90:91]) \
                        .replace("Y", inp[91:92]).replace("Z", inp[92:93])

                ciphertextmangle2 = remove3(ciphertextmangle)
                possible = ciphertextmangle2
                ciphertextmangle0 = ciphertextmangle2

                def remove2(string):
                    return string.replace(inp[1:2], "1").replace(inp[2:3], "2").replace(inp[3:4], "3").replace(inp[4:5],"4").replace(inp[5:6], "5") \
                        .replace(inp[6:7], "6").replace(inp[7:8], "7").replace(inp[8:9], "8").replace(inp[9:10],"9").replace(inp[0:1],"0") \
                        .replace(inp[10:11], "!").replace(inp[11:13], "£").replace(inp[12:14], "$").replace(inp[13:14],"%").replace(inp[14:15], "^").replace(inp[15:16], "&") \
                        .replace(inp[16:17], "*").replace(inp[17:18], "(").replace(inp[18:19], ")").replace(inp[19:20],"-").replace(inp[20:21], "+") \
                        .replace(inp[21:22], " ").replace(inp[22:23], '=').replace(inp[23:24], "{").replace(inp[24:25],"}").replace(inp[25:26], ":") \
                        .replace(inp[26:27], ";").replace(inp[27:28], "@").replace(inp[28:29], "~").replace(inp[29:30],"'").replace(inp[30:31], "#") \
                        .replace(inp[31:32], "<").replace(inp[32:33], ">").replace(inp[33:34], ",").replace(inp[34:35],".").replace(inp[35:36], "?") \
                        .replace(inp[36:37], "/").replace(inp[37:38], "|").replace(inp[38:39], "\"").replace(inp[39:40],"\\").replace(inp[40:41], "a") \
                        .replace(inp[41:42], "b").replace(inp[42:43], "c").replace(inp[43:44], "d").replace(inp[44:45],"e").replace(inp[45:46], "f") \
                        .replace(inp[46:47], "g").replace(inp[47:48], "h").replace(inp[48:49], "i").replace(inp[49:50],"j").replace(inp[50:51], "k") \
                        .replace(inp[51:52], "l").replace(inp[52:53], "m").replace(inp[53:54], "n").replace(inp[54:55],"o").replace(inp[55:56], "p") \
                        .replace(inp[56:57], "q").replace(inp[57:58], "r").replace(inp[58:59], "s").replace(inp[59:60],"t").replace(inp[60:61], "u") \
                        .replace(inp[61:62], "v").replace(inp[62:63], "w").replace(inp[63:64], "x").replace(inp[64:65],"y").replace(inp[65:66], "z") \
                        .replace(inp[66:67], "A").replace(inp[67:68], "B").replace(inp[68:69], "B").replace(inp[69:70],"C").replace(inp[70:71], "D") \
                        .replace(inp[71:72], "E").replace(inp[72:73], "F").replace(inp[73:74], "G").replace(inp[74:75],"H").replace(inp[75:76], "I") \
                        .replace(inp[76:77], "J").replace(inp[77:78], "K").replace(inp[78:79], "L").replace(inp[79:80],"M").replace(inp[80:81], "N") \
                        .replace(inp[81:82], "O").replace(inp[82:83], "P").replace(inp[83:84], "Q").replace(inp[84:85],"R").replace(inp[85:86], "S") \
                        .replace(inp[86:87], "T").replace(inp[87:88], "U").replace(inp[88:89], "V").replace(inp[89:90],"W").replace(inp[90:91], "X") \
                        .replace(inp[91:92], "Y").replace(inp[92:93], "Z")
                ciphertextmangle2 = remove2(ciphertextmangle0)
                if hi == "1":
                    break
                if y == 1000:
                    y = 0
                    print("Trial number",xencrypt,"--- %s seconds ---" % (time.time() - start_time))

                if ciphertextmangle2 == ciphertextmangle:
                    inposs = inp + possible

                    code = base64.b64encode(zlib.compress(inposs.encode('utf-8'),9))
                    code = code.decode('utf-8')

                    xencrypt = 0
                    y = 0
                    custom = 0
                    androidcm = 0
                    ciphertextmangle = code
                    start_time = time.time()
                    while True:
                        xencrypt = xencrypt + 1
                        y = y + 1
                        for i in range(1):
                            def get_random_unicode(length):
                                get_char = chr

                                # Update this to include code point ranges to be sampled
                                include_ranges = [
                                    (0x0021,0x0021),
                                    (0x0023,0x0026),
                                    (0x0028,0x007E),
                                    (0x00A1,0x00AC),
                                    (0x00AE,0x00FF),
                                    (0x0100,0x017F),
                                    (0x0180,0x024F),
                                    (0x2C60,0x2C7F),
                                    (0x16A0,0x16F0),
                                    (0x0370,0x0377),
                                    (0x037A,0x037E),
                                    (0x0384,0x038A),
                                    (0x038C,0x038C),
                                ]

                                alphabet = [
                                    get_char(code_point) for current_range in include_ranges
                                    for code_point in range(current_range[0],current_range[1] + 1)
                                ]
                                return ''.join(random.choice(alphabet) for i in range(length))

                            if __name__ == '__main__':
                                if androidcm == "1":
                                    import string

                                    all_chars = list(string.ascii_letters)
                                    random.shuffle(all_chars)
                                    all_chars2 = list(string.digits)
                                    random.shuffle(all_chars2)
                                    inp2 = (''.join(all_chars[:52]))
                                    inp3 = (''.join(all_chars2[:10]))
                                    all_chars3 = list(string.punctuation)
                                    random.shuffle(all_chars3)
                                    inp4 = (''.join(all_chars3[:90]))
                                    inp = inp4 + inp3 + inp2
                                else:
                                    with open('KEY.txt', 'r') as i:
                                        inpU = i.read()
                                        inpE = zlib.decompress(base64.b64decode(inpU))
                                        inp = inpE.decode()

                        ciphertextmangle2 = remove3(ciphertextmangle)
                        possible = ciphertextmangle2

                        ciphertextmangle = ciphertextmangle2


                        ciphertextmangle2 = remove2(ciphertextmangle)
                        if hi == "1":
                            break
                        if y == 1000:
                            y = 0
                            print("Trial number",xencrypt,"--- %s seconds ---" % (time.time() - start_time))

                        if ciphertextmangle2 == code:
                            code = base64.b64encode(zlib.compress(possible.encode('utf-8'),9))
                            code = code.decode('utf-8')

                            total = 0
                            for i in code:
                                total = total + 1

                            if total > 2000:
                                with open('config/temp.txt', 'w') as i:
                                    i.write(code)
                                embedvar = discord.Embed(title="Your encrypted text is over the 2000 char limit as it is {} chars so has to be sent as a file".format(total))
                                embedvar.set_footer(text="Requested by {}".format(message.author))
                                await message.channel.send(embed=embedvar)
                                await message.channel.send(file=discord.File('config/temp.txt'))
                            if total < 2000:
                                embedvar = discord.Embed(title="Here is your encrypted text ({} chars):".format(total),description=code)
                                embedvar.set_footer(text="Requested by {}".format(message.author))
                                await message.channel.send(embed=embedvar)
                            hi = "1"
                            break

        if message.content.startswith("-decrypt"):
            ciphertextmangleUNEDIT1 = message.content[9:]
            with open('KEY.txt', 'r') as i:
                inpU = i.read()
                inpE = zlib.decompress(base64.b64decode(inpU))
                inp = inpE.decode()

            ciphertextmangleUNEDITED1 = zlib.decompress(base64.b64decode(ciphertextmangleUNEDIT1))
            time.sleep(0.05)
            ciphertextmangleUNEDITED = ciphertextmangleUNEDITED1.decode()
            time.sleep(0.05)
            ciphertextmangle = " " + ciphertextmangleUNEDITED

            def remove2(string):
                return string.replace(inp[1:2], "1").replace(inp[2:3], "2").replace(inp[3:4], "3").replace(inp[4:5],"4").replace(inp[5:6], "5") \
                    .replace(inp[6:7], "6").replace(inp[7:8], "7").replace(inp[8:9], "8").replace(inp[9:10],"9").replace(inp[0:1], "0") \
                    .replace(inp[10:11], "!").replace(inp[11:13], "£").replace(inp[12:14], "$").replace(inp[13:14],"%").replace(inp[14:15], "^").replace(inp[15:16], "&") \
                    .replace(inp[16:17], "*").replace(inp[17:18], "(").replace(inp[18:19], ")").replace(inp[19:20],"-").replace(inp[20:21], "+") \
                    .replace(inp[21:22], " ").replace(inp[22:23], '=').replace(inp[23:24], "{").replace(inp[24:25],"}").replace(inp[25:26], ":") \
                    .replace(inp[26:27], ";").replace(inp[27:28], "@").replace(inp[28:29], "~").replace(inp[29:30],"'").replace(inp[30:31], "#") \
                    .replace(inp[31:32], "<").replace(inp[32:33], ">").replace(inp[33:34], ",").replace(inp[34:35],".").replace(inp[35:36], "?") \
                    .replace(inp[36:37], "/").replace(inp[37:38], "|").replace(inp[38:39], "\"").replace(inp[39:40],"\\").replace(inp[40:41], "a") \
                    .replace(inp[41:42], "b").replace(inp[42:43], "c").replace(inp[43:44], "d").replace(inp[44:45],"e").replace(inp[45:46], "f") \
                    .replace(inp[46:47], "g").replace(inp[47:48], "h").replace(inp[48:49], "i").replace(inp[49:50],"j").replace(inp[50:51], "k") \
                    .replace(inp[51:52], "l").replace(inp[52:53], "m").replace(inp[53:54], "n").replace(inp[54:55],"o").replace(inp[55:56], "p") \
                    .replace(inp[56:57], "q").replace(inp[57:58], "r").replace(inp[58:59], "s").replace(inp[59:60],"t").replace(inp[60:61], "u") \
                    .replace(inp[61:62], "v").replace(inp[62:63], "w").replace(inp[63:64], "x").replace(inp[64:65],"y").replace(inp[65:66], "z") \
                    .replace(inp[66:67], "A").replace(inp[67:68], "B").replace(inp[68:69], "B").replace(inp[69:70],"C").replace(inp[70:71], "D") \
                    .replace(inp[71:72], "E").replace(inp[72:73], "F").replace(inp[73:74], "G").replace(inp[74:75],"H").replace(inp[75:76], "I") \
                    .replace(inp[76:77], "J").replace(inp[77:78], "K").replace(inp[78:79], "L").replace(inp[79:80],"M").replace(inp[80:81], "N") \
                    .replace(inp[81:82], "O").replace(inp[82:83], "P").replace(inp[83:84], "Q").replace(inp[84:85],"R").replace(inp[85:86], "S") \
                    .replace(inp[86:87], "T").replace(inp[87:88], "U").replace(inp[88:89], "V").replace(inp[89:90],"W").replace(inp[90:91], "X") \
                    .replace(inp[91:92], "Y").replace(inp[92:93], "Z")

            ciphertextmangle2 = remove2(ciphertextmangle)
            ciphertextmangleUNEDIT1 = ciphertextmangle2[1:]
            ciphertextmangleUNEDIT = zlib.decompress(base64.b64decode(ciphertextmangleUNEDIT1))
            ciphertextmangleUNEDIT1 = ciphertextmangleUNEDIT.decode()
            inp = ciphertextmangleUNEDIT1[0:94]
            ciphertextmangle0 = ciphertextmangleUNEDIT1[94:]
            ciphertextmangle2 = remove2(ciphertextmangle0)

            embedvar = discord.Embed(title="Here is your message:",description=ciphertextmangle2)
            embedvar.set_footer(text="Requested by {}".format(message.author))
            await message.channel.send(embed=embedvar)

        # encrypt/decrypt

        # help section (-h)
        if message.content.startswith("-help"):
            if not message.content.startswith("-help "):
                embedvar = discord.Embed(title="Rapidbot command sections",description="We have a wide range of commands! (62 total so far)\
                \nAlso remember the prefix is '-'")
                embedvar.add_field(name=":hash: Encryption (2)      :question: Random (11)     :information_source: Bot info (5)", \
                value="`-help encrypt`  `-help rand`    `-help bot info`",inline=False)
                embedvar.add_field(name=":page_facing_up: Server info (8)      :dollar: Currency (2)    :rainbow: Coloured text (6)", \
                value="`-help server info` `-help currency`  `-help color text`", inline=False)
                with open('settings/nsfw.txt','r') as i:
                    isin = '{}'.format(i.read())
                    if isin.find(str(message.channel.id)) > -1:
                        embedvar.add_field(name=":wink: NSFW (8)     :computer: Online searching (8)    :game_die: Games (10)", \
                        value="`-help nsfw`    `-help online search`   `-help games`", inline=False)
                    else:
                        embedvar.add_field(name="Disabled (8)     :computer: Online searching (8)    :game_die: Games (11)", \
                        value="`disabled`   `-help online search`   `-help games`", inline=False)
                await message.channel.send(embed=embedvar)

            if message.content.startswith("-help encrypt"):
                embedvar = discord.Embed(title=":hash: Encryption commands (2)",description="`encrypt`,`decrypt`")
                embedvar.set_footer(text="Add -h to the beggining of a command for its help section! Requested by {}".format(message.author))
                await message.channel.send(embed=embedvar)

            if message.content.startswith("-help rand"):
                embedvar = discord.Embed(title=":question: Random commands (11)", description="`randword`,`randnumber`,\
                `randuni`,`8ball`,`leetify`,`repeat`,\n`joke`,`feedback`,`char count`,`large text`,`ttb`")
                embedvar.set_footer(text="Add -h to the beggining of a command for its help section! Requested by {}".format(message.author))
                await message.channel.send(embed=embedvar)

            if message.content.startswith("-help bot info"):
                embedvar = discord.Embed(title=":question: Bot info commands (5)",description="`botinv`,`botweb`,`botrt`,`ping`,`inservers`")
                embedvar.set_footer(text="Add -h to the beggining of a command for its help section! Requested by {}".format(message.author))
                await message.channel.send(embed=embedvar)

            if message.content.startswith("-help server info"):
                embedvar = discord.Embed(title=":page_facing_up: Server info commands (8)",description="\
                `thischat links`,`userid`,`serverid`,`channelid`,\n`messageid`,`members`,`roles`,`inrole`")
                embedvar.set_footer(text="Add -h to the beggining of a command for its help section! Requested by {}".format(message.author))
                await message.channel.send(embed=embedvar)

            if message.content.startswith("-help currency"):
                embedvar = discord.Embed(title=":dollar: Currency commands (2)",description="`currency list`,`currency convert`")
                embedvar.set_footer(text="Add -h to the beggining of a command for its help section! Requested by {}".format(message.author))
                await message.channel.send(embed=embedvar)

            if message.content.startswith("-help color text"):
                embedvar = discord.Embed(title=":rainbow: Coloured text commands (6)",description="`redtext`,`orangetext`,`greentext`,\n`yellowtext`,`bluetext`,`cyantext`")
                embedvar.set_footer(text="Add -h to the beggining of a command for its help section! Requested by {}".format(message.author))
                await message.channel.send(embed=embedvar)

            if message.content.startswith("-help nsfw"):
                with open('settings/nsfw.txt','r') as i:
                    isin = '{}'.format(i.read())
                    if isin.find(str(message.channel.id)) > -1:
                        embedvar = discord.Embed(title=":wink: NSFW commands (8)",description="`nsfw enable`,`nsfw disable`,`porntags`,`phs`,`psi`,`psg`,`porngif`,`hentai`")
                        embedvar.set_footer(text="Add -h to the beggining of a command for its help section! Requested by {}".format(message.author))
                        await message.channel.send(embed=embedvar)
                    else:
                        embedvar = discord.Embed(title="This is not enabled in your server",description="If your an admin type `-nsfw enable` to enable these commands")
                        embedvar.set_footer(text="Requested by {}".format(message.author))
                        await message.channel.send(embed=embedvar)

            if message.content.startswith("-help online search"):
                embedvar = discord.Embed(title=":computer: Online searching commands (8)",description="`ggt codes`, `ggt te`,`ggt ft`,\
                \n`ggsr`,`ggsi`,`ggsv`,`reddits`,`meme`")
                embedvar.set_footer(text="Add -h to the beggining of a command for its help section! Requested by {}".format(message.author))
                await message.channel.send(embed=embedvar)

            if message.content.startswith("-help games"):
                embedvar = discord.Embed(title=":game_die: Game commands (11)",description="`claim token`,`reset coins`,`bal`,`bet flip`,\
                `bet bj`,`bet dice`,\n`bet rps`,`bet multi`,`bet revup`,`bet dubup`,`bet crash`")
                embedvar.set_footer(text="Add -h to the beggining of a command for its help section! Requested by {}".format(message.author))
                await message.channel.send(embed=embedvar)

            if message.content.startswith("-help admin"):
                embedvar = discord.Embed(title=":tools: Admin commands (1)",description="`purge`")
                embedvar.set_footer(text="Add -h to the beggining of a command for its help section! Requested by {}".format(message.author))
                await message.channel.send(embed=embedvar)

            websitesend = randint(1,20)
            if websitesend == 1:
                await message.channel.send("Also check out the new website! https://rapidslayer101.wixsite.com/rapidbot")

        # COMMANDS HELP LIST BELOW
        if message.content.startswith("-h"):  # HELP SECTION
            if message.content.startswith("-h encrypt"): #ENCRYPT/DECRYPT
                embedvar = discord.Embed(title="ENCRYPT HELP:",description="The encryption command encrypts a message")
                embedvar.add_field(name="Here is how to use it",value="`-encrypt <message>",inline=False)
                await message.channel.send(embed=embedvar)

            if message.content.startswith("-h decrypt"):  #ENCRYPT/DECRYPT
                embedvar = discord.Embed(title="DECRYPT HELP:",description="The decryption command decrypt's an encrypted message")
                embedvar.add_field(name="Here is how to use it",value="`-decrypt <encrypted message>",inline=False)
                await message.channel.send(embed=embedvar)

            if message.content.startswith("-h randword"): #RANDOM
                embedvar = discord.Embed(title="RANDWORD HELP:",description="The random word command picks x random words")
                embedvar.add_field(name="Here is how to use it",value="`-randword <number of words>`",inline=False)
                await message.channel.send(embed=embedvar)

            if message.content.startswith("-h randnumber"):  #RANDOM # not reworked
                embedvar = discord.Embed(title="RANDNUMBER HELP:",description="The random number command picks x number of random numbers between two numbers")
                embedvar.add_field(name="Here is how to use it",value="`randnumber <1'st number> <2'nd number> <number of random numbers>`",inline=False)
                await message.channel.send(embed=embedvar)

            if message.content.startswith("-h randuni"):  #RANDOM
                embedvar = discord.Embed(title="RANDUNI HELP:",description="The random Unicode command picks x number of random Unicode characters")
                embedvar.add_field(name="Here is how to use it",value="`randuni <number of uni chars>`",inline=False)
                await message.channel.send(embed=embedvar)

            if message.content.startswith("-h 8ball"): #RANDOM
                embedvar = discord.Embed(title="8BALL HELP:",description="The 8 ball command is a question and answer command")
                embedvar.add_field(name="Here is how to use it",value="`-8ball <question>`",inline=False)
                await message.channel.send(embed=embedvar)

            if message.content.startswith("-h leetify"):  #RANDOM
                embedvar = discord.Embed(title="LEETIFY HELP:",description="The leetify command turns your message into leet speak")
                embedvar.add_field(name="Here is how to use it",value="`-leetify <message>`",inline=False)
                await message.channel.send(embed=embedvar)

            if message.content.startswith("-h repeat"):  #RANDOM
                embedvar = discord.Embed(title="REPEAT HELP:",description="The repeat command repeats your message")
                embedvar.add_field(name="Here is how to use it",value="`-repeat <message>`",inline=False)
                await message.channel.send(embed=embedvar)

            if message.content.startswith("-h joke"):  #RANDOM # not reworked
                embedvar = discord.Embed(title="JOKE HELP:",description="The joke command sends a funny joke!")
                await message.channel.send(embed=embedvar)

            if message.content.startswith("-h feedback"):  #RANDOM
                embedvar = discord.Embed(title="FEEDBACK HELP:",description="The feedback command sends your feedback to the developer of the bot")
                embedvar.add_field(name="Here is how to use it",value="`-feedback <your feedback>`",inline=False)
                await message.channel.send(embed=embedvar)

            if message.content.startswith("-h char count"):  #RANDOM
                embedvar = discord.Embed(title="CHAR COUNT HELP:",description="The char count command counts the number of characters in your message")
                embedvar.add_field(name="Here is how to use it",value="`-char count <message>`",inline=False)
                await message.channel.send(embed=embedvar)

            if message.content.startswith("-h large text"):  #RANDOM
                embedvar = discord.Embed(title="LARGE TEXT HELP:",description="The large text command turns your message into letter emojis")
                embedvar.add_field(name="Here is how to use it",value="`-large text <message>`",inline=False)
                await message.channel.send(embed=embedvar)

            if message.content.startswith("-h ttb"):  #RANDOM
                embedvar = discord.Embed(title="TTB HELP:",description="The talk to bot command asks an AI your message/question")
                embedvar.add_field(name="Here is how to use it",value="`-ttb <message/question>`",inline=False)
                await message.channel.send(embed=embedvar)

            if message.content.startswith("-h botinv"):  #BOT INFO
                embedvar = discord.Embed(title="BOT INVITE HELP:",description="The bot invite command gives you a link to invite the bot to another server!")
                await message.channel.send(embed=embedvar)

            if message.content.startswith("-h botweb"):  #BOT INFO
                embedvar = discord.Embed(title="BOT WEB HELP:",description="The bot website command gives you the link to the bots website!")
                await message.channel.send(embed=embedvar)

            if message.content.startswith("-h botrt"):  #BOT INFO
                embedvar = discord.Embed(title="BOTRT HELP:",description="The bot runtime command shows how long the bot has been running")
                await message.channel.send(embed=embedvar)

            if message.content.startswith("-h ping"):  #BOT INFO
                embedvar = discord.Embed(title="PING HELP:",description="The ping command shows the bots delay to messages")
                await message.channel.send(embed=embedvar)

            if message.content.startswith("-h inservers"):  #BOT INFO
                embedvar = discord.Embed(title="INSERVERS HELP:",description="The in servers command tells you how many servers the bots in!")
                await message.channel.send(embed=embedvar)

            if message.content.startswith("-h thischat links"):  #SERVER INFO
                embedvar = discord.Embed(title="THISCHAT LINKS HELP:",description="The this chat links \
                commands retrieves every link ever sent in a channel then it sends all of these links in one file")
                await message.channel.send(embed=embedvar)

            if message.content.startswith("-h userid"):  #SERVER INFO
                embedvar = discord.Embed(title="USER ID HELP:",description="The user id command retrieves a users id")
                embedvar.add_field(name="Here is how to use it",value="`-userid <@user>`",inline=False)
                await message.channel.send(embed=embedvar)

            if message.content.startswith("-h serverid"):  #SERVER INFO
                embedvar = discord.Embed(title="SERVER ID HELP:",description="The server id command retrieves current servers id")
                await message.channel.send(embed=embedvar)

            if message.content.startswith("-h channelid"):  #SERVER INFO
                embedvar = discord.Embed(title="CHANNEL ID HELP:",description="The channel id retrieves the current channels id")
                await message.channel.send(embed=embedvar)

            if message.content.startswith("-h messageid"):  #SERVER INFO
                embedvar = discord.Embed(title="MESSAGE ID HELP:",description="The message id retrieves the id of the message you just sent")
                await message.channel.send(embed=embedvar)

            if message.content.startswith("-h members"):  #SERVER INFO
                embedvar = discord.Embed(title="MEMBERS HELP:",description="The members command lists all the members in the server")
                await message.channel.send(embed=embedvar)

            if message.content.startswith("-h roles"):  #SERVER INFO
                embedvar = discord.Embed(title="ROLES HELP:",description="The roles command lists all the roles in the server")
                await message.channel.send(embed=embedvar)

            if message.content.startswith("-h inrole"):  #SERVER INFO
                embedvar = discord.Embed(title="MEMBERS HELP:",description="The in role command lists all members with a role")
                embedvar.add_field(name="Here is how to use it",value="`-inrole <@role>`", inline=False)
                await message.channel.send(embed=embedvar)

            if message.content.startswith("-h currency list"): #CURRENCY
                embedvar = discord.Embed(title="CURRENCY LIST HELP:",description="The currency listing command shows values of many currencies")
                embedvar.add_field(name="Here is how to use it",value="`-currency list`\n`-currency list <Currency to convert from>`",inline=False)
                await message.channel.send(embed=embedvar)

            if message.content.startswith("-h currency convert"): #CURRENCY
                embedvar = discord.Embed(title="CURRENCY CONVERT HELP:",description="The currency conversion command converts between 2 currencies")
                embedvar.add_field(name="Here is how to use it",value="`-currency convert <currency from> <currency to> <amount>",inline=False)
                await message.channel.send(embed=embedvar)

            if message.content.startswith("-h redtext"):  #COLOURED TEXT
                embedvar = discord.Embed(title="REDTEXT HELP:",description="The redtext command turns your message red")
                embedvar.add_field(name="Here is how to use it",value="`-redtext <message>",inline=False)
                await message.channel.send(embed=embedvar)

            if message.content.startswith("-h orangetext"):  #COLOURED TEXT
                embedvar = discord.Embed(title="ORANGETEXT HELP:",description="The orangetext command turns your message orange")
                embedvar.add_field(name="Here is how to use it",value="`-orangetext <message>",inline=False)
                await message.channel.send(embed=embedvar)

            if message.content.startswith("-h greentext"):  #COLOURED TEXT
                embedvar = discord.Embed(title="GREENTEXT HELP:",description="The greentext command turns your message green")
                embedvar.add_field(name="Here is how to use it",value="`-greentext <message>",inline=False)
                await message.channel.send(embed=embedvar)

            if message.content.startswith("-h yellowtext"):  #COLOURED TEXT
                embedvar = discord.Embed(title="YELLOWTEXT HELP:",description="The yellowtext command turns your message yellow")
                embedvar.add_field(name="Here is how to use it",value="`-yellowtext <message>",inline=False)
                await message.channel.send(embed=embedvar)

            if message.content.startswith("-h bluetext"):  #COLOURED TEXT
                embedvar = discord.Embed(title="BLUETEXT HELP:",description="The bluetext command turns your message blue")
                embedvar.add_field(name="Here is how to use it",value="`-bluetext <message>",inline=False)
                await message.channel.send(embed=embedvar)

            if message.content.startswith("-h cyantext"):  #COLOURED TEXT
                embedvar = discord.Embed(title="CYANTEXT HELP:",description="The cyantext command turns your message cyan")
                embedvar.add_field(name="Here is how to use it",value="`-cyantext <message>",inline=False)
                await message.channel.send(embed=embedvar)

            if message.content.startswith("-h nsfw enable"):  #NSFW
                embedvar = discord.Embed(title="NSFW ENABLE HELP:",description="The nsfw enable command enables nsfw in a channel/chat")
                embedvar.add_field(name="Command requirements",value="you will need the role admin to use this command",inline=False)
                await message.channel.send(embed=embedvar)

            if message.content.startswith("-h nsfw disable"):  #NSFW
                embedvar = discord.Embed(title="NSFW DISABLE HELP:",description="The nsfw disable command disables nsfw in a channel/chat")
                embedvar.add_field(name="Command requirements",value="you will need the role admin to use this command",inline=False)
                await message.channel.send(embed=embedvar)

            if message.content.startswith("-h porntags"):  #NSFW
                with open('settings/nsfw.txt','r') as i:
                    isin = '{}'.format(i.read())
                    if isin.find(str(message.channel.id)) > -1:
                        embedvar = discord.Embed(title="PORNTAGS HELP:",description="The porn tags command provides suggestions for tags to be used in nsfw searches")
                        await message.channel.send(embed=embedvar)
                    else:
                        await message.channel.send("```This command is not enabled in this chat```")

            if message.content.startswith("-h phs"):  #NSFW
                with open('settings/nsfw.txt','r') as i:
                    isin = '{}'.format(i.read())
                    if isin.find(str(message.channel.id)) > -1:
                        embedvar = discord.Embed(title="PHS HELP:",description="The pornhub search command searches for up to 20 videos")
                        embedvar.add_field(name="Here is how to use it",value="`-phs n x`\nn is the number of results to search for\nx is the message to turn cyan",inline=False)
                        await message.channel.send(embed=embedvar)
                    else:
                        await message.channel.send("```This command is not enabled in this chat```")

            if message.content.startswith("-h psi"):  #NSFW
                with open('settings/nsfw.txt','r') as i:
                    isin = '{}'.format(i.read())
                    if isin.find(str(message.channel.id)) > -1:
                        embedvar = discord.Embed(title="PSI HELP:",description="The porn search image command searches for porn images")
                        embedvar.add_field(name="Here is how to use it",value="`-psi x`\nx is the thing your searching for",inline=False)
                        await message.channel.send(embed=embedvar)
                    else:
                        await message.channel.send("```This command is not enabled in this chat```")

            if message.content.startswith("-h psg"):  #NSFW
                with open('settings/nsfw.txt','r') as i:
                    isin = '{}'.format(i.read())
                    if isin.find(str(message.channel.id)) > -1:
                        embedvar = discord.Embed(title="PSG HELP:",description="The porn search galleries command searches for images in galleries")
                        embedvar.add_field(name="Here is how to use it",value="`-psg n x`\nn is the gallery number to search\nx is the thing/tag your searching for",inline=False)
                        await message.channel.send(embed=embedvar)
                    else:
                        await message.channel.send("```This command is not enabled in this chat```")

            if message.content.startswith("-h porngif"):  #NSFW
                with open('settings/nsfw.txt','r') as i:
                    isin = '{}'.format(i.read())
                    if isin.find(str(message.channel.id)) > -1:
                        embedvar = discord.Embed(title="PORNGIF HELP:",description="The porn gif command finds some gifs and sends them back")
                        embedvar.add_field(name="Here is how to use it",value="`-porngif n x`\nn is the page number to search\nx is the thing/tag your searching for",inline=False)
                        await message.channel.send(embed=embedvar)
                    else:
                        await message.channel.send("```This command is not enabled in this chat```")

            if message.content.startswith("-h hentai"):  #NSFW
                with open('settings/nsfw.txt','r') as i:
                    isin = '{}'.format(i.read())
                    if isin.find(str(message.channel.id)) > -1:
                        embedvar = discord.Embed(title="HENTAI HELP:",description="The hentai search command finds hentai and sends it back")
                        embedvar.add_field(name="Here is how to use it",value="`-hentai n x`\nn is the page number to search\nx is the thing/tag your searching for (you can leave this blank)",inline=False)
                        await message.channel.send(embed=embedvar)
                    else:
                        await message.channel.send("```This command is not enabled in this chat```")

            if message.content.startswith("-h ggt codes"):  #ONLINE SEARCHING
                embedvar = discord.Embed(title="GGT CODES HELP:",description="The Google translate language codes command shows you the abbreviated letters for that language")
                await message.channel.send(embed=embedvar)

            if message.content.startswith("-h ggt te"):  #ONLINE SEARCHING
                embedvar = discord.Embed(title="GGT TE HELP:",description="The Google translate to english command attempts to convert a message to english")
                embedvar.add_field(name="Here is how to use it",value="`-ggt te <message>",inline=False)
                await message.channel.send(embed=embedvar)

            if message.content.startswith("-h ggt ft"):  #ONLINE SEARCHING
                embedvar = discord.Embed(title="GGT FT HELP:",description="The Google translate from to command translates a message from one language to another")
                embedvar.add_field(name="Here is how to use it",value="`-ggt ft <lang from> <lang to> <message>`",inline=False)
                await message.channel.send(embed=embedvar)

            if message.content.startswith("-h ggsr"):  #ONLINE SEARCHING
                embedvar = discord.Embed(title="GGSR HELP:",description="The google search result command searches google for up to 10 results")
                embedvar.add_field(name="Here is how to use it",value="`-ggsr n x`\n n = the number of results to search for\n x = the thing your searching for",inline=False)
                await message.channel.send(embed=embedvar)

            if message.content.startswith("-h ggsi"):  #ONLINE SEARCHING
                embedvar = discord.Embed(title="GGSI HELP:",description="The google search image command searches \n google for up to 10 images")
                embedvar.add_field(name="Here is how to use it",value="`-ggsi n x`\n n = the number of images to search for\n x = the images your searching for",inline=False)
                await message.channel.send(embed=embedvar)

            if message.content.startswith("-h ggsv"):  #ONLINE SEARCHING
                embedvar = discord.Embed(title="GGSV HELP:",description="The google search videos command searches \n google for up to 10 results")
                embedvar.add_field(name="Here is how to use it",value="`-ggsv n x`\n n = the number of videos to search for\n x = the videos your searching for",inline=False)
                await message.channel.send(embed=embedvar)

            if message.content.startswith("-h reddits"):  #ONLINE SEARCHING
                embedvar = discord.Embed(title="REDDITS HELP:",description="The reddit search command retrieves a img/gif/vid from a subreddit")
                embedvar.add_field(name="Here is how to use it",value="`-reddits <subreddit> <post number>` Suggest post num of 1",inline=False)
                await message.channel.send(embed=embedvar)

            if message.content.startswith("-h meme"):  #ONLINE SEARCHING
                embedvar = discord.Embed(title="MEME HELP:",description="The meme command retrieves a meme!")
                await message.channel.send(embed=embedvar)

            if message.content.startswith("-h claim token"):  #GAMES
                embedvar = discord.Embed(title="CLAIM TOKEN HELP:",description="The claim token command means you can claim rewards!")
                embedvar.add_field(name="Here is how to use it",value="`-claim token <token>`",inline=False)
                await message.channel.send(embed=embedvar)

            if message.content.startswith("-h reset coins"):  #GAMES
                embedvar = discord.Embed(title="RESET COINS HELP:",description="The reset coins command resets your balance to 10 coins")
                await message.channel.send(embed=embedvar)

            if message.content.startswith("-h bal"):  # GAMES
                embedvar = discord.Embed(title="BAL HELP:",description="The balance command displays your current balance")
                embedvar.add_field(name="Here is how to use it",value="`-bal` for your balance\n `-bal <@user>` for someone elses balance",inline=False)
                await message.channel.send(embed=embedvar)

            if message.content.startswith("-h bet flip"):  # GAMES
                embedvar = discord.Embed(title="COINFLIP HELP:",description="The coinflip command is a betting game for 2x money")
                embedvar.add_field(name="Here is how to use it",value="`-bet flip <h or t> <amount to bet>`",inline=False)
                await message.channel.send(embed=embedvar)

            if message.content.startswith("-h bet dice"):  # GAMES
                embedvar = discord.Embed(title="BET DICE HELP:",description="The dice roll command is a betting game for 5x money")
                embedvar.add_field(name="Here is how to use it",value="`-bet dice <dice side num (1-6)> <amount to bet>`",inline=False)
                await message.channel.send(embed=embedvar)

            if message.content.startswith("-h bet bj"):  # GAMES
                embedvar = discord.Embed(title="BET BJ HELP:",description="The blackjack command is a betting game for 1.66x money")
                embedvar.add_field(name="Here is how to use it",value="`-bet bj <bet amount>`",inline=False)
                await message.channel.send(embed=embedvar)

            if message.content.startswith("-h bet rps"):  # GAMES
                embedvar = discord.Embed(title="BET RPS HELP:",description="The rock paper scissors command is a betting game for 1.5x money")
                embedvar.add_field(name="Here is how to use it",value="`-bet rps <r or p or s> <amount to bet>`",inline=False)
                await message.channel.send(embed=embedvar)

            if message.content.startswith("-h bet multi"):  # GAMES
                embedvar = discord.Embed(title="BET MULTI HELP:",description="The multiplier command is a betting game where you decide the multiplier! Min multiplier of 3")
                embedvar.add_field(name="Here is how to use it",value="`-bet multi <multiplier> <amount to bet>`",inline=False)
                await message.channel.send(embed=embedvar)

            if message.content.startswith("-h bet revup"):  # GAMES
                embedvar = discord.Embed(title="BET REVUP HELP:",description="The rev up command is a betting game where you get a random multiplier from 0 to 1000!")
                embedvar.add_field(name="Here is how to use it",value="`-bet revup <amount to bet> <num of goes>`",inline=False)
                await message.channel.send(embed=embedvar)

            if message.content.startswith("-h bet dubup"):  # GAMES
                embedvar = discord.Embed(title="BET DUBUP HELP:",description="The rev up double up command is a \
                betting game where you get 2 multipliers that could get you up to 40000X!")
                embedvar.add_field(name="Here is how to use it",value="`-bet dubup <amount to bet> <num of goes>`",inline=False)
                await message.channel.send(embed=embedvar)

            if message.content.startswith("-h bet crash"):  # GAMES
                embedvar = discord.Embed(title="BET CRASH HELP:",description="The crash command is a \
                betting game where chose when you pull out of the game and keep your winnings!")
                embedvar.add_field(name="Here is how to use it",value="`-bet crash <amount to bet>`",inline=False)
                await message.channel.send(embed=embedvar)

            # admin help
            if message.content.startswith("-h purge"):  #ONLINE SEARCHING
                embedvar = discord.Embed(title="PURGE HELP:",description="The purge command deletes x number of messages")
                embedvar.add_field(name="Here is how to use it",value="`-purge x`\n x = is the number of messages to delete",inline=False)
                await message.channel.send(embed=embedvar)

        # randoms #commands begin
        if message.content.startswith("-randword"):
            n = int(message.content[10:])
            allowcmd = 0
            if n > 1:
                if n > 100:
                    embedvar = discord.Embed(title="Number over max word limit!", description="There is a 100 words limit")
                    embedvar.set_footer(text="Requested by {}".format(message.author))
                    await message.channel.send(embed=embedvar)
                    allowcmd = 1
                else:
                    lookup = str(message.author.id)
                    with open('settings/coin.txt') as myFile:
                        for line in myFile:
                            if lookup in line:
                                import decimal
                                balance = decimal.Decimal(line[20:])
                                balance = balance / 20
                                head, sep, tail = str(balance).partition('.')
                    if n > int(head):
                        embedvar = discord.Embed(title="Number over word limit!", description="There is a {} words limit,\
                        increase this by getting more coins by playing games! do `-help games` to see the games list".format(head))
                        embedvar.set_footer(text="Requested by {}".format(message.author))
                        await message.channel.send(embed=embedvar)
                        allowcmd = 1
            if n < 1:
                await message.channel.send("```The minimum words is 1!```")
                allowcmd = 1
            if not allowcmd == 1:
                from nltk.corpus import words
                from random import sample
                rand_words = ' '.join(sample(words.words(),n))
                embedvar = discord.Embed(title="Random words:",description=rand_words)
                embedvar.set_footer(text="Requested by {}".format(message.author))
                await message.channel.send(embed=embedvar)

        if message.content.startswith("-randnumber"):
            n = message.content[12:]
            n1 = n.split()
            from random import randint
            outputn = random.randint(int(n1[0]),int(n1[1]))
            string = "Your random number between {} and {} is:".format(int(n1[0]),int(n1[1]))
            embedvar = discord.Embed(title=string,description=outputn)
            embedvar.set_footer(text="Requested by {}".format(message.author))
            await message.channel.send(embed=embedvar)

        if message.content.startswith("-randuni"):
            alphaamount = int(message.content[9:])
            allowcmd = 0
            if alphaamount > 1:
                if alphaamount > 500:
                    embedvar = discord.Embed(title="Number over max char limit!", description="There is a 500 char limit")
                    embedvar.set_footer(text="Requested by {}".format(message.author))
                    await message.channel.send(embed=embedvar)
                    allowcmd = 1
                else:
                    lookup = str(message.author.id)
                    with open('settings/coin.txt') as myFile:
                        for line in myFile:
                            if lookup in line:
                                import decimal
                                balance = decimal.Decimal(line[20:])
                                balance = balance / 10
                                head, sep, tail = str(balance).partition('.')
                    if alphaamount > int(head):
                        embedvar = discord.Embed(title="Number over limit char limit!", description="There is a {} char limit,\
                        increase this by getting more coins by playing games! do `-help games` to see the games list".format(head))
                        embedvar.set_footer(text="Requested by {}".format(message.author))
                        await message.channel.send(embed=embedvar)
                        allowcmd = 1
            if alphaamount < 1:
                await message.channel.send("```The minimum char amount is 1!```")
                allowcmd = 1
            if not allowcmd == 1:
                def get_random_unicode(length):
                    get_char = chr

                    # Update this to include code point ranges to be sampled
                    include_ranges = [
                        (0x0021,0x0021),
                        (0x0023,0x0026),
                        (0x0028,0x007E),
                        (0x00A1,0x00AC),
                        (0x00AE,0x00FF),
                        (0x0100,0x017F),
                        (0x0180,0x024F),
                        (0x2C60,0x2C7F),
                        (0x16A0,0x16F0),
                        (0x0370,0x0377),
                        (0x037A,0x037E),
                        (0x0384,0x038A),
                        (0x038C,0x038C),
                    ]

                    alphabet = [
                        get_char(code_point) for current_range in include_ranges
                        for code_point in range(current_range[0],current_range[1] + 1)
                    ]
                    return ''.join(random.choice(alphabet) for i in range(length))

                if __name__ == '__main__':
                    time.sleep(0.25)
                    string = ('A random string of {} symbols: '.format(alphaamount))
                    embedvar = discord.Embed(title=string,description=get_random_unicode(alphaamount))
                    embedvar.set_footer(text="Requested by {}".format(message.author))
                    await message.channel.send(embed=embedvar)


        if message.content.startswith("-8ball"):
            from random import randint
            choice = randint(0,20)
            if choice == 0:
                ballchoice = "It is certain."
            if choice == 1:
                ballchoice ="It is decidedly so."
            if choice == 2:
                ballchoice = "Without a doubt."
            if choice == 3:
                ballchoice = "Yes – definitely."
            if choice == 4:
                ballchoice = "You may rely on it."
            if choice == 5:
                ballchoice = "As I see it,yes."
            if choice == 6:
                ballchoice = "Most likely."
            if choice == 7:
                ballchoice = "Outlook good."
            if choice == 8:
                ballchoice = "Yes."
            if choice == 9:
                ballchoice = "Signs point to yes."
            if choice == 10:
                ballchoice = "Reply hazy,try again."
            if choice == 11:
                ballchoice = "Ask again later."
            if choice == 12:
                ballchoice = "Better not tell you now."
            if choice == 13:
                ballchoice = "Cannot predict now."
            if choice == 14:
                ballchoice = "Concentrate and ask again."
            if choice == 15:
                ballchoice = "Don’t count on it."
            if choice == 16:
                ballchoice = "My reply is no."
            if choice == 17:
                ballchoice = "My sources say no."
            if choice == 18:
                ballchoice = "Outlook not so good"
            if choice == 19:
                ballchoice = "Very doubtful"

            embedvar = discord.Embed(title=ballchoice)
            embedvar.set_footer(text="Requested by {}".format(message.author))
            await message.channel.send(embed=embedvar)

        if message.content.startswith("-leetify"):
            change = message.content[9:]
            def remove1(string):
                return string.replace("o","0").replace("O","0").replace("l","1").replace("L","1").replace("s","5") \
                .replace("S","5").replace("h","8").replace("H","8").replace("e","3").replace("E","3") \
                .replace("i","1").replace("I","1")
            change2 = remove1(change)

            embedvar = discord.Embed(title="Leetified text:",description=change2)
            embedvar.set_footer(text="Requested by {}".format(message.author))
            await message.channel.send(embed=embedvar)

        #rand message responses

        if message.content.startswith("-repeat"):
            embedvar = discord.Embed(description=(message.content[8:48]))
            embedvar.set_footer(text="Requested by {}".format(message.author))
            await message.channel.send(embed=embedvar)

        if message.content.startswith("-joke"):
            import requests

            headers = {
                'Accept': 'text/plain',
            }

            response = requests.get('https://icanhazdadjoke.com/',headers=headers)
            embedvar = discord.Embed(title="Here is your joke",description=response.text)
            embedvar.set_footer(text="Requested by {}".format(message.author))
            await message.channel.send(embed=embedvar)

        if message.content.startswith("-feedback"):
            from discord_webhook import DiscordWebhook, DiscordEmbed
            webhook = DiscordWebhook(url='https://discordapp.com/api/webhooks/747165074904318072/v5A6INiySC90Y4XoVOoTx9h_vJBitAWsYBhyGBnkkrjCHcU06eG-bA3o_hG5PQYhTtI_')
            embed = DiscordEmbed(title="Feedback from user {}/{}".format(message.author, message.author.id),description="Submitted from {}/{}".format(message.channel, message.channel.id))
            embed.add_embed_field(name="Feedback", value="{}".format(message.content[10:]))
            webhook.add_embed(embed)
            webhook.execute()

            embedvar = discord.Embed(description="Feedback submitted, thank you for your time")
            embedvar.set_footer(text="Requested by {}".format(message.author))
            await message.channel.send(embed=embedvar)

        if message.content.startswith("-char count"):
            str1 = message.content[12:]
            total = 0

            for i in str1:
                total = total + 1

            embedvar = discord.Embed(title="Total Number of Characters in this String = {}".format(total))
            embedvar.set_footer(text="Requested by {}".format(message.author))
            await message.channel.send(embed=embedvar)

        if message.content.startswith("-large text"):
            str1 = message.content[12:]

            string = ""
            for i in str1:
                if i == " ":
                    string = string + ":black_large_square:"
                else:
                    string = string + ":regional_indicator_{}:".format(i)

            await message.channel.send(string)
            embedvar = discord.Embed(description=string)
            embedvar.set_footer(text="Requested by {}".format(message.author))
            await message.channel.send(embed=embedvar)

        if message.content.startswith("-ttb"):
            import cleverbotfreeapi
            send = cleverbotfreeapi.cleverbot(message.content[5:])
            await message.channel.send(send)

        # bot info section

        if message.content.startswith("-botinv"):
            embedvar = discord.Embed(title="Wanna invite this bot to another server? Great!", description="\
            [Click to add bot to your server](https://discord.com/oauth2/authorize?client_id=711578412103368707&scope=bot&permissions=8)")
            embedvar.set_footer(text="Requested by {}".format(message.author))
            await message.channel.send(embed=embedvar)

        if message.content.startswith("-botweb"):
            embedvar = discord.Embed(title="Wanna see the bots website? Great! Here is the link you will need:\
            https://rapidslayer101.wixsite.com/rapidbot")
            embedvar.set_footer(text="Requested by {}".format(message.author))
            await message.channel.send(embed=embedvar)

        if message.content.startswith("-botrt"):
            if (time.time() - startt) < 60:
                startx = "%s seconds" % (time.time() - startt)
            if (time.time() - startt) > 60:
                startx = "%s mins" % ((time.time() - startt) / 60)
            if (time.time() - startt) > 3600:
                startx = "%s hours" % ((time.time() - startt) / 60 / 60)
            embedvar = discord.Embed(description="The bot has been running for: \n{}\n\nIt was started/restarted at: \n{}".format(startx,startr))
            embedvar.set_footer(text="Requested by {}".format(message.author))
            await message.channel.send(embed=embedvar)

        if message.content.startswith("-ping"):
            rtimepong = str(rtime)
            rtimepong2 = (rtimepong[17:])
            msg = await message.channel.send("pong")
            pongtime = str(datetime.datetime.now())
            ptime = pongtime[17:]
            pongping = float(ptime) - float(rtimepong2)
            pongping2 = str(pongping)
            string = "pong,{}s respone time, FROM PY BOT".format(pongping2[:10])
            await msg.edit(content=string)

        if message.content.startswith("-inservers"):
            embedvar = discord.Embed(title="I'm in " + str(len(client.guilds)) + " servers")
            embedvar.set_footer(text="Requested by {}".format(message.author))
            await message.channel.send(embed=embedvar)

        #messages and ids
        if message.content.startswith("-thischat links"):
            counter = 0
            linksfound = 0
            requestedby = message.author
            msg3 = await message.channel.send("Processing messages")
            with open('strs/edits/chatmsg-onlylinks-{}.txt'.format(message.channel.id), 'w', encoding='utf-8') as rmdup:
                async for message in message.channel.history(limit=10000):
                    a = (re.findall(r'(https?://[^\s]+)', str(message.content)))
                    b = (re.findall(r'(http?://[^\s]+)', str(message.content)))
                    if not str(a) == "[]":
                        linksfound = linksfound + 1
                        rmdup.write(str(a)+"\n")
                    if not str(b) == "[]":
                        linksfound = linksfound + 1
                        rmdup.write(str(b)+"\n")
                    if counter % 250 == 0:
                        await msg3.edit(content="Processed {} messages".format(counter))
                    if counter == 10000:
                        await msg3.edit(content="Processed {} messages, You hit the 100k messages processing limit!\
                        any messages further back than 100k have not be included in the text file below".format(counter))
                    counter += 1
                    message.content = ""
                rmdup.close()
                await msg3.edit(content="Processed {} messages".format(counter))
                embedvar = discord.Embed(title="Here is this chats entire link history, total {} links".format(linksfound))
                embedvar.set_footer(text="Requested by {}".format(requestedby))
                await message.channel.send(embed=embedvar)
                await message.channel.send(file=discord.File('strs/edits/chatmsg-onlylinks-{}.txt'.format(message.channel.id)))

        if message.content.startswith("-userid"):
            userget = message.content[8:]
            send = 'The user/role ID for {} is: {}'.format(userget,userget[3:21])
            await message.channel.send(send)

        if message.content.startswith("-serverid"):
            send = 'The ID for {} (this server) is: {}\n\nTo get to this server online copy this link: \ndiscord.com/channels/{}'.format(message.guild,message.guild.id,message.guild.id)
            await message.channel.send(send)

        if message.content.startswith("-channelid"):
            send = 'The ID for {} (this channel) is: {}\n\nTo get to this channel online copy this link: \ndiscord.com/channels/{}/{}'.format(message.channel,message.channel.id,message.guild.id,message.channel.id)
            await message.channel.send(send)

        if message.content.startswith("-messageid"):
            send = 'The ID for the message you sent made output is: {}\n\nTo get to this message online copy this link: \ndiscord.com/channels/{}/{}/{}'.format(message.id,message.guild.id,message.channel.id,message.id)
            await message.channel.send(send)

        if message.content.startswith("-members"):
            e4 = ""
            a5 = 0
            for item in message.guild.members:
                e4 = e4 + "\n" + "<@!" + str(item.id) + ">"
                a5 = a5 + 1
            embedvar = discord.Embed(title="Member count: {}".format(a5),description=str(e4))
            embedvar.set_footer(text="Requested by {}".format(message.author))
            await message.channel.send(embed=embedvar)

        if message.content.startswith("-roles"):
            e4 = ""
            rolecount = 0
            a5 = 0
            for item in message.guild.roles:
                e4 = e4 + "\n" + "<@&" + str(item.id) + ">"
                a5 = a5 + 1
                rolecount = rolecount + 1
            embedvar = discord.Embed(title="Role count: {}".format(rolecount),description=str(e4))
            embedvar.set_footer(text="Requested by {}".format(message.author))
            await message.channel.send(embed=embedvar)

        if message.content.startswith("-inrole"):
            rolecheck1 = message.content[11:]
            def remmove(string):
                return string.replace(">", "")
            rolecheck = remmove(rolecheck1)
            withrolenum = 0
            e4 = ""
            for item in message.guild.members:
                if str(rolecheck) in str(message.guild.get_member(item.id).roles):
                    e4 = e4 + "\n" + "<@!" + str(item.id) + ">"
                    withrolenum = withrolenum + 1
            embedvar = discord.Embed(title="Members with role {}: {}".format(message.guild.get_role(int(rolecheck)), withrolenum), description=str(e4))
            embedvar.set_footer(text="Requested by {}".format(message.author))
            await message.channel.send(embed=embedvar)

        #if message.content.startswith("-whois"):
            #for item in message.guild.members:
                #print(item.id)

        # currency section and maths (3)

        if message.content.startswith("-currency list"):
            values = (message.content[15:18])
            from forex_python.converter import CurrencyRates
            c = CurrencyRates()
            currencylistinput = c.get_rates(values)
            stuff_in_string = "```glsl\n#{}\n\n#Requested by {}```".format(currencylistinput,message.author)
            await message.channel.send(stuff_in_string)

        if message.content.startswith("-currency convert"):
            from forex_python.converter import CurrencyRates
            from forex_python.converter import CurrencyCodes
            c = CurrencyRates()
            d = CurrencyCodes()
            values = (message.content[18:21])
            values2 = (message.content[22:25])
            values3 = float(message.content[26:])
            output2 = d.get_symbol(values2)
            output = c.convert(values,values2,values3)
            embedvar = discord.Embed(title="Here is the value in {}: {}{}".format(values2,output2,output))
            embedvar.set_footer(text="Requested by {}".format(message.author))
            await message.channel.send(embed=embedvar)

        # colours

        if message.content.startswith("-redtext"):
            redinput = (message.content[9:])
            stuff_in_string = "```diff\n- {}\n\nRequested by {}```".format(redinput,message.author)
            await message.channel.send(stuff_in_string)

        if message.content.startswith("-orangetext"):
            orangeinput = (message.content[12:])
            stuff_in_string = "```glsl\n#{}\n\nRequested by {}```".format(orangeinput,message.author)
            await message.channel.send(stuff_in_string)

        if message.content.startswith("-greentext"):
            greeninput = (message.content[11:])
            stuff_in_string = "```css\n {}\n\nRequested by {}```".format(greeninput,message.author)
            await message.channel.send(stuff_in_string)

        if message.content.startswith("-yellowtext"):
            yellowinput = (message.content[12:])
            stuff_in_string = "```fix\n {}\n\nRequested by {}```".format(yellowinput,message.author)
            await message.channel.send(stuff_in_string)

        if message.content.startswith("-bluetext"):
            blueinput = (message.content[10:])
            stuff_in_string = "```css\n.{}\n\nRequested by {}```".format(blueinput,message.author)
            await message.channel.send(stuff_in_string)

        if message.content.startswith("-cyantext"):
            cyaninput = (message.content[10:])
            stuff_in_string = "```xl\n'{}\n\nRequested by {}```".format(cyaninput,message.author)
            await message.channel.send(stuff_in_string)

        # N S F W

        if message.content.startswith("-nsfw enable"):
            with open('settings/nsfw.txt','r') as f:
                isin = '{}'.format(f.read())
                if isin.find(str(message.channel.id)) > -1:
                    await message.channel.send("```NSFW is already enabled in this channel```")
                else:
                    if discord.utils.get(message.author.roles, name="admin") or discord.utils.get(message.author.roles, name="Admin") \
                        or discord.utils.get(message.author.roles, name="administrator") or discord.utils.get(message.author.roles, name="Administrator"):
                        with open('settings/nsfw.txt','a') as f:
                            f.write(str(message.channel.id) + '\n')
                            await message.channel.send("```NSFW is now enabled for this channel```")
                    else:
                        await message.channel.send("```You cannot turn on NSFW as\nyou do not have the admin role\n\nIf you are an admin in this server \ngive yourself the role admin\n\nIf your not and admin then ask an admin\nto turn nsfw on```")

        if message.content.startswith("-nsfw disable"):
            if discord.utils.get(message.author.roles,name="admin") or discord.utils.get(message.author.roles,name="Admin"):
                lists = []
                putin = '{}'.format(message.channel.id)
                lists.append(putin)
                bad_words = lists
                with open('settings/nsfw.txt') as oldfile,open('settings/nsfw.txt'.format(message.channel.id),'w') as newfile:
                    for line in oldfile:
                        if any(bad_word in line for bad_word in bad_words):
                            newfile.write(line)
                    await message.channel.send("```If NSFW was enabled before it now wont be```")

        if message.content.startswith("-porntags"):
            embedvar = discord.Embed(title="porntags HELP:",description="suggested tags that can be used with the many nsfw search commands")
            embedvar.add_field(name="Tags",value="`69`,`Amateur`,`Anal`,`Animated`,`Asian`,`Ass`,`Bbc`,`Bbw`,`Bdsm`,`Big Ass`,`Big Dick`,`Big Tits`,`Blonde`,`Blowjob`,`Bondage`,`Boobs`\
            `Caption`,`Cartoon`,`Cheating`,`Cosplay`,`Cowgirl`,`Creampie`,`Cuckold`,`Cum`,`Cumshot`,`Deepthroat`,`Dildo`,`Doggystyle`,`Dp`,`Ebony`,\
            `Feet`,`Ffm`,`Fingering`,`Foursome`,`Fuck`,`Funny`,`Handjob`",inline=False)
            embedvar.set_footer(text="Requested by {}".format(message.author))
            await message.channel.send(embed=embedvar)

        if message.content.startswith("-phs"):
            with open('settings/nsfw.txt','r') as f:
                isin = '{}'.format(f.read())
                if isin.find(str(message.channel.id)) > -1:
                    from pornhub_api import PornhubApi
                    api = PornhubApi()
                    from pornhub_api.backends.aiohttp import AioHttpBackend

                    async def execute():
                        backend = AioHttpBackend()
                        api = PornhubApi(backend=backend)

                        await backend.close()

                    search = message.content[7:]
                    data = api.search.search("{}".format(search),ordering="mostviewed",period="weekly")
                    limit = int(message.content[5:7])

                    if limit > 20:
                        await message.channel.send("```You cant have more than 20 searches per phs search!```")
                    else:
                        for vid in data.videos:
                            send = "https://www.pornhub.com/view_video.php?viewkey={}".format(vid.video_id)
                            await message.channel.send(send)
                            time.sleep(4)
                            limit = limit - 1
                            if limit == 0:
                                break
                else:
                    await message.channel.send("```NSFW is not enabled in this chat\n To enable it you must have role admin\n then type -nsfw enable```")

        if message.content.startswith("-psi"):
            with open('settings/nsfw.txt', 'r') as f:
                isin = '{}'.format(f.read())
                if isin.find(str(message.channel.id)) > -1:
                    import urllib.request, re
                    pagesearch = ('https://www.pornpics.com/?q={}/'.format(message.content[5:]))

                    def remove10(string):
                        return string.replace(" ", "+")

                    pagesearch2 = remove10(pagesearch)
                    page = urllib.request.urlopen(pagesearch2)
                    a = (re.findall(r'(https?://[^\s]+)', str(page.read())))
                    b = (re.findall(r'(http?://[^\s]+)', str(page.read())))
                    c = ('\n'.join(a))
                    d = ('\n'.join(b))
                    e = c + d

                    def remove(string):
                        return string.replace("\\n", "")

                    def remove1(string):
                        return string.replace("'", "")

                    def remove2(string):
                        return string.replace("\"", "")

                    e1 = remove(e)
                    e2 = remove1(e1)
                    e3 = remove2(e2)
                    e4 = e3.split()
                    e5 = e4[26:]
                    imgsent = 0
                    for imgn in range(200):
                        e6 = ''.join(e5[imgn:imgn + 1])
                        if 'https://cdni.pornpics.com' in e6:
                            embedvar = discord.Embed()
                            embedvar.set_image(url=e6[:-1])
                            embedvar.set_footer(text="Requested by {}".format(message.author))
                            await message.channel.send(embed=embedvar)
                            time.sleep(2)
                            imgsent = imgsent + 1
                        if 'https://img.pornpics.com' in e6:
                            embedvar = discord.Embed()
                            embedvar.set_image(url=e6[:-1])
                            embedvar.set_footer(text="Requested by {}".format(message.author))
                            await message.channel.send(embed=embedvar)
                            time.sleep(2)
                            imgsent = imgsent + 1
                        if 'https://images.pornpics.com' in e6:
                            embedvar = discord.Embed()
                            embedvar.set_image(url=e6[:-1])
                            embedvar.set_footer(text="Requested by {}".format(message.author))
                            await message.channel.send(embed=embedvar)
                            time.sleep(2)
                            imgsent = imgsent + 1
                        if imgn == 199:
                            if imgsent > 0:
                                string = "```diff\nWant more {}? Try some galleries!\n-psg 1 {}\n\nWant something else?\nTry another -psi search```".format(message.content[5:], message.content[5:])
                                await message.channel.send(string)
                            else:
                                await message.channel.send("```OH NO! There was no results for your search! try another search```")

                else:
                    await message.channel.send("```NSFW is not enabled in this chat\n To enable it you must have role admin\n then type -nsfw enable```")

        if message.content.startswith("-psg"):
            with open('settings/nsfw.txt','r') as f:
                isin = '{}'.format(f.read())
                if isin.find(str(message.channel.id)) > -1:
                    global choicesz,choiceszz
                    choicesz = str(message.content[5:7])
                    def remove12(string):
                        return string.replace(" ","")
                    choiceszz = remove12(choicesz)
                    import urllib.request,re
                    pagesearch = ('https://www.pornpics.com/?q={}/'.format(message.content[7:]))
                    def remove10(string):
                        return string.replace(" ","+")
                    pagesearch2 = remove10(pagesearch)
                    page = urllib.request.urlopen(pagesearch2)
                    a = (re.findall(r'(https?://[^\s]+)',str(page.read())))
                    b = (re.findall(r'(http?://[^\s]+)',str(page.read())))
                    c = ('\n'.join(a))
                    d = ('\n'.join(b))
                    e = c+d
                    def remove(string):
                        return string.replace("\\n", "").replace("'", "").replace("\"", "")
                    e1 = remove(e)
                    e4 = e1.split()
                    e5 = e4[26:]
                    global PRNN
                    PRNN = 0
                    for imgn in range(200):
                        e6 = ''.join(e5[imgn:imgn+1])
                        if 'https://www.pornpics.com/galleries/' in e6[:-1]:
                            PRNN = PRNN + 1
                            if str(PRNN) == (choiceszz):
                                import urllib.request,re
                                pagesearch3 = ('{}'.format(e6[:-1]))
                                def remove10(string):
                                    return string.replace(" ","+")
                                pagesearch4 = remove10(pagesearch3)
                                page = urllib.request.urlopen(pagesearch4)
                                a = (re.findall(r'(https?://[^\s]+)',str(page.read())))
                                b = (re.findall(r'(http?://[^\s]+)',str(page.read())))
                                c = ('\n'.join(a))
                                d = ('\n'.join(b))
                                e = c + d
                                def remove(string):
                                    return string.replace("\\n", "").replace("'", "").replace("\"", "")
                                e1 = remove(e)
                                e4 = e1.split()
                                e5 = e4[26:]
                                for imgn in range(200):
                                    e6 = ''.join(e5[imgn:imgn + 1])
                                    if 'https://cdni.pornpics.com/1280' in e6:
                                        embedvar = discord.Embed()
                                        embedvar.set_image(url=e6[:-1])
                                        embedvar.set_footer(text="Requested by {}".format(message.author))
                                        await message.channel.send(embed=embedvar)
                                        time.sleep(2)
                                    if 'https://img.pornpics.com/460' in e6:
                                        embedvar = discord.Embed()
                                        embedvar.set_image(url=e6[:-1])
                                        embedvar.set_footer(text="Requested by {}".format(message.author))
                                        await message.channel.send(embed=embedvar)
                                        time.sleep(2)
                                    if 'https://images.pornpics.com/1280' in e6:
                                        embedvar = discord.Embed()
                                        embedvar.set_image(url=e6[:-1])
                                        embedvar.set_footer(text="Requested by {}".format(message.author))
                                        await message.channel.send(embed=embedvar)
                                        time.sleep(2)
                                    if imgn == 199:
                                        pgnum = message.content[5:7]
                                        def remove13(string):
                                            return string.replace(" ", "")
                                        pgnum2 = remove13(pgnum)
                                        pgnum3 = int(pgnum) + 1
                                        string = "```diff\nWant even more?! try this command\n-psg {} {}\n\nWant something else?\nTry another -psi search```".format(
                                            pgnum3, message.content[7:])
                                        def remove14(string):
                                            return string.replace("  ", " ")
                                        string2 = remove14(string)
                                        await message.channel.send(string2)
                                else:
                                    await message.channel.send("```NSFW is not enabled in this chat\n To enable it you must have role admin\n then type -nsfw enable```")

        if message.content.startswith("-porngif"):
            with open('settings/nsfw.txt','r') as f:
                isin = '{}'.format(f.read())
                if isin.find(str(message.channel.id)) > -1:
                    import urllib.request,re
                    def remove2(string):
                        return string.replace(" ","")
                    pgsearch = message.content[10:]
                    pagen = remove2(message.content[9:11])
                    pagesearch = 'https://www.pornhub.com/gifs/search?search={}&page={}'.format(pgsearch,pagen)
                    def remove10(string):
                        return string.replace(" ","+")
                    pagesearch2 = remove10(pagesearch)
                    page = urllib.request.urlopen(pagesearch2)
                    a = (re.findall(r'(data-mp4[^\s]+)',str(page.read())))
                    b = (re.findall(r'(https://cl.phncdn.com/pics/gifs/[^\s]+)',str(page.read())))
                    c = ('\n'.join(a))
                    d = ('\n'.join(b))
                    e = c+d
                    def remove(string):
                        return string.replace("<span","").replace("\"","").replace(">","").replace("\\","")
                    e1 = remove(e)
                    e4 = e1.split()
                    e5 = e4[9:]

                    imgsent = 0
                    for imgn in range(200):
                        e6 = ''.join(e5[imgn:imgn+1])
                        print(e6)
                        if 'https://cl.phncdn.com/pics/gifs/' or 'https://dl.phncdn.com/pics/gifs/' in e6:
                            edit = e6[65:66]
                            def remove2(string):
                                return string.replace("<", "").replace("n", "").replace("t", "").replace("a","")
                            e7edit = remove2(edit)
                            e7 = e6[9:65] + e7edit
                            await message.channel.send(e7)
                            print(e7)

                            e7edit = e7[44:52]
                            e7edit2 = remove2(e7edit)
                            import urllib.request, re
                            pagesearch3 = ('https://www.pornhub.com/gif/{}'.format(e7edit2))

                            def remove10(string):
                                return string.replace(" ", "+")

                            pagesearch4 = remove10(pagesearch3)
                            page = urllib.request.urlopen(pagesearch4)
                            a = (re.findall(r'(href="/view_video.php[^\s]+)', str(page.read())))
                            b = (re.findall(r'(href="/view_video.php[^\s]+)', str(page.read())))
                            c = ('\n'.join(a))
                            d = ('\n'.join(b))
                            e = c + d
                            def remove(string):
                                return string.replace("\\n", "").replace("'", "").replace("\"", "")
                            e1 = remove(e)
                            e4 = e1.split()
                            for imgn1 in range(200):
                                e6 = ''.join(e4[imgn1:imgn1 + 1])
                                if 'href=/view_video.php?viewkey=' in e6:
                                    if '&amp;t=' in e6:
                                        e7 = e6[:45]
                                        e8 = e7[5:]
                                        finale = "https://www.pornhub.com" + e8
                                        embedvar = discord.Embed(title="Full video link: {}".format(finale))
                                        embedvar.set_footer(text="Requested by {}".format(message.author))
                                        await message.channel.send(embed=embedvar)

                            time.sleep(4)
                            imgsent = imgsent + 1

                        if imgn == 199:
                                def remove13(string):
                                    return string.replace(" ","")
                                pgnum2 = remove13(pagen)
                                pgnum3 = int(pgnum2) + 1
                                string = "```diff\nWant more? Type this command:\n-porngif {} {}```".format(pgnum3,pgsearch)
                                await message.channel.send(string)
                                time.sleep(3)
                else:
                    await message.channel.send("```NSFW is not enabled in this chat\n To enable it you must have role admin\n then type -nsfw enable```")

        if message.content.startswith("-hentai"):
            with open('settings/nsfw.txt','r') as f:
                isin = '{}'.format(f.read())
                if isin.find(str(message.channel.id)) > -1:
                    import urllib.request,re
                    def remove2(string):
                        return string.replace(" ","")
                    hensearch = remove2(message.content[10:])
                    pagesearch = 'https://konachan.com/post?page={}&tags=uncensored+nude+{}'.format(message.content[8:10],hensearch)
                    def remove10(string):
                        return string.replace(" ","+")
                    pagesearch2 = remove10(pagesearch)
                    page = urllib.request.urlopen(pagesearch2)
                    a = (re.findall(r'(https?://[^\s]+)',str(page.read())))
                    b = (re.findall(r'(http?://[^\s]+)',str(page.read())))
                    c = ('\n'.join(a))
                    d = ('\n'.join(b))
                    e = c+d
                    def remove(string):
                        return string.replace("<span", "").replace("\"", "").replace(">", "")
                    e1 = remove(e)
                    e4 = e1.split()
                    e5 = e4[9:]
                    imgsent = 0
                    for imgn in range(200):
                        e6 = ''.join(e5[imgn:imgn + 1])
                        if 'https://konachan.com/jpeg/' in e6:
                            embedvar = discord.Embed()
                            embedvar.set_image(url=e6)
                            embedvar.set_footer(text="Requested by {}".format(message.author))
                            await message.channel.send(embed=embedvar)
                            time.sleep(3)
                            imgsent = imgsent + 1
                        if 'https://konachan.com/image/' in e6:
                            embedvar = discord.Embed()
                            embedvar.set_image(url=e6)
                            embedvar.set_footer(text="Requested by {}".format(message.author))
                            await message.channel.send(embed=embedvar)
                            time.sleep(3)
                            imgsent = imgsent + 1
                        if imgn == 199:
                            pgnum = message.content[8:10]

                            def remove13(string):
                                return string.replace(" ", "")

                            pgnum2 = remove13(pgnum)
                            pgnum3 = int(pgnum2) + 1
                            if imgsent > 0:
                                string = "```diff\nWant more? Type this command:\n-hentai {} {}```".format(pgnum3,
                                                                                                           hensearch)
                                await message.channel.send(string)
                            else:
                                await message.channel.send(
                                    "```OH NO! There was no results for your search! try another search```")
                    else:
                        await message.channel.send(
                            "```NSFW is not enabled in this chat\n To enable it you must have role admin\n then type -nsfw enable```")

        # ONLINE SEARCHING

        if message.content.startswith("-gg"):
            if message.content.startswith("-ggt codes"):
                embedvar = discord.Embed(title="Here are the language codes:",description=str(googletrans.LANGCODES))
                embedvar.set_footer(text="Requested by {}".format(message.author))
                await message.channel.send(embed=embedvar)

            if message.content.startswith("-ggt te"):
                from googletrans import Translator
                values4 = (message.content[8:])

                translator = Translator()
                translated = translator.translate(values4)
                embedvar = discord.Embed(title="Translated text:",description=translated.text)
                embedvar.set_footer(text="Requested by {}".format(message.author))
                await message.channel.send(embed=embedvar)

            if message.content.startswith("-ggt ft"):
                from googletrans import Translator
                inputla = (message.content[8:10])
                outputla = (message.content[11:13])
                values5 = (message.content[14:])

                translator = Translator()
                translated = translator.translate(values5,src=inputla,dest=outputla)
                embedvar = discord.Embed(title="Translated text:",description=translated.text)
                embedvar.set_footer(text="Requested by {}".format(message.author))
                await message.channel.send(embed=embedvar)

            if message.content.startswith("-ggsr"):
                embedvar = discord.Embed(description="Below results requested by {}".format(message.author))
                await message.channel.send(embed=embedvar)
                from googlesearch import search
                values6 = int(message.content[6:8])
                values5 = (message.content[8:])
                query = values5
                if values6 > 10:
                    await message.channel.send("```Sorry there is a message limit to reduce spam \nTry a number less than 11```")
                else:
                    for j in search(query,tld="co.in",num=values6,stop=values6,pause=2):
                        await message.channel.send(j)

            if message.content.startswith("-ggsi"):
                embedvar = discord.Embed(description="Below results requested by {}".format(message.author))
                await message.channel.send(embed=embedvar)
                from googlesearch import search_images
                values6 = int(message.content[6:8])
                values5 = (message.content[8:])
                query = values5

                if values6 > 10:
                    await message.channel.send("```Sorry there is a message limit to reduce spam \nTry a number less than 11```")
                else:
                    for j in search_images(query,tld="co.in",num=values6,stop=values6,pause=2):
                        await message.channel.send(j)

            if message.content.startswith("-ggsv"):
                embedvar = discord.Embed(description="Below results requested by {}".format(message.author))
                await message.channel.send(embed=embedvar)
                from googlesearch import search_videos
                values6 = int(message.content[6:8])
                values5 = (message.content[8:])
                query = values5

                if values6 > 10:
                    await message.channel.send("```Sorry there is a message limit to reduce spam \nTry a number less than 11```")
                else:
                    for j in search_videos(query,tld="co.in",num=values6,stop=values6,pause=2):
                        await message.channel.send(j)

        if message.content.startswith("-reddits"):
            import praw
            redditall = message.content[9:]
            redditall = redditall.split()
            subreddit = redditall[0]
            postnum = redditall[1]
            reddit = praw.Reddit(client_id='RuvVgZ-jMqw9lw', client_secret='tj4cbJuTKAum0ZszB_DJwY5cFjo',user_agent='Reddit webscraper')
            hot_posts = reddit.subreddit(subreddit).hot(limit=int(postnum))
            postcurrent = 0
            type = 0
            for post in hot_posts:
                postcurrent = postcurrent + 1
                if postcurrent == int(postnum):
                    if "redgifs.com/" in str(post.url):
                        embedvar = discord.Embed(description="Below result Requested by {}".format(message.author))
                        await message.channel.send(embed=embedvar)
                        await message.channel.send(str(post.url)+"/")
                        break
                        type = 1
                    if "https://i.imgur.com/" in str(post.url):
                        embedvar = discord.Embed(description="Below result Requested by {}".format(message.author))
                        await message.channel.send(embed=embedvar)
                        await message.channel.send(str(post.url)+"/")
                        break
                        type = 1
                    if not type == 1:
                        embedvar = discord.Embed(description="[Click to go to post]({})".format(post.url))
                        embedvar.set_image(url=post.url)
                        embedvar.set_footer(text="Requested by {}".format(message.author))
                        await message.channel.send(embed=embedvar)
                        break

        if message.content.startswith("-meme"):
            import praw
            reddit = praw.Reddit(client_id='RuvVgZ-jMqw9lw', client_secret='tj4cbJuTKAum0ZszB_DJwY5cFjo',user_agent='Reddit webscraper')
            postnum = randint(1,250)
            hot_posts = reddit.subreddit('dankmemes').hot(limit=postnum)
            postcurrent = 0
            for post in hot_posts:
                postcurrent = postcurrent + 1
                if postcurrent == postnum:
                    print(post.url)
                    embedvar = discord.Embed()
                    embedvar.set_image(url=post.url)
                    embedvar.set_footer(text="Requested by {}".format(message.author))
                    await message.channel.send(embed=embedvar)

        #if message.content.startswith("-homepage"):
            #if discord.utils.get(message.author.roles,name="bots"):
                #print("")
            #else:
                #from selenium import webdriver
                #from selenium.webdriver.common.keys import Keys

                #browser = webdriver.Chrome()
                #browser.maximize_window()
                #browser.get('https://buff.163.com/market/?game=csgo#tab=selling&page_num=1')
                #currencyurl = browser.current_url
                #print(currencyurl)

        #if message.content.startswith("-dataharvest"):
            #import requests

            #url = (message.content[13:])
            #r = requests.get(url,allow_redirects=True)
            #print(url)

            #open('test.txt','wb').write(r.content)
            #print()
            #with open('test.txt','r') as f:
                #yes = (f.read())
                #yes1 = "```data harvest: {}```".format(yes)

        # gamble section
        if message.content.startswith("-claim token"):
            wasuserthere = 0
            lookup = str(message.content[13:])
            with open('settings/token.txt') as myFile:
                for lnum3, line in enumerate(myFile, 1):
                    if line:
                        if lookup in line:
                            reward = line[31:]
                            if not reward == "CLAIMED\n":
                                wasuserthere = wasuserthere + 1
                                with open('settings/token.txt', 'r') as file:
                                    data = file.readlines()
                                data[int(lnum3) - 1] = '{}, CLAIMED\n'.format((message.content[13:]))
                                file.close()

                                with open('settings/token.txt', 'w') as file:
                                    file.writelines(data)

                                wasuserthere1 = 0
                                lookup = str(message.author.id)
                                with open('settings/coin.txt') as myFile:
                                    for lnum2, line in enumerate(myFile, 1):
                                        if lookup in line:
                                            head, sep, tail = line[20:].partition('.')
                                            wasuserthere1 = wasuserthere1 + 1
                                            coincurrent = int(head)
                                            linenum1 = int(lnum2)
                                            coincurrent = coincurrent + int(reward)
                                            def remoove(string):
                                                return string.replace("\n","")
                                            reward = remoove(reward)
                                            embedvar = discord.Embed(description="This is a valid token for {} coins".format(reward))
                                            embedvar.set_footer(text="Requested by {}".format(message.author))
                                            await message.channel.send(embed=embedvar)

                                            with open('settings/coin.txt', 'r') as file:
                                                data = file.readlines()
                                            data[linenum1 - 1] = '{}, {}\n'.format(message.author.id, coincurrent)
                                            file.close()

                                            with open('settings/coin.txt', 'w') as file:
                                                file.writelines(data)

                                    if wasuserthere1 == 0:
                                        embedvar = discord.Embed(description="You dont have a balance yet! Dont worry i just made you one")
                                        embedvar.set_footer(text="Requested by {}".format(message.author))
                                        await message.channel.send(embed=embedvar)
                                        with open('settings/coin.txt', 'a+') as f:
                                            f.write("{}, 100 \n".format(message.author.id))

                if wasuserthere == 0:
                    if "CLAIMED" in line:
                        embedvar = discord.Embed(description="This token has already been claimed")
                        embedvar.set_footer(text="Requested by {}".format(message.author))
                        await message.channel.send(embed=embedvar)
                    else:
                        embedvar = discord.Embed(description="This is not a valid token")
                        embedvar.set_footer(text="Requested by {}".format(message.author))
                        await message.channel.send(embed=embedvar)

        if message.content.startswith("-reset coins"):
            embedvar = discord.Embed(title="WARNING THIS WILL RESET YOU BALANCE TO 10", description="Type -reset confirm to confirm this action")
            embedvar.set_footer(text="Requested by {}".format(message.author))
            await message.channel.send(embed=embedvar)

        if message.content.startswith("-reset confirm"):
            wasuserthere = 0
            lookup = str(message.author.id)
            with open('settings/resetclaims.txt') as myFile:
                for lnum, line in enumerate(myFile, 1):
                    if lookup in line:
                        import decimal
                        line20 = decimal.Decimal(line[20:])
                        wasuserthere = wasuserthere + 1
                        claimnum = line20
                        allowreset = 0
                        if int(claimnum) > 10:
                            allowreset = 1
                            embedvar = discord.Embed(description="You cant reset again you have already hit your limit of 10 resets per day")
                            embedvar.set_footer(text="Requested by {}".format(message.author))
                            await message.channel.send(embed=embedvar)
                        linenum2 = int(lnum)
                if wasuserthere == 0:
                    with open('settings/resetclaims.txt', 'a+') as f:
                        f.write("{}, 1 \n".format(message.author.id))
                else:
                    with open('settings/resetclaims.txt', 'r') as file:
                        data = file.readlines()
                    data[linenum2 - 1] = '{}, {}\n'.format(message.author.id, claimnum+1)
                    file.close()

                    with open('settings/resetclaims.txt', 'w') as file:
                        file.writelines(data)

                if not allowreset == 1:
                    wasuserthere = 0
                    lookup = str(message.author.id)
                    with open('settings/coin.txt') as myFile:
                        for lnum1, line in enumerate(myFile, 1):
                            if lookup in line:
                                head, sep, tail = line[20:].partition('.')
                                wasuserthere = wasuserthere + 1
                                linenum2 = int(lnum1)
                        if wasuserthere == 0:
                            embedvar = discord.Embed(description="You dont have a balance yet! Dont worry i just made you one with 100 coins")
                            embedvar.set_footer(text="Requested by {}".format(message.author))
                            await message.channel.send(embed=embedvar)
                            with open('settings/coin.txt', 'a+') as f:
                                f.write("{}, 100 \n".format(message.author.id))
            if not allowreset == 1:
                with open('settings/coin.txt', 'r') as file:
                    data = file.readlines()
                data[linenum2 - 1] = '{}, 10\n'.format(message.author.id)
                file.close()

                with open('settings/coin.txt', 'w') as file:
                    file.writelines(data)
                embedvar = discord.Embed(title="Your balance was just reset to 10 coins!")
                embedvar.set_footer(text="Requested by {}".format(message.author))
                await message.channel.send(embed=embedvar)

        if message.content.startswith("-bal"):
            wasuserthere = 0
            addbal = 0
            if message.content[5:] == "":
                lookup = str(message.author.id)
            else:
                lookup = message.content[8:26]
                addbal = 1
            with open('settings/coin.txt') as myFile:
                for num, line in enumerate(myFile, 1):
                    if lookup in line:
                        import decimal
                        line20 = decimal.Decimal(line[20:])
                        if not addbal == 1:
                            embedvar = discord.Embed(title="Your balance is {}".format(line20))
                            embedvar.set_footer(text="Requested by {}".format(message.author))
                            await message.channel.send(embed=embedvar)
                        else:
                            embedvar = discord.Embed(description="{} has a balance of {}".format(message.content[5:27], line20))
                            embedvar.set_footer(text="Requested by {}".format(message.author))
                            await message.channel.send(embed=embedvar)
                        wasuserthere = wasuserthere + 1
                if not addbal == 1:
                    if wasuserthere == 0:
                        embedvar = discord.Embed(description="You dont have a balance yet! Dont worry i just made you one")
                        embedvar.set_footer(text="Requested by {}".format(message.author))
                        await message.channel.send(embed=embedvar)
                        with open('settings/coin.txt', 'a+') as f:
                            f.write("{}, 100 \n".format(message.author.id))
                else:
                    if wasuserthere == 0:
                        embedvar = discord.Embed(description="This user does not have a balance yet")
                        embedvar.set_footer(text="Requested by {}".format(message.author))
                        await message.channel.send(embed=embedvar)

        #if message.content.startswith("-leaderboard"):
            #print("hi")
            #with open('settings/coin.txt') as FileName:
                #data = FileName.readlines()
                #data = str(data)
                #data[20:].sort()
                #for i in range(len(data)):
                    #print(data[i])
                    #print("2")

        if message.content.startswith("-bet"):
            global coin, linenum
            wasuserthere = 0
            lookup = str(message.author.id)
            with open('settings/coin.txt') as myFile:
                for lnum, line in enumerate(myFile, 1):
                    if lookup in line:
                        import decimal
                        line20 = decimal.Decimal(line[20:])
                        wasuserthere = wasuserthere + 1
                        coin = line20
                        linenum = int(lnum)
                if wasuserthere == 0:
                    embedvar = discord.Embed(description="You dont have a balance yet! Dont worry i just made you one")
                    embedvar.set_footer(text="Requested by {}".format(message.author))
                    await message.channel.send(embed=embedvar)
                    with open('settings/coin.txt', 'a+') as f:
                        f.write("{}, 100 \n".format(message.author.id))

            with open('settings/coin.txt', 'r') as file:
                data = file.readlines()
            data[linenum - 1] = '{}, {}\n'.format(message.author.id, coin)
            file.close()

            with open('settings/coin.txt', 'w') as file:
                file.writelines(data)

            if message.content.startswith("-bet flip"):
                headortail = message.content[10:11]
                flipbet = int(message.content[12:])
                allowbet = 0
                if flipbet > coin:
                    embedvar = discord.Embed(title="You cant bet more than you have!")
                    embedvar.set_footer(text="Requested by {}".format(message.author))
                    await message.channel.send(embed=embedvar)
                    allowbet = 1
                if flipbet < 1:
                    embedvar = discord.Embed(title="You cant bet nothing!")
                    embedvar.set_footer(text="Requested by {}".format(message.author))
                    await message.channel.send(embed=embedvar)
                    allowbet = 1
                if not allowbet == 1:
                    flipresult = random.randint(0,100)
                    if flipresult < 36:
                        coins2 = coin + flipbet
                        coin = coins2
                        if headortail == "h":
                            headortail = "heads"
                        if headortail == "t":
                            headortail = "tails"
                        embedvar = discord.Embed(title="You Won {}".format(flipbet), description="Coin landed on {} and You now have: {}".format(headortail, coin), color=discord.Colour(0x00ff00))
                        embedvar.set_footer(text="Requested by {}".format(message.author))
                        await message.channel.send(embed=embedvar)
                        with open('settings/coin.txt', 'r') as file:
                            data = file.readlines()
                        data[linenum - 1] = '{}, {}\n'.format(message.author.id, coin)
                        file.close()

                        with open('settings/coin.txt', 'w') as file:
                            file.writelines(data)

                    if flipresult > 35:
                        coins2 = coin - flipbet
                        coin = coins2
                        if headortail == "h":
                            headortail = "tails"
                        if headortail == "t":
                            headortail = "heads"
                        embedvar = discord.Embed(title="You Lost {}".format(flipbet),description="Coin landed on {} You now have: {}".format(headortail, coin),color=discord.Colour(0xff0000))
                        embedvar.set_footer(text="Requested by {}".format(message.author))
                        await message.channel.send(embed=embedvar)
                        with open('settings/coin.txt', 'r') as file:
                            data = file.readlines()
                        data[linenum - 1] = '{}, {}\n'.format(message.author.id, coin)
                        file.close()

                        with open('settings/coin.txt', 'w') as file:
                            file.writelines(data)


            if message.content.startswith("-bet bj"):
                blackjackbet = int(message.content[8:])
                blackjackmult = blackjackbet/1.5
                blackjackmult = blackjackmult.as_integer_ratio()

                allowbet = 0
                if blackjackbet > coin:
                    embedvar = discord.Embed(title="You cant bet more than you have!")
                    embedvar.set_footer(text="Requested by {}".format(message.author))
                    await message.channel.send(embed=embedvar)
                    allowbet = 1
                if blackjackbet < 1:
                    embedvar = discord.Embed(title="You cant bet nothing!")
                    embedvar.set_footer(text="Requested by {}".format(message.author))
                    await message.channel.send(embed=embedvar)
                    allowbet = 1
                if not allowbet == 1:

                    global card, card_count, bot_card_count, ace, two, three, four, bust, bustbot
                    global five, six, seven, eight, nine, ten, jack, queen, king, validation

                    bust = 0
                    bustbot = 0

                    card_count = 0
                    bot_card_count = 0
                    ace = 1
                    two = 2
                    three = 3
                    four = 4
                    five = 5
                    six = 6
                    seven = 7
                    eight = 8
                    nine = 9
                    ten = 10
                    jack = 10
                    queen = 10
                    king = 10

                    def hit():
                        card_deal = random.randint(1, 13)
                        global ace, card, card_count
                        if card_deal == 1:
                            ace = 11
                            card = ace
                        elif card_deal == 2:
                            card = two
                        elif card_deal == 3:
                            card = three
                        elif card_deal == 4:
                            card = four
                        elif card_deal == 5:
                            card = five
                        elif card_deal == 6:
                            card = six
                        elif card_deal == 7:
                            card = seven
                        elif card_deal == 8:
                            card = eight
                        elif card_deal == 9:
                            card = nine
                        else:
                            card = ten
                        card_count += card
                        if card_count > 21 and card == ace:
                            card_count -= 10
                        return card_count

                    def bot_hit():
                        card_deal = random.randint(1, 13)
                        global ace, card, bot_card_count
                        if card_deal == 1:
                            ace = 11
                            card = ace
                        elif card_deal == 2:
                            card = two
                        elif card_deal == 3:
                            card = three
                        elif card_deal == 4:
                            card = four
                        elif card_deal == 5:
                            card = five
                        elif card_deal == 6:
                            card = six
                        elif card_deal == 7:
                            card = seven
                        elif card_deal == 8:
                            card = eight
                        elif card_deal == 9:
                            card = nine
                        else:
                            card = ten
                        bot_card_count += card
                        if bot_card_count > 21 and card == ace:
                            bot_card_count -= 10
                        return bot_card_count

                    bot_first_card = bot_hit()
                    bot_total = bot_hit()
                    bot_second_card = bot_total - bot_first_card
                    first_card = hit()
                    total = hit()
                    second_card = total - first_card
                    embedvar = discord.Embed(title="Your total is: {} ({}+{})".format(total,first_card,second_card))
                    embedvar.set_footer(text="Requested by {}".format(message.author))
                    await message.channel.send(embed=embedvar)
                    while True:
                        embedvar = discord.Embed(title="Hit or stand?",description="Tick is hit, X is stand")
                        msg = await message.channel.send(embed=embedvar)
                        await msg.add_reaction('✔')
                        await msg.add_reaction('🚫')
                        channel = message.channel

                        global reaction2, user2, validation

                        def check(reaction2, user2):
                            return user2 == msg.author and str(reaction2.emoji) == '✔' or '🚫'

                        try:
                            reaction2, user2 = await client.wait_for('reaction_add', timeout=10.0, check=check)
                        except asyncio.TimeoutError:
                            await channel.send('No reaction was recieved timed out')
                        else:
                            try:
                                reaction2, user2 = await client.wait_for('reaction_add', timeout=10.0, check=check)
                            except asyncio.TimeoutError:
                                embedvar = discord.Embed(title="No reaction was recieved timed out")
                                await message.channel.send(embed=embedvar)
                            else:
                                if reaction2.emoji == '✔':
                                    validation = 1
                                if reaction2.emoji == '🚫':
                                    embedvar = discord.Embed(title="You stuck with your current cards")
                                    await message.channel.send(embed=embedvar)
                                    validation = 0

                        if validation == 1:
                            total = hit()
                            embedvar = discord.Embed(title="You hit and your new total is: {}".format(total))
                            await message.channel.send(embed=embedvar)
                            if card_count > 21:
                                embedvar = discord.Embed(title="Your bust",color=discord.Colour(0xff0000))
                                await message.channel.send(embed=embedvar)
                                bust = 1
                                validation = 0
                        if validation == 2:
                            total = hit()
                            embedvar = discord.Embed(title="You hit and your new total is: {}".format(total))
                            await message.channel.send(embed=embedvar)
                            validation = 1
                            if card_count > 21:
                                embedvar = discord.Embed(title="Your bust",color=discord.Colour(0xff0000))
                                await message.channel.send(embed=embedvar)
                                bust = 1
                        elif validation == 0:
                            break
                        else:
                            time.sleep(1)
                            pass

                    embedvar = discord.Embed(title="The bot's total is: {} ({}+{})".format(bot_total,bot_first_card, bot_second_card))
                    await message.channel.send(embed=embedvar)
                    while True:
                        if bot_card_count <= 15:
                            bot_total = bot_hit()
                            embedvar = discord.Embed(title="The bot hit and now has: {}".format(bot_total))
                            await message.channel.send(embed=embedvar)
                            if bot_total > 21:
                                embedvar = discord.Embed(title="The bot is bust", color=discord.Colour(0x00ff00))
                                await message.channel.send(embed=embedvar)
                                bustbot = 1
                        else:
                            break
                    coin = coin.as_integer_ratio()
                    embedvar = discord.Embed(title="Your final total is: {}".format(total))
                    await message.channel.send(embed=embedvar)
                    if bust == 0:
                        if bustbot == 0:
                            if bot_total > total:
                                coins2 = (coin[0]/coin[1]) - blackjackbet
                                coin = coins2
                                embedvar = discord.Embed(title="You Lost {}".format(blackjackbet),description="\
                                Your bal is now: {}".format(coin), color=discord.Colour(0xff0000))
                                await message.channel.send(embed=embedvar)
                                with open('settings/coin.txt', 'r') as file:
                                    data = file.readlines()
                                data[linenum - 1] = '{}, {}\n'.format(message.author.id, coin)
                                file.close()

                                with open('settings/coin.txt', 'w') as file:
                                    file.writelines(data)
                            elif bot_total == total:
                                embedvar = discord.Embed(title="Tie, you're money was returned", color=discord.Colour(0xffffff))
                                await message.channel.send(embed=embedvar)
                            else:
                                blackjackoutput = blackjackbet + (blackjackmult[0]/blackjackmult[1])
                                coins2 = (coin[0]/coin[1]) + blackjackbet + round(blackjackmult[0]/blackjackmult[1],2)
                                coin = coins2
                                embedvar = discord.Embed(title="You Won {}".format(round(blackjackoutput,2)), description="\
                                Your bal is now: {}".format(coin),color=discord.Colour(0x00ff00))
                                await message.channel.send(embed=embedvar)
                                with open('settings/coin.txt', 'r') as file:
                                    data = file.readlines()
                                data[linenum - 1] = '{}, {}\n'.format(message.author.id, coin)
                                file.close()

                                with open('settings/coin.txt', 'w') as file:
                                    file.writelines(data)
                        else:
                            blackjackoutput = blackjackbet + (blackjackmult[0]/blackjackmult[1])
                            coins2 = (coin[0]/coin[1]) + blackjackbet + round(blackjackmult[0]/blackjackmult[1],2)
                            coin = coins2
                            embedvar = discord.Embed(title="You Won {}".format(round(blackjackoutput,2)),description="\
                            Your bal is now: {}".format(coin), color=discord.Colour(0x00ff00))
                            await message.channel.send(embed=embedvar)
                            with open('settings/coin.txt', 'r') as file:
                                data = file.readlines()
                            data[linenum - 1] = '{}, {}\n'.format(message.author.id, coin)
                            file.close()

                            with open('settings/coin.txt', 'w') as file:
                                file.writelines(data)
                    else:
                        if bot_total > total:
                            coins2 = (coin[0]/coin[1]) - blackjackbet
                            coin = coins2
                            embedvar = discord.Embed(title="You Lost {}".format(blackjackbet), description="\
                            Your bal is now: {}".format(coin),color=discord.Colour(0xff0000))
                            await message.channel.send(embed=embedvar)
                            with open('settings/coin.txt', 'r') as file:
                                data = file.readlines()
                            data[linenum - 1] = '{}, {}\n'.format(message.author.id, coin)
                            file.close()

                            with open('settings/coin.txt', 'w') as file:
                                file.writelines(data)
                        elif bot_total == total:
                            embedvar = discord.Embed(title="Tie, you're money was returned", color=discord.Colour(0xffffff))
                            await message.channel.send(embed=embedvar)
                        else:
                            coins2 = (coin[0]/coin[1]) - blackjackbet
                            coin = coins2
                            embedvar = discord.Embed(title="You Lost {}".format(blackjackbet), description="\
                            Your bal is now: {}".format(coin),color=discord.Colour(0xff0000))
                            await message.channel.send(embed=embedvar)
                            with open('settings/coin.txt', 'r') as file:
                                data = file.readlines()
                            data[linenum - 1] = '{}, {}\n'.format(message.author.id, coin)
                            file.close()

                            with open('settings/coin.txt', 'w') as file:
                                file.writelines(data)

            if message.content.startswith("-bet dice"):
                betdicen = int(message.content[10:11])
                betdiceb = int(message.content[12:])
                betdicewin = betdiceb * 5
                allowbet = 0
                if betdiceb > coin:
                    embedvar = discord.Embed(title="You cant bet more than you have!")
                    embedvar.set_footer(text="Requested by {}".format(message.author))
                    await message.channel.send(embed=embedvar)
                    allowbet = 1
                if betdiceb < 1:
                    embedvar = discord.Embed(title="You cant bet nothing!")
                    embedvar.set_footer(text="Requested by {}".format(message.author))
                    await message.channel.send(embed=embedvar)
                    allowbet = 1
                if betdicen > 6:
                    embedvar = discord.Embed(title="You cant bet on anything above 6!")
                    embedvar.set_footer(text="Requested by {}".format(message.author))
                    await message.channel.send(embed=embedvar)
                    allowbet = 1
                if betdicen < 0:
                    embedvar = discord.Embed(title="You cant bet on anything below 0!")
                    embedvar.set_footer(text="Requested by {}".format(message.author))
                    await message.channel.send(embed=embedvar)
                    allowbet = 1
                if not allowbet == 1:
                    betdiceroll = random.randint(1,6)
                    if betdicen == betdiceroll:
                        coins2 = coin + betdicewin
                        coin = coins2
                        embedvar = discord.Embed(title="Dice rolled {} and You Won {}".format(betdiceroll, betdicewin),description="You now have: {}".format(coin),color=discord.Colour(0x00ff00))
                        embedvar.set_footer(text="Requested by {}".format(message.author))
                        await message.channel.send(embed=embedvar)
                        with open('settings/coin.txt', 'r') as file:
                            data = file.readlines()
                        data[linenum - 1] = '{}, {}\n'.format(message.author.id, coin)
                        file.close()

                        with open('settings/coin.txt', 'w') as file:
                            file.writelines(data)
                    else:
                        coins2 = coin - betdiceb
                        coin = coins2
                        embedvar = discord.Embed(title="Dice rolled {} You Lost {}".format(betdiceroll, betdiceb),description="You now have: {}".format(coin),color=discord.Colour(0xff0000))
                        embedvar.set_footer(text="Requested by {}".format(message.author))
                        await message.channel.send(embed=embedvar)
                        with open('settings/coin.txt', 'r') as file:
                            data = file.readlines()
                        data[linenum - 1] = '{}, {}\n'.format(message.author.id, coin)
                        file.close()

                        with open('settings/coin.txt', 'w') as file:
                            file.writelines(data)

            if message.content.startswith("-bet rps"):
                from random import randint

                t = ["R","P","S"]
                computer = t[randint(0,2)]
                player = False

                while player == False:
                    player = (message.content[9:10])
                    rpsbet = int(message.content[11:])
                    rpsbet2 = rpsbet/2 # change multiplier here
                    rpsbet2 = rpsbet2.as_integer_ratio()
                    allowbet = 0
                    if int(rpsbet) > coin:
                        embedvar = discord.Embed(title="You cant bet more than you have!")
                        embedvar.set_footer(text="Requested by {}".format(message.author))
                        await message.channel.send(embed=embedvar)
                        allowbet = 1
                    if int(rpsbet) < 1:
                        embedvar = discord.Embed(title="You cant bet nothing!")
                        embedvar.set_footer(text="Requested by {}".format(message.author))
                        await message.channel.send(embed=embedvar)
                        allowbet = 1
                    if not allowbet == 1:
                        if player == computer:
                            await message.channel.send("Tie!")
                        elif player == "r":
                            if computer == "P":
                                coins2 = coin - rpsbet
                                coin = coins2
                                embedvar = discord.Embed(title="You Lose! rapidbot covers {}".format(message.author),description="You now have: {}".format(coin),color=discord.Colour(0xff0000))
                                embedvar.set_footer(text="Requested by {}".format(message.author))
                                await message.channel.send(embed=embedvar)
                                with open('settings/coin.txt', 'r') as file:
                                    data = file.readlines()
                                data[linenum - 1] = '{}, {}\n'.format(message.author.id, coin)
                                file.close()

                                with open('settings/coin.txt', 'w') as file:
                                    file.writelines(data)
                            else:
                                coins2 = int(coin) + (rpsbet2[0]/rpsbet2[1])
                                coin = coins2
                                embedvar = discord.Embed(title="You Win! {} smashes rapidbot".format(message.author),description="You now have: {}".format(coin),color=discord.Colour(0x00ff00))
                                embedvar.set_footer(text="Requested by {}".format(message.author))
                                await message.channel.send(embed=embedvar)
                                with open('settings/coin.txt', 'r') as file:
                                    data = file.readlines()
                                data[linenum - 1] = '{}, {}\n'.format(message.author.id, coin)
                                file.close()

                                with open('settings/coin.txt', 'w') as file:
                                    file.writelines(data)
                        elif player == "p":
                            if computer == "S":
                                coins2 = int(coin) - rpsbet
                                coin = coins2
                                embedvar = discord.Embed(title="You Lose! rapidbot cut {}".format(message.author),description="You now have: {}".format(coin),color=discord.Colour(0xff0000))
                                embedvar.set_footer(text="Requested by {}".format(message.author))
                                await message.channel.send(embed=embedvar)
                                with open('settings/coin.txt', 'r') as file:
                                    data = file.readlines()
                                data[linenum - 1] = '{}, {}\n'.format(message.author.id, coin)
                                file.close()

                                with open('settings/coin.txt', 'w') as file:
                                    file.writelines(data)
                            else:
                                coins2 = int(coin) + (rpsbet2[0]/rpsbet2[1])
                                coin = coins2
                                embedvar = discord.Embed(title="You Win! {} covers rapidbot".format(message.author),description="You now have: {}".format(coin),color=discord.Colour(0x00ff00))
                                embedvar.set_footer(text="Requested by {}".format(message.author))
                                await message.channel.send(embed=embedvar)
                                with open('settings/coin.txt', 'r') as file:
                                    data = file.readlines()
                                data[linenum - 1] = '{}, {}\n'.format(message.author.id, coin)
                                file.close()

                                with open('settings/coin.txt', 'w') as file:
                                    file.writelines(data)
                        elif player == "s":
                            if computer == "R":
                                coins2 = coin - rpsbet
                                coin = coins2
                                embedvar = discord.Embed(title="You Lose! rapidbot smashes {}".format(message.author),description="You now have: {}".format(coin),color=discord.Colour(0xff0000))
                                embedvar.set_footer(text="Requested by {}".format(message.author))
                                await message.channel.send(embed=embedvar)
                                with open('settings/coin.txt', 'r') as file:
                                    data = file.readlines()
                                data[linenum - 1] = '{}, {}\n'.format(message.author.id, coin)
                                file.close()

                                with open('settings/coin.txt', 'w') as file:
                                    file.writelines(data)
                            else:
                                coins2 = coin + (rpsbet2[0]/rpsbet2[1])
                                coin = coins2
                                embedvar = discord.Embed(title="You Win! {} cut rapidbot".format(message.author),description="You now have: {}".format(coin),color=discord.Colour(0x00ff00))
                                embedvar.set_footer(text="Requested by {}".format(message.author))
                                await message.channel.send(embed=embedvar)
                                with open('settings/coin.txt', 'r') as file:
                                    data = file.readlines()
                                data[linenum - 1] = '{}, {}\n'.format(message.author.id, coin)
                                file.close()

                                with open('settings/coin.txt', 'w') as file:
                                    file.writelines(data)
                        else:
                            embedvar = discord.Embed(title="Thats not a move")
                            embedvar.set_footer(text="Requested by {}".format(message.author))
                            await message.channel.send(embed=embedvar)

                        player = True
                        computer = t[randint(0,2)]

            if message.content.startswith("-bet multi"):
                betmulticontent = message.content[11:]
                betmulticontlist = betmulticontent.split()
                betmultiplyer = betmulticontlist[0]
                betmultiamount = betmulticontlist[1]

                allowbet = 0
                if int(betmultiamount) > coin:
                    embedvar = discord.Embed(title="You cant bet more than you have!")
                    embedvar.set_footer(text="Requested by {}".format(message.author))
                    await message.channel.send(embed=embedvar)
                    allowbet = 1
                if int(betmultiamount) < 1:
                    embedvar = discord.Embed(title="You cant bet nothing!")
                    embedvar.set_footer(text="Requested by {}".format(message.author))
                    await message.channel.send(embed=embedvar)
                    allowbet = 1
                if int(betmultiplyer) < 3:
                    embedvar = discord.Embed(title="You cant have a multiplier lower than 3!")
                    embedvar.set_footer(text="Requested by {}".format(message.author))
                    await message.channel.send(embed=embedvar)
                    allowbet = 1
                if int(betmultiplyer) > 100000:
                    embedvar = discord.Embed(title="You cant have a multiplier higher than 100000!")
                    embedvar.set_footer(text="Requested by {}".format(message.author))
                    await message.channel.send(embed=embedvar)
                    allowbet = 1
                if not allowbet == 1:
                    multiplyerunedit = int(betmultiplyer) * 1.20 * 10 # change multiplier here
                    lookup = "."
                    if lookup in str(multiplyerunedit):
                        head, sep, tail = str(multiplyerunedit).partition('.')

                    botmultichoice = randint(1,int(head))
                    print(str(botmultichoice)+"/"+str(multiplyerunedit))
                    if botmultichoice < 11:
                        coins2 = coin + (int(betmultiamount) * int(betmultiplyer))
                        coin = coins2
                        embedvar = discord.Embed(title="You Won: {}".format(int(betmultiamount) * int(betmultiplyer)),description="You bet {} on a {}X multiplier and you now have: {}"\
                        .format(betmultiamount, betmultiplyer, coin),color=discord.Colour(0x00ff00))
                        embedvar.set_footer(text="Requested by {}".format(message.author))
                        await message.channel.send(embed=embedvar)
                        with open('settings/coin.txt', 'r') as file:
                            data = file.readlines()
                        data[linenum - 1] = '{}, {}\n'.format(message.author.id, coin)
                        file.close()

                        with open('settings/coin.txt', 'w') as file:
                            file.writelines(data)
                    else:
                        coins2 = coin - int(betmultiamount)
                        if coins2 < 0:
                            coins2 = 0
                        coin = coins2
                        embedvar = discord.Embed(title="You Lost: {}".format(betmultiamount),description="You bet {} on a {}X multiplier and you now have: {}" \
                        .format(betmultiamount, betmultiplyer, coin),color=discord.Colour(0xff0000))
                        embedvar.set_footer(text="Requested by {}".format(message.author))
                        await message.channel.send(embed=embedvar)
                        with open('settings/coin.txt', 'r') as file:
                            data = file.readlines()
                        data[linenum - 1] = '{}, {}\n'.format(message.author.id, coin)
                        file.close()

                        with open('settings/coin.txt', 'w') as file:
                            file.writelines(data)

            if message.content.startswith("-bet revup"):
                betrevcontent = message.content[11:]
                betrevlist = betrevcontent.split()
                revupbet = betrevlist[0]
                betrevtimes = betrevlist[1]
                allowcmd = 0

                if int(betrevtimes) > 1:
                    if int(betrevtimes) > 15:
                        embedvar = discord.Embed(title="Number over max goes limit!",description="There is a 15 goes limit")
                        embedvar.set_footer(text="Requested by {}".format(message.author))
                        await message.channel.send(embed=embedvar)
                        allowcmd = 1
                    elif int(betrevtimes) > 1:
                        lookup = str(message.author.id)
                        with open('settings/coin.txt') as myFile:
                            for line in myFile:
                                if lookup in line:
                                    import decimal
                                    balance = decimal.Decimal(line[20:])
                                    balance = balance / 100
                                    head, sep, tail = str(balance).partition('.')
                        if int(betrevtimes) > int(head):
                            if head == "0":
                                head = "1"
                            embedvar = discord.Embed(title="Number over goes limit!", description="There is a {} goes limit,\
                            increase this by getting more coins by playing games! do `-help games` to see the games list".format(head))
                            embedvar.set_footer(text="Requested by {}".format(message.author))
                            await message.channel.send(embed=embedvar)
                            allowcmd = 1
                if int(betrevtimes) < 1:
                    await message.channel.send("```The minimum goes is 1!```")
                    allowcmd = 1
                if not allowcmd == 1:
                    for i in range(int(betrevtimes)):
                        allowbet = 0
                        if int(revupbet) > coin:
                            embedvar = discord.Embed(title="You cant bet more than you have!")
                            embedvar.set_footer(text="Requested by {}".format(message.author))
                            await message.channel.send(embed=embedvar)
                            allowbet = 1
                        if int(revupbet) < 1:
                            embedvar = discord.Embed(title="You cant bet nothing!")
                            embedvar.set_footer(text="Requested by {}".format(message.author))
                            await message.channel.send(embed=embedvar)
                            allowbet = 1
                        if not allowbet == 1:
                            import decimal
                            revupdivider = decimal.Decimal(random.randrange(0, 2750)) # change multiplier here
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
                                embedvar = discord.Embed(title="You Won: {}".format(round(coinadd, 2)),description="You bet {} and got a {}X multiplier and you now have: {}" \
                                .format(revupbet, round(revumtotal, 2), coin),color=discord.Colour(0x00ff00))
                                embedvar.set_footer(text="Requested by {}".format(message.author))
                                await message.channel.send(embed=embedvar)
                            if coinadd < revupbet:
                                embedvar = discord.Embed(title="You Got Back: {}".format(revupbet - (revupbet - round(coinadd, 2))),description=
                                "You bet {} and got a {}X multiplier and you now have: {}" \
                                .format(revupbet, round(revumtotal, 2), coin),color=discord.Colour(0xff0000))
                                embedvar.set_footer(text="Requested by {}".format(message.author))
                                await message.channel.send(embed=embedvar)
                            with open('settings/coin.txt', 'r') as file:
                                data = file.readlines()
                            data[linenum - 1] = '{}, {}\n'.format(message.author.id, coin)
                            file.close()

                            with open('settings/coin.txt', 'w') as file:
                                file.writelines(data)

            if message.content.startswith("-bet dubup"):
                betrevcontent = message.content[11:]
                betrevlist = betrevcontent.split()
                revupbet = betrevlist[0]
                betrevtimes = betrevlist[1]
                allowcmd = 0

                if int(betrevtimes) > 1:
                    if int(betrevtimes) > 15:
                        embedvar = discord.Embed(title="Number over max goes limit!",description="There is a 15 goes limit")
                        embedvar.set_footer(text="Requested by {}".format(message.author))
                        await message.channel.send(embed=embedvar)
                        allowcmd = 1
                    if int(betrevtimes) > 1:
                        lookup = str(message.author.id)
                        with open('settings/coin.txt') as myFile:
                            for line in myFile:
                                if lookup in line:
                                    import decimal
                                    balance = decimal.Decimal(line[20:])
                                    balance = balance / 100
                                    head, sep, tail = str(balance).partition('.')
                        if int(betrevtimes) > int(head):
                            if head == "0":
                                head = "1"
                            embedvar = discord.Embed(title="Number over goes limit!", description="There is a {} goes limit,\
                            increase this by getting more coins by playing games! do `-help games` to see the games list".format(head))
                            embedvar.set_footer(text="Requested by {}".format(message.author))
                            await message.channel.send(embed=embedvar)
                            allowcmd = 1
                if int(betrevtimes) < 1:
                    await message.channel.send("```The minimum goes is 1!```")
                    allowcmd = 1
                if not allowcmd == 1:
                    for i in range(int(betrevtimes)):
                        allowbet = 0
                        if int(revupbet) > coin:
                            embedvar = discord.Embed(title="You cant bet more than you have!")
                            embedvar.set_footer(text="Requested by {}".format(message.author))
                            await message.channel.send(embed=embedvar)
                            allowbet = 1
                        if int(revupbet) < 1:
                            embedvar = discord.Embed(title="You cant bet nothing!")
                            embedvar.set_footer(text="Requested by {}".format(message.author))
                            await message.channel.send(embed=embedvar)
                            allowbet = 1
                        if not allowbet == 1:
                            import decimal
                            revupdivider = decimal.Decimal(random.randrange(0, 1000)) # change multiplier here
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
                                embedvar = discord.Embed(title="You Won: {}".format(round(coinadd, 2)),description=
                                "You bet {} and got a ({}x{}) {}X multiplier\nyou now have: {}" \
                                .format(revupbet, round(revupmulti, 2), round(revupmulti2, 2), round(revuptotal, 2),coin),color=discord.Colour(0x00ff00))
                                embedvar.set_footer(text="Requested by {}".format(message.author))
                                await message.channel.send(embed=embedvar)
                            if coinadd < revupbet:
                                embedvar = discord.Embed(title="You Got Back: {}".format(revupbet - (revupbet - round(coinadd, 2))),description=
                                "You bet {} and got a ({}x{}) {}X multiplier\nyou now have: {}" \
                                .format(revupbet, round(revupmulti, 2), round(revupmulti2, 2), round(revuptotal, 2), coin),color=discord.Colour(0xff0000))
                                embedvar.set_footer(text="Requested by {}".format(message.author))
                                await message.channel.send(embed=embedvar)
                            with open('settings/coin.txt', 'r') as file:
                                data = file.readlines()
                            data[linenum - 1] = '{}, {}\n'.format(message.author.id, coin)
                            file.close()

                            with open('settings/coin.txt', 'w') as file:
                                file.writelines(data)

            if message.content.startswith("-bet crash"):
                crashbet = message.content[11:]
                crashbet = int(crashbet)
                allowbet = 0
                if crashbet > coin:
                    embedvar = discord.Embed(title="You cant bet more than you have!")
                    embedvar.set_footer(text="Requested by {}".format(message.author))
                    await message.channel.send(embed=embedvar)
                    allowbet = 1
                if crashbet < 1:
                    embedvar = discord.Embed(title="You cant bet nothing!")
                    embedvar.set_footer(text="Requested by {}".format(message.author))
                    await message.channel.send(embed=embedvar)
                    allowbet = 1
                if not allowbet == 1:
                    embedvar = discord.Embed(title="Welcome to crash!".format(crashbet), description=
                    "Smash x to pull out of game before you lose!")
                    msg = await message.channel.send(embed=embedvar)
                    await msg.add_reaction('🚫')
                    crashmultiplier = 1

                    global reaction3, user3

                    def check(reaction3, user3):
                        return user3 == message.author and str(reaction3.emoji) == '🚫'

                    try:
                        reaction3, user3 = await client.wait_for('reaction_add', timeout=0.75, check=check)
                    except asyncio.TimeoutError:
                        coin = coin.as_integer_ratio()
                        for i in range(100000):
                            try:
                                reaction3, user3 = await client.wait_for('reaction_add', timeout=0.75, check=check)
                            except asyncio.TimeoutError:
                                crashmultiplier = crashmultiplier * 1.05
                                crashmultiplier = round(crashmultiplier,2)
                                endnow = randint(1, 9)
                                if endnow == 5:
                                    embedvar = discord.Embed(title="You lost {}".format(crashbet),description="Crashed on multiplier\
                                     of {} and your bal is now {}".format(crashmultiplier, (coin[0]/coin[1])),color=discord.Colour(0xff0000))
                                    await msg.edit(embed=embedvar)
                                    coin2 = (coin[0]/coin[1]) - crashbet
                                    coin = coin2
                                    with open('settings/coin.txt', 'r') as file:
                                        data = file.readlines()
                                    data[linenum - 1] = '{}, {}\n'.format(message.author.id, coin)
                                    file.close()

                                    with open('settings/coin.txt', 'w') as file:
                                        file.writelines(data)
                                    break

                                embedvar = discord.Embed(title="CURRENT MULTIPLIER {}X".format(crashmultiplier), description="Smash x to pull out of game before you lose")
                                await msg.edit(embed=embedvar)
                            else:
                                if reaction3.emoji == '🚫':
                                    crashmultiplier = round(crashmultiplier,2)
                                    crashmultiplier = crashmultiplier.as_integer_ratio()
                                    crashwinnings = crashbet * (crashmultiplier[0]/crashmultiplier[1])
                                    coin2 = (coin[0]/coin[1]) - crashbet + crashwinnings
                                    coin = coin2
                                    embedvar = discord.Embed(title="You won {}".format(crashwinnings),description="Game ended on a multiplier of {}X and your bal is now {}"
                                    .format((crashmultiplier[0]/crashmultiplier[1]), coin), color=discord.Colour(0x00ff00))
                                    await msg.edit(embed=embedvar)
                                    with open('settings/coin.txt', 'r') as file:
                                        data = file.readlines()
                                    data[linenum - 1] = '{}, {}\n'.format(message.author.id, coin)
                                    file.close()

                                    with open('settings/coin.txt', 'w') as file:
                                        file.writelines(data)
                                    break
        # if message.content.startswith("-bet roulette"):

        # ADMIN

        if message.content.startswith("-purge"):
            await message.delete()
            values3 = int(message.content[7:])
            values7 = values3 + 2
            time.sleep(1)
            pass
            def is_me(m):
                return m.author == message.author
            deleted = await message.channel.purge(limit=values7, check=is_me)
            await message.channel.send('Deleted {} message(s)'.format(len(deleted)), delete_after=10)

        # BOT CREATOR ONLY COMMANDS

        if message.content.startswith("-empcv"):
            if message.author.id == 425373518566260766:
                from forex_python.converter import CurrencyRates
                c = CurrencyRates()
                valuess = float(message.content[7:])
                values = valuess * 0.62103592767
                output = c.convert('EUR','GBP',values)
                stuff_in_string = "```Here is the value: £{}```".format(output)
                outputp = output * 1.20
                stuff_in_string2 = "```profit value for 20% prof: £{}```".format(outputp)
                outputs = outputp * 1.15
                stuff_in_string3 = "```Profit + Steam tax: £{}```".format(outputs)
                await message.channel.send(stuff_in_string)
                await message.channel.send(stuff_in_string2)
                await message.channel.send(stuff_in_string3)
            else:
                await message.channel.send("```you dont have perms to use this command```")

        if message.content.startswith("-steam tax"):
            if message.author.id == 425373518566260766:
                valuess = float(message.content[11:])
                values = valuess * 0.85
                stuff_in_string = "```Here is the value: £{}```".format(values)
                await message.channel.send(stuff_in_string)
            else:
                await message.channel.send("```you dont have perms to use this command```")

        if message.content.startswith("-update strs"):
            if message.author.id == 425373518566260766:
                with open('strs/msgstore.txt','r') as f:
                    sendback = f.read()
                    with open('strs/linkstore.txt','w') as f:
                        a =(re.findall(r'(https?://[^\s]+)',sendback))
                        b =(re.findall(r'(http?://[^\s]+)',sendback))
                        c = ('\n'.join(a))
                        d = ('\n'.join(b))
                        write = '{},{}'.format(c,d)
                        f.write(write)
                        f.close()
                        with open('strs/linkstore.txt') as result:
                            uniqlines = set(result.readlines())
                            with open('strs/linkndp.txt','w') as rmdup:
                                rmdup.writelines(set(uniqlines))

                                bad_words = ['https://discord.com/channels/']
                                with open('strs/linkndp.txt') as oldfile,open('strs/linknd-ndsc.txt','w') as newfile:
                                    for line in oldfile:
                                        if not any(bad_word in line for bad_word in bad_words):
                                            newfile.write(line)

                await message.channel.send("```Lnk data Success```")
                file_name = ("strs/msgstore.txt")
                file1 = open(file_name,"r")
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

                with open('strs/occurdata.txt','w') as f:
                    f.write("\n\nNumber of occurrences of each word in file is:")
                    f.write("\n ===============\n")

                    for key in list(d.keys()):
                        yeis = '{},":",{} \n'.format(key,d[key])
                        writethat = str(yeis)
                        f.write(writethat)

                    file1.close()
                    await message.channel.send("```Occr data Success```")

        if message.content.startswith("-randlink"):
            if message.author.id == 425373518566260766:
                import random
                lines = open('strs/linknd-ndsc.txt').read().splitlines()
                myline = random.choice(lines)
                await message.channel.send(myline)

        if message.content.startswith("-allmsg without"):
            if message.author.id == 425373518566260766:
                bad_word = message.content[16:]
                bad_words = bad_word.split()
                await message.channel.send(bad_words)
                with open('strs/msgstore.txt') as oldfile,open('strs/edits/allmsg-withoutwords-{}.txt'.format(message.content[16:]),'w') as newfile:
                    for line in oldfile:
                        if not any(bad_word in line for bad_word in bad_words):
                            newfile.write(line)
                    await message.channel.send("```SUCCESS```")
                    await message.channel.send(file=discord.File('strs/edits/allmsg-withoutwords-{}.txt'.format(message.content[16:])))

        if message.content.startswith("-allmsg only"):
            if message.author.id == 425373518566260766:
                bad_word = message.content[13:]
                bad_words = bad_word.split()
                await message.channel.send(bad_words)
                with open('strs/msgstore.txt') as oldfile,open('strs/edits/allmsg-findwords-{}.txt'.format(message.content[13:]),'w') as newfile:
                    for line in oldfile:
                        if any(bad_word in line for bad_word in bad_words):
                            newfile.write(line)
                    await message.channel.send("```SUCCESS```")
                    await message.channel.send(file=discord.File('strs/edits/allmsg-findwords-{}.txt'.format(message.content[13:])))

        if message.content.startswith("-admin upload"):
            if message.author.id == 425373518566260766:
                await message.channel.send(file=discord.File('{}'.format(message.content[14:])))

        #data not admin
        if message.content.startswith("-thischat msg"):
            if message.author.id == 425373518566260766:
                lists = []
                putin = '{}'.format(message.channel.id)
                lists.append(putin)
                bad_words = lists
                await message.channel.send(bad_words)
                with open('strs/msgstore.txt') as oldfile,open('strs/edits/chatmsg-{}.txt'.format(message.channel.id),'w') as newfile:
                    for line in oldfile:
                        if any(bad_word in line for bad_word in bad_words):
                            newfile.write(line)
                    await message.channel.send("```SUCCESS```")
                    await message.channel.send(file=discord.File('strs/edits/chatmsg-{}.txt'.format(message.channel.id)))

        if message.content.startswith("-beta access"):
            giveto = message.content[13:]
            giveto2 = giveto[3:21]
            if message.author.id == 425373518566260766:
                with open('settings/beta.txt','r') as f:
                    isin = '{}'.format(f.read())
                    if isin.find(str(giveto2)) > -1:
                        await message.channel.send("```This user is already has the beta rank```")
                    else:
                        with open('settings/beta.txt','a') as i:
                            i.write(giveto2)
                            i.close()
                        string = "```User {} has been given beta rank!```".format(giveto)
                        await message.channel.send(string)
            else:
                await message.channel.send("```You will need to ask rapidslayer101 for access to the beta rank")

        if message.content.startswith("-status dev"):
            if message.author.id == 425373518566260766:
                game = discord.Game("Currently programming")
                await client.change_presence(status=discord.Status.online, activity=game)

        if message.content.startswith("-status on"):
            if message.author.id == 425373518566260766:
                game = discord.Game("On since {}".format(datetime.datetime.now()))
                await client.change_presence(status=discord.Status.online, activity=game)

        if message.content.startswith("-status make"):
            if message.author.id == 425373518566260766:
                game = discord.Game("{}".format(message.content[13:]))
                await client.change_presence(status=discord.Status.online, activity=game)

        if message.content.startswith("-token make"):
            if message.author.id == 425373518566260766:
                import string
                token = ""
                for i in range(25):
                    token = token + (random.choice(string.ascii_uppercase))
                    if i == 4:
                        token = token + "-"
                    if i == 9:
                        token = token + "-"
                    if i == 14:
                        token = token + "-"
                    if i == 19:
                        token = token + "-"
                with open('settings/token.txt', 'a+') as f:
                    f.write(token + ", " + message.content[12:] + "\n")

                from discord_webhook import DiscordWebhook, DiscordEmbed
                webhook = DiscordWebhook(url='https://discordapp.com/api/webhooks/747795345295278101/bI1yWpdM0g_XudLzDcDdCoX4MjuOYGgSBaqWipZ5oQ4FX9mK8Hr0Dj0YJRxfWRx58Y3a')
                embed = DiscordEmbed(title="{}".format(token),description="Claim the above {} coin token by typing -claim token <token>".format(message.content[12:]))
                webhook.add_embed(embed)
                webhook.execute()
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
            vc.play(discord.FFmpegPCMAudio(executable="ffmpeg/bin/ffmpeg.exe",source="C://Users/rapid/Downloads/video1.mp4"))
            await message.channel.send("```now playing: wide_putin.mp4```")

        if message.content.startswith("-react"):
            msg = await message.channel.send("hi")
            await msg.add_reaction('1️⃣')
            await msg.add_reaction('🎲')
            channel = message.channel
            global reaction1, user1
            def check(reaction1, user1):
                return user1 == message.author and str(reaction1.emoji) == '1️⃣' or '🎲'

            try:
                reaction1, user1 = await client.wait_for('reaction_add', timeout=10.0, check=check)
            except asyncio.TimeoutError:
                await channel.send('No reaction was recieved timed out')
            else:
                await channel.send('Reaction recieved!!')

        if message.content.startswith("-tts"):
            import gtts
            text = message.content[5:]
            tts = gtts.gTTS(text)
            tts.save("temp.mp3")
            vc.play(discord.FFmpegPCMAudio(executable="ffmpeg/bin/ffmpeg.exe",source="temp.mp3"))

        if message.content.startswith("-update"):
            from discord_webhook import DiscordWebhook, DiscordEmbed
            webhook = DiscordWebhook(url='https://discordapp.com/api/webhooks/746835238319292487/8fUZx7YAOH47g0m7FbydDJBH6tQuyWRQEyIL-HsTO33bWnqDo7b_ui3JiXeRW9reFLnH')
            embed = DiscordEmbed(title="Rapidbot update!", description="Rapidbot V{} released".format(message.content[8:14]))
            embed.add_embed_field(name="Change log", value="{}".format(message.content[15:]))
            webhook.add_embed(embed)
            webhook.execute()

        if message.content.startswith("-test"):
            from discord.utils import get
            msg = await message.channel.send("react to this")
            msg.add_reaction(":repeat:")
            @client.event
            async def on_raw_reaction_add(payload):
                if payload.emoji.name == "🔁":
                    reaction = get(message.reactions, emoji=payload.emoji.name)
                    await msg.edit(content="Reaction added")
                    reaction = get(msg.reactions, emoji="🔁")
# client.run("NzExNTc4NDEyMTAzMzY4NzA3.XsFGcw.kuaqIiivBkE0Ji1Bq2koZWnfFLw")
client.run("mfa.nAqjx8-2-8qMkdWRSILfSgPuGdmnrsdCAY5MJr8vsSIQ_R7h7_Fpk7GnPpl3nDaxP_pPqq-JOkNBTLKatuU4", bot=False)