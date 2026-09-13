import sqlite3
conn = sqlite3.connect('practice.db')
cur = conn.cursor()

cur.execute("SELECT name, department, salary FROM employees WHERE department = 'Engineering'")
rows = cur.fetchall()

for row in rows:
    print(row)