import pickle
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier

# Load dataset
data = load_iris()
X = data.data
y = data.target

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train models
log_model = LogisticRegression(max_iter=200)
knn_model = KNeighborsClassifier(n_neighbors=5)

log_model.fit(X_train, y_train)
knn_model.fit(X_train, y_train)

# Save models
with open("model.pkl", "wb") as f:
    pickle.dump((log_model, knn_model, data.feature_names, data.target_names, X_test, y_test), f)

print("Models trained successfully")