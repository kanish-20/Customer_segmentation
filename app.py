# app.py

from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)

# Load model and scaler
with open("kmeans_model.pkl", "rb") as f:
    kmeans = pickle.load(f)
with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

labels_map = {0: "High Value Customer", 1: "Low Spender", 2: "Average Spender"}

@app.route("/", methods=["GET", "POST"])
def index():
    segment = None
    if request.method == "POST":
        try:
            age = int(request.form["age"])
            income = float(request.form["annual_income"])
            spending_score = float(request.form["spending_score"])

            input_df = pd.DataFrame([[age, income, spending_score]],
                                    columns=["Age", "Annual_Income", "Spending_Score"])
            input_scaled = scaler.transform(input_df)
            cluster = kmeans.predict(input_scaled)[0]
            segment = labels_map[cluster]
        except Exception as e:
            segment = f"Error: {e}"

    return render_template("index.html", segment=segment)

if __name__ == "__main__":
    app.run(debug=True)
