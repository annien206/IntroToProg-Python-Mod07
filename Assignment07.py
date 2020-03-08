#--------------------------------------------#
# Title: Assignment07
# Description: Creating Script with Pickle Method and Error Handling
# ChangeLog: (Who, When, What)
# ANg, 3.6.2020, Created Script

# Data-------------------------------------------#
strName = str(input("Enter a Name: "))

# Processing------------------------------------#
try:
    num = int(input("Enter an Age: "))
except ValueError:
    print("Please enter an age: ")
    num = int(input(" "))
lstCustomer = [strName, num]

import pickle

with open("AgeData.dat", "wb") as pickle_file:
    pickle.dump(lstCustomer, pickle_file)

with open("AgeData.dat", "rb") as pickle_file:
    new_data = pickle.load(pickle_file)

# Presentation----------------------------------#
print(lstCustomer)
print(new_data)