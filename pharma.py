import sqlite3

# Connect to SQLite database
connection = sqlite3.connect("pharma.db")

# Create a cursor object to interact with the database
cursor = connection.cursor()

# Create the DRUGS table with parameters: ID, NAME, THERAPEUTIC_AREA, COMPOUND, PRICE
table_info = """
CREATE TABLE DRUGS (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NAME TEXT NOT NULL,
    THERAPEUTIC_AREA TEXT,
    COMPOUND TEXT,
    PRICE DECIMAL(8, 2)
);
"""

# Execute the table creation query
cursor.execute(table_info)

# Insert the data into the database
cursor.execute('''INSERT INTO DRUGS (NAME, THERAPEUTIC_AREA, COMPOUND, PRICE) VALUES ('Aspirin', 'Pain Management, Cardiovascular', 'Acetylsalicylic Acid', 5.99)''')
cursor.execute('''INSERT INTO DRUGS (NAME, THERAPEUTIC_AREA, COMPOUND, PRICE) VALUES ('Paracetamol', 'Pain Management', 'Paracetamol', 3.49)''')
cursor.execute('''INSERT INTO DRUGS (NAME, THERAPEUTIC_AREA, COMPOUND, PRICE) VALUES ('Amoxicillin', 'Infectious Diseases', 'Amoxicillin', 8.99)''')
cursor.execute('''INSERT INTO DRUGS (NAME, THERAPEUTIC_AREA, COMPOUND, PRICE) VALUES ('Lisinopril', 'Cardiovascular', 'Lisinopril', 12.50)''')
cursor.execute('''INSERT INTO DRUGS (NAME, THERAPEUTIC_AREA, COMPOUND, PRICE) VALUES ('Ciprofloxacin', 'Infectious Diseases', 'Ciprofloxacin', 7.25)''')
cursor.execute('''INSERT INTO DRUGS (NAME, THERAPEUTIC_AREA, COMPOUND, PRICE) VALUES ('Ibuprofen', 'Pain Management', 'Ibuprofen', 4.99)''')
cursor.execute('''INSERT INTO DRUGS (NAME, THERAPEUTIC_AREA, COMPOUND, PRICE) VALUES ('Atorvastatin', 'Cardiovascular', 'Atorvastatin', 15.75)''')
cursor.execute('''INSERT INTO DRUGS (NAME, THERAPEUTIC_AREA, COMPOUND, PRICE) VALUES ('Azithromycin', 'Infectious Diseases', 'Azithromycin', 9.45)''')
cursor.execute('''INSERT INTO DRUGS (NAME, THERAPEUTIC_AREA, COMPOUND, PRICE) VALUES ('Omeprazole', 'Gastrointestinal', 'Omeprazole', 11.20)''')
cursor.execute('''INSERT INTO DRUGS (NAME, THERAPEUTIC_AREA, COMPOUND, PRICE) VALUES ('Metformin', 'Diabetes', 'Metformin', 6.99)''')
cursor.execute('''INSERT INTO DRUGS (NAME, THERAPEUTIC_AREA, COMPOUND, PRICE) VALUES ('Prednisone', 'Inflammatory Diseases', 'Prednisone', 9.99)''')
cursor.execute('''INSERT INTO DRUGS (NAME, THERAPEUTIC_AREA, COMPOUND, PRICE) VALUES ('Metoprolol', 'Cardiovascular', 'Metoprolol', 8.99)''')
# Display all the records in the DRUGS table
print("The inserted records are:")
data = cursor.execute('''SELECT * FROM DRUGS''')
for row in data:
    print(row)

# Commit changes to the database
connection.commit()

# Close the connection
connection.close()
