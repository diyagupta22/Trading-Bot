# Trading Bot (Binance Futures Testnet)

# Setup

1. Clone repo
2. Install dependencies:
   pip install -r requirements.txt

3. Create .env file:
   API_KEY=your_api_key
   API_SECRET=your_secret_key
   BASE_URL=https://testnet.binancefuture.com

# Run

#  Market Order
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002

# Limit Order
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.002 --price 60000

# Features
- Market & Limit orders
- CLI input
- Logging
- Error handling


-diya gupta