Calculating the stock return as a percentage and scaling the risk matrix to an annual format.

from imports import np

def calculate_annual_metrics(table):
    steps = table.pct_change().dropna()                                     # Считаем изменение цен в процентах
    
    y_returns = steps.mean().values * 252                                   # Считаем годовую доходность(252 дня торгов в году)
    
    y_cov = steps.cov().values * 252                                        # Считаем годовую матрицу рисков (ковариацию) 
    return y_returns, y_cov
