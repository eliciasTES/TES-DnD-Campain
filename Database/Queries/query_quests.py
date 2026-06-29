import sqlite3
import os


DB_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "app.db")
DB_PATH = os.path.abspath(DB_PATH)

connection = sqlite3.connect(DB_PATH)


with connection as conn:
    # 2. Create a cursor object to execute commands
    cursor = conn.cursor()
    
    # 3. Execute a SELECT query
    cursor.execute("SELECT * FROM quest")
#    cursor.execute("SELECT id, race_id, description FROM characters WHERE name = ?", ("Elias",))

    
    # 4. Fetch the results
    rows = cursor.fetchall()
    

    # 5. Process and display the data

    for quest_record in rows:
        print(quest_record)
        # print(f"Character: {rows[row]}")

