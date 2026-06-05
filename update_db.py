import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

try:
    cursor.execute("""
    ALTER TABLE reservasi
    ADD COLUMN is_deleted INTEGER DEFAULT 0
    """)

    conn.commit()

    print("Kolom is_deleted berhasil ditambahkan")

except Exception as e:

    print("Error:", e)

conn.close()