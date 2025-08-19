from flask import Flask , send_from_directory
import psycopg2

app = Flask(__name__)

# เชื่อมต่อฐานข้อมูล
conn = psycopg2.connect(
    host="db",      #ชื่อ service ใน Docker เช่น db
    port=5432,
    database="mydb",
    user="user",
    password="pass"
)
conn.autocommit = True

@app.route("/")
def home():
    return "<h1>Hello Supreecha</h1>"

@app.route("/students")
def show_students():
    return send_from_directory("frontend","web.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
