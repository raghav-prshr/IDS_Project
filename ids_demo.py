import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest

# Create normal network traffic
normal_data = np.random.normal(loc=50, scale=5, size=(200, 2))

# Create attack traffic (anomalies)
attack_data = np.random.normal(loc=100, scale=10, size=(20, 2))

# Combine dataset
X = np.vstack((normal_data, attack_data))

# Train Isolation Forest
model = IsolationForest(contamination=0.1, random_state=42)
model.fit(X)

# Predict anomalies
predictions = model.predict(X)

# Plot results
plt.scatter(X[:, 0], X[:, 1], c=predictions, cmap='coolwarm')
plt.title("Anomaly Detection using Isolation Forest")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.savefig("anomaly_output.png")
print("Graph saved as anomaly_output.png")