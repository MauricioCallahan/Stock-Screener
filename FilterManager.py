import constant as const_var
from SimplifyClases import MyInput
import error_manager

class FilterManager:

    # Initializing
    def __init__(self, filepath):
        self.filepath = filepath
        self.accepted_filters = {}
        self.rejected_filters = {}

    # This method reads from file and accepts or rejects user given filters
    def load_filters(self) -> bool:
        try:
            with open(self.filepath, "r") as file:
                # Grabs both line_num and line ex.(0, line)
                for line_num, line in enumerate(file, start=1):
                    line = line.lower().strip()
                    # checking with accepted filters
                    if line in const_var.ACCEPTABLE_FILTERS_LIST:
                        self.accepted_filters[line] = line_num
                    else:
                        self.rejected_filters[line] = line_num
        except FileNotFoundError as e:
            # Deals with bad file somewhere else
            error_manager.set_file_error(True)

        error_manager.check_file_error(self.filepath)
        
            
    # This method, with the rejected filters, gives the user the ability to edit their list
    # TODO work on how option == n should function (ex. looping back to main or letting user enter another file from method)
    def fix_rejected_filters(self):
        if self.rejected_filters:
            print(f"Rejected filters: {self.rejected_filters}")
            option = MyInput.clean("Would you like to edit them Y/N: ")
            # Dealing with inputs
            if option == "y":
                self.remove_and_append()
            elif option == "n":
                return "Have a Good Day"

    """
    Removes rejected filters from the file and allows
    user to input valid replacements. Stops once the number
    of valid new filters matches the removed
    """
    def remove_and_append(self):
        # Reads file
        with open(self.filepath, "r") as file:
            lines = file.readlines()
        
        # Filter out the lines that marked "rejected" in self.reject_filters.
        # Checks each line number to make sure its not in the list of rejected values
        # Keeps only lines that aren't in self.rejected_filters.values()
        rejected_lines_nums = set(self.rejected_filters.values())
        lines = [
            line for i, line in enumerate(lines, start=1)
            if i not in rejected_lines_nums
        ]
        
        # New filter(s)
        self.filter_replacement_and_edit(lines)

        # Puts lines back into file 
        with open(self.filepath, "w") as file:
            file.writelines(lines)

    """
    Takes inputted lines from remove_and_append and allows user to
    input replacement filters and make minor edits throughout replacement process
    """
    def filter_replacement_and_edit(self, lines):
        number_of_new_filters = len(self.rejected_filters)
        count = 0
        
        print(f"There are {number_of_new_filters} that need replaced: Input count to see how many are left")
        while True:
            new_filter = MyInput.clean("Enter replacement filter: ")
            # Grabs existing filters
            existing_filters = {line.strip().lower() for line in lines}

            if new_filter in const_var.ACCEPTABLE_FILTERS_LIST:
                if new_filter in existing_filters:
                    print(f"Ignored {new_filter} due to already being in file")
                else:
                    # new_filter is not a dup.
                    lines.append(new_filter + "\n")
                    count += 1
            # allows user to find amount left 
            elif new_filter == "count":
                print(number_of_new_filters-count)
            elif new_filter == "break":
                pass
            elif new_filter == "accepted list":
                print(const_var.ACCEPTABLE_FILTERS_LIST)
            else:
                print("Ignored due to bad input")