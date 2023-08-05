# This excercise will tell you about some python data structures, including the one we will work the most - pandas DataFrame

import pandas as pd
import random
# 1. Make a loop that will print numbers from 0 to 10
for a in range(11):
    print(a);

# 2. Make a loop that prints numbers from 0 to 10, but skips number 5
for b in range(11):
    if b == 5: continue
    print (b);
# 3. Make a function that takes a two arguments: max_num and stop_num. 
# Function prints all numbers from 0 to max_num, 
# but stops (function exits) at number 5
# Try to call this function with different parameters
stop_num = 5
def funcFive (max_num):
    for c in range(max_num):
        if c == stop_num: break
        print(c);
funcFive(20);

# 4. Make a dictionary that can store max_num and stop_num values. 
# Now improve the function to take a dictionary as an argument
data2 = dict(stop_num = 5, max_num = funcFive(20));

# 5. Convert a dictionary to pandas DataFrame

newpd = pd.DataFrame.from_dict([data2])
print(newpd)

# 6. Create a list of numbers. Print it and then print it sorted
# for d in range (10):
#    list1 = random.randrange(1,20)
#    list1.sort()
#    print(list1) # not working solution
     
list3 = [random.randint(1,20) for _ in range(100)] # working solution
list3.sort()
print(list3);
# 7. Now, make a list of dictionaries. Each dictionary should have two 
# keys: "name" and "age".

data3 = {'name' : ["Nicholas", "Nikita"], 
        'age': [34, 30]
        }
# 8. Convert a list of dictionaries to pandas DataFrame, visualise it 
# as you like

df = pd.DataFrame.from_dict(data3)

df
print(df)

# 9. Make a function that takes pandas DataFrame and column name as 
# arguments. It will return all values stored in the DatFrame column 
# with this column name
# Basically, just visualises the column

def pFunct(df, colname):
    print(colname);