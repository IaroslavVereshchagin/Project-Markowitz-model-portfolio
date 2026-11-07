Combining the prices of several stocks into a single, comprehensive data table.

from imports import pd
from api_loader import get_moex_data

def make_portfolio_table(list_papers):
    main_table = pd.DataFrame()                                      # Create an empty base for the table
  
    for paper in list_papers:                                        # We go through each stock in a cycle and adjust the prices.
        main_table[paper] = get_moex_data(paper)
        
    return main_table.dropna()                                       # We exclude the weekend days when the exchange wasn’t operating.




6. The function takes a list of stock tickers as input (for example, "SBER", "GAZP", "LKOH").
7. We create an empty table where we will combine the data.
9. We run a loop that takes each stock from our list in turn.
10. It calls the download function from File 2 and writes the prices to the column under the name of the current stock.
12. dropna() is the most important command that finds rows containing empty cells(for example, during holidays, Sber traded,
but Lukoil did not) and completely removes them. The result is a perfectly even table without any gaps.
