import mysql.connector

# MySQL 연결 설정
connection = mysql.connector.connect(
    host="localhost",            # MySQL 서버 주소
    user="user1",                # MySQL 사용자 이름
    password="user1",            # MySQL 암호
    database="user1"             # 사용할 데이터베이스 이름
)

# 커서 생성
cursor = connection.cursor()

# 0. 테이블 생성
def create_table():
    query = """
    CREATE TABLE IF NOT EXISTS students (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        age INT NOT NULL,
        department VARCHAR(50) NOT NULL
    );
    """
    cursor.execute(query)
    print("Table 'students' has been created or already exists.")

# 1. CREATE: 데이터 삽입
def create_example():
    query = "INSERT INTO students (name, age, department) VALUES (%s, %s, %s)"
    values = ("John Doe", 20, "Computer Science")
    cursor.execute(query, values)
    connection.commit()
    print(f"Inserted ID: {cursor.lastrowid}")

# 2. READ: 데이터 조회
def read_example():
    query = "SELECT * FROM students"
    cursor.execute(query)
    results = cursor.fetchall()
    print("Current data in 'students' table:")
    for row in results:
        print(row)

# 3. UPDATE: 데이터 수정
def update_example():
    query = "UPDATE students SET age = %s WHERE name = %s"
    values = (21, "John Doe")
    cursor.execute(query, values)
    connection.commit()
    print(f"Updated Rows: {cursor.rowcount}")

# 4. DELETE: 데이터 삭제
def delete_example():
    query = "DELETE FROM students WHERE name = %s"
    values = ("John Doe",)
    cursor.execute(query, values)
    connection.commit()
    print(f"Deleted Rows: {cursor.rowcount}")

# 메인 실행
if __name__ == "__main__":
    # 0. 테이블 생성
    create_table()
    # 1. CREATE
    create_example()
    # 2. READ
    read_example()
    # 3. UPDATE
    update_example()
    # 4. READ (After Update)
    read_example()
    # 5. DELETE
    delete_example()
    # 6. READ (After Delete)
    read_example()

# 연결 종료
cursor.close()
connection.close()
