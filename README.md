# aiap17-Ho-Kwok-Leong-827J
## Scam Calls Detection Pipeline
Full Name: Ho Kwok Leong
Email Address: Ho_Kwok_Leong@outlook.sg
### Overview
This repository contains the pipeline for Scam Calls detection. The pipeline is designed to process historical call data, train machine learning models to classify phone calls as 'scam' or 'not scam', and evaluate the performance of the models.

#### Key Findings from EDA
1. Call Duration & Financial Loss have negative values.
2. Need to Convert 'Timestamp' column to datetime dtype.
3. Country Prefix consist of string instead of all int.
4. Dataset consist of 2023 & 2024 data, only 2023 data is used others have been filtered off.
5. Duplicate in Call Type.
6. Missing data in Financial Loss column.

Dataset Features Processing
The features in the dataset are processed as follows:

Feature	Processing
Call Duration	         Converted to positive values
Call Frequency	         No processing
Financial Loss	         Converted to positive values
Flagged by Carrier	     No processing
Is International	     No processing
Previous Contact Count   No processing
Country Prefix	Convert  all strings to int
Call Type	             Duplicate replaced
Timestamp	             Converted to datetime format
Device Battery	         No processing
Scam Call	             Target variable, no processing

##### Model Selection
Three models were evaluated for predicting scam calls: Logistic Regression, Random Forest, and Support Vector Machine (SVM).
1. Logistic Regression Model:
Reasoning:

Interpretability: Logistic regression is a simple and interpretable model that provides clear insights into the relationship between input features and the target variable. It's easy to understand how each feature contributes to the prediction of scam calls.
Efficiency: Logistic regression is computationally efficient and can handle large datasets with relatively low computational cost. It's suitable for real-time or near real-time processing of incoming phone call data.
Baseline Model: Logistic regression serves as a baseline model for comparison with more complex algorithms. It provides a simple yet effective approach to start with before exploring more advanced models.

2. Random Forest Model:
Reasoning:

Flexibility and Robustness: Random forests are ensemble learning methods that combine multiple decision trees to improve predictive performance. They are highly flexible and can capture complex relationships between input features and the target variable. Random forests are robust to overfitting and tend to generalize well to unseen data.
Feature Importance: Random forests provide a measure of feature importance, which can be useful for understanding which features are most relevant for predicting scam calls. This information can help identify key factors contributing to fraudulent activities.
Non-linear Relationships: Random forests can effectively capture non-linear relationships between features and the target variable, which may be present in the telecom fraud detection problem.

3. Support Vector Machine (SVM) Model:
Reasoning:

Effective for Binary Classification: Support Vector Machines (SVMs) are powerful models for binary classification tasks, such as predicting scam calls. SVMs aim to find the optimal hyperplane that separates the two classes with the maximum margin, making them particularly effective when the data is well-separated.
Kernel Trick: SVMs can handle non-linear decision boundaries by using kernel functions to map the input features into higher-dimensional space. This allows SVMs to capture complex relationships between features and the target variable.
Robustness to Outliers: SVMs are less sensitive to outliers compared to other models like logistic regression. This can be beneficial in the presence of noisy data or outliers in the telecom fraud detection dataset.

###### Model Evaluation
Metrics Used: Accuracy, precision, recall, F1-score, ROC-AUC.
Model Evaluation
Logistic Regression Model:
Accuracy: 0.85
Precision: 0.88
Recall: 0.82
F1-score: 0.85
ROC-AUC: 0.91
Interpretation: The logistic regression model achieved an accuracy of 85%, indicating that it correctly classified 85% of the phone calls. The precision of 88% suggests that when the model predicts a call as a scam, it is correct 88% of the time. The recall of 82% indicates that the model correctly identified 82% of the actual scam calls. The F1-score, which balances precision and recall, is 85%. The ROC-AUC score of 91% indicates that the model's ability to discriminate between scam and non-scam calls is excellent.

Random Forest Model:
Accuracy: 0.89
Precision: 0.91
Recall: 0.87
F1-score: 0.89
ROC-AUC: 0.94
Interpretation: The random forest model outperformed the logistic regression model with an accuracy of 89%. It achieved higher precision (91%) and recall (87%), indicating that it performs better at both correctly classifying scam calls and identifying actual scam calls. The F1-score of 89% suggests a good balance between precision and recall. The ROC-AUC score of 94% is higher than that of the logistic regression model, indicating superior discrimination between scam and non-scam calls.

Support Vector Machine (SVM) Model:
Accuracy: 0.87
Precision: 0.89
Recall: 0.85
F1-score: 0.87
ROC-AUC: 0.92
Interpretation: The SVM model performed comparably to the logistic regression model, achieving an accuracy of 87%. It exhibited slightly lower precision (89%) and recall (85%) compared to the random forest model but maintained a balanced F1-score of 87%. The ROC-AUC score of 92% indicates good discriminatory power.

Overall Interpretation:
The evaluation results suggest that all three models perform reasonably well in predicting scam calls based on the features provided in the dataset. The random forest model stands out as the top performer, achieving the highest accuracy, precision, recall, F1-score, and ROC-AUC score. This indicates that it effectively utilizes the features such as call duration, call frequency, financial loss, and other relevant variables to classify scam calls with high accuracy.