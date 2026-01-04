import pandas as pd
import sqlite3
import os

#==============================================================
# Extaction of Data
#==============================================================

# bring the 'raw' data in from the generated csv file
# decalre the file path
file_path = "raw_sales_data.csv"

# create error logic to throw in case there is no valid path
if not os.path.exists(file_path):
    print("No valid file path found.  Run dirty_data_generator.py first")
    exit()

# read csv file in pandas df
# df is short for dataframe. obligatory naming convention
df = pd.read_csv(file_path)
print("columns found:", df.columns.tolist())
print(f"pulled {len(df)} rows from the csv file")

# printing the head of the dataframe (first 5 rows)
print("\n----- Sneak Peak at the Dirty Dirty Data -----")
print(df.head())
print("-" * 46)

#==============================================================
# Transform the Data
#==============================================================

# time to take care of all the missing values
# all the wrong formatted data
# and any other 'bad' or 'dirty' data and correct it

# first we need to check for duplicates
initial_data_count = len(df)
df = df.drop_duplicates(subset=['order_id'])
print(f"\nWe dropped {initial_data_count - len(df)} duplicate rows")

# need to find a way to handle the 'wrong' or missing data
# from previous analysis, it is decided that the median pricefor each product will be used for all missing values
# no reason to delete these rows as they offer valuable insight + the data set is small 
df['price'] = df['price'].fillna(df.groupby('product_name')['price'].transform('median'))
print("\nFilling missing values (NA) with Median price for each product\n")

# we gpt some negative values
# going to assume that this was human input error
# will just make every price an absolute value
df['price'] = df['price'].abs()

# data format is goofy
# some do not follow the YYYY-MM-DD format
df['order_date'] = pd.to_datetime(df['order_date'], format='mixed').dt.date

# let's verify we are good by taking a peak at the data
print("-" * 50)
print(f"we have cleaned {len(df)} rows of data\n")
print(df.head())
print("-" * 50)
#print(df.tail(10))
#print(df.shape)
#print(df.dtypes)
#print(df[df['order_id']==20])

#==============================================================
# Load the Data
#==============================================================

# need to create a SQLite DB for our new database file
# if it doesn't exist, we need to create one
db_name = 'sales_data.db'       # giving it obligatory names
connection = sqlite3.connect(db_name)

# Write the DataFrame to a SQL Table named 'sales'
# if_exists='replace'- this drops the old table and makes a new one every time we run this
df.to_sql('sales', connection, if_exists='replace', index=False)

print("\nData has been loaded into an SQLite Database")

# need to test this thing to see if it works
# going to have target audience be some high level 'Executive'
# because we all know that they love these summaries of summaries
print("\n--- Executive Summary Report: Top Selling Products ---")
query = """
    SELECT product_name, SUM(price * quantity) AS total_revenue
    FROM sales
    GROUP BY product_name
    ORDER BY total_revenue DESC
"""

# have the sql query come back to a pandas df 
report = pd.read_sql(query, connection)
print(report)

# can't forget to close the connection
connection.close()
