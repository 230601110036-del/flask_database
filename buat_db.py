import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE reservasi(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nama TEXT NOT NULL,
    telepon TEXT NOT NULL,
    paket TEXT NOT NULL,
    tanggal TEXT NOT NULL,
    jam TEXT NOT NULL
)
""")

conn.commit()
conn.close()

print("Database Studio Reservasi berhasil dibuat")