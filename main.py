from flask import Flask, request, jsonify
import os
import sqlite3

app = Flask(__name__)

DATABASE_URI = os.getenv('DATABASE_URI', 'database.db')

def initialize_db():
    conn = sqlite3.connect(DATABASE_URI)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS site_connections (
            id INTEGER PRIMARY KEY, 
            site_name TEXT, 
            site_url TEXT, 
            active INTEGER
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS farming_tasks (
            id INTEGER PRIMARY KEY, 
            task_name TEXT, 
            site_id INTEGER, 
            status TEXT,
            FOREIGN KEY(site_id) REFERENCES site_connections(id)
        )
    ''')
    conn.commit()
    conn.close()

def get_db_connection():
    conn = sqlite3.connect(DATABASE_URI)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/site-connections', methods=['POST', 'GET'])
def manage_site_connections():
    if request.method == 'POST':
        data = request.get_json()
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute(
            "INSERT INTO site_connections (site_name, site_url, active) VALUES (?, ?, ?)",
            (data['site_name'], data['site_url'], data.get('active', 1))
        )
        conn.commit()
        conn.close()
        
        return jsonify({'message': 'Site connection added successfully'}), 201
    
    elif request.method == 'GET':
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM site_connections")
        connections = cursor.fetchall()
        conn.close()
        
        return jsonify([dict(row) for row in connections]), 200

@app.route('/farming-tasks', methods=['POST', 'GET'])
def handle_farming_tasks():
    if request.method == 'POST':
        data = request.get_json()
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute(
            "INSERT INTO farming_tasks (task_name, site_id, status) VALUES (?, ?, ?)",
            (data['task_name'], data['site_id'], data.get('status', 'pending'))
        )
        conn.commit()
        conn.close()
        
        return jsonify({'message': 'Farming task added successfully'}), 201
    
    elif request.method == 'GET':
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM farming_tasks")
        tasks = cursor.fetchall()
        conn.close()
        
        return jsonify([dict(row) for row in tasks]), 200

@app.route('/farming-tasks/update', methods=['POST'])
def update_farming_task():
    data = request.get_json()
    task_id = data['id']
    new_status = data['status']
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE farming_tasks SET status=? WHERE id=?",
                   (new_status, task_id))
    conn.commit()
    conn.close()
    
    return jsonify({'message': 'Farming task updated successfully'}), 200

if __name__ == '__main__':
    initialize_db()
    app.run(debug=True)