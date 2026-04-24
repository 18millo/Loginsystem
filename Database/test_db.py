from Loginsystem.Database.db import get_connection

try:
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT version();")
    result = cursor.fetchone()

    print("DB connected successfully")
    print("PostgreSQL:", result)

    conn.close()

except Exception as e:
    print("Connection failed:")
    print(e)