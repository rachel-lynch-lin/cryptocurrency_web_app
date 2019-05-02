from model import GlobalCD
from consts import GLOBAL_CRYPTO_DATA, TICKERS_ALL_COINS, TICKER_SPECIFIC_COIN, SPECIFIC_COIN_MARKET, ALL_EXCHANGES, SPECIFIC_EXCHANGE_DATA, SOCIAL_STATS
import requests

# Need to replace bitcoin as a variable. Left here to test the API requests.

def get_global_crypto_data():
    """Gathers general data about the cryptocurrrency market"""

    print("Global cryptocurrency market")

    request = requests.get(GLOBAL_CRYPTO_DATA)
    request_json = request.json()
    print(request_json)
    return request_json

get_global_crypto_data()

def get_tickers_all_coins():
    """Information about all coins, maximum result 100 coins per request, should use start and limit"""

    print("Ticker for a range of all coins")
    start = "?start="
    start_at = 1        # Need to turn into a variable later
    limit = "&limit="
    limit_at = 2        # Need to turn into a variable later

    if start_at:
        print("Start at " + str(start_at))
        start_and_limit = (TICKERS_ALL_COINS + start + str(start_at) + limit + str(limit_at))
        request = requests.get(start_and_limit)
        request_json = request.json()
        print(request_json['data'])
        return request_json['data']

    # Need to add a case if they also want to include the first one. 

    else:
        print("First 100 coins")
        request = requests.get(TICKERS_ALL_COINS)
        request_json = request.json()
        print(request_json['data'])
        return request_json['data']

get_tickers_all_coins()

def get_ticker_specific_coin():
    """Get information for a specific coin, you should pass coin id(Your should use id from tickers endpoint)"""

    print("Specific Coin Ticker")
    
    request = requests.get(TICKER_SPECIFIC_COIN + str(90))
    request_json = request.json()
    print(request_json)
    return request_json

get_ticker_specific_coin()

def get_market_for_coin():
    """Returns first 50 markets for specific coin"""

    print("Specific Coin Market")
    
    request = requests.get(SPECIFIC_COIN_MARKET + str(90))
    request_json = request.json()
    print(request_json)
    return request_json

get_market_for_coin()

def get_all_exchanges():
    """Get all exchanges"""

    print("Get All Exchanges")
    request = requests.get(ALL_EXCHANGES)
    request_json = request.json()
    print(request_json)
    return request_json

get_all_exchanges()

def get_specific_exchange():
    """Get a specific exchange data"""

    print("Get Specific Exchanges")
     
    request = requests.get(SPECIFIC_EXCHANGE_DATA + str(90))
    request_json = request.json()
    print(request_json)
    return request_json

get_specific_exchange()

def get_social_stats():
    """Get social stats for coin"""
    
    print("Get Specific Social Stats")

     
    request = requests.get(SOCIAL_STATS + str(90))
    request_json = request.json()
    print(request_json)
    return request_json

get_social_stats()