from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

db_config = {
    'host': os.getenv('MYSQL_HOST'),
    'user': os.getenv('MYSQL_USER'),
    'password': os.getenv('MYSQL_PASSWORD'),
    'database': os.getenv('MYSQL_DB')
}

@app.route('/')
def hello():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("SELECT message FROM messages WHERE version = %s", (os.getenv('APP_VERSION'),))
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        if result:
            return f"Hello from {os.getenv('APP_VERSION')} version: {result[0]}"
        else:
            return f"Hello from {os.getenv('APP_VERSION')} version: No message found"
    except Exception as e:
        return f"Error connecting to DB: {str(e)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)