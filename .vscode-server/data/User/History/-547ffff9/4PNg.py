from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # 세션을 사용할 때는 secret_key가 필요합니다.

# MySQL 데이터베이스 연결 설정
db_config = {
    'host': 'localhost',
    'user': 'uys_1705817',
    'password': 'uys_1705817',
    'database': 'uys_1705817'
}

# MySQL 연결 함수
def get_db_connection():
    try:
        conn = mysql.connector.connect(**db_config)
        return conn
    except Error as e:
        print(f"Error: {e}")
        return None

# 홈 페이지
@app.route('/')
def home():
    return render_template('home.html')


# 수업 CRUD - 추가 (Add Course)
@app.route('/courses/add', methods=['GET', 'POST'])
def add_course():
    if request.method == 'POST':
        name = request.form['name']
        instructor = request.form['instructor']
        location = request.form['location']
        time = request.form['time']
        
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "INSERT INTO courses (name, instructor, location, time) VALUES (%s, %s, %s, %s)"
        values = (name, instructor, location, time)
        cursor.execute(query, values)
        conn.commit()
        conn.close()
        
        # 수업 추가 성공 시 알림 메시지
        flash('수업이 추가되었습니다!', 'success')

        # 홈 페이지로 리디렉션
        return redirect(url_for('home'))

    return render_template('add_course.html')

# 수업 CRUD - 조회 (View Courses)
@app.route('/courses', methods=['GET'])
def get_courses():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM courses")
    courses = cursor.fetchall()
    conn.close()
    
    return render_template('read_courses.html', courses=courses)

# 수업 CRUD - 수정 (Update Course)
@app.route('/courses/update', methods=['GET', 'POST'])
def update_course():
    if request.method == 'POST':
        course_id = request.form['course_id']
        name = request.form['name']
        instructor = request.form['instructor']
        location = request.form['location']
        time = request.form['time']

        conn = get_db_connection()
        cursor = conn.cursor()
        query = "UPDATE courses SET name=%s, instructor=%s, location=%s, time=%s WHERE id=%s"
        values = (name, instructor, location, time, course_id)
        cursor.execute(query, values)
        conn.commit()
        conn.close()

        return "Course updated successfully"

    return """
    <html>
        <head><title>Update Course</title></head>
        <body>
            <h1>Update Course</h1>
            <form method="POST">
                <label for="course_id">Course ID:</label><br>
                <input type="text" id="course_id" name="course_id" required><br><br>
                <label for="name">Course Name:</label><br>
                <input type="text" id="name" name="name" required><br><br>
                <label for="instructor">Instructor:</label><br>
                <input type="text" id="instructor" name="instructor" required><br><br>
                <label for="location">Location:</label><br>
                <input type="text" id="location" name="location" required><br><br>
                <label for="time">Time:</label><br>
                <input type="text" id="time" name="time" required><br><br>
                <input type="submit" value="Update Course">
            </form>
        </body>
    </html>
    """

# 수업 CRUD - 삭제 (Delete Course)
@app.route('/courses/delete', methods=['GET', 'POST'])
def delete_course():
    if request.method == 'POST':
        course_id = request.form['course_id']

        conn = get_db_connection()
        cursor = conn.cursor()
        query = "DELETE FROM courses WHERE id=%s"
        cursor.execute(query, (course_id,))
        conn.commit()
        conn.close()

        return "Course deleted successfully"

    return """
    <html>
        <head><title>Delete Course</title></head>
        <body>
            <h1>Delete Course</h1>
            <form method="POST">
                <label for="course_id">Course ID:</label><br>
                <input type="text" id="course_id" name="course_id" required><br><br>
                <input type="submit" value="Delete Course">
            </form>
        </body>
    </html>
    """



if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=15022)
