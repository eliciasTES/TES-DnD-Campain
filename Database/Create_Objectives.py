from data.ArmorData import armor_data
import sqlite3
import os

BASE_DIR = os.path.dirname(__file__)
DB_PATH = os.path.abspath(os.path.join(BASE_DIR, "..", "app.db"))

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS armor (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    -- identity
    name TEXT NOT NULL,
    description TEXT,
    is_unique INTEGER DEFAULT 0,
    armor_code TEXT UNIQUE NOT NULL,

    -- classification
    armor_slot TEXT,          -- helmet, chest, gloves, boots, shield
    armor_type TEXT,          -- light, medium, heavy
    material TEXT,
    rarity TEXT,

    -- lore
    origin TEXT,
    lore_text TEXT,

    -- defensive stats
    armor_rating INTEGER,
    magic_resistance INTEGER,
    fire_resistance INTEGER,
    frost_resistance INTEGER,
    shock_resistance INTEGER,
    poison_resistance INTEGER,

    -- physical properties
    weight REAL,
    durability INTEGER,

    -- progression
    level_required INTEGER,
    scaling_stat TEXT,
    scaling_factor REAL,

    -- special effects
    effect_type TEXT,
    status_effect TEXT,
    effect_strength REAL,

    -- enchantments
    enchantment_slots INTEGER DEFAULT 0,
    elemental_affinity TEXT,

    -- meta
    created_at TEXT DEFAULT (datetime('now')),
    updated_at TEXT DEFAULT (datetime('now'))
)
""")

connection.commit()

cursor.executemany("""
INSERT OR IGNORE INTO armor (
    name,
    description,
    is_unique,
    armor_code,

    armor_slot,
    armor_type,
    material,
    rarity,

    origin,
    lore_text,

    armor_rating,
    magic_resistance,
    fire_resistance,
    frost_resistance,
    shock_resistance,
    poison_resistance,

    weight,
    durability,

    level_required,
    scaling_stat,
    scaling_factor,

    effect_type,
    status_effect,
    effect_strength,

    enchantment_slots,
    elemental_affinity
)
VALUES (
    ?, ?, ?, ?,
    ?, ?, ?, ?,
    ?, ?,
    ?, ?, ?, ?, ?, ?,
    ?, ?,
    ?, ?, ?,
    ?, ?, ?,
    ?, ?
)
""", armor_data)

connection.commit()