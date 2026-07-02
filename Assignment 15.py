import yfinance as yf

def get_stock(symbol):
    try:
        ticker = yf.Ticker(symbol)
        data = ticker.history(period="1d")
        
        if data.empty:
            print("Error: Ticker not found.")
            return

        latest = data.iloc[-1]
        print(f"Symbol: {symbol.upper()}")
        print(f"Price:  ${latest['Close']:.2f}")
        print(f"Volume: {int(latest['Volume'])}")
        
    except Exception as e:
        print(f"Network or System Error: {e}")

if __name__ == "__main__":
    get_stock("AAPL")
    get_stock("INVALID_SYMBOL")
