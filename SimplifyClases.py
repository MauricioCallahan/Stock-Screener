# This file is only used for classes 
# That will simplify the code

class MyInput:
    @staticmethod
    def clean(prompt=""):
        return input(prompt).lower().strip()