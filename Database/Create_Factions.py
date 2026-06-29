from data.FactionData import faction_data
import sqlite3
import os

BASE_DIR = os.path.dirname(__file__)
DB_PATH = os.path.abspath(os.path.join(BASE_DIR, "..", "app.db"))

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()


# Create a users table
cursor.execute("""
CREATE TABLE IF NOT EXISTS faction (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    -- identity
    name TEXT NOT NULL,
    description TEXT,
    faction_code TEXT UNIQUE NOT NULL,

    -- classification
    faction_type TEXT,      -- kingdom, guild, religion, military, criminal, noble_house, etc.
    alignment TEXT,         -- lawful_good, neutral, chaotic_evil, etc.

    -- relationships
    headquarters_location_code TEXT,
    parent_faction_code TEXT,
    leader_character_code TEXT,

    -- gameplay
    is_joinable INTEGER DEFAULT 1,
    reputation_required INTEGER DEFAULT 0,

    -- lore
    founded_era TEXT,
    motto TEXT,
    lore_text TEXT,

    -- meta
    created_at TEXT DEFAULT (datetime('now')),
    updated_at TEXT DEFAULT (datetime('now'))
)
""")


# Commit changes to make them permanent
connection.commit()


# Inserting a single row safely
cursor.executemany("""
INSERT OR IGNORE INTO faction (
    name,
    description,

    faction_code,

    faction_type,
    alignment,

    headquarters_location_code,
    parent_faction_code,
    leader_character_code,

    is_joinable,
    reputation_required,

    founded_era,
    motto,
    lore_text
)
VALUES (
    ?, ?,

    ?,

    ?, ?,

    ?, ?, ?,

    ?, ?,

    ?, ?, ?
)
""", faction_data)


# Always commit changes after data modifications
connection.commit()
