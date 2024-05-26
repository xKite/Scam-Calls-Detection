#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

def train_logistic_regression_model(X_train, y_train):
    # Initialize and train logistic regression model
    model = LogisticRegression()
    model.fit(X_train, y_train)
    return model

def train_random_forest_model(X_train, y_train):
    # Initialize and train random forest model
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    return model

def train_support_vector_machine_model(X_train, y_train):
    # Initialize and train support vector machine model
    model = SVC()
    model.fit(X_train, y_train)
    return model

if __name__ == "__main__":
    # Example usage
    # Assume X_train, y_train are preprocessed training data
    logistic_regression_model = train_logistic_regression_model(X_train, y_train)
    random_forest_model = train_random_forest_model(X_train, y_train)
    svm_model = train_support_vector_machine_model(X_train, y_train)

