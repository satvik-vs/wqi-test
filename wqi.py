from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

# Define the raw GitHub URL for your dataset (replace with your GitHub URL)
github_raw_url = "https://raw.githubusercontent.com/satvik-vs/wqi-test/main/sih_water_data_mi.csv"

# Load the WQI dataset from the GitHub raw URL
df = pd.read_csv(github_raw_url)

# Define an API endpoint to get the WQI data
@app.route("/api/wqi")
def get_wqi_data():
    # Convert the dataset to a list of dictionaries
    data = df.to_dict(orient="records")
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
