from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Function to connect to the database
def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row  # So we can use column names
    return conn

# Home route - Display all tasks
@app.route('/')
def index():
    conn = get_db_connection()
    tasks = conn.execute("SELECT * FROM tasks").fetchall()
    conn.close()
    return render_template('index.html', tasks=tasks)

# Add a new task
@app.route('/add', methods=['POST'])
def add_task():
    description = request.form['description']
    if description:  # Prevent empty tasks
        conn = get_db_connection()
        conn.execute("INSERT INTO tasks (description) VALUES (?)", (description,))
        conn.commit()
        conn.close()
    return redirect(url_for('index'))

# Mark a task as completed
@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    try:
        conn = get_db_connection()
        # First check if the completed column exists
        cursor = conn.execute("SELECT * FROM tasks LIMIT 1")
        columns = [description[0] for description in cursor.description]
        
        if 'completed' not in columns:
            # Add completed column if it doesn't exist
            conn.execute("ALTER TABLE tasks ADD COLUMN completed INTEGER DEFAULT 0")
            conn.commit()
            
        conn.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,))
        conn.commit()
    except sqlite3.OperationalError as e:
        print(f"Database error: {e}")
    finally:
        conn.close()
    return redirect(url_for('index'))

# Delete a task
@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    conn = get_db_connection()
    conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))




if __name__ == '__main__':
    app.run(debug=True)
