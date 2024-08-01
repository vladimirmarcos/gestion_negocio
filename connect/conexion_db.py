import sqlite3

class ConexionDB:

    def __init__(self):
        """_summary_:open database
        """        
        self.database='users.db'
        self.conexion=sqlite3.connect(self.database)
        self.cursor =self.conexion.cursor()
        

    def close(self):
        """_summary_: commit and close database 
        """        
        self.conexion.commit()
        self.conexion.close()