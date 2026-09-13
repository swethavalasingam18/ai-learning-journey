

import sqlite3
import pandas as pd
conn =sqlite3.connect("practice.db")

def run_query(sql):
    return pd.read_sql_query(sql, conn)

df = pd.read_sql_query("SELECT orders.order_id, employees.name, orders.product, orders.amount FROM orders INNER JOIN employees ON orders.emp_id = employees.emp_id", conn)
print (df)

df = pd.read_sql_query("SELECT e.name, o.order_id, o.product, o.amount FROM employees e LEFT JOIN orders o ON e.emp_id = o.emp_id", conn)
print (df)

df = pd.read_sql_query("SELECT e.name, SUM(o.amount) AS total_orders FROM employees e LEFT JOIN orders o ON e.emp_id = o.emp_id GROUP BY e.name ORDER BY total_orders DESC", conn)
print (df)







