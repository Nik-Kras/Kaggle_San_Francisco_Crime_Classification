"""
In this Learning section you will get skills on writing code in several files
That is how most of the projects are done
You build one datastructure and then import it to several other scripts
Or you bild one function and do the same
It works the same way as in C/C++, so you should pick it up easily

You will work with two files. This one and utils.py, so open both of them
"""
from utils import pring_helllo


# This statement says, that the code
# Inside this IF statement will be called only if you run this file directly
# Otherwise the code will run any time you import the script
if __name__ == "__main__":
    """
    I want you to create several function in utils.py and then call them here
    One by one. Make a print statement before calling them, so you can easily see the output
    Of each function separately in the Terminal
    """
    
    # An example  
    print("***\nCalling function: {}".format("pring_helllo"))
    pring_helllo()

    # Call all your functions here

    # 1. Call all functions from Section 2
    
    # ...
    
    # 2. Create functions in Section 2 to solve next propblem
    
    """
    There is a file in learningData/example02.json
    It represents car prices for different car brands
    However, the data is corrupted and you need to fix it
    Some data entries are missing. We might drop them or fill them
    
    Sometimes dropping is the right thing to do, the other time it is better to fill the gaps
    So, I want you to try do both
    
    1. Load the data
    2. Remove all entries that have missing values [Remember that each price value is linked to a brand and you should drop both of them]
    3. Save the data to a new file [Save it with new name so we can check and compare]
    
    ***
    
    1. Load the data
    2. Find average price for each brand
    3. Fill gaps with average price for each brand
    4. Save the data to a new file [Save it with new name so we can check and compare]
    """
    
    # ...
