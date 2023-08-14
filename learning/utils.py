# While developing have a look at this article to learn how to write good looking code:
# https://realpython.com/python-pep8/
from typing import Dict

def pring_helllo():
    print("Hello World")
    

########### SECTION 1 ###########

def read_json(filePath: str) -> Dict: 
    """ This function takes a path to the .json file and returns its data in a dictionary format """
    raise NotImplementedError("You need to implement this function")    # When implementing a function, remove this line

def view_users(data: dict):
    """ This function takes a dictionary of data and prints all the users 
    
    I want you to do next in the '02-imporing-functions.py' file:
    - Read learningData/example01.json [it consist a data sample of users: their age, name and city they are from]
    - Call this function to visualise users
    
    Visualise them in a way to show each user separately with their name, age and city:
    
    NAME - AGE - CITY
    Nikita - 25 - Riga
    John - 30 - London
    ...
    
    PS: make a for loop
    
    """
    raise NotImplementedError("You need to implement this function")    # When implementing a function, remove this line

def view_statistical_description(data: dict):
    """ This function takes a dictionary of data and prints statistical description of the data
    
    I want you to visualise next statistical parameters:
    - Mean  [Numerical only]
    - Median
    - Standard Deviation [Numerical only]
    - Max [Numerical only]
    - Min [Numerical only]
    - Frequency of each value 
    
    For example:
    
    Property: age
    Min: 18
    Max: 90
    STD: 10.5
    Mean: 30.5
    ...
    
    or
    
    Property: name
    Frequency: [
        "Nikita": 2,
        "John": 1,
        "Anna": 1,
        ...
    ]
    
    """
    
    raise NotImplementedError("You need to implement this function")    # When implementing a function, remove this line

########### SECTION 2 ###########

# In this section you are given a problem and you will need to design function from them on your own
# Do what you find is most suitable for the problem
# The description of the problem to solve is in '02-importing-functions.py'

# ...
