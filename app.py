import os
from werkzeug.utils import secure_filename
from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)
UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/report")
def report():
    return render_template("report.html")


@app.route("/submit-report", methods=["POST"])
def submit_report():
    photo = request.files["photo"]

    filename = secure_filename(photo.filename)

    photo.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

    name = request.form["name"]
    age = request.form["age"]
    gender = request.form["gender"]
    location = request.form["location"]
    date = request.form["date"]
    description = request.form["description"]


    conn = sqlite3.connect("hopelink.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO missing_persons
   (name, age, gender, location, date_missing, description, photo)
   VALUES (?, ?, ?, ?, ?, ?, ?)
""",(name,age,gender,location,date,description,filename))
    conn.commit()
    conn.close()

    return """
    <h2>✅ Report Submitted Successfully!</h2>
    <a href="/">Go to Home</a>
    """
@app.route("/dashboard")
def dashboard():

    conn = sqlite3.connect("hopelink.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM missing_persons")

    reports = cursor.fetchall()

    conn.close()

    return render_template("dashboard.html", reports=reports)

if __name__ == "__main__":
    app.run(debug=True)