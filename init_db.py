import sqlite3

# Connect to database (creates if it doesn't exist)
conn = sqlite3.connect("database.db")

# Read the schema.sql file
with open("schema.sql") as f:
    conn.executescript(f.read())

# Commit changes and close connection
conn.commit()
conn.close()

print("Database initialized successfully.")
