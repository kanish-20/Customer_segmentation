# Customer Segmentation using K-Means
## Project Overview

This project uses K-Means clustering to segment customers based on their purchasing behavior. By analyzing features like Age, Annual Income, and Spending Score, we classify customers into meaningful groups such as high-value, average, or low-spending customers. This helps businesses target marketing strategies more effectively.

### Dataset

**The dataset contains the following columns:**

- CustomerID – Unique ID for each customer

- Age – Customer's age

- Annual_Income – Customer's annual income in dollars

- Spending_Score – A score (1-100) representing customer spending behavior

## Algorithm

- We use **K-Means Clustering** from sklearn to segment customers.

- The number of clusters is chosen based on the Elbow Method.

-- Each customer is assigned to a cluster, which is then interpreted as:

 - High-Value Customer

 - Average Spender

 - Low Spender

## Folder Structure
```
Customer_Segmentation/
│
├── train_model.py       # Script to train the K-Means model
├── app.py               # Flask application
├── templates/
│   └── index.html       # HTML frontend
├── static/
│   └── style.css        # CSS styling
├── requirements.txt     # Dependencies
└── customer_data.csv    # Dataset
```

## Output

**After inputting customer details, the app predicts a customer segment, e.g.,**

- "High-Value Customer"

- "Average Spender"

- "Low Spender"

## How to Run

### 1.Install dependencies from requirements.txt:
```
pip install -r requirements.txt
```

### 2. Train the model:
```
python train_model.py
```

### 3. Run the web app:
```
python app.py
```

## Screenshots

![WhatsApp Image 2025-08-17 at 12 17 08](https://github.com/user-attachments/assets/46dbe339-9b04-4fc9-ba87-e0530e3df73d)
![WhatsApp Image 2025-08-17 at 12 17 08 (1)](https://github.com/user-attachments/assets/4c55436b-c836-44a4-ac57-cb00e60a6c6a)

