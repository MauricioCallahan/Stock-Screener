# This program will take a list of filters and will find stocks that find its parameters
import yfinance as yf
import constant as const_var

def user_input_selection():
    print("""
    Hello, Welcome to the Stock Screener
    ------------------------------------
    What would you like to do?
    
    1. Input filters
    2. See list of accepted filters
    """)
    return input()

# Takes the list of filters and prints them out
def print_acceptable_filter():
    print("The accepted filters are as followed: " + '\n')
    for filter in const_var.ACCEPTABLE_FILTERS_LIST:
        print(filter)

# This method will take the user's imported file and confirm they are all good
def user_input_filter_acceptor():
    # Converts the users file into list then checks
    user_filter_list = []
    ignore_phrase_n = '\n'
    user_file_filter_input =  input("Please enter the file of filters you would like to use: ").strip()
    try:
        with open(user_file_filter_input, "r") as file:
            for line in file:
                user_filter_list.append(line.lower())
    except Exception as e:
        # TODO Find what to do if list has bad inputs
        pass

    print(user_filter_list)
        

def main():
    #list_selection_user_input = user_input_selection()

    list_selection_user_input = "1"
    while True:
        if list_selection_user_input == "1": user_input_filter_acceptor()
        if list_selection_user_input == "2": print_acceptable_filter()




if __name__ == "__main__": main()
