from flask import Flask, send_file
import random
import pandas as pd

app = Flask(__name__)

@app.route("/")
def download_file():
    df = pd.read_csv("assignment.csv")
    random_rows = df.sample(10)  # adjust logic if needed
    random_rows.to_csv("student_assignment.csv", index=False)
    return send_file("student_assignment.csv", as_attachment=True)

if __name__ == "__main__":
    app.run()
