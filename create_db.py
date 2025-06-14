import sqlite3

conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS sales (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product TEXT,
        quantity INTEGER,
        price REAL
    )
''')

sales_data = [
    ('Product A', 10, 20.5),
    ('Product B', 5, 15.0),
    ('Product A', 7, 20.5),
    ('Product C', 3, 30.0),
    ('Product B', 8, 15.0)
]

cursor.executemany('INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)', sales_data)
conn.commit()
conn.close()
print("Database created and sample data inserted!")
