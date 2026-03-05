import streamlit as st
import pickle
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.metrics import classification_report, accuracy_score

st.set_page_config(page_title="ML Model Comparison", layout="wide")

# ---------------- UI STYLE ----------------
st.markdown("""
<style>

.stApp {
    background-color: #eef4fb;
}

.metric-card {
    background-color: white;
    padding: 20px;
    border-radius: 12px;
    text-align: center;
    box-shadow: 0px 4px 8px rgba(0,0,0,0.05);
}

.metric-title {
    font-size: 16px;
    color: #333;
}
/* Make all titles black */
h1, h2, h3, h4 {
    color: black !important;
}
.metric-value {
    font-size: 28px;
    font-weight: bold;
    color: #1f77b4;
}

</style>
""", unsafe_allow_html=True)

st.title("📊 Machine Learning Model Comparison Dashboard")

# ---------------- LOAD MODELS ----------------
with open("model.pkl", "rb") as f:
    log_model, knn_model, feature_names, target_names, X_test, y_test = pickle.load(f)

# ---------------- SIDEBAR ----------------
st.sidebar.header("Model Selection")

model_choice = st.sidebar.selectbox(
    "Select Model",
    ("Logistic Regression", "KNN")
)

st.sidebar.header("Input Features")

input_data = []

for feature in feature_names:
    val = st.sidebar.slider(feature, 0.0, 10.0, 5.0)
    input_data.append(val)

input_array = np.array([input_data])

# ---------------- MODEL SELECT ----------------
if model_choice == "Logistic Regression":
    model = log_model
else:
    model = knn_model

# ---------------- PREDICTION ----------------
if st.sidebar.button("Predict"):

    prediction = model.predict(input_array)[0]

    st.subheader("🔍 Prediction Result")

    st.success(f"Predicted Class: {target_names[prediction]}")

# ---------------- MODEL EVALUATION ----------------
st.subheader("📈 Model Evaluation")

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

# Accuracy card
col1 = st.columns(1)[0]

col1.markdown(f"""
<div class="metric-card">
<div class="metric-title">Accuracy Score</div>
<div class="metric-value">{accuracy:.2f}</div>
</div>
""", unsafe_allow_html=True)

st.divider()

# ---------------- CONFUSION MATRIX ----------------
st.subheader("📊 Confusion Matrix")

cm = confusion_matrix(y_test, y_pred)

fig, ax = plt.subplots()
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=target_names)
disp.plot(ax=ax)

st.pyplot(fig)

# ---------------- CLASSIFICATION REPORT ----------------
st.subheader("📄 Classification Report")

report = classification_report(y_test, y_pred, target_names=target_names, output_dict=True)

report_df = pd.DataFrame(report).transpose()

st.dataframe(report_df)