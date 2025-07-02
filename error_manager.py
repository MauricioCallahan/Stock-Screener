# This file will deal with errors, and other issues that come up in the program
# The purpose to decenteralize the issues and have the main methods do the work
# With errors done on the side
FILE_ERROR = False

def set_file_error(val: bool):
    global FILE_ERROR
    FILE_ERROR = val

def get_file_error(val: bool):
    return FILE_ERROR

def check_file_error(filepath):
    if FILE_ERROR:
        print(f"{filepath} does not exist")