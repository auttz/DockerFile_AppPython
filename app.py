from flask import Flask, request, render_template
import psycopg2
import os

app = Flask(__name__, template_folder="templates", static_folder="static")

DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")

@app.route("/")
def home():
    return "<h1>Hello Supreecha</h1>"

@app.route("/students", methods=["GET", "POST"])
def show_students():
    results = None
    name = None

    if request.method == "POST":
        name = request.form.get("name", "").strip()

        if name:  # ถ้ามีการกรอกชื่อ
            conn = psycopg2.connect(host=DB_HOST, port=DB_PORT, dbname=DB_NAME, user=DB_USER, password=DB_PASS)
            cur = conn.cursor()
            # ใช้ ILIKE + wildcard เพื่อค้นหาบางส่วน (partial match)
            cur.execute("SELECT name, age, grade FROM students WHERE name ILIKE %s",(f"%{name}%",))
            results = cur.fetchall()
            cur.close()
            conn.close()

    return render_template("students.html", results=results, name=name)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
