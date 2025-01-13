from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

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

# 데이터베이스 모델
class Item:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

    def to_dict(self):
        return {"id": self.id, "name": self.name, "description": self.description}

# CREATE: 항목 추가
@app.route('/items', methods=['POST'])
def create_item():
    data = request.get_json()
    if not data or not data.get('name'):
        return jsonify({"error": "Name is required."}), 400

    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        query = "INSERT INTO items (name, description) VALUES (%s, %s)"
        cursor.execute(query, (data['name'], data.get('description')))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"message": "Item created."}), 201
    return jsonify({"error": "Database connection failed."}), 500

# READ: 모든 항목 조회
@app.route('/items', methods=['GET'])
def get_items():
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM items"
        cursor.execute(query)
        items = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(items), 200
    return jsonify({"error": "Database connection failed."}), 500

# READ: 특정 항목 조회
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM items WHERE id = %s"
        cursor.execute(query, (item_id,))
        item = cursor.fetchone()
        cursor.close()
        conn.close()
        if item:
            return jsonify(item), 200
        return jsonify({"error": "Item not found."}), 404
    return jsonify({"error": "Database connection failed."}), 500

# UPDATE: 항목 수정
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.get_json()
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        query = "UPDATE items SET name = %s, description = %s WHERE id = %s"
        cursor.execute(query, (data.get('name'), data.get('description'), item_id))
        conn.commit()
        cursor.close()
        conn.close()
        if cursor.rowcount > 0:
            return jsonify({"message": "Item updated."}), 200
        return jsonify({"error": "Item not found."}), 404
    return jsonify({"error": "Database connection failed."}), 500

# DELETE: 항목 삭제
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        query = "DELETE FROM items WHERE id = %s"
        cursor.execute(query, (item_id,))
        conn.commit()
        cursor.close()
        conn.close()
        if cursor.rowcount > 0:
            return jsonify({"message": "Item deleted."}), 200
        return jsonify({"error": "Item not found."}), 404
    return jsonify({"error": "Database connection failed."}), 500

if __name__ == '__main__':
    app.run(port=15022, debug=True)
