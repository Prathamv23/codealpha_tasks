# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2800,
    "AMZN": 3500,
    "MSFT": 320
}

# Store user’s stocks and quantities
portfolio = {}  

print("Welcome to the Stock Portfolio Tracker!")
print("Available stocks and their prices:")
for stock, price in stock_prices.items():
    print(f"  {stock}: Rs.{price}")

while True:
    stock_name = input("\nEnter a stock symbol or type 'done' to finish: ").upper()
    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("This stock is not in our list. Please enter one of the available stocks.")
        continue

    quantity_input = input(f"How many shares of {stock_name} do you own? ")

    if not quantity_input.isdigit():
        print("Please enter a valid number for quantity.")
        continue

    quantity = int(quantity_input)
    portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity

# Calculate total investment value
total_value = 0
print("\nYour Portfolio Summary:")
for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    investment = price * quantity
    total_value += investment
    print(f"{stock}: {quantity} shares x Rs.{price} = Rs.{investment}")

print(f"\nTotal investment value: Rs.{total_value}")

