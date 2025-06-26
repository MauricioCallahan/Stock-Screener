# This program will take a list of filters and will find stocks that find its parameters
import yfinance as yf
import constant as const_var

class FilterManager:
    def __init__(self, filepath):
        self.filepath = filepath
        self.accepted_filters = {}
        self.rejected_filters = {}

    def load_filters(self):
        with open(self.filepath, "r") as file:
            for line_num, line in enumerate(file, start=1):
                line = line.lower().strip()

                if line in const_var.ACCEPTABLE_FILTERS_LIST:
                    self.accepted_filters[line] = line_num
                else:
                    self.rejected_filters[line] = line_num

    def fix_rejected_filters(self):
        if self.rejected_filters:
            print(f"Rejected filters: {self.rejected_filters}")
            option = input("Would you like to edit them Y/N: ").lower()
            if option == "y":
                self.remove_and_append()

    def remove_and_append(self):
        with open(self.filepath, "r") as file:
            lines = file.readlines()

        lines = [
            line for i, line in enumerate(lines, start=1)
            if i not in self.rejected_filters.values()
        ]

        new_filter = input("Enter a replacement filter: ").strip().lower()
        lines.append(new_filter + "\n")

        with open(self.filepath, "w") as file:
            file.writelines(lines)

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
        manager = FilterManager("List_of_Filters.txt")
        manager.load_filters()
        manager.fix_rejected_filters()
    elif choice == "2":
        print("The accepted filters are: ")
        for f in const_var.ACCEPTABLE_FILTERS_LIST:
            print(f)


if __name__ == "__main__": main()


