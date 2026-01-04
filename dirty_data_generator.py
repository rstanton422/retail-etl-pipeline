import pandas as pd
import numpy as np
import random

# setting up my messy data
# this is a first for me in generating raw data
# gonna be fun
# creating dictionary of products and price
products = {
    'Laptop': 1200,
    'Mouse': 25,
    'Monitor': 300,
    'Keyboard': 50,
    'HDMI Cable': 15
}

# creating a list of products from the dictionary keys
product_list = list(products.keys())

# create an empty data list to store items
data =[]

# time to create the dirty data.  gonna do 100 rows for 100 fake orders
for i in range(100):
    prod = random.choice(product_list)      # randomly pick one item
    price = products[prod]                  # looks up price of item

    # here we add the 'mud' to make it 'dirty'
    # randomy insert null values for the price
    if random.random() < 0.05:      # rolls the random dice to see if it is < 0.05 for TRUE
        price = np.nan              # if TRUE, executes this.  If FALSE, moves to elif  

    # introducing some human input error by adding negative price values
    elif random.random() < 0.05:    # rolls the random dice to see if it < 0.5 for TRUE
        price = price * -1          # if TRUE it makes price negative. if FALSE, keeps price as original value

    # just bad formatting
    date = '2025-01-01'
    if random.random() < 0.10:      # rolls random dice to see if it < 0.10 for TRUE
        date = '01/01/2025'         # if TRUE, sets new date format (the wrong one). if FALSE, it keeps original format

    # create a random int between 1 and 5 for quantity
    quantity = random.randint(1, 5)

    # append newly created to data list
    data.append([i, prod, price, quantity, date])

# time to make a dataframe for the newly created dirty data
df = pd.DataFrame(data, columns=['order_id', 'product_name', 'price', 'quantity', 'order_date'])

# introduce duplicates because of human error 
df = pd.concat([df, df.iloc[20:30]])

# save this guy to a csv
df.to_csv("raw_sales_data.csv", index=False)

print("Successfully saved dirty data: raw_sales_data.csv")

