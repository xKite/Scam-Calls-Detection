#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from data_preprocessing import load_data, preprocess_data
from model_training import train_logistic_regression_model, train_random_forest_model
from visualization import plot_feature_distribution

def main():
    # Load and preprocess data
    database_file = 'calls.db'
    df = load_data(database_file)
    X_train, X_test, y_train, y_test = preprocess_data(df)

    # Train machine learning models
    logistic_regression_model = train_logistic_regression_model(X_train, y_train)
    random_forest_model = train_random_forest_model(X_train, y_train)

    # Generate visualizations
    plot_feature_distribution(df, 'Call Duration')

if __name__ == "__main__":
    main()

