import mysql.connector
QUERIES = [ 
"SELECT * FROM ",  
"SHOW DATABASES;",
"USE elevator_service;",
"SHOW TABLES;", 

"""CREATE TABLE IF NOT EXISTS EmployeeStatus (
	EmployeeStatusId Int NOT NULL ,
	StatusDescription VARCHAR(50) NOT NULL,
	PRIMARY KEY (EmployeeStatusId)
);""",

"""CREATE TABLE IF NOT EXISTS City (
	CityId INT NOT NULL,
  CityName VARCHAR(90) NOT NULL,
	PRIMARY KEY (CityId)
);""",

"""CREATE TABLE IF NOT EXISTS Building (
	BuildingId INT NOT NULL,
	CityId INT NOT NULL,
  Floors INT NOT NULL,
	PRIMARY KEY (BuildingId),
	FOREIGN KEY (CityId) REFERENCES City(CityId)
);""",

"""CREATE TABLE IF NOT EXISTS ServiceStatus (
	ServiceStatusId INT NOT NULL,
	StatusDescription VARCHAR(100) NOT NULL,
	PRIMARY KEY (ServiceStatusId)
);""",

"""CREATE TABLE IF NOT EXISTS ElevatorType (
	ElevatorTypeId INT NOT NULL,
  TypeName VARCHAR(60) NOT NULL,
	PRIMARY KEY (ElevatorTypeId)
);""",

"""CREATE TABLE IF NOT EXISTS ElevatorModel (
	ElevatorModelId INT NOT NULL,
	ModelName INT NOT NULL,
  Speed INT NOT NULL,
  MaxWeight INT NOT NULL,
  PeopleLimit INT NOT NULL,
  ElevatorTypeId INT NOT NULL,
	PRIMARY KEY (ElevatorModelId),
	FOREIGN KEY (ElevatorTypeId) REFERENCES ElevatorType(ElevatorTypeId)
);""",
          
"""CREATE TABLE IF NOT EXISTS Technician (
  EmployeeId INT NOT NULL,
  FirstName VARCHAR(255) NOT NULL,
  LastName VARCHAR(255) NOT NULL,   
  EmailAddress VARCHAR(255) NOT NULL,    
  AnnualSalary INT NOT NULL,
  SpecialSkill VARCHAR(255),
	EmployeeStatusId INT NOT NULL,
	PRIMARY KEY (EmployeeId),
  FOREIGN KEY (EmployeeStatusId) REFERENCES EmployeeStatus(EmployeeStatusId)
);""",

"""CREATE TABLE IF NOT EXISTS Elevator (
	ElevatorId INT NOT NULL,
	ElevatorModelId INT NOT NULL,
  BuildingId INT NOT NULL,
	PRIMARY KEY (ElevatorId),
	FOREIGN KEY (ElevatorModelId) REFERENCES ElevatorModel(ElevatorModelId),
  FOREIGN KEY (BuildingId) REFERENCES Building(BuildingId)
);""",

"""CREATE TABLE IF NOT EXISTS ServiceActivity (
  ServiceActivityId INT NOT NULL,
  EmployeeId INT NOT NULL,
  ElevatorId INT NOT NULL,   
  ServiceDateTime Date NOT NULL,    
  ServiceDescription VARCHAR(155),
  ServiceStatusId INT NOT NULL,
	PRIMARY KEY (ServiceActivityId),
  FOREIGN KEY (EmployeeId) REFERENCES Technician(EmployeeId),
  FOREIGN KEY (ElevatorId) REFERENCES Elevator(ElevatorId),
	FOREIGN KEY (ServiceStatusId) REFERENCES ServiceStatus(ServiceStatusId)
);""",

"""INSERT INTO City
VALUES  (34, "Istanbul"),
		(35, "Izmir"),
		(09, "Aydin"),
        (120, "Denizli"),
		(06, "Ankara");""",
        
"""INSERT INTO City
VALUES  
        (55, "Samsun");""",       

"""UPDATE City
SET CityId = 20
WHERE CityName = 'Denizli';""",

"""INSERT INTO Building
VALUES  (3344, 20, 7);""",
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
    query = QUERIES[0] + table + ";"
    cursor = dbase.cursor()
    cursor.execute(query)
    result = cursor.fetchall() 
    return result  

def display_result(result):
    for value in result:
      print(value)

def run_table_commands(dbase):
   for command in QUERIES[4:]:
      write_dbase(dbase, command)
    
def main():
  if check_database_exists("elevator_service"):
    print("Already exists")
    dbase = connect_dbase("elevator_service")
  else:
     print("Create it!")
     dbase = create_dbase("elevator_service")
     run_table_commands(dbase)

  display_result(read_dbase(dbase, "City"))
  display_result(read_dbase(dbase, "Building"))
  dbase.close()


if __name__ == "__main__":
  main()
