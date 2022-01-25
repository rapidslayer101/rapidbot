import time, datetime, os, re
import yahoo_fin.stock_info as yf
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from discord_webhook import DiscordWebhook
from forex_python.converter import CurrencyRates
from forex_python.converter import CurrencyCodes

from twilio.rest import Client
account_sid = "ACb558feef19198d8ccfe96ca8220dd189"
auth_token = "10cde7f7f64ada3f43c90a4d721bd1ac"
client = Client(account_sid, auth_token)

## LOGGING ##

start_time = time.time()
start_time_standard = datetime.now()

with open(f"output/logs.txt", "w") as f:
    f.write("")


def log(text):
    print(text)
    with open("output/logs.txt", "a+", encoding="utf-8") as f:
        try:
            write = f"{str(datetime.now())[:-4]} RUNTIME: {round(time.time() - start_time, 2):.2f} | {text}\n"
            f.write(write)
        except:
            write = f"{str(datetime.now())[:-4]} RUNTIME: {round(time.time() - start_time, 2):.2f} | PRINTING ERROR\n"
            f.write(write)


## SETTINGS ##

discord_webhook_url = "https://discord.com/api/webhooks/816688140755664936/CZ4O2nEis1mRByptt5kJMT19qsLtMJebu-xej7YudoJBhl6MsDQXU5VsA5WNoYfJpTFH"

# stocks to watch #
stocks = ["CCIV", "TSLA", "BP"]
# "CCIV", "TSLA", "INRG", "BP"

# the amount of the stocks you own (shares/dollars)
stocks_own = ["", "6", ""]
purchase_price = ["", "2927.66", ""]


# watch live stock price data #
stockwatch = 1

if stockwatch == 1:

    # how often to check stocks list (seconds) #
    checktime = 1           # when market "open"
    checktime_closed = 5    # when market in "POST" or "PRE"

    # how often to check market status (mins) #
    statuscheck = 5

    # how often to check stock change data (seconds) #
    changedatacheck = 320


## SETTINGS LOGGING ##

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


def text(user, message):
    message = client.messages.create(to="+447597299247", from_="+15155188444",
    body="EXAMPLE BITCOIN NOTIFICATION MESSAGE")


log("Bot started with settings:")
log(f"├─> Stocks({len(stocks)}): {stocks}")
stcounter1 = 0
#try:
for stock in stocks:
    if not stocks_own[stcounter1] == "":
        log(f"│   ├─> Registered owning of {stocks_own[stcounter1]} shares of {stock}")
        if not purchase_price[stcounter1] == "":
            log(f"│   │   └─> Buy price for {stocks_own[stcounter1]}x {stock} at {purchase_price[stcounter1]}")
            current_profit(bought=float(purchase_price[stcounter1]), current=yf.get_live_price(stock), amount=stocks_own[stcounter1])
        else:
            log(f"│   │   └─> Buy price missing, please add in settings")
    stcounter1 = stcounter1 + 1
log("│   └─> Total portfolio information:")
log("│       ├─> Buy price:")
log("│       ├─> Current value:")
log("│       └─> Profit:")
#except:
log(f"│   └─> Could not read owned stock information, this is likely due to to a lack of fields in the settings")
if stockwatch == 1:
    log("└─> Stockwatch ON, settings:")
    log(f"    ├─> How often to check live stocks: every {checktime}s")
    log(f"    ├─> How often to check closed stocks: every {checktime_closed}s")
    log(f"    └─> How often to check the current market status: every {statuscheck}m")
if stockwatch == 0:
    log("└─> Stockwatch OFF")


## DEFINING ##


def plotgraph(stock, name, readback):
    with open(f'stocks/{stock}/{stock}.txt') as f:
        lines = f.readlines()
        linenum = 0
        for line in lines:
            linenum = linenum + 1
        line_st = linenum - readback
        y = [round(float(line.split()[0]), 2) for line in lines[line_st:]]
        x = [line.split()[1] for line in lines[line_st:]]

        #first_line = lines[0]
        #last_line = lines[-1]
        #log(f"FIRST: {first_line}")
        #log(f"LAST: {last_line}")

    plt.style.use("dark_background")
    ax1 = plt.figure().add_subplot(111)

    ax1.set_title(f"STOCK: {stock}")
    ax1.plot(x, y, c='r', label='share price')

    plt.savefig(f'stocks/{stock}/{stock}.png')
    plt.close()

    #webhook = DiscordWebhook(url=discord_webhook_url, content=name)
    #with open(f'stocks/{stock}/{stock}.png', "rb") as f:
        #webhook.add_file(file=f.read(), filename=f'{stock}.png')
    #webhook.execute()

