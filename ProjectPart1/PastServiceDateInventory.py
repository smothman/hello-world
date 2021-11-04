import pandas as pd
import csv
from datetime import date

# read contents of csv file
file = pd.read_csv("PastServiceDateInventory.csv")
print("Original file:")
print(file)


# adding header
headerList = ["Item ID", "Manufacturer Name", "Item Type", "Price", "Service Date", "Damaged Status"]
# converting data frame to csv
file.to_csv("PastServiceDateInventory2.csv", header=headerList, index=False)

# display modified csv file
file2 = pd.read_csv("PastServiceDateInventory2.csv")
sorted_file = file2.sort_values(by=["Manufacturer Name"], ascending=True)
file.to_csv("PastServiceDateInventory2.csv", header=headerList, index=False)

with open('PastServiceDateInventory.csv', 'r') as f1, open('PastServiceDateInventory2.csv', 'a+') as f2:
    f2.write(f1.read())
    today = date.today()
    reader = csv.DictReader(f2)
    rows = [row for row in reader if row['Service Date'] < today]


print('\nModified file:')
print(file2)

