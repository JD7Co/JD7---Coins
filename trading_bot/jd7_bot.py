import ccxt
import time

exchange = ccxt.binance({
    'apiKey': 'YOUR_API_KEY',
    'secret': 'YOUR_SECRET_KEY',
})

symbol = 'JD7/BTC'
amount = 100  # JD7
threshold = 0.0005  # BTC

def get_price():
    ticker = exchange.fetch_ticker(symbol)
    return ticker['last']

def trade():
    price = get_price()
    if price < threshold:
        order = exchange.create_market_buy_order(symbol, amount)
        print(f"Buy order executed at {price}")
    else:
        print(f"Price too high: {price}")

while True:
    trade()
    time.sleep(60)  # Проверка каждую минуту
