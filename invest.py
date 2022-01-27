import time, datetime, os, re  # inbuilt

# import yfinance as yf1
import matplotlib.pyplot as plt
import yahoo_fin.stock_info as yf
import numpy as np
from datetime import datetime, timedelta
# from discord_webhook import DiscordWebhook
from forex_python.converter import CurrencyRates, CurrencyCodes

from enclib import search  # custom lib


# from twilio.rest import Client
# account_sid = ""
# auth_token = ""
# client = Client(account_sid, auth_token)

# LOGGING / FOLDER CHECKING #

start_time = time.time()

if not os.path.exists(f"output"):
    os.mkdir("output")
with open(f"output/logs.txt", "w") as f:
    f.write("")


def log(text):
    print(text)
    with open("output/logs.txt", "a+", encoding="utf-8") as f:
        try:
            write = f"{str(datetime.now())[:-4]} RUNTIME: {round(time.time()-start_time, 2):.2f} | {text}\n"
        except:
            write = f"{str(datetime.now())[:-4]} RUNTIME: {round(time.time()-start_time, 2):.2f} | PRINTING ERROR\n"
        f.write(write)


if not os.path.exists(f"stocks"):
    os.mkdir("stocks")
if not os.path.exists(f"stocks/stock_data.txt"):
    with open("stocks/stock_data.txt", "w") as f:
        f.write("")
with open("stocks/stock_data.txt") as f:
    data = f.readlines()


# SETTINGS #

# the amount of the stocks you own (shares/dollars)

user_list = []
user_stock_data = []
unique_stocks = []


class users:
    def add_user(self, user):
        user_list.append(user)
        user_stock_data.append({})

    def get_user_stocks(self, user):
        return user_stock_data[user_list.index(user)]

    def get_user_stock(self, user, stock):
        return user_stock_data[user_list.index(user)][stock]

    def buy_stock(self, user, stock, amount_buy, buy_price, buy_time):
        if stock not in unique_stocks:
            unique_stocks.append(stock)
        avg_price = 0
        if stock in user_stock_data[user_list.index(user)]:
            old_data = user_stock_data[user_list.index(user)][stock]
            amount_buy += old_data[0][0][0]
            buys = []
            for price in old_data[0][2]:
                avg_price += price
                buys.append(price)
            buys.append(buy_price)
            avg_price += buy_price
            avg_price /= len(buys)
            avg_price = round(avg_price, 2)
            buy_time = old_data[0][3]
        else:
            avg_price += buy_price
            buys = [buy_price]
        amount_own = amount_buy
        user_stock_data[user_list.index(user)]\
            .update({stock: [[[float(amount_buy), float(amount_own)],
                              float(avg_price), buys, buy_time], []]})

    def sell_stock(self, user, stock, amount_sell, sell_price, sell_time):
        sales = user_stock_data[user_list.index(user)][stock][1]
        sales.append([float(amount_sell), float(sell_price), sell_time])
        old_data = users.get_user_stock(0, user, stock)[0]
        old_data[0][1] = old_data[0][1] - amount_sell
        user_stock_data[user_list.index(user)].update({stock: [old_data, sales]})

    def load(self):  # todo redo load
        with open(f"stocks/stock_data.txt") as f:
            for line in f.readlines():
                user, user_data = line.replace("}\n", "").split(" {")
                if user not in user_list:
                    users.add_user(0, user)
                user_data = user_data.split("]], ")

                for stock in user_data:
                    name = stock.split("': [[")[0].replace("'", "")
                    stock_data = str(stock.split("': [[")[1:])[:-2]
                    purchase = stock_data.split("'], [")[0]
                    sell = stock_data.split("'], [")[1:]
                    amount_buy, buy_price, buy_time = purchase[2:].replace("'", "").split(", ")

                    sales = []
                    for sale in sell:
                        try:
                            if not sale == "":
                                sale = sale.replace("]", "").replace("\"", "").replace("[", "").replace("'", "")
                                amount_sell, sell_price, sell_time = sale.split(", ")
                                sales.append([float(amount_sell), float(sell_price), sell_time])
                        except:
                            pass
                    user_stock_data[user_list.index(user)]\
                        .update({name: [[float(amount_buy), float(buy_price), buy_time.replace("'", "")], sales]})

    def save(self):
        with open(f"stocks/stock_data.txt", "w") as f:
            [f.write(f"{user} {user_stock_data[user_list.index(user)]}\n") for user in user_list]


new_values = True

if new_values:
    users.add_user(0, "scott")
    users.buy_stock(0, "scott", "AMD", 0.03, 103.31, "27-01-22-18:47")
    print(user_stock_data)
    users.buy_stock(0, "scott", "AMD", 0.07, 103.61, "27-01-22-18:51")
    print(user_stock_data)
    users.buy_stock(0, "scott", "AMD", 0.15, 103.08, "27-01-22-19:32")
    print(user_stock_data)
    users.sell_stock(0, "scott", "AMD", 0.15, 103.40, "dt.object")
    print("unique stock", unique_stocks)
    print(user_stock_data)
    users.save(0)

