# train_model.py

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import pickle

# Load dataset
df = pd.read_csv("customer_dataset.csv", on_bad_lines='skip')

# Features for clustering
X = df[["Age", "Annual_Income", "Spending_Score"]]

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train KMeans
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X_scaled)

# Map clusters to labels
labels_map = {0: "High Value Customer", 1: "Low Spender", 2: "Average Spender"}
df["Cluster"] = kmeans.labels_
df["Segment_Label"] = df["Cluster"].map(labels_map)

# Save model and scaler
with open("kmeans_model.pkl", "wb") as f:
    pickle.dump(kmeans, f)
with open("scaler.pkl", "wb") as f:
    pickle.dump(scaler, f)

print("Training complete. Model and scaler saved!")
