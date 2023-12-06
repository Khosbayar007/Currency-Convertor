# Define exchange rates with currency symbols
exchange_rates = {
    "USD": {"rate": 1.0, "symbol": "$"},
    "EUR": {"rate": 0.93, "symbol": "€"},
    "CAD": {"rate": 1.38, "symbol": "C$"},
    "JPY": {"rate": 151.07, "symbol": "¥"},
    "GBP": {"rate": 0.81, "symbol": "£"},
    "CHF": {"rate": 0.90, "symbol": "CHF"},
    "AUD": {"rate": 1.56, "symbol": "A$"},
    "MNT": {"rate": 3447.3, "symbol": "₮"},
    "INR": {"rate": 83.26, "symbol": "₹"},
}

# Function to perform currency conversion
def convert_currency(amount, from_currency, to_currency):
    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        return "Invalid currency selection."

    from_rate = exchange_rates[from_currency]["rate"]
    to_rate = exchange_rates[to_currency]["rate"]
    result_amount = (amount / from_rate) * to_rate
    return result_amount

# Function to ask the user if they want to convert again
def convert_again():
    return input("Do you want to convert again? (yes/no): ").lower().startswith('y')

# Perform currency conversion and ask if the user wants to convert again
while True:
    # Input currency details
    from_currency = input("Enter the source currency (USD, EUR, CAD, JPY, GBP, CHF, AUD, MNT, INR): ").upper()
    to_currency = input("Enter the target currency (USD, EUR, CAD, JPY, GBP, CHF, AUD, MNT, INR): ").upper()

    # Input amount to convert
    amount = float(input("Enter the amount to convert: "))

    # Perform the currency conversion
    result = convert_currency(amount, from_currency, to_currency)

    if isinstance(result, float):
        from_symbol = exchange_rates[from_currency]["symbol"]
        to_symbol = exchange_rates[to_currency]["symbol"]
        print(f"{amount:.2f} {from_symbol} is equal to {result:.2f} {to_symbol}")
    else:
        print(result)

    # Ask the user if they want to convert again
    if not convert_again():
        break