# 🧱 Elder Scrolls Campaign Database Schema

This document defines the structure of all SQLite tables used in the campaign world database.

Each table uses:
- `id` as the primary key
- `*_code` as the stable external identifier used for relationships


# 🧠 DESIGN INTENT

This schema is designed to:

Support a fully connected RPG world
Allow hierarchical world-building (locations, factions)
Enable quest chains and world logic
Keep all entities referenceable via stable codes
Avoid tight coupling between systems

# Core Design Rules

1. Primary Keys
Every table uses id INTEGER PRIMARY KEY
2. Stable References
All cross-table references use *_code
3. Hierarchies
Locations and factions use self-referencing parent_*_code
4. Expandability
New systems should follow the same pattern:
id
name
description
*_code
relationship fields last


---

# 🧍 CHARACTER

Represents all playable characters and NPCs.

```sql
id INTEGER PRIMARY KEY
name TEXT
description TEXT
character_code TEXT UNIQUE

race TEXT
class TEXT

level INTEGER
health INTEGER
stamina INTEGER
magicka INTEGER

faction_code TEXT
location_code TEXT

created_at TEXT
updated_at TEXT
```

# Weapon

```sql
id INTEGER PRIMARY KEY
name TEXT
description TEXT
weapon_code TEXT UNIQUE

weapon_class TEXT
weapon_type TEXT
material TEXT
rarity TEXT

damage INTEGER
damage_type TEXT
attack_speed REAL
crit_chance REAL
range INTEGER

weight REAL
durability INTEGER

level_required INTEGER
scaling_stat TEXT
scaling_factor REAL

effect_type TEXT
status_effect TEXT
effect_strength REAL

enchantment_slots INTEGER
elemental_affinity TEXT

is_unique INTEGER

created_at TEXT
updated_at TEXT
```

# Armor

```sql
id INTEGER PRIMARY KEY
name TEXT
description TEXT
armor_code TEXT UNIQUE

armor_slot TEXT
armor_type TEXT
material TEXT
rarity TEXT

armor_rating INTEGER

magic_resistance INTEGER
fire_resistance INTEGER
frost_resistance INTEGER
shock_resistance INTEGER
poison_resistance INTEGER

weight REAL
durability INTEGER

level_required INTEGER
scaling_stat TEXT
scaling_factor REAL

effect_type TEXT
status_effect TEXT
effect_strength REAL

enchantment_slots INTEGER
elemental_affinity TEXT

is_unique INTEGER

created_at TEXT
updated_at TEXT
```

# Location

```sql
id INTEGER PRIMARY KEY
name TEXT
description TEXT
location_code TEXT UNIQUE

location_type TEXT

parent_location_code TEXT

worldspace TEXT

climate TEXT
danger_level INTEGER

is_discoverable INTEGER

owner_character_code TEXT
faction_code TEXT

lore_text TEXT

created_at TEXT
updated_at TEXT
```

# Faction

```sql
id INTEGER PRIMARY KEY
name TEXT
description TEXT
faction_code TEXT UNIQUE

faction_type TEXT
alignment TEXT

headquarters_location_code TEXT
parent_faction_code TEXT
leader_character_code TEXT

is_joinable INTEGER
reputation_required INTEGER

founded_era TEXT
motto TEXT
lore_text TEXT

created_at TEXT
updated_at TEXT
```

# Quest

```sql
id INTEGER PRIMARY KEY
name TEXT
description TEXT
quest_code TEXT UNIQUE

quest_type TEXT
rarity TEXT

level_required INTEGER
difficulty INTEGER

giver_character_code TEXT
start_location_code TEXT
end_location_code TEXT
faction_code TEXT

prerequisite_quest_code TEXT
next_quest_code TEXT

reward_gold INTEGER
reward_experience INTEGER
reward_item_code TEXT

lore_text TEXT

is_repeatable INTEGER

created_at TEXT
updated_at TEXT
```
