# Example prices for this programming exercise only.
# These are not live stock-market prices.

STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 420,
}


def main():
    total_investment = 0
    holdings = []

    print("Stock Portfolio Tracker")
    print("Example prices (not live):")
    for symbol, price in STOCK_PRICES.items():
        print(f"  {symbol}: ${price}")
    print("Enter 'done' when you have finished adding stocks.")

    while True:
        stock = input("\nStock symbol: ").upper().strip()

        if stock == "DONE":
            break

        if stock not in STOCK_PRICES:
            print("Stock not found. Choose one of the listed symbols.")
            continue

        try:
            quantity = int(input("Quantity: "))
            if quantity <= 0:
                print("Quantity must be a positive whole number.")
                continue
        except ValueError:
            print("Please enter a valid whole number.")
            continue

        investment = STOCK_PRICES[stock] * quantity
        total_investment += investment
        holdings.append((stock, quantity, investment))
        print(f"{quantity} share(s) of {stock}: ${investment}")

    print("\n--- Portfolio Summary ---")
    if not holdings:
        print("No stocks added.")
    else:
        for stock, quantity, investment in holdings:
            print(f"{stock}: {quantity} share(s) = ${investment}")
    print(f"Total investment: ${total_investment}")


if __name__ == "__main__":
    main()
