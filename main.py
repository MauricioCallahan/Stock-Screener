# This program will take a list of filters and will find stocks that find its parameters
import yfinance as yf
import constant as const_var
import error_manager

from SimplifyClases import MyInput
from FilterManager import FilterManager

# TODO make each function return a bool to have self-validating ways to make sure everything is working correctly
def main():
    print("""
    Hello, Welcome to the Stock Screener
    ------------------------------------
    What would you like to do?
          
    1. Input filters
    2. See list of accepted filters
    """)
    choice = input()

    if choice == "1":
        while True:
            file = input("Input File: ")
            manager = FilterManager(file)
            manager.load_filters()
            manager.fix_rejected_filters()
            # If issue with file then loop
            if not error_manager.get_file_error(): break
    
    elif choice == "2":
        print("The accepted filters are: ")
        for filter in const_var.ACCEPTABLE_FILTERS_LIST:
            print(filter)


if __name__ == "__main__": main()


