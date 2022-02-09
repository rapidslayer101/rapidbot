import time, datetime, os, re  # inbuilt

# import yfinance as yf1
import matplotlib.pyplot as plt
import yahoo_fin.stock_info as yf
import numpy as np
from datetime import datetime, timedelta
# from discord_webhook import DiscordWebhook
from forex_python.converter import CurrencyRates

from enclib import search  # custom lib


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

c = CurrencyRates()
rate = c.get_rate("GBP", "USD")
to_gbp = 1/rate


class users:
    def add_user(self, user):
        user_list.append(user)
        user_stock_data.append({})

    def get_user_stocks(self, user):
        return user_stock_data[user_list.index(user)]

    def get_user_stock(self, user, stock):
        return user_stock_data[user_list.index(user)][stock]

    def buy_stock(self, users_, stock, amount_buy, buy_cost, avg_price, ex_rate, buy_time):
        if stock not in unique_stocks:
            unique_stocks.append(stock)
        for user in users_:
            amount_buy_ = amount_buy
            if stock in user_stock_data[user_list.index(user)]:
                old_data = user_stock_data[user_list.index(user)][stock]
                buy_prices = old_data[0][2]+(buy_cost*ex_rate)
                buy_prices_lc = old_data[0][3]+buy_cost
                amount_buy_ += old_data[0][0][0]
            else:
                buy_prices = buy_cost*ex_rate
                buy_prices_lc = buy_cost
            amount_own = amount_buy_
            user_stock_data[user_list.index(user)]\
                .update({stock: [[[float(amount_buy_), float(amount_own)],
                                  float(avg_price), round(buy_prices, 4), round(buy_prices_lc, 4), buy_time], []]})

    def sell_stock(self, users_, stock, amount_sell, sell_price, result, sell_time):
        for user in users_:
            sales = user_stock_data[user_list.index(user)][stock][1]
            sales.append([float(amount_sell), float(sell_price*rate), result, sell_time])
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


# fee is in GBP
# buy price is in local stock currency
if new_values:
    without_deposit_fee = 70  # amount in GBP of money without deposit fee
    users.add_user(0, "Scott")
    users.add_user(0, "David")

    #                   Users   Ticker StkAmt BuyCost AvgPce FxFee  FXFee   BuyTime
    users.buy_stock(0, ["Scott"], "AMD", 0.03, 2.31, 103.31, 1.3372, "27-01-22-18:47")
    users.buy_stock(0, ["Scott"], "AMD", 0.07, 5.43, 103.61, 1.33766, "27-01-22-18:51")
    users.buy_stock(0, ["Scott"], "AMD", 0.15, 11.58, 103.08, 1.33785, "27-01-22-19:32")
    users.buy_stock(0, ["Scott"], "AMD", 0.20, 15.01, 100.62, 1.34256, "28-01-22-14:42")
    users.buy_stock(0, ["Scott"], "AMD", 0.25, 18.66, 101.36, 1.34258, "28-01-22-14:54")
    users.buy_stock(0, ["Scott"], "INTC", 0.5, 17.38, 46.54, 1.34123, "28-01-22-15:11")
    users.buy_stock(0, ["Scott"], "MSFT", 1.0, 227.79, 306.90, 1.34931, "01-02-22-14:47")
    users.buy_stock(0, ["David"], "MSFT", 1.0, 227.67, 307.11, 1.35094, "01-02-22-16:11")
    users.buy_stock(0, ["Scott", "David"], "AMZN", 0.09, 199.52, 2989.06, 1.35032, "01-02-22-16:16")
    users.buy_stock(0, ["Scott", "David"], "PYPL", 0.5, 48.80, 132.13, 1.35607, "02-02-22-16:35")
    users.buy_stock(0, ["Scott", "David"], "BRK-B", 0.5, 117.26, 317.65, 1.35656, "02-02-22-16:58")
    users.sell_stock(0, ["Scott", "David"], "PYPL", 0.5, 128.68, 1.45, "02-02-22-16:58")
    users.buy_stock(0, ["Scott", "David"], "AMZN", 0.035, 73.715, 2953.60, 1.36109, "02-02-22-16:58")

    print("unique stock", unique_stocks)
    print(user_stock_data)
    users.save(0)

#users.load(0)
#print(user_stock_data)

profit_list = [0 for x in range(len(user_list))]
spend_list = [0 for x in range(len(user_list))]
for stock_name in unique_stocks:
    lv_stock = yf.get_quote_data(stock_name)
    market_price = lv_stock["regularMarketPrice"]
    # stock_val = lv_stock["postMarketPrice"]
    for user in user_list:
        try:
            u_stock = user_stock_data[user_list.index(user)][stock_name]
            if u_stock[0][0][1] != 0:
                stock_val = market_price*u_stock[0][0][1]
                try:
                    full_name = lv_stock['displayName']
                except KeyError:
                    full_name = lv_stock['longName']
                fx_impact = round(u_stock[0][2]/u_stock[0][3]/rate, 5)
                price = u_stock[0][2]*0.9985  # back to price without fx fee
                profit = price*(1+(((stock_val/price)*100-100)-(100-(fx_impact*100)))/100)-u_stock[0][2]
                #profit = (profit-(u_stock[0][2]*0.0015))*to_gbp  # final fees
                profit = profit*to_gbp

                print(f"{full_name} ({stock_name}) -- "
                      f"{round(u_stock[0][1]/rate*u_stock[0][0][1], 2)} -> "
                      f"{round(market_price/rate*u_stock[0][0][1], 2)} -- "
                      f"£{round(profit, 2)} "
                      f"({round(((stock_val/u_stock[0][2])*100-100)-(100-(fx_impact*100)), 2):.2f}%) "
                      f"(sk{round((stock_val/u_stock[0][2])*100-100, 2)}%)(fx{round(100-(fx_impact*100), 2)*(-1)}%)")
                profit_list[user_list.index(user)] = round(profit_list[user_list.index(user)]+profit, 4)
                spend_list[user_list.index(user)] = round(spend_list[user_list.index(user)]+u_stock[0][2], 4)
        except KeyError:
            pass  # this pass means that user does not own that stock
print(profit_list)
all_prof = 0
all_spend = 0
all_end = 0
rate = 1/rate

for profit in profit_list:
    user_spend = spend_list[profit_list.index(profit)]*to_gbp
    all_prof += profit
    all_spend += user_spend
    all_end += user_spend+profit
    print(f"{user_list[profit_list.index(profit)]}'s profit: £{round(user_spend, 2)} "
          f"-> £{round(user_spend+profit, 2)} -- "
          f"£{round(profit, 2)} ({round((user_spend+profit)/user_spend*100, 2)}%)")
print(f"Total user profit: £{round(all_spend, 2)} -> £{round(all_end, 2)} -- "
      f"£{round(all_prof, 2)} ({round(all_end/all_spend*100, 2)}%)")





# OLD INVEST CODE BELOW

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


update_stocks = False

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
            try:
                m = re.search("'regularMarketPrice':(.+?), 'regularMarketDayHigh'", stockdata)
                if m:
                    current = float(m.group(1))
                else:
                    current = yf.get_premarket_price(stock)
            except ValueError:
                m = re.search("'regularMarketPrice':(.+?), 'regularMarketTime'", stockdata)
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
