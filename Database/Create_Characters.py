from data.CharactersData import characters_data
import sqlite3
import os

BASE_DIR = os.path.dirname(__file__)
DB_PATH = os.path.abspath(os.path.join(BASE_DIR, "..", "app.db"))

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()


# Create a users table
cursor.execute("""
CREATE TABLE IF NOT EXISTS characters (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    race_id INTEGER,
    gender INTEGER,
    birthsign_id INTEGER, 
    birth_date TEXT,
    age INTEGER,
    height INTEGER, 
    weight INTEGER,
    occupation TEXT,
    current_location_id INTEGER,
    current_residence_id INTEGER,
    status TEXT,
    description TEXT
)
""")


# Commit changes to make them permanent
connection.commit()


# Inserting a single row safely
cursor.executemany("""
INSERT INTO characters (
    name,
    race_id,
    gender,
    birthsign_id,
    birth_date,
    age,
    height,
    weight,
    occupation,
    current_location_id,
    current_residence_id,
    status,
    description
)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
""", characters_data)


# Always commit changes after data modifications
connection.commit()
