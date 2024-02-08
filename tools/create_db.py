"""
Create the database and tables
"""

import sqlite3

if __name__ == "__main__":
    # Create the database
    db = sqlite3.connect('../assistant.db')
    cursor = db.cursor()

    # Create the tables
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS joined_groups(
        id INTEGER PRIMARY KEY,
        entity TEXT,
        access_hash TEXT,
        timestamp_joined INTEGER)
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS messages(
        id INTEGER PRIMARY KEY,
        from_id INTEGER,
        group_username TEXT, 
        message TEXT,
        timestamp_sent INTEGER)
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS groups_to_watch(
        id INTEGER PRIMARY KEY,
        group_username TEXT)
    ''')

    db.commit()
    db.close()
    print("Database created successfully")
