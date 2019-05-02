from os import environ

# COINLORE API - https://www.coinlore.com/cryptocurrency-data-api

# Global Crypto Data - Information about crypto market
GLOBAL_CRYPTO_DATA = "https://api.coinlore.com/api/global/"

# Tickers (All Coins) - Informatin about all coins, maximum resut 100 coins per request, you should use start and limit
# The coins are organized by rank
TICKERS_ALL_COINS = "https://api.coinlore.com/api/tickers/"
# With Start and Limit
# TICKERS_ALL_COINS_SL_EXAMPLE = "https://api.coinlore.com/api/tickers/?start=(Number - Excluded)&limit=(Number <= 100)"

# Ticker (Specific Coin) - Get information for specific coin, you should pass coin id(You should use id from tickers endpoint)
# TICKER_SPECIFIC_COIN_EXAMPLE = "https://api.coinlore.com/api/ticker/?id=(an id)"
TICKER_SPECIFIC_COIN = "https://api.coinlore.com/api/ticker/?id="

# Get Markets For Coin - Returns first 50 markets for specific coin
SPECIFIC_COIN_MARKET = "https://api.coinlore.com/api/coin/markets/?id="

# All Exchanges - Get all exchanges
ALL_EXCHANGES = "https://api.coinlore.com/api/exchanges/"

# Fetch Exchange Data - Get specific exchange by ID (Returns Top 100 Pairs)
SPECIFIC_EXCHANGE_DATA = "https://api.coinlore.com/api/exchange/?id="

# Social Stats - Get social stats for coin
SOCIAL_STATS = "https://api.coinlore.com/api/coin/social_stats/?id="