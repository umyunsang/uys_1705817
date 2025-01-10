from flask import Flask, jsonify, request, abort
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# MySQL 데이터베이스 연결 설정
db_config = {
    'host': 'localhost',
    'user': 'your_acc',
    'password': 'your_acc',
    'database': 'your_acc'
}

# MySQL 연결 함수
def get_db_connection():
    try:
        conn = mysql.connector.connect(**db_config)
        return conn
    except Error as e:
        print(f"Error: {e}")
        return None

# 수업 CRUD
@app.route('/courses', methods=['GET'])
def get_courses():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM courses")
    courses = cursor.fetchall()
    conn.close()
    return jsonify(courses)

@app.route('/courses', methods=['POST'])
def add_course():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "INSERT INTO courses (name, instructor, location, time) VALUES (%s, %s, %s, %s)"
    values = (data['name'], data['instructor'], data['location'], data['time'])
    cursor.execute(query, values)
    conn.commit()
    conn.close()
    return jsonify({'message': 'Course added successfully'}), 201

@app.route('/courses/<int:course_id>', methods=['PUT'])
def update_course(course_id):
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "UPDATE courses SET name=%s, instructor=%s, location=%s, time=%s WHERE id=%s"
    values = (data['name'], data['instructor'], data['location'], data['time'], course_id)
    cursor.execute(query, values)
    conn.commit()
    conn.close()
    return jsonify({'message': 'Course updated successfully'})

@app.route('/courses/<int:course_id>', methods=['DELETE'])
def delete_course(course_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "DELETE FROM courses WHERE id=%s"
    cursor.execute(query, (course_id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Course deleted successfully'})

# 학생 CRUD
@app.route('/students', methods=['GET'])
def get_students():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    conn.close()
    return jsonify(students)

@app.route('/students', methods=['POST'])
def add_student():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "INSERT INTO students (name, student_id) VALUES (%s, %s)"
    values = (data['name'], data['student_id'])
    cursor.execute(query, values)
    conn.commit()
    conn.close()
    return jsonify({'message': 'Student added successfully'}), 201

@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "UPDATE students SET name=%s, student_id=%s WHERE id=%s"
    values = (data['name'], data['student_id'], student_id)
    cursor.execute(query, values)
    conn.commit()
    conn.close()
    return jsonify({'message': 'Student updated successfully'})

@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "DELETE FROM students WHERE id=%s"
    cursor.execute(query, (student_id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Student deleted successfully'})

# 수업 신청/취소
@app.route('/enrollments', methods=['POST'])
def enroll_student():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "INSERT INTO enrollments (course_id, student_id) VALUES (%s, %s)"
    values = (data['course_id'], data['student_id'])
    cursor.execute(query, values)
    conn.commit()
    conn.close()
    return jsonify({'message': 'Student enrolled successfully'})

@app.route('/enrollments', methods=['DELETE'])
def unenroll_student():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "DELETE FROM enrollments WHERE course_id=%s AND student_id=%s"
    values = (data['course_id'], data['student_id'])
    cursor.execute(query, values)
    conn.commit()
    conn.close()
    return jsonify({'message': 'Student unenrolled successfully'})

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=15022)  # your_port
