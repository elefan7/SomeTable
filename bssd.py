import sqlite3
import pandas as pd

conn = sqlite3.connect('full.db')

tables = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table';", conn)

for table in tables['name']:
    query = f'SELECT * FROM {table};'
    table_data = pd.read_sql_query(query, conn)

    print(f"\nTabla: {table}")
    print(table_data)

conn.close()