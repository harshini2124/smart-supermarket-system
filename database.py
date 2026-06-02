import sqlite3

# Connect to (or create) database
conn = sqlite3.connect("products.db")
cursor = conn.cursor()

# Create products table
cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    barcode TEXT PRIMARY KEY,
    name TEXT,
    expiry_date TEXT,
    price REAL,
    stock INTEGER
)
""")

# Insert multiple sample products
products = [
    ("8901234567890", "Milk", "2026-01-28", 40.0, 20),
    ("8909876543210", "Bread", "2026-01-25", 25.0, 15),
    ("8901112223334", "Eggs", "2026-01-23", 60.0, 12),
    ("8905556667778", "Cheese", "2026-01-30", 120.0, 8),
    ("8909998887776", "Butter", "2026-02-01", 70.0, 10),
]

for p in products:
    try:
        cursor.execute("INSERT INTO products (barcode, name, expiry_date, price, stock) VALUES (?, ?, ?, ?, ?)", p)
    except sqlite3.IntegrityError:
        pass  # Already exists

conn.commit()
conn.close()
print("Database created with sample products!")

