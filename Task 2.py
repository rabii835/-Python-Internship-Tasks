def stock_portfolio_tracker():
    # Hardcoded stock prices
    stock_prices = {"AAPL": 180, "TSLA": 250, "GOOG": 120, "AMZN": 140, "MSFT": 200}

    print("Welcome to Stock Portfolio Tracker!")
    print("Available stocks and prices (USD):")
    for stock, price in stock_prices.items():
        print(f"{stock}: ${price}")

    total_investment = 0
    portfolio = {}

    while True:
        stock_name = input("\nEnter stock symbol (or type 'done' to finish): ").upper()
        if stock_name == "DONE":
            break
        if stock_name not in stock_prices:
            print("Invalid stock symbol. Please choose from available stocks.")
            continue

        try:
            quantity = int(input(f"Enter quantity of {stock_name}: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        cost = stock_prices[stock_name] * quantity
        total_investment += cost
        portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity
        print(f"Added {quantity} shares of {stock_name} worth ${cost}")

    print("\n----- Portfolio Summary -----")
    for stock, qty in portfolio.items():
        print(f"{stock}: {qty} shares (Price: ${stock_prices[stock]} each)")
    print("Total Investment Value: $", total_investment)

    # Optional: Save result to text file
    save_option = input("\nDo you want to save the result to a file? (yes/no): ").lower()
    if save_option == "yes":
        with open("portfolio.txt", "w") as f:
            f.write("----- Portfolio Summary -----\n")
            for stock, qty in portfolio.items():
                f.write(f"{stock}: {qty} shares (Price: ${stock_prices[stock]} each)\n")
            f.write(f"Total Investment Value: ${total_investment}\n")
        print("Portfolio saved to 'portfolio.txt'.")

if __name__ == "__main__":
    stock_portfolio_tracker()