from flask import Flask, Response
import pandas as pd
import random

app = Flask(__name__)

# Load the assignment CSV once
df = pd.read_csv("assignment.csv")

@app.route("/")
def download_random_txt():
    # Pick one random row from the CSV
    random_row = df.sample(1).iloc[0]

    # Step-by-step instructions for students
    instructions = """# Instructions:
# 1. Edit the values below.
# 2. GroupName should be IT320
# 3. AssignCountry should be your home country
# 4. CountryCode should be the correct code for your country
# 5. StudentName should be your full name
# 6. After editing, save this file.
# 7. Upload the updated file to your EC2 instance in the updated_reports directory.
"""

    # Convert row data into editable lines
    content = "\n".join(f"{col}: {val}" for col, val in random_row.items())

    # Combine and return as downloadable file
    full_text = instructions + "\n" + content
    return Response(
        full_text,
        mimetype="text/plain",
        headers={"Content-Disposition": "attachment;filename=task.txt"}
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
