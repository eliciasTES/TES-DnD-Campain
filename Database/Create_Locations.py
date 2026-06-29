from data.LocationData import location_data
import sqlite3
import os

BASE_DIR = os.path.dirname(__file__)
DB_PATH = os.path.abspath(os.path.join(BASE_DIR, "..", "app.db"))

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS location (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    name TEXT NOT NULL,
    description TEXT,
    location_code TEXT UNIQUE NOT NULL,
    location_type TEXT,
    parent_location_code TEXT,
    region TEXT,
    is_discoverable INTEGER DEFAULT 1,
    danger_level INTEGER,
    owner TEXT,
    faction TEXT,
    lore_text TEXT,
    created_at TEXT DEFAULT (datetime('now')),
    updated_at TEXT DEFAULT (datetime('now'))
)
""")

cursor.executemany("""
INSERT OR IGNORE INTO location (
    name,
    description,
    location_code,
    location_type,
    parent_location_code,
    region,
    is_discoverable,
    danger_level,
    owner,
    faction,
    lore_text
)
VALUES (
    ?, ?,
    ?,
    ?,
    ?,
    ?,
    ?,
    ?,
    ?,
    ?,
    ?
)
""", location_data)

# Always commit changes after data modifications
connection.commit()
