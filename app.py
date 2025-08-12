from flask import Flask
import psycopg2

app = Flask(__name__)

# เชื่อมต่อฐานข้อมูล
conn = psycopg2.connect(
    host="db",      # หรือชื่อ service ใน Docker เช่น db
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
    with conn.cursor() as cur:
        cur.execute("SELECT name, age, grade FROM students;")
        students = cur.fetchall()
    # แปลงข้อมูลแต่ละแถวเป็นข้อความ
    student_lines = []
    for name, age, grade in students:
        student_lines.append(f"ชื่อ: {name}, อายุ: {age} ปี, เกรด: {grade}")
    # รวมเป็น HTML ใช้ <br> คั่น
    return "<br>".join(student_lines)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
