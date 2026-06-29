from data.WeaponData import weapon_data
import sqlite3
import os

BASE_DIR = os.path.dirname(__file__)
DB_PATH = os.path.abspath(os.path.join(BASE_DIR, "..", "app.db"))

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS weapon (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    -- identity
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    is_unique INTEGER DEFAULT 0,
    weapon_code TEXT UNIQUE NOT NULL,

    -- classification
    weapon_class TEXT,        -- sword, axe, bow, dagger, staff, spear
    weapon_type TEXT,         -- melee, ranged, thrown, hybrid
    material TEXT,            -- steel, iron, silver, bone, daedric, etc
    rarity TEXT,
    origin TEXT,
    lore_text TEXT,

    -- combat stats
    damage INTEGER,
    damage_type TEXT,         -- slashing, piercing, bludgeoning, elemental
    attack_speed REAL,
    crit_chance REAL,
    range INTEGER,

    -- handling / physical properties
    weight REAL,
    durability INTEGER,
    required_hand_count INTEGER DEFAULT 1,

    -- scaling / progression
    level_required INTEGER,
    scaling_stat TEXT,        -- strength, dexterity, agility, etc
    scaling_factor REAL,

    -- special effects
    effect_type TEXT,
    status_effect TEXT,
    effect_strength REAL,

    -- enchantment / magic infusion support
    enchantment_slots INTEGER DEFAULT 0,
    elemental_affinity TEXT,

    -- gameplay rules
    is_two_handed INTEGER DEFAULT 0,
    can_be_thrown INTEGER DEFAULT 0,

    -- meta
    created_at TEXT DEFAULT (datetime('now')),
    updated_at TEXT DEFAULT (datetime('now'))
)
""")

connection.commit()


cursor.executemany("""
INSERT OR IGNORE INTO weapon (
    name,
    description,
    is_unique,
    weapon_code, 

    weapon_class,
    weapon_type,
    material,
    rarity,
    origin,
    lore_text,

    damage,
    damage_type,
    attack_speed,
    crit_chance,
    range,

    weight,
    durability,
    required_hand_count,

    level_required,
    scaling_stat,
    scaling_factor,

    effect_type,
    status_effect,
    effect_strength,

    enchantment_slots,
    elemental_affinity,

    is_two_handed,
    can_be_thrown
)
VALUES (
    ?, ?, ?, ?,
    ?, ?, ?, ?, ?, ?,
    ?, ?, ?, ?, ?,
    ?, ?, ?,
    ?, ?, ?,
    ?, ?, ?,
    ?, ?,
    ?, ?
)
""", weapon_data)

connection.commit()