## FOLDER CREATION ##


log("--------------------------------------------------")
for stock in stocks:
    log(f"Checking directory paths for {stock}")
    if not os.path.exists(f'stocks/{stock}'):
        os.makedirs(f'stocks/{stock}')
        log("└─> Directory missing, now been added")
    else:
        log("└─> Directory present")


## STOCK MARKET INFORMATION ##


def market_status():
    log("--------------------------------------------------")
    stock_market_status = yf.get_market_status()

    if stock_market_status == "POSTPOST":
        stock_market_status = "CLOSED (popo)"
        loopchecks = 0
    if stock_market_status == "POST":
        stock_market_status = "POST-MARKET"
        loopchecks = 2

    if stock_market_status == "PREPRE":
        stock_market_status = "CLOSED (pepe)"
        loopchecks = 0
    if stock_market_status == "PRE":
        stock_market_status = "PRE-MARKET"
        loopchecks = 1

    if stock_market_status == "CLOSED":
        loopchecks = 0

    if stock_market_status == "REGULAR":
        stock_market_status = "OPEN"
        loopchecks = 3
    if stock_market_status == "OPEN":
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


## CHECKING OLD STOCK DATA ##


log("Collecting old stock data")
date = datetime.now()

date_1d = date - timedelta(days=10)
date_1d = str(date_1d)[:10]

date_begin = date - timedelta(weeks=2609)
date_begin = str(date_begin)[:10]

date = str(date)[:10]


def datacollect(start_date, end_date, stock, run):
    runs = len(stocks)
    stockdata_1d = yf.get_data(start_date=start_date, end_date=end_date, ticker=stock)
    try:
        datacollect_go = 0
        with open(f"stocks/{stock}/{stock}-all_1d.txt", "w") as f:
            while True:
                datacollect_go = datacollect_go + 1
                stockdata_1d_write = stockdata_1d['close'].values[datacollect_go]
                stockdata_1d_write = f"{round(stockdata_1d_write,2)}\n"
                f.write(stockdata_1d_write)
    except:
        if run == runs:
            log(f"└─> {stock} data successfully collected from {start_date} to {end_date}, total entries {datacollect_go-1}")
        else:
            log(f"├─> {stock} data successfully collected from {start_date} to {end_date}, total entries {datacollect_go-1}")


run = 0
for stock in stocks:
    run = run + 1
    #datacollect(start_date=date_1d, end_date=date, stock=stock, run=run) # data collect 1d
    datacollect(start_date=date_begin, end_date=date, stock=stock, run=run)  # data collect 1d all
    #print(yf.get_stats(stock))
    #print(yf.get_quote_data(stock))

## CHECKING LIVE STOCKS ##

if stockwatch == 1:

    if loopchecks in range(0, 3):
        log("getting close prices...")

    for stock in stocks:
        with open(f"stocks/{stock}/{stock}.txt", "w") as f:
            f.write("")

    go = 0
    while True:
        go = go + 1
        stockwatchinfo = ""
        for stock in stocks:
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
                with open(f"stocks/{stock}/{stock}.txt", "a+") as f:
                    f.write(f"{current:.2f} {go} {str(datetime.now())[:-4]} OPEN\n")

            if go % changedatacheck == 0:
                plotgraph(stock=stock, name=f"{stock} live [time period]", readback=30)

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
            go_closed = go_closed + 1
            stockwatchinfo_closed = ""
            try:
                for stock in stocks:
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

                    with open(f"stocks/{stock}/{stock}.txt", "a+") as f:
                        f.write(f"{current_closed:.2f} {go_closed} {str(datetime.now())[:-4]} POST\n")

                    if go_closed % changedatacheck/5 == 0:
                        plotgraph(stock=stock, name=f"{stock} closed", readback=30)

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

#stock = "TSLA"
#plotgraph(stock=stock, name=f"{stock} closed")

log("--------------------------------------------------")
log(f"SCRIPT FINISHED EXECUTING AT {str(datetime.now())[:-4]}")
f.close()
os.startfile(f"C:/Users/rapid/PycharmProjects/plzwork/output/logs.txt")