import sqlite3

conn = sqlite3.connect('practice.db')
cur = conn.cursor()

# Drop tables if they exist (so you can re-run this cleanly)
cur.execute("DROP TABLE IF EXISTS employees")
cur.execute("DROP TABLE IF EXISTS orders")

# Create employees table
cur.execute("""
CREATE TABLE employees (
    emp_id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    salary INTEGER,
    hire_year INTEGER
)
""")

# Create orders table
cur.execute("""
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    emp_id INTEGER,
    product TEXT,
    amount INTEGER,
    order_date TEXT
)
""")

employees_data = [
    (1, 'Anitha', 'Sales', 45000, 2019),
    (2, 'Ravi', 'Engineering', 65000, 2021),
    (3, 'Priya', 'Engineering', 72000, 2018),
    (4, 'Karan', 'Sales', 38000, 2022),
    (5, 'Divya', 'Marketing', 50000, 2020),
    (6, 'Suresh', 'Engineering', 58000, 2023),
    (7, 'Meena', 'Marketing', 47000, 2017),
    (8, 'Arjun', 'Sales', 41000, 2021),
]

orders_data = [
    (101, 1, 'Widget A', 1200, '2024-01-15'),
    (102, 1, 'Widget B', 800, '2024-02-10'),
    (103, 4, 'Widget A', 1500, '2024-01-20'),
    (104, 8, 'Widget C', 600, '2024-03-05'),
    (105, 2, 'Service Plan', 5000, '2024-02-14'),
    (106, 3, 'Service Plan', 5000, '2024-04-01'),
    (107, 4, 'Widget B', 900, '2024-03-22'),
    (108, 1, 'Widget C', 700, '2024-04-18'),
]

cur.executemany("INSERT INTO employees VALUES (?,?,?,?,?)", employees_data)
cur.executemany("INSERT INTO orders VALUES (?,?,?,?,?)", orders_data)

conn.commit()
print("Database ready!")