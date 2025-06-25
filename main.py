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

def list_of_accepted_filters():
    acceptable_filters_list = [
        "currentPrice","previousClose","marketCap","forwardPE","trailingPE",
        "dividendYield","fiftyTwoWeekLow","sector","beta","volume"
    ]

    #TODO USE for-loop for filter list and user filter list


def main(): 
    user_input_selection()




if __name__ == "__main__":
    main()
