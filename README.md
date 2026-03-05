# 📊 Machine Learning Model Comparison Dashboard

An interactive **Machine Learning Web Application** built using **Streamlit** that compares the performance of two classification models:

* Logistic Regression
* K-Nearest Neighbors (KNN)

The application uses a **built-in dataset from Scikit-learn** and provides a professional dashboard to evaluate model performance using metrics and visualizations.

---

# 🚀 Features

* 🤖 Multiple ML models (Logistic Regression & KNN)
* 📊 Accuracy Score evaluation
* 📉 Confusion Matrix visualization
* 📄 Classification Report display
* 📊 Interactive prediction using user input
* 🎨 Professional dashboard UI
* 📱 Sidebar controls for model selection and input features

---

# 🧠 Machine Learning Models

The application compares two classification algorithms:

### 1️⃣ Logistic Regression

A statistical classification algorithm used for predicting categorical outcomes.

### 2️⃣ K-Nearest Neighbors (KNN)

A distance-based classification algorithm that predicts the class based on the nearest neighbors.

---

# 📊 Model Evaluation Metrics

The dashboard evaluates models using:

| Metric                | Description                              |
| --------------------- | ---------------------------------------- |
| Accuracy              | Overall correctness of predictions       |
| Confusion Matrix      | Shows correct and incorrect predictions  |
| Classification Report | Includes precision, recall, and F1-score |

These metrics help understand the performance of each model.

---

# 🖥 Application Interface

### 🔹 Model Selection

Users can select the model from the sidebar:

* Logistic Regression
* KNN

### 🔹 Feature Input

Users can adjust feature values using sliders in the sidebar.

### 🔹 Prediction Result

The application predicts the class based on user input.

### 🔹 Performance Visualization

The dashboard displays:

* Accuracy Score
* Confusion Matrix
* Classification Report

---

# 📁 Project Structure

```
ml-model-comparison-dashboard
│
├── app.py
├── train_model.py
├── model.pkl
├── requirements.txt
└── README.md
```

| File             | Description               |
| ---------------- | ------------------------- |
| app.py           | Streamlit web application |
| train_model.py   | Model training script     |
| model.pkl        | Saved trained models      |
| requirements.txt | Python dependencies       |
| README.md        | Project documentation     |

---

# ⚙️ Installation

Clone the repository:

```
git clone https://github.com/yourusername/ml-model-comparison-dashboard.git
cd ml-model-comparison-dashboard
```

Install dependencies:

```
pip install -r requirements.txt
```

---

# ▶️ Run the Application

Start the Streamlit app:

```
streamlit run app.py
```

Open the browser:

```
http://localhost:8501
```

---

# 🧪 Technologies Used

* Python
* Streamlit
* Scikit-learn
* NumPy
* Pandas
* Matplotlib

---

# 🌍 Deployment

You can deploy the project easily using **Streamlit Cloud**:

1. Push the project to GitHub
2. Visit https://share.streamlit.io
3. Connect your repository
4. Select `app.py`
5. Click **Deploy**

Your app will be live instantly.

---


---

# 👨‍💻 Author

**Siva Balan G**
