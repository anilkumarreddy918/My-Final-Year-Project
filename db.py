import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="anil143",  # your MySQL password
        database="student_db"
    )

def calculate_achievement(marks):
    if marks >= 90:
        return "Diamond"
    elif marks >= 75:
        return "Platinum"
    elif marks >= 60:
        return "Silver"
    elif marks >= 50:
        return "Bronze"
    else:
        return "No Achievement"

def insert_result(name, subject, marks):
    conn = connect_db()
    achievement = calculate_achievement(marks)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO result (name, subject, marks, achievement) VALUES (%s, %s, %s, %s)",
        (name, subject, marks, achievement)
    )
    conn.commit()
    conn.close()

def fetch_results():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM result")
    results = cursor.fetchall()
    conn.close()
    return results

def delete_result(record_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM result WHERE id=%s", (record_id,))
    conn.commit()
    conn.close()

def update_result(record_id, name, subject, marks):
    achievement = calculate_achievement(marks)
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE result SET name=%s, subject=%s, marks=%s, achievement=%s WHERE id=%s",
        (name, subject, marks, achievement, record_id)
    )
    conn.commit()
    conn.close()
