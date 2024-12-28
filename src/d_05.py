import sqlite3

conn = sqlite3.connect('time_entries.db')
db_cursor = conn.cursor()

db_cursor.execute('''
CREATE TABLE time_entries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT,
    duration INTEGER)''')

conn.commit()

class SQLModel:
    def __init__(self):
        self.conn = sqlite3.connect('time_entries.db')
        self.cursor = self.conn.cursor()

    def all(self):
        self.cursor.execute('SELECT * FROM {}'.format(self.table_name))
        return self.cursor.fetchall()
    
    def insert(self, **kwargs):
        keys = ', '.join(kwargs.keys())
        values = ', '.join(['"{}"'.format(value) for value in kwargs.values()])
        self.cursor.execute('INSERT INTO {} ({}) VALUES ({})'.format(self.table_name, keys, values))
        self.conn.commit()

    def __del__(self):
        self.conn.close()