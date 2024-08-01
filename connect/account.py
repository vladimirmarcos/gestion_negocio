import sqlite3

from .conexion_db import ConexionDB

def verify_user(username, password):
    conexion=ConexionDB()
    conexion.cursor.execute('SELECT role FROM users WHERE username=? AND password=?', (username, password))
    result = conexion.cursor.fetchone()
    conexion.close()
    return result

def user_exists(username):
    conexion=ConexionDB()
    conexion.cursor.execute('SELECT * FROM users WHERE username=?', (username,))
    result = conexion.cursor.fetchone()
    conexion.close()
    return result

def create_user(username, password, role):
    if user_exists(username):
        return False
    conexion=ConexionDB()
    conexion.cursor.execute('INSERT INTO users (username, password, role) VALUES (?, ?, ?)', (username, password, role))
    conexion.close()
    return True

def delete_user(username):
    if not user_exists(username):
        return False
    conexion=ConexionDB()
    conexion.cursor.execute('DELETE FROM users WHERE username=?', (username,))
    conexion.close()
    return True

def update_user_role(username, role):
    if not user_exists(username):
        return False
    conexion=ConexionDB()
    conexion.cursor.execute('UPDATE users SET role=? WHERE username=?', (role, username))
    
    conexion.close()
    return True

def update_password(username, new_password):
    conexion=ConexionDB()
    conexion.cursor.execute('UPDATE users SET password=? WHERE username=?', (new_password, username))
    conexion.close()
    return True
