import math

def calculate_option_price(asset_price, strike_price, time_to_expiration, risk_free_rate, volatility, option_type):
    d1 = (math.log(asset_price / strike_price) + (risk_free_rate + 0.5 * volatility**2) * time_to_expiration) / (volatility * math.sqrt(time_to_expiration))
    d2 = d1 - volatility * math.sqrt(time_to_expiration)

    if option_type == "call":
        option_price = asset_price * norm_cdf(d1) - strike_price * math.exp(-risk_free_rate * time_to_expiration) * norm_cdf(d2)
        delta = norm_cdf(d1)
        gamma = norm_pdf(d1) / (asset_price * volatility * math.sqrt(time_to_expiration))
    elif option_type == "put":
        option_price = strike_price * math.exp(-risk_free_rate * time_to_expiration) * norm_cdf(-d2) - asset_price * norm_cdf(-d1)
        delta = norm_cdf(d1) - 1
        gamma = norm_pdf(d1) / (asset_price * volatility * math.sqrt(time_to_expiration))
    else:
        raise ValueError("Invalid option type. Must be either 'call' or 'put'.")

    return option_price, delta, gamma

def norm_cdf(x):
    return (1 + math.erf(x / math.sqrt(2))) / 2

def norm_pdf(x):
    return math.exp(-0.5 * x**2) / math.sqrt(2 * math.pi)

def get_user_input(prompt):
    return input(prompt)

def display_option_price(option_price, delta, gamma):
    print("The calculated option price is:", option_price)
    print("Delta:", delta)
    print("Gamma:", gamma)

def main():
    print("Welcome to the Option Pricer!")

    # Get user inputs
    asset_price = float(get_user_input("Enter the current asset price: "))
    strike_price = float(get_user_input("Enter the strike price: "))
    time_to_expiration = float(get_user_input("Enter the time to expiration (in years): "))
    risk_free_rate = float(get_user_input("Enter the risk-free interest rate: "))
    volatility = float(get_user_input("Enter the volatility: "))
    option_type = get_user_input("Enter the option type (call/put): ")

    # Calculate option price, delta, and gamma
    option_price, delta, gamma = calculate_option_price(asset_price, strike_price, time_to_expiration, risk_free_rate, volatility, option_type)

    # Display the calculated option price, delta, and gamma
    display_option_price(option_price, delta, gamma)

if __name__ == '__main__':
    main()
