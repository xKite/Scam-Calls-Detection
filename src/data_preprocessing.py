#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sqlite3
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder

def load_data(database_file):
    # Connect to SQLite database
    conn = sqlite3.connect(database_file)
    # Read data from database into a DataFrame
    df = pd.read_sql_query("SELECT * FROM calls", conn)
    conn.close()
    return df

def preprocess_data(df):
    # Perform data cleaning and preprocessing tasks
    # Example: handle missing values, encode categorical variables, scale numerical features
    # Split data into features and target variable
    X = df.drop(columns=['Scam Call'])
    y = df['Scam Call']
    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test

if __name__ == "__main__":
    # Example usage
    database_file = 'calls.db'
    df = load_data(database_file)
    X_train, X_test, y_train, y_test = preprocess_data(df)

