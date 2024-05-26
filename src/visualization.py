#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import matplotlib.pyplot as plt

def plot_feature_distribution(data, feature):
    # Plot distribution of a feature
    plt.figure(figsize=(8, 6))
    # Example: histogram of feature distribution
    plt.hist(data[feature], bins=20, color='skyblue', edgecolor='black')
    plt.title(f'Distribution of {feature}')
    plt.xlabel(feature)
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    # Example usage
    # Assume df is the preprocessed DataFrame
    plot_feature_distribution(df, 'Call Duration')

