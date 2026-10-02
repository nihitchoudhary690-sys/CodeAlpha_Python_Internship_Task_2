"""
CodeAlpha Python Programming Internship - Task 02
Stock Portfolio Tracker (Core Python Calculation & CLI)

Description:
A beginner-friendly console program that tracks stock holdings, calculates individual
and total portfolio investment values based on predefined manual prices, and allows
exporting portfolio summaries to a CSV file.
"""

import csv

# Manually defined sample stock prices (sample values only, not live market data)
PREDEFINED_PRICES = {
    "AAPL": 180.0,
    "TSLA": 250.0,
    "GOOGL": 150.0,
    "MSFT": 420.0,
    "AMZN": 185.0,
    "NVDA": 120.0,
    "META": 500.0,
}


def get_predefined_prices():
    """Returns a copy of the predefined stock price dictionary."""
    return PREDEFINED_PRICES.copy()


def display_available_stocks():
    """Prints the list of available stocks and their predefined sample prices."""
    print("\n" + "=" * 45)
    print("      AVAILABLE STOCKS & PREDEFINED PRICES   ")
    print("=" * 45)
    print(f"{'Stock Symbol':<15} {'Sample Price ($)':>20}")
    print("-" * 45)
    for symbol, price in PREDEFINED_PRICES.items():
        print(f"{symbol:<15} ${price:>19.2f}")
    print("=" * 45)


def calculate_stock_investment(quantity, price):
    """
    Calculates the investment value of a stock.
    Formula: Investment Value = Quantity * Stock Price
    """
    return quantity * price


def add_stock_to_portfolio(portfolio, symbol, quantity):
    """
    Validates and adds/updates a stock in the portfolio dictionary.
    
    Args:
        portfolio (dict): Current portfolio dictionary.
        symbol (str): Stock ticker symbol.
        quantity (int or float): Number of shares purchased.
        
    Returns:
        tuple: (bool success, str message)
    """
    symbol = symbol.strip().upper()

    # Validate stock symbol
    if symbol not in PREDEFINED_PRICES:
        return False, f"Stock '{symbol}' is not available in the predefined list."

    # Validate quantity
    if quantity <= 0:
        return False, "Quantity must be a positive number greater than 0."

    price = PREDEFINED_PRICES[symbol]

    if symbol in portfolio:
        portfolio[symbol]["quantity"] += quantity
        portfolio[symbol]["investment_value"] = calculate_stock_investment(
            portfolio[symbol]["quantity"], price
        )
        msg = f"Updated '{symbol}': New quantity is {portfolio[symbol]['quantity']} shares."
    else:
        investment_value = calculate_stock_investment(quantity, price)
        portfolio[symbol] = {
            "symbol": symbol,
            "quantity": quantity,
            "price": price,
            "investment_value": investment_value,
        }
        msg = f"Added '{symbol}': {quantity} shares at ${price:.2f} each."

    return True, msg


def calculate_total_investment(portfolio):
    """Calculates the total investment value across all stocks in the portfolio."""
    return sum(item["investment_value"] for item in portfolio.values())


def display_portfolio(portfolio):
    """Displays a clean tabular overview of current holdings and total value."""
    if not portfolio:
        print("\n[!] Your portfolio is currently empty.")
        return

    print("\n" + "=" * 65)
    print("                    YOUR STOCK PORTFOLIO                     ")
    print("=" * 65)
    print(f"{'Symbol':<10} {'Quantity':>12} {'Price ($)':>15} {'Total Value ($)':>20}")
    print("-" * 65)

    for item in portfolio.values():
        print(
            f"{item['symbol']:<10} "
            f"{item['quantity']:>12} "
            f"${item['price']:>14.2f} "
            f"${item['investment_value']:>19.2f}"
        )

    total_value = calculate_total_investment(portfolio)
    print("-" * 65)
    print(f"{'TOTAL PORTFOLIO VALUE:':<38} ${total_value:>21.2f}")
    print("=" * 65)


def save_portfolio_to_csv(portfolio, filename="portfolio.csv"):
    """
    Exports the portfolio holdings and total investment to a CSV file.
    
    Args:
        portfolio (dict): Current portfolio dictionary.
        filename (str): Target CSV file path.
    """
    if not portfolio:
        print("\n[!] Cannot export empty portfolio.")
        return False

    try:
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Symbol", "Quantity", "Price ($)", "Investment Value ($)"])
            for item in portfolio.values():
                writer.writerow(
                    [
                        item["symbol"],
                        item["quantity"],
                        f"{item['price']:.2f}",
                        f"{item['investment_value']:.2f}",
                    ]
                )
            writer.writerow([])
            writer.writerow(
                ["Total Portfolio Value", "", "", f"{calculate_total_investment(portfolio):.2f}"]
            )
        print(f"\n[+] Portfolio successfully saved to '{filename}'.")
        return True
    except Exception as e:
        print(f"\n[-] Error saving to CSV: {e}")
        return False


def run_cli():
    """Interactive command-line interface loop for testing and user interaction."""
    portfolio = {}

    print("=" * 55)
    print("   CODEALPHA TASK 02: STOCK PORTFOLIO TRACKER (CLI)   ")
    print("=" * 55)

    while True:
        print("\nMain Menu:")
        print("1. View Available Stocks & Prices")
        print("2. Add / Update Stock Holding")
        print("3. View Portfolio Summary")
        print("4. Save Portfolio to CSV")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            display_available_stocks()

        elif choice == "2":
            symbol = input("Enter Stock Symbol (e.g., AAPL, TSLA): ").strip().upper()
            qty_input = input("Enter Quantity of shares: ").strip()

            try:
                quantity = int(qty_input)
            except ValueError:
                print("[!] Invalid quantity! Please enter a valid whole number.")
                continue

            success, message = add_stock_to_portfolio(portfolio, symbol, quantity)
            if success:
                print(f"[+] {message}")
            else:
                print(f"[!] {message}")

        elif choice == "3":
            display_portfolio(portfolio)

        elif choice == "4":
            filename = input("Enter filename (default: portfolio.csv): ").strip()
            if not filename:
                filename = "portfolio.csv"
            save_portfolio_to_csv(portfolio, filename)

        elif choice == "5":
            print("\nThank you for using Stock Portfolio Tracker!")
            break

        else:
            print("[!] Invalid option. Please select 1 to 5.")


if __name__ == "__main__":
    run_cli()
