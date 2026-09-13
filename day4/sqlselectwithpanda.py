import sqlite3
import pandas as pd
conn =sqlite3.connect("practice.db")

def run_query(sql):
    return pd.read_sql_query(sql, conn)

df = pd.read_sql_query("SELECT name, department, salary FROM employees WHERE department = 'Engineering'", conn)
print (df)

