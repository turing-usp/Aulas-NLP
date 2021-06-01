import pandas as pd
import numpy as np
import sqlite3

database = pd.read_csv("zomato.csv")
database = database[:150]
database['rate_clean'] = database['rate'].replace(regex={"/5": ""})

cuisines = database['cuisines']
cuisines = [c.split() for c in cuisines]
cuisines_classes = []
for c in cuisines:
    for i in c:
        if i not in cuisines_classes:
            cuisines_classes.append(str(i).replace(",",""))
            
def define_cuisines(cuisines_str):
    cuisines_list = cuisines_str.replace(",","").split()
    cuisines_bool = np.zeros(len(cuisines_classes))
    for i,co in enumerate(cuisines_classes):
        if co in cuisines_list:
            cuisines_bool[i] =1
    cuisines_bool = list(cuisines_bool)
    return cuisines_bool

cuisines_data = np.array(list(database['cuisines'].apply(define_cuisines)))

for i,co in enumerate(cuisines_classes):
    database[co] = cuisines_data[:,i]

database['approx_cost(for two people)'] = database['approx_cost(for two people)'].replace(regex={",":""}).astype(float)
    
def price_classification(price):
    if price > 600:
        return "high-price"
    elif price > 350 and price <600:
        return "average-price"
    else:
        return "low-price"
    
database['price_classification'] = database['approx_cost(for two people)'].apply(price_classification)

keep_columns = cuisines_classes + ['address', 'name', 'price_classification', 'rate_clean']

keep_database = database[keep_columns]

keep_database = keep_database.loc[:,~keep_database.columns.duplicated()]

conn = sqlite3.connect('nlp.db')
c = conn.cursor()
keep_database.to_sql("restaurants_bengaluru", conn, if_exists="replace")
keep_database.to_csv("restaurants_bengaluru.csv")