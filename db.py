import sqlite3

def create_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            role TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def verify_user(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT role FROM users WHERE username=? AND password=?', (username, password))
    result = cursor.fetchone()
    conn.close()
    return result

def user_exists(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username=?', (username,))
    result = cursor.fetchone()
    conn.close()
    return result

def create_user(username, password, role):
    if user_exists(username):
        return False
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (username, password, role) VALUES (?, ?, ?)', (username, password, role))
    conn.commit()
    conn.close()
    return True

def delete_user(username):
    if not user_exists(username):
        return False
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM users WHERE username=?', (username,))
    conn.commit()
    conn.close()
    return True

def update_user_role(username, role):
    if not user_exists(username):
        return False
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE users SET role=? WHERE username=?', (role, username))
    conn.commit()
    conn.close()
    return True

def update_password(username, new_password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE users SET password=? WHERE username=?', (new_password, username))
    conn.commit()
    conn.close()
    return True
