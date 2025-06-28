import constant as const_var
from SimplifyClases import MyInput

class FilterManager:

    # Initializing
    def __init__(self, filepath):
        self.filepath = filepath
        self.accepted_filters = {}
        self.rejected_filters = {}

    # This method reads from file and accepts or rejects user given filters
    def load_filters(self):
        with open(self.filepath, "r") as file:
            # Grabs both line_num and line ex.(0, line)
            for line_num, line in enumerate(file, start=1):
                line = line.lower().strip()
                # checking with accepted filters
                if line in const_var.ACCEPTABLE_FILTERS_LIST:
                    self.accepted_filters[line] = line_num
                else:
                    self.rejected_filters[line] = line_num

    # This method, with the rejected filters, gives the user the ability to edit their list
    def fix_rejected_filters(self):
        if self.rejected_filters:
            print(f"Rejected filters: {self.rejected_filters}")
            option = MyInput.clean("Would you like to edit them Y/N: ")
            # Dealing with inputs
            if option == "y":
                self.remove_and_append()
            #TODO DEAL WITH IF OPTION == n

    def remove_and_append(self):
        # Reads file
        with open(self.filepath, "r") as file:
            lines = file.readlines()
        
        # Filter out the lines that marked "rejected" in self.reject_filters.
        # Checks each line number to make sure its not in the list of rejected values
        # Keeps only lines that aren't in self.rejected_filters.values()
        lines = [
            line for i, line in enumerate(lines, start=1)
            if i not in self.rejected_filters.values()
        ]
        # New filter(s)
        new_filter = MyInput.clean("Enter a replacement filter: ")
        lines.append(new_filter + "\n")

        with open(self.filepath, "w") as file:
            file.writelines(lines)
