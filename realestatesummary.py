# Convert price string with 'k' to thousands or 'm' to millions.
def parse_price(price_str):
    try:
        # Convert to lowercase and remove leading/trailing whitespace
        price_str = price_str.lower().strip()
        # Check if the price string ends with 'k'
        if price_str.endswith('k'):
            # Convert the price to an integer by removing 'k' and multiplying by 1000
            return int(float(price_str[:-1]) * 1000)
        # Check if the price string ends with 'm'
        elif price_str.endswith('m'):
            # Convert the price to an integer by removing 'm' and multiplying by 1000000
            return int(float(price_str[:-1]) * 1000000)
        # Convert the price to an integer
        return int(price_str)
    # Handle invalid inputs
    except ValueError:
        print(f"Invalid input: {price_str}")
        return 0

# Get inputs
current_price = parse_price(input("Please enter the house's current price: "))
last_month_price = parse_price(input("Please enter last month's price: "))

# Calculate the change in price
price_change = current_price - last_month_price

# Get the mortgage rate and convert it to a decimal
mortgage_rate = float(input("Enter the mortgage rate (e.g., 4.5 for 4.5%): ")) / 100

# Calculate the estimated monthly mortgage
estimated_mortgage = (current_price * mortgage_rate) / 12

# Print the summary
print(f"This house's current price is ${current_price:,.0f}. The price has changed by ${price_change:,.0f}, and the estimated monthly mortgage is ${estimated_mortgage:,.2f}.")