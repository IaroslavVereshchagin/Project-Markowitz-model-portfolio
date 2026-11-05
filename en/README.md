Project Overview (English Version)

In this project, we create a program for smart investment management using the Markowitz Model and the Python development environment.

Here is a specific breakdown of what we will do:
1. First, we connect to the official servers of the Moscow Exchange (MOEX) via the Internet.
2. We download real historical stock prices of the largest companies (Sberbank, Gazprom, Lukoil).
3. We convert prices into percentage returns and calculate stock risks *(covariance matrix)*.
4. Using the Markowitz Model, we simulate 5,000 random portfolios.
5. We find the two best options: the portfolio with minimum risk and the portfolio with maximum efficiency.

* Covariance matrix is a risk table that shows how stocks fluctuate and move in price relative to each other.
