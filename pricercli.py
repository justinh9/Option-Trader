import math

def calculate_option_price(asset_price, strike_price, time_to_expiration, risk_free_rate, volatility, option_type):
    d1 = (math.log(asset_price / strike_price) + (risk_free_rate + 0.5 * volatility**2) * time_to_expiration) / (volatility * math.sqrt(time_to_expiration))
    d2 = d1 - volatility * math.sqrt(time_to_expiration)

    if option_type == "call":
        option_price = asset_price * norm_cdf(d1) - strike_price * math.exp(-risk_free_rate * time_to_expiration) * norm_cdf(d2)
    elif option_type == "put":
        option_price = strike_price * math.exp(-risk_free_rate * time_to_expiration) * norm_cdf(-d2) - asset_price * norm_cdf(-d1)
    else:
        raise ValueError("Invalid option type. Must be either 'call' or 'put'.")

    return option_price

def norm_cdf(x):
    return (1 + math.erf(x / math.sqrt(2))) / 2

def get_user_input(prompt):
    return input(prompt)

def display_option_price(option_price):
    print("The calculated option price is:", option_price)

def main():
    print("Welcome to the Option Pricer!")

    # Get user inputs
    asset_price = float(get_user_input("Enter the current asset price: "))
    strike_price = float(get_user_input("Enter the strike price: "))
    time_to_expiration = float(get_user_input("Enter the time to expiration (in years): "))
    risk_free_rate = float(get_user_input("Enter the risk-free interest rate: "))
    volatility = float(get_user_input("Enter the volatility: "))
    option_type = get_user_input("Enter the option type (call/put): ")

    # Calculate option price
    option_price = calculate_option_price(asset_price, strike_price, time_to_expiration, risk_free_rate, volatility, option_type)

    # Display the calculated option price
    display_option_price(option_price)

if __name__ == '__main__':
    main()
