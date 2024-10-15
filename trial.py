import pandas as pd
import numpy as np

data=pd.read_excel('customer_data.xlsx')
print(data.head())

missing_values = data.isnull().sum()
print("Missing values:")
print(missing_values)

# Fill missing values with the mean of the column
from sklearn.impute import SimpleImputer

imputer = SimpleImputer(strategy = "median")
imputer.fit(data[["Income"]])
data[["Income"]] = imputer.transform(data[["Income"]])

imputer_2 = SimpleImputer(strategy = "most_frequent")
imputer_2.fit(data[["City"]])
data[["City"]] = imputer_2.transform(data[["City"]])

missing_data = data.isnull().sum()
print("Missing Data:")
missing_data
