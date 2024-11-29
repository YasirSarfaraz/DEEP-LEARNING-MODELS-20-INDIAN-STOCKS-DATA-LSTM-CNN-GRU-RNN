import yfinance as yf
sectors = {
    "Communication Services": ['BHARTIARTL.NS', 'RELIANCE.NS', 'IDEA.NS', 'TATACOMM.NS'],
    "Consumer Cyclical": ['TATAMOTORS.NS', 'M&M.NS', 'MARUTI.NS', 'EICHERMOT.NS'],
    "Energy": ['RELIANCE.NS', 'ONGC.NS', 'IOC.NS', 'BPCL.NS'],
    "Healthcare": ['SUNPHARMA.NS', 'DRREDDY.NS', 'CIPLA.NS', 'DIVISLAB.NS'],
    "Technology": ['INFY.NS', 'TCS.NS', 'WIPRO.NS', 'HCLTECH.NS']
}
for sector, tickers in sectors.items():
    print(f"Downloading data for {sector} sector")
    for ticker in tickers:
        stock_data = yf.download(ticker)
        output_filename = f"{ticker}.csv"
        stock_data.to_csv(output_filename)
        print(f"Data for {ticker} saved as '{output_filename}'.")
print("All data downloaded")
