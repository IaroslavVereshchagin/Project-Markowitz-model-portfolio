Downloading closing prices for one specific stock from the official Moscow Exchange server.

from imports import pd, requests
    

def get_moex_data(paper, day_start="2025-01-01"):
    link = f"https://moex.com{paper}.json"                            # Link to the trading history of a specific security
    params = {"from": day_start, "columns": "TRADEDATE, CLOSE"}
  
    response = requests.get(link, params = params)                    # Downloading data from the internet
    raw_json = response.json()
    
    rows = raw_json["history"]["data"]                                # We get an array of prices and dates
    table = pd.DataFrame(rows, columns = ["Date", "Close"])
  
    table.set_index("Date", inplace = True)                           # We make the date the main reference point in the line
    return table["Close"]


6. We declare a function that takes the stock ticker “paper” and an initial date as input(we take a date one calendar year earlier
so that the program can analyze how the stock behaved throughout the entire previous stable period)
7. We create a request string to the servers of the Moscow Exchange (ISS MOEX interface)
8. We set the filtering parameters — where to download from and which columns to take(TRADEDATE — trading date,
CLOSE — closing price of the day)
10. Download the raw data over the network
11. Convert the downloaded text into a convenient dictionary format in Python
13. Go deeper into the structure to the array of trading days
14. Create a Pandas table with columns 'Date'(Date) and 'Close'(Closing Price)
16. Make the date the main index of the row so that different stocks can be aligned by it later
17. Output only the price column
