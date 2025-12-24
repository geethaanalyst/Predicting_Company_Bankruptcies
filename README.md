# Predicting_Company_Bankruptcies
## **Introduction**
### **Objective**
* **Develop a robust machine learning model to accurately predict company bankruptcies.**
*  **By utilizing this model, the institution aims to improve risk assessment, make informed lending decisions, and optimize their financial portfolio management.**

## **Deployment Flow** 
<img width="957" height="421" alt="image" src="https://github.com/user-attachments/assets/611385ea-1310-481a-8b9e-034fef1f6c5d" />

## **Dataset Overview**
<img width="847" height="306" alt="image" src="https://github.com/user-attachments/assets/e430369f-2304-4552-8c9c-6284f59636df" />

## **Data Preprocessing**
* **Checked for missing values:  Missing data was not found in  columns.**
* **Normalize the features(using standardscaler).**
* **For data imbalance using RandomUnderSampler**
* **Split data into training (80%) and testing (20%) sets for model building.**

## **Exploratory Data Analysis**
<img width="713" height="546" alt="image" src="https://github.com/user-attachments/assets/83521b60-021e-4f74-859c-694c0ed89ff3" />

### **Top Features correlates with bankruptcy**
The top financial ratios influencing bankruptcy predictions are:
* **Net Income to Total Assets**
* **ROA(A) before interest and % after tax**
* **ROA(B) before interest and depreciation after tax**
* **ROA(C) before interest and depreciation before interest**
* **Net worth/Assets**
* **Debt ratio %**
* **Persistent EPS in the Last Four Seasons**
* **Retained Earnings to Total Assets**
* **Net profit before tax/Paid-in capital**
* **Per Share Net profit before tax (Yuan ¥)**

## **Machine Learning Models**
All models were evaluated using accuracy, precision, recall, and F1-score to ensure robust performance comparison.

### **Models Used**
* **Logistic Regression**
* **Decision Tree Classifier**
* **Random Forest Classifier**
* **Support Vector Machine**
* **K-Nearest Neighbors(KNN)**
### **Model Performance**
* **Hyper parameter tuning and cross validation in decision tree (Accuracy-0.82)**
* **Hyper parameter tuning and cross validation in random forest (Accuracy-0.83)**
* **Ensemble voting in random forest (accuracy-0.85)**

## **Model Performance**
<img width="897" height="290" alt="image" src="https://github.com/user-attachments/assets/eeeb790d-40b8-458a-95e6-48f3a519884f" />

## **Key Insights**
* **Financial leverage, liquidity, and profitability metrics are strong predictors.**
* **High debt ratios, low ROA & low liquidity strongly linked to bankruptcy risk.**
* **Certain efficiency ratios have less impact.**

## **Conclusion**
* **Profitability ratios (Net Income to Assets, ROA variants) are the strongest early warning signals.**
* **Leverage ratios (Debt % and Net Worth/Assets) also significantly impact bankruptcy probability.**
* **Using RandomUnderSampler improves model sensitivity to bankruptcies but at the cost of potentially losing information from the majority class.**
* **Ensemble ML models(in voting classifier), especially random forest, achieve  predictive metrics (~85% accuracy) and also logistic regression give same accuracy.**
* **Careful governance, retraining, and explainability are essential for sustainable deployment.**
