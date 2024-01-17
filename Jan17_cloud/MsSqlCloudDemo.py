from os import getenv
import pymssql

# server = getenv("PYMSSQL_TEST_SERVER")
# user = getenv("PYMSSQL_TEST_USERNAME")
# password = getenv("PYMSSQL_TEST_PASSWORD")

server = 'mymssqlserver.database.windows.net'
user = 'myusernama'
password = 'mypassword'

conn = pymssql.connect(server, user, password, "LexiconCloudDB769")
cursor = conn.cursor(as_dict=True)

cursor.execute("""
IF OBJECT_ID('persons', 'U') IS NOT NULL
    DROP TABLE persons
CREATE TABLE persons (
    id INT NOT NULL,
    name VARCHAR(100),
    salesrep VARCHAR(100),
    PRIMARY KEY(id)
)
""")
cursor.executemany(
    "INSERT INTO persons VALUES (%d, %s, %s)",
    [(1, 'John Smith', 'John Doe'),
     (2, 'Jane Doe', 'Joe Dog'),
     (3, 'Mike T.', 'Sarah H.'),
     (4, 'Arif Smith', 'John Doe'),
     (5, 'Can Cetin', 'Joe Dog'),
     (6, 'Selim Kaan Herro', 'John Doe'),])

conn.commit()

print("Just the customers whose sales repr. is John Doe")
print("----------------------------------------")
cursor.execute('SELECT * FROM persons WHERE salesrep=%s', 'John Doe')
for row in cursor:
    print("ID=%d, Name=%s" % (row['id'], row['name']))

print("----------------------------------------")
print("Whole list here:")
cursor.execute('SELECT * FROM persons')
for row in cursor:
    print("ID=%d, Name=%s" % (row['id'], row['name']))
print("----------------------------------------")

conn.close()

# if you like to use context manager see below:
"""
with pymssql.connect(server, user, password, "tempdb") as conn:
    with conn.cursor(as_dict=True) as cursor:
        cursor.execute('SELECT * FROM persons WHERE salesrep=%s', 'John Doe')
        for row in cursor:
            print("ID=%d, Name=%s" % (row['id'], row['name']))
"""
