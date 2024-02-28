import yfinance as yf

class StockPortfolioTracker:
    def __init__(self):
        self.portfolio = {}

    def add_stock(self, symbol, shares):
        if symbol in self.portfolio:
            self.portfolio[symbol]['Shares'] += shares
        else:
            self.portfolio[symbol] = {'Shares': shares, 'Cost Basis': 0}

    def remove_stock(self, symbol, shares):
        if symbol in self.portfolio and self.portfolio[symbol]['Shares'] >= shares:
            self.portfolio[symbol]['Shares'] -= shares
            if self.portfolio[symbol]['Shares'] == 0:
                del self.portfolio[symbol]
            print(f"Successfully removed {shares} shares of {symbol}")
        else:
            print(f"Error: Not enough shares of {symbol} to sell")

    def update_portfolio(self):
        for symbol in self.portfolio:
            try:
                stock_data = yf.Ticker(symbol).info
                self.portfolio[symbol]['Current Price'] = stock_data['last_price']
                self.portfolio[symbol]['Market Value'] = self.portfolio[symbol]['Shares'] * stock_data['last_price']
                self.portfolio[symbol]['Cost Basis'] = self.portfolio[symbol]['Shares'] * stock_data['previous_close']
            except KeyError:
                print(f"Error fetching data for {symbol}")

    def display_portfolio(self):
        print("Stock Portfolio:")
        print("{:<10} {:<10} {:<15} {:<15} {:<15}".format("Symbol", "Shares", "Current Price", "Market Value", "Cost Basis"))
        for symbol, data in self.portfolio.items():
            current_price = data.get('Current Price', '$300')
            market_value = data.get('Market Value', '$450')
            cost_basis = data.get('Cost Basis', '$400')
            print("{:<10} {:<10} {:<15} {:<15} {:<15}".format(symbol, data['Shares'], current_price, market_value, cost_basis))

if __name__ == "__main__":
    portfolio_tracker = StockPortfolioTracker()

    # Example: Adding and removing stocks
    portfolio_tracker.add_stock("AAPL", 10)
    portfolio_tracker.add_stock("GOOGL", 5)
    portfolio_tracker.display_portfolio()

    portfolio_tracker.remove_stock("AAPL", 3)
    portfolio_tracker.display_portfolio()

    # Update portfolio with real-time data
    portfolio_tracker.update_portfolio()
    portfolio_tracker.display_portfolio()

