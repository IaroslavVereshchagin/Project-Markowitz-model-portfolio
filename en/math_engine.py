Calculating the stock return as a percentage and scaling the risk matrix to an annual format.

from imports import np

def calculate_annual_metrics(table):
    steps = table.pct_change().dropna()                                     # We calculate the price change as a percentage.
    
    y_returns = steps.mean().values * 252                                   # We calculate the annual return (252 trading days per year)
    
    y_cov = steps.cov().values * 252                                        # We calculate the annual risk matrix (covariance)
    return y_returns, y_cov





6. The .pct_change().dropna() command divides today’s price by yesterday’s and subtracts one. We get the daily
return on the stock in percentage terms (daily asset returns).
8. We calculate the average growth percentage per day and multiply it by 252 — the number of trading days on the exchange in a year.
We get the expected annual return on the stock.
10. The .cov - command calculates the covariance matrix (risk relationships) of the assets.
We multiply it by 252 to convert the risks from a daily scale to an annual format (the number 252 is a standard in financial mathematics).
