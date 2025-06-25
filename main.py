# This program will take a list of filters and will find stocks that find its parameters
import yfinance as yf
def user_input_selection():
    print("""
    Hello, Welcome to the Stock Screener
    ------------------------------------
    What would you like to do?
    
    1. Input filters
    2. See list of accepted filters
    """)
    return input()

def print_acceptable_filter():
    pass

def main():
    user_input = user_input_selection()

    if user_input == "1": pass
    if user_input == "2": pass


if __name__ == "__main__": main()
