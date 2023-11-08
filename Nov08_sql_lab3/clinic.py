
import mysql.connector
QUERIES = [ 
"""CREATE DATABASE IF NOT EXISTS clinic02;""",
 
"""USE clinic02;""",
 
"""CREATE TABLE departments (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(50) NOT NULL
);""",
 
"""INSERT INTO departments (name) VALUES
  ('Therapy'),
  ('Support'),
  ('Management'),
  ('Other');""",
 
"""CREATE TABLE employees (
  id INT PRIMARY KEY AUTO_INCREMENT,
  first_name VARCHAR(60) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  job_title VARCHAR(50) NOT NULL,
  department_id INT NOT NULL,
  salary DOUBLE NOT NULL,
  CONSTRAINT fk_department_id FOREIGN KEY (department_id) REFERENCES departments(id)
);""",
 
"""INSERT INTO employees (first_name, last_name, job_title, department_id, salary) VALUES
  ('Maria', 'Anderson', 'Therapist', 1, 400.00),
  ('Anna', 'Johansson', 'Acupuncturist', 1, 830.00),
  ('Ingrid', 'Petersson', 'Technician', 2, 1140.00),
  ('Lena', 'Hagnusson', 'Supervisor', 3, 1200.00),
  ('Sandy', 'Petersson', 'Dentist', 4, 1400.23),
  ('Max', 'Persson', 'Therapist', 1, 992.00),
  ('Anders', 'Tegnell', 'Epidemiologist', 2, 1340.00),
  ('Margareta', 'Olsson', 'Medical Director', 3, 2500.00),
  ('Daniel', 'Nilsson', 'Nutrition Technician', 4, 2600.00);""",
 
"""CREATE TABLE rooms (
  id INT PRIMARY KEY AUTO_INCREMENT,
  occupation VARCHAR(50)
);""",
 
"""INSERT INTO rooms (occupation) VALUES
  ('free'),
  ('occupied'),
  ('free'),
  ('free'),
  ('occupied');""",
 
"""CREATE TABLE patients (
  id INT PRIMARY KEY AUTO_INCREMENT,
  first_name VARCHAR(60) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  room_id INT NOT NULL
);""",
 
"""INSERT INTO patients (first_name, last_name, room_id) VALUES
  ('Birgitta', 'Larsson', 1),
  ('Marianne', 'Landeberg', 3),
  ('Bertil', 'Dahlberg', 2),
  ('Filip', 'Willhelm', 2),
  ('Nikolay', 'Mikolaev', 4);""",

"""SELECT * from
""",
  
# question 2
"""select * from employees
where salary > 1000.00
ORDER BY id ASC;""",

# question 3
"""update clinic02.employees
set salary = salary * 1.1
where job_title = "Dentist";""",

"""select * from clinic02.employees
ORDER BY salary ASC;""",

# question 4
"""DELETE FROM clinic02.employees 
WHERE department_id IN (3,4);""",

"""select * from clinic02.employees
ORDER BY id ASC;""",
]



def create_dbase(dbase_name):
  dbase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="21_leXicon_53"
  )
  cs = dbase.cursor()
  cs.execute(f"CREATE DATABASE {dbase_name}")
  cs.execute(f"USE {dbase_name}")
  return dbase
 
def check_database_exists(dbase):
  conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="21_leXicon_53"
  )
  mycursor = conn.cursor()
  mycursor.execute("SHOW DATABASES")
  result = mycursor.fetchall()
  for item in result:
    if item[0] == dbase:
       return True
    else:
       return False

def connect_dbase(target_dbase):
    dbase = mysql.connector.connect(
      host ="localhost",
      user ="root",
      passwd ="21_leXicon_53",
      database = target_dbase)
    return dbase

def write_dbase(dbase, query):
    cursor = dbase.cursor()
    cursor.execute(query)
    dbase.commit()

def read_dbase(dbase, table):
    query = QUERIES[10] + table + ";"
    cursor = dbase.cursor()
    cursor.execute(query)
    result = cursor.fetchall() 
    return result  

def read_dbase_raw(dbase, query):
    cursor = dbase.cursor()
    cursor.execute(query)
    result = cursor.fetchall() 
    return result  

def display_result(result):
    for value in result:
      print(value)

def run_table_commands(dbase):
   for command in QUERIES[:10]:
      write_dbase(dbase, command)
    
def main():
  if check_database_exists("clinic02"):
    print("Already exists")
    dbase = connect_dbase("clinic02")
  else:
     print("Create it!")
     dbase = create_dbase("clinic02")
     run_table_commands(dbase)

  display_result(read_dbase(dbase, "clinic02.departments"))
  display_result(read_dbase(dbase, "clinic02.employees"))
  display_result(read_dbase(dbase, "clinic02.rooms"))
  display_result(read_dbase(dbase, "clinic02.patients"))

  print("\n------question 2--------------------")
  display_result(read_dbase_raw(dbase,  QUERIES[11]))
  print("--------------------------\n")
  print("\n------question 3--------------------")
  write_dbase(dbase, QUERIES[12])
  display_result(read_dbase_raw(dbase,  QUERIES[13]))
  print("--------------------------\n")  
  print("\n------question 4--------------------")  
  write_dbase(dbase, QUERIES[14])
  display_result(read_dbase_raw(dbase,  QUERIES[15]))  
  print("--------------------------\n")


  dbase.close()


if __name__ == "__main__":
  main()



