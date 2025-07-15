from flask import Flask, Response
import pandas as pd
import random

app = Flask(__name__)

# Load CSV once
df = pd.read_csv("assignment.csv")

@app.route("/")
def download_random_txt():
    # Get a random row as a dictionary
    random_row = df.sample(1).iloc[0]

    # Build the text content (e.g., as key-value lines)
    content = "\n".join(f"{col}: {val}" for col, val in random_row.items())

    # Return as a downloadable .txt file
    return Response(
        content,
        mimetype="text/plain",
        headers={"Content-Disposition": "attachment;filename=task.txt"}
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
