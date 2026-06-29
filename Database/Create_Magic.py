
from data.MagicData import magic_data
import sqlite3
import os

BASE_DIR = os.path.dirname(__file__)
DB_PATH = os.path.abspath(os.path.join(BASE_DIR, "..", "app.db"))

connection = sqlite3.connect(DB_PATH)


cursor = connection.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS magic (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    name TEXT NOT NULL,
    description TEXT,

    -- classification
    school TEXT,
    magic_type TEXT,
    element TEXT,
    subtype TEXT,

    -- mechanics
    mana_cost INTEGER,
    stamina_cost INTEGER,
    cooldown INTEGER,
    cast_time REAL,
    duration INTEGER,
    range INTEGER,
    area_of_effect INTEGER,

    damage INTEGER,
    healing INTEGER,

    -- scaling
    level_required INTEGER,
    scaling_stat TEXT,
    power_scale REAL,

    -- effects
    effect_type TEXT,
    status_effect TEXT,
    effect_strength REAL,

    -- gameplay rules
    requires_target INTEGER DEFAULT 1,
    is_aoe INTEGER DEFAULT 0,

    -- lore
    rarity TEXT,
    origin TEXT,
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
INSERT INTO magic (
    name,
    description,

    school,
    magic_type,
    element,
    subtype,

    mana_cost,
    stamina_cost,
    cooldown,
    cast_time,
    duration,
    range,
    area_of_effect,

    damage,
    healing,

    level_required,
    scaling_stat,
    power_scale,

    effect_type,
    status_effect,
    effect_strength,

    requires_target,
    is_aoe,

    rarity,
    origin,
    lore_text
)
VALUES (
    ?, ?, 
    ?, ?, ?, ?,
    ?, ?, ?, ?, ?, ?, ?,
    ?, ?,
    ?, ?, ?,
    ?, ?, ?,
    ?, ?,
    ?, ?, ?
)
""", magic_data)


# Always commit changes after data modifications
connection.commit()
