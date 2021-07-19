import socket, os, time, re
from base64 import b64decode
from zlib import decompress
from random import randint
from hashlib import sha512
from threading import Thread
from datetime import datetime
from win10toast import ToastNotifier


import file_send, file_receive

SERVER_HOST = "0.0.0.0"
SERVER_PORT = 8079
separator_token = "<SEP>"

client_sockets = set()
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((SERVER_HOST, SERVER_PORT))
s.listen(5)


def listen_for_client(cs):
    while True:
        msg = cs.recv(1024).decode()
        with open("socket_return.txt", "w", encoding="utf-8") as f:
            msg_write = "~" + msg + f" ___TIME: {datetime.now()}"
            f.write(msg_write)


while True:
    client_socket, client_address = s.accept()
    client_sockets.add(client_socket)
    t = Thread(target=listen_for_client, args=(client_socket,))
    t.daemon = True
    t.start()
    break


def to_c(text):
    for client_socket in client_sockets:
        client_socket.send(text.encode())


def inp(text):
    if text != "":
        to_c(text)
    while True:
        try:
            with open("socket_prev.txt", encoding="utf-8") as f:
                prev_send = ""
                for line in f.readlines():
                    prev_send = prev_send + line

            with open("socket_return.txt", encoding="utf-8") as f:
                to_send = ""
                for line in f.readlines():
                    to_send = to_send + line
                time.sleep(0.1)
                if to_send != prev_send:
                    with open("socket_prev.txt", "w", encoding="utf-8") as f:
                        f.write(to_send)
                    m = re.search("~(.+?)\$ ___TIME:", to_send)
                    if m:
                        to_send = m.group(1)
                        to_send = ": " + to_send
                        break
        except:
            with open("socket_return.txt", "w", encoding="utf-8") as f:
                f.write("")
            with open("socket_prev.txt", "w", encoding="utf-8") as f:
                f.write("")
    return to_send


