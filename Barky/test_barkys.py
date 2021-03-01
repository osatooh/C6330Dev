import unittest

from barky import Option
from barky import print_options

def test_option_choice_is_valid(self):
        #Assume
        choice = 'A'
        optionlist = {"(A)": "Add a bookmark"}

        #Action
        result = print_options.option_choice_is_valid(choice)

        #Assert
        self.assertTrue(result)
            
def test_option_choice_is_invalid(self): 
        choice = 'F'
        optionlist = {"(A)": "Add a bookmark"}     

        result = print_options.option_choice_is_valid(choice)   
        self.assertFalse(result)  

if __name__ == "__main__":
     unittest.main()
