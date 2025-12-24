import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from imblearn.under_sampling import RandomUnderSampler
from sklearn.metrics import classification_report, confusion_matrix

# Title
st.title("Company Bankruptcy Prediction App")

data = pd.read_csv('Bankruptcies.csv')

st.write("Sample data")
st.write(data.head())

# Features and target
X = data.drop(columns=['Bankrupt?'])  # 'Bankrupt?' is the target column (0 or 1)
y = data['Bankrupt?']
rus = RandomUnderSampler(random_state=42)
X_res, y_res = rus.fit_resample(X, y)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X_res, y_res, test_size=0.2, random_state=42)

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
#  Feature selection by correlation with target 'Bankrupt'
corr = data.corr()
top_features = corr['Bankrupt?'].abs().sort_values(ascending=False).iloc[1:11].index.tolist()

# Use only top 10 features for prediction
X_train_top = X_train[top_features]
X_test_top = X_test[top_features]

# Retrain model with top features
model.fit(X_train_top, y_train)

# Predict on test
y_pred = model.predict(X_test_top)

# Display evaluation
st.subheader("Model Performance")
st.text(confusion_matrix(y_test, y_pred))
st.text(classification_report(y_test, y_pred))

# User input for prediction
st.subheader("Make a Prediction")

user_input = {}
for col in top_features:
    user_input[col] = st.number_input(f"Enter {col}")

input_df = pd.DataFrame([user_input])

prediction = model.predict(input_df)[0]
prediction_proba = model.predict_proba(input_df)[0][1]

if st.button("Predict Bankruptcy"):
    if prediction == 1:
        st.error(f"Predicted: Bankrupt (Probability: {prediction_proba:.2f})")
    else:
        st.success(f"Predicted: Not Bankrupt (Probability: {prediction_proba:.2f})")
# ...existing code...