BUF_SIZE = 32768
sha512 = sha512()
try:
    with open('process.exe', 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            sha512.update(data)
except:
    with open('process.py', 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            sha512.update(data)
    with open("sha512_list.txt", "a+") as f:
        f.write(f"SHA: {sha512.hexdigest()} VERSION: '0.7.TESTBUILD'\n")


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


def new_key(master_key):
    def key_test(master_key):

        p0_alpha = master_key[:95]
        p1_key = master_key[95:190]
        p1_e = master_key[190:191]
        p2_key = master_key[191:286]
        p2_e = master_key[286:288]
        p3_alpha = master_key[288:]

        def mkey_to_num(alpha, e):
            conversion_table = {}
            cvtable_counter = 0
            for i in alpha:
                conversion_table.__setitem__(i, cvtable_counter)
                cvtable_counter = cvtable_counter + 1

            hexadecimal = e.strip().upper()
            decimal = 0

            power = len(hexadecimal) - 1

            for digit in hexadecimal:
                decimal += conversion_table[digit] * 95 ** power
                power -= 1

            return decimal

        num1 = mkey_to_num(alpha=p1_key, e=p1_e)
        num2 = mkey_to_num(alpha=p2_key, e=p2_e)

        return num1, num2, p0_alpha, p3_alpha

    master_key = decompress(b64decode(master_key))
    master_key = master_key.decode()
    key_data = key_test(master_key)

    old_key = master_key[95:]

    p1_key = old_key[:95]
    p1_e = old_key[95:96]
    p2_key = old_key[96:191]
    p2_e = old_key[191:193]

    def mkey_to_num(alpha, e):
        conversion_table = {}
        cvtable_counter = 0
        for i in alpha:
            conversion_table.__setitem__(i, cvtable_counter)
            cvtable_counter = cvtable_counter + 1

        hexadecimal = e.strip().upper()
        decimal = 0

        power = len(hexadecimal) - 1

        for digit in hexadecimal:
            decimal += conversion_table[digit] * 95 ** power
            power -= 1

        return decimal

    num1 = mkey_to_num(alpha=p1_key, e=p1_e)
    num2 = mkey_to_num(alpha=p2_key, e=p2_e)

    def fib_iter(n):
        a = 1
        b = 1
        c = 1
        if n == 1:
            xxx = 0
        elif n == 2:
            xxx = 0
        else:
            for i in range(n - 3):
                total = (a + b * num2) * c
                c = b
                b = a
                a = total
            return b

    b = str(fib_iter(num1))
    p0_alpha = key_data[2]
    p3_alpha = key_data[3]

    with open("enc-code.txt", "w", encoding="utf-8") as f:
        f.write(b)

    with open("enc-num.txt", "w", encoding="utf-8") as f:
        f.write(f"1:{num1}2:{num2}3:{num1 + num2}")

    with open("enc-alpha.txt", "w", encoding="utf-8") as f:
        f.write(f"{p0_alpha}{p3_alpha}")


def get_prime_number():
    prime_numbers = []
    candidate = randint(100000, 800000)
    while True:
        if candidate <= 3:
            prime_numbers.append(candidate)
            yield candidate

        is_prime = True
        for prime_num in prime_numbers:
            if candidate % prime_num == 0:
                is_prime = False
                break

        if is_prime:
            prime_numbers.append(candidate)
            yield candidate

        candidate += 1


def get_prime_number2(content):
    prime_numbers = []
    candidate = int(content)
    while True:
        if candidate <= 3:
            prime_numbers.append(candidate)
            yield candidate

        is_prime = True
        for prime_num in prime_numbers:
            if candidate % prime_num == 0:
                is_prime = False
                break

        if is_prime:
            prime_numbers.append(candidate)
            yield candidate

        candidate += 1


def encrypt(plaintext):
    try:
        with open("enc-code.txt") as f:
            b = f.readlines()
            b = str(b)[2:-2]

        with open("enc-num.txt") as f:
            for line in f.readlines():
                num2 = int(search(data=line, filter_fr="2:", filter_to="3:"))

        with open("enc-alpha.txt", encoding="utf-8") as f:
            for line in f.readlines():
                alpha1 = line[:95]
                alpha2 = line[95:]

        while True:
            global prime_numbers
            counter = 0
            for i in plaintext:
                counter = counter + 1

            prime_numbers = get_prime_number()
            while True:
                if next(prime_numbers) > 100000:
                    if randint(1, 1000) == 1:
                        num = next(prime_numbers)
                        break
            newnum = ""
            for i in range(counter):
                newnum = str(newnum) + str(next(prime_numbers))
            outputenc = ""
            counter = 0
            for i in plaintext:
                counter = counter + 2
                alphabet = alpha1
                msg = i
                if msg in alphabet:
                    key = newnum[counter:counter + 2]
                    key = int(key)
                    if key > 95:
                        key = num2
                    if key == 0:
                        newAlphabet = alphabet
                    elif key > 0:
                        partialOne = alphabet[:key]
                        partialTwo = alphabet[key:]
                        newAlphabet = partialTwo + partialOne
                    else:
                        partialOne = alphabet[:(95 + key)]
                        partialTwo = alphabet[(95 + key):]
                        newAlphabet = partialTwo + partialOne
                    encrypted = ""
                    for message_index in range(0, len(msg)):
                        if msg[message_index] == " ":
                            encrypted += " "
                        for alphabet_index in range(0, len(newAlphabet)):
                            if msg[message_index] == alphabet[alphabet_index]:
                                encrypted += newAlphabet[alphabet_index]
                    outputenc = outputenc + encrypted
                else:
                    outputenc = outputenc + msg
                num = str(num).replace("0", "g").replace("1", "e").replace("2", "k").replace("3", "i").replace("4", "u") \
                    .replace("5", "d").replace("6", "r").replace("7", "w").replace("8", "q").replace("9", "p")

            etext = num + outputenc

            counter = 0
            for i in etext:
                counter = counter + 1
            content = str(etext[:6]).replace("g", "0").replace("e", "1").replace("k", "2").replace("i", "3")\
            .replace("u", "4").replace("d", "5").replace("r", "6").replace("w", "7").replace("q", "8").replace("p", "9")

            prime_numbers = get_prime_number2(content)
            while True:
                x = next(prime_numbers)
                if x == int(content):
                    num = x
                    break
            newnum = ""
            for i in range(counter):
                newnum = str(newnum) + str(next(prime_numbers))
            counter = 0
            outputend = ""
            for letter in etext[6:]:
                counter = counter + 2
                alphabet = alpha1
                msg = letter
                if msg in alphabet:
                    key = newnum[counter:counter + 2]
                    key = int(key)
                    if key > 95:
                        key = num2
                    key = key - key - key
                    if key == 0:
                        newAlphabet = alphabet
                    elif key > 0:
                        partialOne = alphabet[:key]
                        partialTwo = alphabet[key:]
                        newAlphabet = partialTwo + partialOne
                    else:
                        partialOne = alphabet[:(95 + key)]
                        partialTwo = alphabet[(95 + key):]
                        newAlphabet = partialTwo + partialOne
                    encrypted = ""
                    for message_index in range(0, len(msg)):
                        if msg[message_index] == " ":
                            encrypted += " "
                        for alphabet_index in range(0, len(newAlphabet)):
                            if msg[message_index] == alphabet[alphabet_index]:
                                encrypted += newAlphabet[alphabet_index]
                    outputend = outputend + encrypted
                else:
                    outputend = outputend + msg

            if outputend == plaintext:
                break

        while True:

            outputenc = ""
            counter = 0
            for i in etext:
                counter = counter + 2
                alphabet = alpha2
                msg = i
                if msg in alphabet:
                    key = b[counter:counter + 2]
                    key = int(key)
                    if key > 95:
                        key = num2
                    if key == 0:
                        newAlphabet = alphabet
                    elif key > 0:
                        partialOne = alphabet[:key]
                        partialTwo = alphabet[key:]
                        newAlphabet = partialTwo + partialOne
                    else:
                        partialOne = alphabet[:(95 + key)]
                        partialTwo = alphabet[(95 + key):]
                        newAlphabet = partialTwo + partialOne
                    encrypted = ""
                    for message_index in range(0, len(msg)):
                        if msg[message_index] == " ":
                            encrypted += " "
                        for alphabet_index in range(0, len(newAlphabet)):
                            if msg[message_index] == alphabet[alphabet_index]:
                                encrypted += newAlphabet[alphabet_index]
                    outputenc = outputenc + encrypted
                else:
                    outputenc = outputenc + msg

            etext2 = outputenc

            counter = 0
            outputend = ""
            for letter in etext2:
                counter = counter + 2
                alphabet = alpha2
                msg = letter
                if msg in alphabet:
                    key = b[counter:counter + 2]
                    key = int(key)
                    if key > 95:
                        key = num2
                    key = key - key - key
                    if key == 0:
                        newAlphabet = alphabet
                    elif key > 0:
                        partialOne = alphabet[:key]
                        partialTwo = alphabet[key:]
                        newAlphabet = partialTwo + partialOne
                    else:
                        partialOne = alphabet[:(95 + key)]
                        partialTwo = alphabet[(95 + key):]
                        newAlphabet = partialTwo + partialOne
                    encrypted = ""
                    for message_index in range(0, len(msg)):
                        if msg[message_index] == " ":
                            encrypted += " "
                        for alphabet_index in range(0, len(newAlphabet)):
                            if msg[message_index] == alphabet[alphabet_index]:
                                encrypted += newAlphabet[alphabet_index]
                    outputend = outputend + encrypted
                else:
                    outputend = outputend + msg

            if outputend == etext:
                break

        return etext2
    except:
        to_c("Encryption error")


def encrypt2(plaintext):
    plaintext = f"[E] " + plaintext
    etext = encrypt(plaintext)
    return etext


def decrypt(enc_text):
    try:
        with open("enc-code.txt") as f:
            b = f.readlines()
            b = str(b)[2:-2]

        with open("enc-num.txt") as f:
            for line in f.readlines():
                num2 = int(search(data=line, filter_fr="2:", filter_to="3:"))

        with open("enc-alpha.txt", encoding="utf-8") as f:
            for line in f.readlines():
                alpha1 = line[:95]
                alpha2 = line[95:]

        counter = 0
        outputend = ""
        for letter in enc_text:
            counter = counter + 2
            alphabet = alpha2
            msg = letter
            if msg in alphabet:
                key = b[counter:counter + 2]
                key = int(key)
                if key > 95:
                    key = num2
                key = key - key - key
                if key == 0:
                    newAlphabet = alphabet
                elif key > 0:
                    partialOne = alphabet[:key]
                    partialTwo = alphabet[key:]
                    newAlphabet = partialTwo + partialOne
                else:
                    partialOne = alphabet[:(95 + key)]
                    partialTwo = alphabet[(95 + key):]
                    newAlphabet = partialTwo + partialOne
                encrypted = ""
                for message_index in range(0, len(msg)):
                    if msg[message_index] == " ":
                        encrypted += " "
                    for alphabet_index in range(0, len(newAlphabet)):
                        if msg[message_index] == alphabet[alphabet_index]:
                            encrypted += newAlphabet[alphabet_index]
                outputend = outputend + encrypted
            else:
                outputend = outputend + msg

        dtext = outputend

        counter = 0
        for i in dtext:
            counter = counter + 1
        content = str(dtext[:6]).replace("g", "0").replace("e", "1").replace("k", "2").replace("i", "3") \
            .replace("u", "4").replace("d", "5").replace("r", "6").replace("w", "7").replace("q", "8").replace("p", "9")

        prime_numbers = get_prime_number2(content)
        while True:
            x = next(prime_numbers)
            if x == int(content):
                num = x
                break
        newnum = ""
        for i in range(counter):
            newnum = str(newnum) + str(next(prime_numbers))
        counter = 0
        outputend = ""
        for letter in dtext[6:]:
            counter = counter + 2
            alphabet = alpha1
            msg = letter
            if msg in alphabet:
                key = newnum[counter:counter + 2]
                key = int(key)
                if key > 95:
                    key = num2
                key = key - key - key
                if key == 0:
                    newAlphabet = alphabet
                elif key > 0:
                    partialOne = alphabet[:key]
                    partialTwo = alphabet[key:]
                    newAlphabet = partialTwo + partialOne
                else:
                    partialOne = alphabet[:(95 + key)]
                    partialTwo = alphabet[(95 + key):]
                    newAlphabet = partialTwo + partialOne
                encrypted = ""
                for message_index in range(0, len(msg)):
                    if msg[message_index] == " ":
                        encrypted += " "
                    for alphabet_index in range(0, len(newAlphabet)):
                        if msg[message_index] == alphabet[alphabet_index]:
                            encrypted += newAlphabet[alphabet_index]
                outputend = outputend + encrypted
            else:
                outputend = outputend + msg

        return outputend
    except:
        return "[CND] " + enc_text

# jump


# 0.1 created encryption algorithm
# 0.2 created rchat end to end application
# 0.3 created file sending system
# 0.4 created auto update, mkey sending
# 0.5 created rewrote and improved e
# 0.6 created GUI and c# <--> python system
# 0.7 created auto update 2.0

# 0.8 created chats
# 0.9 created e+ higher e layer
# 0.10 discord chat invites
# 0.11 created file encryption system

# ports 8080, 5001, 8079
# Made by rapidslayer101
# Testers: James judge, Kit jackson

with open("sending.txt", "w", encoding="utf-8") as f:
    f.write("0")


def date_now():
    return datetime.now().strftime('%d-%m-%Y %H:%M:%S')


h_name = socket.gethostname()

#SERVER_HOST = inp("Input HOST IP: ")[2:]
#SERVER_PORT = int(inp("Input HOST port: ")[2:])
SERVER_HOST = "26.101.12.103"
SERVER_PORT = 8080
separator_token = "<SEP1>"
separator_token2 = "<SEP2>"

s = socket.socket()
to_c(f"[NE] [{date_now()}] --> Connecting to {SERVER_HOST}:{SERVER_PORT}...")
while True:
    try:
        s.connect((SERVER_HOST, SERVER_PORT))
        break
    except:
        warn("Could not connect to host, hit enter to try again")
    inp("")
to_c(f"[NE] [{date_now()}] --> Connected to host, awaiting key")

if not os.path.exists(f'name.txt'):
    to_c("\nYou have not set a name yet! Type one and hit enter")
    while True:
        name = inp("")[2:]
        if len(name) > 24:
            warn("This name is to long, max length 24 chars")
        else:
            with open("name.txt", "w", encoding="utf-8") as f:
                f.write(name)
                break
else:
    with open("name.txt", encoding="utf-8") as f:
        for line in f.readlines():
            name = line
            if len(name) > 24:
                warn("\nThis loaded name is to long, max length 24 chars, type a new one")
                while True:
                    name = inp("")[2:]
                    if len(name) > 24:
                        warn("This name is to long, max length 24 chars")
                    else:
                        with open("name.txt", "w", encoding="utf-8") as f:
                            f.write(name)
                            break


if not os.path.exists(f'ip.txt'):
    h_name = socket.gethostname()
    IP_address = socket.gethostbyname(h_name)
    if "26." not in str(IP_address):
        to_c("\nYou have not set a ip yet, tried to set automatically but radmin was not your default")
        to_c("\nPlease find and copy your radmin IP and enter it")
        while True:
            IP_address = inp("")
            if "26." not in str(IP_address):
                warn("This IP is not a radmin 26. IP, you will not be able to receive files unless you change this IP")
            with open("ip.txt", "w", encoding="utf-8") as f:
                f.write(IP_address)
                break
    else:
        with open("ip.txt", "w", encoding="utf-8") as f:
            f.write(IP_address)
else:
    with open("ip.txt", encoding="utf-8") as f:
        for line in f.readlines():
            IP_address = line

s.send(f"[REQUEST CONNECTION] --> SHA512: '{sha512.hexdigest()}'".encode())


def listen_for_messages():
    while True:
        message = s.recv(1024).decode()
        if "[NE]" not in message[:20]:
            message = decrypt(message)
        m = re.search('<SEP1>(.+?)<SEP2>', message)
        if m:
            command = m.group(1)
        else:
            command = ""

        if command.startswith(" [CONNECTIONS]"):
            to_send = " [CONNECTIONS RESPONSE]"
            text = f"[{date_now()}] {h_name} {name}" \
                   f"{separator_token}{to_send}{separator_token2}"
            text = encrypt2(text)
            s.send(text.encode())

        if command.startswith(" [PING]"):
            if command[12:] == name:
                ToastNotifier().show_toast(title="PING!", msg="A user has pinged you in Rchat!",
                                           icon_path="rchat.ico", duration=5, threaded=True)

        #if command.startswith(" [CONNECTIONS RESPONSE]"):
            #message = search(data=line, filter_fr="", filter_to="<SEP2>")

        if command.startswith(" [FILE TRANSFER]"):
            with open("sending.txt", encoding="utf-8") as f:
                for line in f.readlines():
                    if line == "0":
                        to_c("FILE TRANSFER DETECTED")

                        to_send = f" [ACCEPT TRANSFER] --> {IP_address} | 21"
                        text = f"[{date_now()}] {h_name} {IP_address} {name}" \
                               f"{separator_token}{to_send}{separator_token2}"
                        text = encrypt2(text)
                        s.send(text.encode())

                        try:
                            file_receive.receive(IP_address=IP_address)
                        except:
                            to_c(f"[{date_now()}] ERROR [!] - File receive failure")

        if "[KEY] -->" in str(message):
            master_key = search(data=message, filter_fr="KEY] --> '", filter_to="'")
            new_key(master_key)
            message = message.replace(f" --> '{master_key}'", "")

        if command.startswith(" [ACCEPT TRANSFER]"):
            with open("sending.txt", encoding="utf-8") as f:
                for line in f.readlines():
                    if line == "1":
                        to_c(f"ACCEPT TRANSFER FROM {command}")
                        ip = search(data=line, filter_fr="ACCEPT TRANSFER] --> ", filter_to=" | 21")
                        try:
                            file_send.send(filename=filename, ip=ip)
                        except:
                            to_c(f"[{date_now()}] ERROR [!] - File send failure")

        message = message.replace("/shrug", "¯\_(ツ)_/¯")
        message = message.replace(separator_token, "")
        message = message.replace(separator_token2, "")

        to_c(message)


t = Thread(target=listen_for_messages)
t.daemon = True
t.start()

while True:
    allow_send = 1
    exiter = 0
    to_send = inp("")

    if to_send == ": ":
        warn("You cannot send an empty message!")
        allow_send = 0

    try:
        with open("last_sent.txt") as f:
            for line in f.readlines():
                last_msg_time = line
        last_msg_time = datetime.strptime(last_msg_time, '%Y-%m-%d %H:%M:%S.%f')
        time_since_insertion = datetime.utcnow() - last_msg_time
        if time_since_insertion.seconds < 0.5:
            msg_to_fast = msg_to_fast + 1
            if msg_to_fast > 10:
                warn(f"YOU'RE SENDING MESSAGES TOO FAST! last message was {time_since_insertion}")
                allow_send = 0
        if time_since_insertion.seconds > 5:
            msg_to_fast = 0
    except:
        xxx = 0

    with open("last_sent.txt", "w") as f:
        f.write(str(datetime.utcnow()))

    if len(to_send) > 2000:
        warn("Your message is over the 2000 char limit, send a shorter message!")
    else:
        if to_send.lower() == ': -client commands':
            to_send = f" [CLIENT COMMANDS] --> -client commands, -update, -restart," \
                      f" -change ip, -change name, -change mkey, -connected, -send, -ping"

        if to_send.lower() == ': -update':
            to_c("This client will now exit, update initialising file transfer")
            os.startfile("updater.exe")
            exiter = 1
            allow_send = 0

        if to_send.lower() == ': -quit':
            exiter = 1
            to_send = " [QUIT]"

        if to_send.lower() == ': -restart':
            os.startfile("restart.bat")
            exiter = 1
            to_send = " [RESTART]"

        if to_send.lower().startswith(': -change ip'):
            allow_send = 0
            new_ip = to_send[13:]
            if new_ip == "":
                warn("You did enter an ip! Do '-change ip <NEW IP>'")
            else:
                if "26." not in str(new_ip):
                    warn("This IP is not a radmin 26. IP, you will not be able"
                         " to receive files unless you change this IP")
                IP_address = new_ip
                with open("ip.txt", "w", encoding="utf-8") as f:
                    f.write(IP_address)

        if to_send.lower().startswith(': -change name'):
            new_name = to_send[15:]
            if new_name == "":
                warn("You did enter a name! Do '-change ip <NEW NAME>'")
                allow_send = 0
            else:
                to_send = f" [CHANGE NAME] {name} --> {new_name}"
                name = new_name
                with open("name.txt", "w", encoding="utf-8") as f:
                    f.write(name)

        if to_send.lower().startswith(': -change mkey'):
            new_mkey = to_send[15:]
            allow_send = 0
            if new_mkey == "":
                warn("You did enter a new key! Do '-change mkey <NEW MKEY>'")
            else:
                to_send = f" [CHANGE MKEY]"
                try:
                    new_key(new_mkey)
                except:
                    warn("The key you entered is not valid")

        if to_send.lower() == ': -connected':
            to_send = " [CONNECTIONS]"

        if to_send.lower() == ': -send':
            filename = inp("Drag file onto window and hit enter\n")
            try:
                filename = filename.replace("\"", "")
                filesize = os.path.getsize(filename)
                filebasename = os.path.basename(filename)
                f_name, f_ext = os.path.splitext(filename)

                if f_ext in [".txt"]:
                    inp("This file type will soon support file encryption, but it doesnt yet, hit enter to cont.")
                else:
                    inp("THIS FILE TYPE DOES NOT SUPPORT ENCRYPTION (yet), YOUR FILE WILL NOT BE SENT ENCRYPTED.\n"
                        "HIT ENTER TO CONFIRM SEND")

                def format_bytes(size):
                    power = 2 ** 10
                    n = 0
                    power_labels = {0: '', 1: 'kilo', 2: 'mega', 3: 'giga', 4: 'tera'}
                    while size > power:
                        size /= power
                        n += 1
                    return f"{round(size,2)} {power_labels[n]}bytes"
                filesize_converted = format_bytes(filesize)
                to_send = f" [FILE TRANSFER] --> {filebasename} | {filesize_converted} == {filesize} bytes"
                with open("sending.txt", "w", encoding="utf-8") as f:
                    f.write("1")
            except:
                warn("Invalid file, exiting")
                to_send = f" [FAILED FILE TRANSFER]"

        if to_send.lower().startswith(': -ping'):
            ping = to_send[8:]
            if ping == "":
                warn("You did enter who to ping! Do '-ping <NAME>'")
                allow_send = 0
            else:
                to_send = f" [PING] --> {ping}"

        # LIEF

        if to_send.lower() == ': -lief':
            to_c("ENTERED LIEF PRIVATE CHANNEL")
            to_send = " [L I E F]"

        # LIEF

        if allow_send == 1:
            text = f"[{date_now()}] {h_name} {name}" \
                   f"{separator_token}{to_send}{separator_token2}"
            text = encrypt2(text)
            s.send(text.encode())

    if exiter == 1:
        time.sleep(5)
        break

s.close()