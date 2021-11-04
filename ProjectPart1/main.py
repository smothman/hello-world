
import pandas as pd
import csv

# read contents of csv file
file = pd.read_csv("FullInventory.csv")
print("Original file:")
print(file)


# adding header
headerList = ["Item ID", "Manufacturer Name", "Item Type", "Price", "Service Date", "Damaged Status"]
# converting data frame to csv
file.to_csv("FullInventory2.csv", header=headerList, index=False)

# display modified csv file
file2 = pd.read_csv("FullInventory2.csv")
sorted_file = file2.sort_values(by=["Manufacturer Name"], ascending=True)
file.to_csv("FullInventory2.csv", header=headerList, index=False)
print('\nModified file:')
print(file2)