input()
users.load(0)
print(user_stock_data)
input("Hit enter to continue: ")


# watch live stock price data #
stockwatch = True


if stockwatch:

    # how often to check stocks list (seconds) #
    checktime = 1           # when market "open"
    checktime_closed = 5    # when market in "POST" or "PRE"

    # how often to check market status (mins) #
    statuscheck = 5

    # how often to check stock change data (seconds) #
    changedatacheck = 320


# CODE START #

def current_profit(current, bought, amount):
    c = CurrencyRates()
    #d = CurrencyCodes()
    output = c.convert("USD", "GBP", float(current))
    profit = ((bought/float(amount)) - output) * float(amount)
    profit = profit - profit*2
    print((bought+profit))
    percent = ('{0:.2f}%'.format((bought+profit / bought * 100)))
    print(percent)
    log(f"Profit of: {profit} {percent}")


#def text(user, message):
#    message = client.messages.create(to="+447597299247", from_="+15155188444", body="EXAMPLE TEXT")


log("Bot started with settings:")
log(f"├─> Stocks({len(unique_stocks)}): {unique_stocks}")
stcounter1 = 0
if stockwatch:
    log("└─> Stock watch ON, settings:")
    log(f"    ├─> How often to check live stocks: every {checktime}s")
    log(f"    ├─> How often to check closed stocks: every {checktime_closed}s")
    log(f"    └─> How often to check the current market status: every {statuscheck}m")
else:
    log("└─> Stock watch OFF")


# DEFINING #


def plot_graph(stock, name, price_bought, readback):
    with open(f'stocks/{stock}/{stock}.txt') as f:
        lines = f.readlines()
        line_st = len(lines) - readback
        y = np.array([round(float(line.split(", ")[4]), 2) for line in lines[line_st:]])
        x = [x for x in range(len(lines[line_st:]))]
        #x = [line.split(" [")[0][:4] for line in lines[line_st:]]

    y_masked = np.ma.masked_less_equal(y, price_bought)

    plt.style.use("dark_background")
    ax1 = plt.figure().add_subplot(111)

    ax1.set_title(name)
    ax1.set_ylabel("Price £")
    ax1.set_xlabel("Days ago")
    ax1.plot(x, y, c='r', label='share price', linewidth=0.5)
    plt.plot(y_masked, 'g', linewidth=0.5)
    plt.axhline(1000, color='b', linestyle='--', linewidth=0.25)

    plt.savefig(f'stocks/{stock}/{stock}.png', dpi=300)
    plt.close()

    #webhook = DiscordWebhook(url=discord_webhook_url, content=name)
    #with open(f'stocks/{stock}/{stock}.png', "rb") as f:
        #webhook.add_file(file=f.read(), filename=f'{stock}.png')
    #webhook.execute()

# STOCK FOLDER CREATION #


log("--------------------------------------------------")
for stock in unique_stocks:
    log(f"Checking directory paths for {stock}")
    if not os.path.exists(f'stocks/{stock}'):
        os.makedirs(f'stocks/{stock}')
        log("└─> Directory missing, now been added")
    else:
        log("└─> Directory present")


# STOCK MARKET INFORMATION #


def market_status():
    log("--------------------------------------------------")
    stock_market_status = yf.get_market_status()

    if stock_market_status == "PRE":
        stock_market_status = "PRE-MARKET"
        loopchecks = 1

    if stock_market_status == "PREPRE":
        stock_market_status = "CLOSED (pepe)"
        loopchecks = 0

    if stock_market_status == "CLOSED":
        loopchecks = 0

    if stock_market_status == "POSTPOST":
        stock_market_status = "CLOSED (popo)"
        loopchecks = 0

    if stock_market_status == "POST":
        stock_market_status = "POST-MARKET"
        loopchecks = 2

    if stock_market_status in ["REGULAR", "OPEN"]:
        stock_market_status = "OPEN"
        loopchecks = 3

    log(f"Stock market is currently: {stock_market_status}")

    # loopchecks status codes #
    # -1 = code has not checked the status yet
    # 0 = closed, no checks
    # 1 = pre, some checks
    # 2 = post, some checks
    # 3 = open, all checks
    log(f"LOOPCHECK STATUS CODE: {loopchecks}")
    log(f"CURRENT TIME: {str(datetime.now())[:-4]}")
    log("--------------------------------------------------")
    return loopchecks


loopchecks = -1  # default status code in-case of status retrieval failure
loopchecks = market_status()


# CHECKING OLD STOCK DATA #


log("Collecting old stock data")
date = datetime.now()

date_1d = date - timedelta(days=10)
date_1d = str(date_1d)[:10]

date_begin = date - timedelta(weeks=2609)
date_begin = str(date_begin)[:10]

date = str(date)[:10]


def data_collect(start_date, end_date, stock):
    stock_prices = yf.get_data(start_date=start_date, end_date=end_date, ticker=stock, interval="1d")
    with open(f"stocks/{stock}/{stock}.txt", "w") as f:
        [f.write(f'{search(str(stock_prices.loc[rname]), "Name: ", ", dtype")} '
                 f'{str(list(stock_prices.loc[rname])[:-1])}\n') for rname in stock_prices.index]


