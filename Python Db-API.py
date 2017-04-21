import sqlite3

# Fetch some student records from the database.db = sqlite3.connect("students")
c = db.cursor()
query = "select name, id from students order by name;"
c.execute(query)
rows = c.fetchall()


# Print the structure
Print "Row data:"
Print rows

#loop over the list
Print
Print "Student names:"
for row in rows:
    print "", row[0]

db.close()





