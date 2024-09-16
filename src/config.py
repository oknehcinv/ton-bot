BOT_TOKEN = 'BOT TOKEN'
DEPOSIT_ADDRESS = 'DEPOSIT ADDRESS'
API_KEY = 'API KEY'
RUN_IN_MAINNET = True  # Switch True/False to change mainnet to testnet

if RUN_IN_MAINNET:
    API_BASE_URL = 'https://toncenter.com'
else:
    API_BASE_URL = 'https://testnet.toncenter.com'
