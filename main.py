
import sqlite3
from Employee import Employee

# e1 = Employee()

connection = sqlite3.connect("employees.db")
connection.row_factory = sqlite3.Row
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fname TEXT NOT NULL,
    lname TEXT NOT NULL,
    salary REAL NOT NULL
);
''')

# cursor.executemany('''
# INSERT INTO employees (fname, lname, salary) VALUES (?, ?, ?);
# ''', [
#     ('John', 'Doe', 50000),
#     ('Jane', 'Smith', 60000),
#     ('Alice', 'Johnson', 55000),
#     ('Bob', 'Brown', 45000),
#     ('Charlie', 'Davis', 70000)
# ])
#
# connection.commit()

cursor.execute("SELECT * FROM employees WHERE id = 2")
employee_record = cursor.fetchone()
tup = tuple(employee_record)

jane_1 = Employee(*tup)
# f"INSERT INTO EMPLOYEE VALUES({jane.fname}" ...)
print(jane_1)
jane_2 = Employee(*tup)

#jane_1.fname = "clara"
#         44       789
print(jane_1 == jane_2)

connection.close()

votes = {jane_1: "bowling"}
print(votes[jane_1])

# {'hi': 1, jane_1: 12 }
# { -652853193430086177: 1 , }


