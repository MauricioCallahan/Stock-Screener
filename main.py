# This program will take a list of filters and will find stocks that find its parameters
import yfinance as yf
import constant as const_var

ACCEPTABLE_FILERS_LIST =const_var.ACCEPTABLE_FILTERS_LIST

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
    # Conerts the users file into dict then checks (dict to get line and value)
    user_filter_dict = {}
    non_accepted_filter_dict = {}

    #user_file_filter_input =  input("Please enter the file of filters you would like to use: ").strip()
    user_file_filter_input = "List_of_Filters.txt"

    with open(user_file_filter_input, "r") as file:
        for file_line in file:
            # Consistancy
            file_line = file_line.lower().strip()
            # Checking user filter with acceptable filter
            if file_line in ACCEPTABLE_FILERS_LIST:
                user_filter_dict[file_line] = user_filter_dict.get(file_line, + 0) + 1
            else:
                non_accepted_filter_dict[file_line] = non_accepted_filter_dict.get(file_line, 0) + 1

    print(user_filter_dict)
    print(non_accepted_filter_dict)

    print(ACCEPTABLE_FILERS_LIST)
        

def main():
    #list_selection_user_input = user_input_selection()

    list_selection_user_input = "1"

    if list_selection_user_input == "1": user_input_filter_acceptor()
    if list_selection_user_input == "2": print_acceptable_filter()




if __name__ == "__main__": main()


