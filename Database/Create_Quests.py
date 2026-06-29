from data.QuestData import quest_data
import sqlite3
import os

BASE_DIR = os.path.dirname(__file__)
DB_PATH = os.path.abspath(os.path.join(BASE_DIR, "..", "app.db"))

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()


# Create a users table
cursor.execute("""
CREATE TABLE IF NOT EXISTS quest (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    -- identity
    name TEXT NOT NULL,
    description TEXT,
    quest_code TEXT UNIQUE NOT NULL,

    -- classification
    quest_type TEXT,          -- main, side, guild, daedric, radiant, misc
    rarity TEXT,

    -- progression
    level_required INTEGER,
    difficulty INTEGER,

    -- relationships
    giver_character_code TEXT,
    start_location_code TEXT,
    end_location_code TEXT,
    faction_code TEXT,

    -- quest chain
    prerequisite_quest_code TEXT,
    next_quest_code TEXT,

    -- rewards
    reward_gold INTEGER,
    reward_experience INTEGER,
    reward_item_code TEXT,

    -- lore
    lore_text TEXT,

    -- status
    is_repeatable INTEGER DEFAULT 0,

    -- meta
    created_at TEXT DEFAULT (datetime('now')),
    updated_at TEXT DEFAULT (datetime('now'))
)
""")


# Commit changes to make them permanent
connection.commit()


# Inserting a single row safely
cursor.executemany("""
INSERT OR IGNORE INTO quest (
    name,
    description,
    quest_code,

    quest_type,
    rarity,

    level_required,
    difficulty,

    giver_character_code,
    start_location_code,
    end_location_code,
    faction_code,

    prerequisite_quest_code,
    next_quest_code,

    reward_gold,
    reward_experience,
    reward_item_code,

    lore_text,

    is_repeatable
)


VALUES (
    ?, ?,

    ?,

    ?, ?,

    ?, ?,

    ?, ?, ?, ?,

    ?, ?,

    ?, ?, ?,

    ?,

    ?
)
""", quest_data)

# Always commit changes after data modifications
connection.commit()