update_stocks = True

if update_stocks:
    [data_collect(start_date=date_begin, end_date=date, stock=stock) for stock in unique_stocks]
    log("Finished collecting stock data")

# CHECKING LIVE STOCKS #

if stockwatch:
    if loopchecks in range(0, 3):
        log("getting close prices...")
    for stock in unique_stocks:
        with open(f"stocks/{stock}/{stock}_live.txt", "w") as f:
            f.write("")
    go = 0
    while True:
        go += 1
        stockwatchinfo = ""
        for stock in unique_stocks:
            stockdata = str(yf.get_quote_data(stock))

            # current price
            m = re.search("'regularMarketPrice':(.+?), 'regularMarketDayHigh'", stockdata)
            if m:
                current = float(m.group(1))
            else:
                current = yf.get_premarket_price(stock)

            # current profit
            m = re.search("'regularMarketChange':(.+?), 'regularMarketChangePercent'", stockdata)
            if m:
                open_change = round(float(m.group(1)), 2)
            else:
                open_change = 0

            # current % change
            m = re.search("'regularMarketChangePercent':(.+?), 'regularMarketTime'", stockdata)
            if m:
                open_change_percent = round(float(m.group(1)), 2)
            else:
                open_change_percent = 0

            if loopchecks == 3:
                with open(f"stocks/{stock}/{stock}_live.txt", "a+") as f:
                    f.write(f"{current:.2f} {go} {str(datetime.now())[:-4]} OPEN\n")

            if go % changedatacheck == 0:
                plot_graph(stock, f"{stock} live [time period]", 1000, 30)

            stockwatchinfo = f"{stockwatchinfo}{stock} {current:.2f} {open_change:.2f} {open_change_percent:.2f}% "

        log(f"{stockwatchinfo}  {str(datetime.now())[:-4]}")

        if go * checktime / 60 % statuscheck == 0:
            loopchecks = market_status()

        if loopchecks in range(0, 3):
            break

        time.sleep(checktime)

    if loopchecks in range(0, 3):
        log("getting latest prices...")
        go_closed = 0
        while True:
            go_closed += 1
            stockwatchinfo_closed = ""
            try:
                for stock in unique_stocks:
                    # pre market
                    if loopchecks == 1:
                        stockdata = str(yf.get_quote_data(stock))

                        # current_closed price
                        m = re.search("'preMarketPrice':(.+?), 'regularMarketChange'", stockdata)
                        if m:
                            current_closed = float(m.group(1))
                        else:
                            current_closed = yf.get_premarket_price(stock)

                        # current profit
                        m = re.search("'preMarketChange':(.+?), 'preMarketChangePercent'", stockdata)
                        if m:
                            closed_change = round(float(m.group(1)), 2)
                        else:
                            closed_change = 0

                        # current % change
                        m = re.search(", 'preMarketChangePercent':(.+?), 'preMarketTime'", stockdata)
                        if m:
                            closed_change_percent = round(float(m.group(1)), 2)
                        else:
                            closed_change_percent = 0

                    # post market
                    if loopchecks == 2:
                        stockdata = str(yf.get_quote_data(stock))

                        # current_closed price
                        m = re.search("'postMarketPrice':(.+?), 'regularMarketChange'", stockdata)
                        if m:
                            current_closed = float(m.group(1))
                        else:
                            current_closed = yf.get_premarket_price(stock)

                        # current profit
                        m = re.search("'regularMarketChange':(.+?), 'regularMarketChangePercent'", stockdata)
                        if m:
                            closed_change = round(float(m.group(1)), 2)

                        # current % change
                        m = re.search("'regularMarketChangePercent':(.+?), 'regularMarketTime'", stockdata)
                        if m:
                            closed_change_percent = round(float(m.group(1)), 2)

                    with open(f"stocks/{stock}/{stock}_live.txt", "a+") as f:
                        f.write(f"{current_closed:.2f} {go_closed} {str(datetime.now())[:-4]} POST\n")

                    if go_closed % changedatacheck/5 == 0:
                        plot_graph(stock, f"{stock} closed", 1000, 30)

                    stockwatchinfo_closed = f"{stockwatchinfo_closed}{stock} {current_closed:.2f} {closed_change} {closed_change_percent}% "
                log(f"{stockwatchinfo_closed}  {str(datetime.now())[:-4]}")
            except:
                loopchecks = market_status()

            if go_closed * checktime_closed / 60 % statuscheck == 0:
                loopchecks = market_status()

            if loopchecks == 0:
                break

            time.sleep(checktime_closed)

    log("checking stopped, the stock market has no new data to read")

stock = "TSLA"
plot_graph(stock, f"{stock} closed", 1000, 500)

log("--------------------------------------------------")
log(f"SCRIPT FINISHED EXECUTING AT {str(datetime.now())[:-4]}")
