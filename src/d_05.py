import sqlite3


class SQLModel:

    def __init__(self):
        self.conn = sqlite3.connect("time_entries.db")
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()

        self.cursor.execute(
            '''
            CREATE TABLE if not exists time_entries(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            project TEXT,
            client TEXT,
            description TEXT,
            duration FLOAT,
            created_at TEXT
            )''')
        self.conn.commit()


    def insert_entry(self, 
                     project:str,
                     client:str,
                     description:str, 
                     duration:float,
                     created_at:str):
        self.cursor.execute(
            '''
            INSERT INTO time_entries(
            project,
            client,
            description, 
            duration,
            created_at
            ) VALUES (?, ?, ?, ?, ?)''',(project, client, description, duration, created_at),)
        self.conn.commit()

    
    def remove_entry(self, entry_id):
        self.cursor.execute(
            '''
            DELETE FROM time_entries WHERE id=?''', 
            (entry_id,))
        self.conn.commit()


    def get_entries(self):
        self.cursor.execute('''SELECT * FROM time_entries''')
        return self.cursor.fetchall()


    def get_entry(self, entry_id):
        self.cursor.execute('''SELECT * FROM time_entries WHERE id=?''', (entry_id,))
        return self.cursor.fetchone()