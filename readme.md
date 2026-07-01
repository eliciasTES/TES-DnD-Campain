# 📜 Elder Scrolls Campaign Database

Welcome to the repository for the **Elias & Virel** campaign, set in the Elder Scrolls universe.

This project is designed as a relational world database for tracking characters, locations, equipment, quests, factions, and other game content. While originally created for roleplaying in the Elder Scrolls games, the database is structured to support a tabletop-style RPG campaign with interconnected world data.

---

# 🏛️ Design Philosophy

Every major entity in the world has:

* An internal database ID
* A unique `*_code` used for stable references
* Gameplay data
* Lore and descriptive information

Relationships between entities are made through these unique codes rather than duplicated text.

For example:

* Weapons reference locations.
* Characters reference equipment.
* Quests reference locations, factions, and characters.
* Locations form a hierarchy using `parent_location_code`.

This keeps the world organized, scalable, and easy to query.

---

# 📂 Current Database Modules

## Characters

Represents player characters, NPCs, companions, merchants, rulers, and other individuals.

Examples:

* Elias
* Virel
* Jarl Balgruuf

---

## Weapons

Stores all melee, ranged, and artifact weapons.

Examples:

* Steel Sword
* Silver Sword
* Dawnbreaker

---

## Armor

Stores wearable equipment.

Examples:

* Steel Cuirass
* Helmet of Stendarr

---

## Magic

Stores spells, shouts, powers, and magical abilities.

Examples:

* Fireball
* Healing
* Whispering Shadow

---

## Locations

A hierarchical world map using `parent_location_code`.

Example:

```text
Skyrim
└── Whiterun Hold
    └── Whiterun
        ├── Wind District
        │   └── Dragonsreach
        │       └── Great Porch
        ├── Bannered Mare
        └── Breezehome
```

Supported location types include:

* Province
* Hold
* City
* District
* Building
* House
* Inn
* Temple
* Cave
* Dungeon
* Ruin
* Tower
* Fort
* Camp
* Room

---

## Factions

Organizations, governments, guilds, religious orders, criminal groups, and noble houses.

Examples:

* Kingdom of Whiterun
* The Companions
* Order of Stendarr

---

## Quests

Stores quests and quest chains.

Each quest can reference:

* Quest giver
* Start location
* End location
* Faction
* Reward item
* Previous/next quests

---

# 🔗 Entity Relationships

The database is designed around connected entities.

Examples:

```text
Character
    ├── belongs to → Faction
    ├── equips → Weapon
    ├── equips → Armor
    └── lives at → Location

Quest
    ├── starts at → Location
    ├── ends at → Location
    ├── given by → Character
    └── rewards → Item

Location
    └── parent → Location

Faction
    ├── headquartered at → Location
    └── led by → Character
```

---

# 📖 Lore Documentation

While structured gameplay data is stored in SQLite, Markdown documents are still useful for long-form content such as:

* Character biographies
* Historical timelines
* Session logs
* Maps
* Artwork
* Worldbuilding notes
* Story outlines

---

# 🚀 Future Database Modules

Planned additions include:

* Creatures
* NPCs
* Races
* Skills
* Perks
* Deities
* Religions
* Organizations
* Crafting Recipes
* Ingredients
* Alchemy
* Books
* Dialogue
* Merchants
* Inventory
* Character Factions
* Quest Objectives
* World Events

---

# 🎯 Goals

* Create a fully connected Elder Scrolls world database.
* Separate gameplay data from creative writing.
* Make all entities searchable and reusable.
* Support long-running roleplaying campaigns.
* Provide a foundation for future tools such as encounter generators, quest generators, NPC generators, and campaign management software.

---

> "Every legend begins as a single record."
>
> <img width="2560" height="1920" alt="Skyrim Province Map" src="https://github.com/user-attachments/assets/b1f91f14-4916-44cb-a349-28e870d75bea" />

