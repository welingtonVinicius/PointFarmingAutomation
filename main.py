from flask import Flask, request, jsonify
import os
import sqlite3

app = Flask(__name__)

DATABASE_PATH = os.getenv('DATABASE_PATH', 'database.db')

def init_database():
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS connections (
            id INTEGER PRIMARY KEY, 
            name TEXT, 
            url TEXT, 
            is_active INTEGER
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY, 
            name TEXT, 
            connection_id INTEGER, 
            status TEXT,
            FOREIGN KEY(connection_id) REFERENCES connections(id)
        )
    ''')
    connection.commit()
    connection.close()

def get_database_connection():
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    return connection

@app.route('/connections', methods=['POST', 'GET'])
def site_connections():
    if request.method == 'POST':
        post_data = request.get_json()
        connection = get_database_connection()
        cursor = connection.cursor()
        
        cursor.execute(
            "INSERT INTO connections (name, url, is_active) VALUES (?, ?, ?)",
            (post_data['name'], post_data['url'], post_data.get('is_active', 1))
        )
        connection.commit()
        connection.close()
        
        return jsonify({'message': 'Connection added successfully'}), 201
    
    elif request.method == 'GET':
        connection = get_database_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM connections")
        connections_list = cursor.fetchall()
        connection.close()
        
        return jsonify([dict(row) for row in connections_list]), 200

@app.route('/tasks', methods=['POST', 'GET'])
def farming_tasks():
    if request.method == 'POST':
        post_data = request.get_json()
        connection = get_database_connection()
        cursor = connection.cursor()
        
        cursor.execute(
            "INSERT INTO tasks (name, connection_id, status) VALUES (?, ?, ?)",
            (post_data['name'], post_data['connection_id'], post_data.get('status', 'pending'))
        )
        connection.commit()
        connection.close()
        
        return jsonify({'message': 'Task added successfully'}), 201
    
    elif request.method == 'GET':
        connection = get_database_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM tasks")
        tasks_list = cursor.fetchall()
        connection.close()
        
        return jsonify([dict(row) for row in tasks_list]), 200

@app.route('/tasks/update', methods=['POST'])
def update_task():
    post_data = request.get_json()
    task_id = post_data['id']
    new_status = post_data['status']
    
    connection = get_database_connection()
    cursor = connection.cursor()
    cursor.execute("UPDATE tasks SET status=? WHERE id=?",
                   (new_status, task_id))
    connection.commit()
    connection.close()
    
    return jsonify({'message': 'Task updated successfully'}), 200

if __name__ == '__main__':
    init_database()
    app.run(debug=True)