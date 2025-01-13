from flask import Flask, jsonify, request
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# MySQL 데이터베이스 연결 설정
db_config = {
    'host': 'localhost',
    'user': 'uys_1705817',
    'password': 'uys_1705817',
    'database': 'shopping_mall'
}

# MySQL 연결 함수
def get_db_connection():
    try:
        conn = mysql.connector.connect(**db_config)
        return conn
    except Error as e:
        print(f"Error: {e}")
        return None

# 상품 CRUD
@app.route('/products', methods=['GET'])
def get_products():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    conn.close()
    return jsonify(products)

@app.route('/products', methods=['POST'])
def add_product():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "INSERT INTO products (name, price, stock) VALUES (%s, %s, %s)"
    values = (data['name'], data['price'], data['stock'])
    cursor.execute(query, values)
    conn.commit()
    conn.close()
    return jsonify({'message': 'Product added successfully'}), 201

@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "UPDATE products SET name=%s, price=%s, stock=%s WHERE id=%s"
    values = (data['name'], data['price'], data['stock'], product_id)
    cursor.execute(query, values)
    conn.commit()
    conn.close()
    return jsonify({'message': 'Product updated successfully'})

@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "DELETE FROM products WHERE id=%s"
    cursor.execute(query, (product_id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Product deleted successfully'})

# 사용자 CRUD
@app.route('/users', methods=['GET'])
def get_users():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()
    return jsonify(users)

@app.route('/users', methods=['POST'])
def add_user():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "INSERT INTO users (name, email) VALUES (%s, %s)"
    values = (data['name'], data['email'])
    cursor.execute(query, values)
    conn.commit()
    conn.close()
    return jsonify({'message': 'User added successfully'}), 201

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "UPDATE users SET name=%s, email=%s WHERE id=%s"
    values = (data['name'], data['email'], user_id)
    cursor.execute(query, values)
    conn.commit()
    conn.close()
    return jsonify({'message': 'User updated successfully'})

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "DELETE FROM users WHERE id=%s"
    cursor.execute(query, (user_id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'User deleted successfully'})

# 주문 CRUD
@app.route('/orders', methods=['GET'])
def get_orders():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM orders")
    orders = cursor.fetchall()
    conn.close()
    return jsonify(orders)

@app.route('/orders', methods=['POST'])
def add_order():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "INSERT INTO orders (user_id, product_id, quantity) VALUES (%s, %s, %s)"
    values = (data['user_id'], data['product_id'], data['quantity'])
    cursor.execute(query, values)
    conn.commit()
    conn.close()
    return jsonify({'message': 'Order added successfully'}), 201

@app.route('/orders/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "UPDATE orders SET user_id=%s, product_id=%s, quantity=%s WHERE id=%s"
    values = (data['user_id'], data['product_id'], data['quantity'], order_id)
    cursor.execute(query, values)
    conn.commit()
    conn.close()
    return jsonify({'message': 'Order updated successfully'})

@app.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "DELETE FROM orders WHERE id=%s"
    cursor.execute(query, (order_id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Order deleted successfully'})

# 홈 화면
@app.route('/')
def home():
    return """
    <html>
        <head><title>Shopping Mall Web Service</title></head>
        <body>
            <h1>Welcome to the Shopping Mall Web Service</h1>
            <p>Developed by: 엄윤상</p>
            <h2>Available Features:</h2>
            <ul>
                <li><a href="/products">Manage Products</a></li>
                <li><a href="/users">Manage Users</a></li>
                <li><a href="/orders">Manage Orders</a></li>
            </ul>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=15022)
