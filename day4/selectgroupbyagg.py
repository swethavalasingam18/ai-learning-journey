

import sqlite3
import pandas as pd
conn =sqlite3.connect("practice.db")

def run_query(sql):
    return pd.read_sql_query(sql, conn)

df = pd.read_sql_query("SELECT department, COUNT(*) AS num_employees FROM employees GROUP BY department", conn)
print (df)

df = pd.read_sql_query("SELECT department, AVG(salary) AS avg_salary FROM employees GROUP BY department", conn)
print (df)

df = pd.read_sql_query("SELECT department,  COUNT(*) AS num_employees, SUM(salary) AS total_salary ,AVG(salary) AS avg_salary, MAX(salary) AS highest_salary, MIN(salary) AS lowest_salary FROM employees GROUP BY department", conn)
print (df)


df = pd.read_sql_query("SELECT department, AVG(salary) AS avg_salary FROM employees GROUP BY department HAVING AVG(salary) > 50000", conn)
print (df)





