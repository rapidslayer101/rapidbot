import socket, os, time, re
from hashlib import sha512
from threading import Thread
from datetime import datetime
import discum


client_sockets = set()
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("0.0.0.0", 8079))
s.listen(5)


def to_c(text):
    for client_sock in client_sockets:
        client_sock.send(text.encode(encoding="utf-16"))


#BUF_SIZE = 32768
#sha512 = sha512()
#try:
#    with open('process.exe', 'rb') as f:
#        while True:
#            data = f.read(BUF_SIZE)
#            if not data:
#                break
#            sha512.update(data)
#except:
#    with open('process.py', 'rb') as f:
#        while True:
#            data = f.read(BUF_SIZE)
#            if not data:
#                break
#            sha512.update(data)
#    with open("sha512_list.txt", "a+") as f:
#        f.write(f"SHA: {sha512.hexdigest()} VERSION: '0.7.TESTBUILD'\n")


def warn(text):
    to_c(f"[WARN THREAD] [!] [{date_now()}] {text}")


with open("restart.bat", "w", encoding="utf-8") as f:
    f.write("rchat.exe")


def search(data, filter_fr, filter_to):
    data = str(data)
    m = re.search(f"""{filter_fr}(.+?){filter_to}""", data)
    if m:
        output = m.group(1)
    else:
        output = None
    return output

# jump

# implemented code:
# rchat 0.7.119.14 (process build 119, rchat GUI build 14)
# enc 5.5.0 (not yet implemented)


# 0.1 created encryption algorithm
# 0.2 created rchat end to end application
# 0.3 created file sending system
# 0.4 created auto update, mkey sending
# 0.5 created rewrote and improved e
# 0.6 created GUI and c# <--> python system
# 0.7 created auto update 2.0

# 0.1 code rewrite and code foundations/framework

# 0.2 discord integration
# 0.3 implemented the new higher enc 5.5.0+


# ports 8079
# Made by rapidslayer101
# Testers: James Judge


def date_now():
    return datetime.now().strftime('%d-%m-%Y %H:%M:%S')


cooldown_data = {"x": (str(datetime.utcnow()))}


class cooldown():
    def check(self, msg_to_fast):
        last_msg_time = datetime.strptime(cooldown_data["x"], '%Y-%m-%d %H:%M:%S.%f')
        time_since_insertion = datetime.utcnow() - last_msg_time
        if time_since_insertion.seconds < 0.35:
            msg_to_fast += 1
        if time_since_insertion.seconds > 3:
            msg_to_fast = 0
        cooldown_data.update({"x": (str(datetime.utcnow()))})
        return msg_to_fast


client_socket, client_address = s.accept()
print(client_socket)
client_sockets.add(client_socket)
to_c(f"Connected to socket via {client_address}")


def listen_for_discord():
    while True:
        bot = discum.Client(token='mfa.KENk5OoFlLk-Z_nklzH_JjjcjdzyxiLjyIsBSiM'
                                  '-OoqethlnNwxvJmDNktI069A1CmbaMaJeCUL4bJQxKhQJ', log=True)

        @bot.gateway.command
        def helloworld(resp):
            if resp.event.ready_supplemental:  # ready_supplemental is sent after ready
                user = bot.gateway.session.user
                to_c("Logged in as {}#{}".format(user['username'], user['discriminator']))
            if resp.event.message:
                m = resp.parsed.auto()
                guildID = m['guild_id'] if 'guild_id' in m else None  # because DMs are technically channels too
                channelID = m['channel_id']
                username = m['author']['username']
                discriminator = m['author']['discriminator']
                content = m['content']
                to_c("> guild {} channel {} | {}#{}: {}".format(guildID, channelID, username, discriminator, content))

        bot.gateway.run(auto_reconnect=True)

        # code to actually send new stuff to c
        time.sleep(30)
        message = "hello"
        to_c(message)


discord_on = False
# get preloaded discord token here

if discord_on:
    t = Thread(target=listen_for_discord)  # this launches a thread that watches discord updates
    t.daemon = True
    t.start()

if not discord_on:
    def listen_for_client(cs):
        msg_to_fast = 0
        if not discord_on:
            to_c("\n >> Please setup discord auth. Enter token now")
            while True:
                to_send = cs.recv(1024).decode(encoding="utf-16")
                print(to_send)

                if to_send == "TOKEN":
                    #t = Thread(target=listen_for_discord)  # this launches a thread that watches discord updates
                    #t.daemon = True
                    #t.start()
                    to_c("\n >> Token accepted\n")
                    break
                else:
                    to_c("Invalid token, please re-enter")

                if to_send.lower() == '-restart':
                    os.startfile("restart.bat")

                if to_send.lower() == '-quit':
                    print(f"quit {1.0 / 0.0}")
        while True:
            allow_send = 1
            to_send = cs.recv(1024).decode(encoding="utf-16")

            if to_send == ": ":
                warn("You cannot send an empty message!")
                allow_send = 0

            msg_to_fast = cooldown.check(0, msg_to_fast)
            if msg_to_fast > 10:
                warn(f"YOU'RE SENDING MESSAGES TOO FAST! (cooldown 3s)")
                allow_send = 0

            if len(to_send) > 2000:
                warn("Your message is over the 2000 char limit, send a shorter message!")
            else:
                if to_send.lower() == '-restart':
                    os.startfile("restart.bat")

                if to_send.lower() == '-quit':
                    print(f"quit {1.0/0.0}")

                if allow_send == 1:
                    print(to_send)
                    to_c(to_send)


    t = Thread(target=listen_for_client, args=(client_socket,))
    t.daemon = True
    t.start()
    print("[!] listen_for_client thread launched")

while True:
    time.sleep(10000)


# will 2 discord logins be required?
# 1 for new data being collected and 1 for sending data to discord. 
