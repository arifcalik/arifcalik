import pymongo
import pprint

#TODO : def setup! 
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydatabase_name = "taskmanager" 
database = myclient [mydatabase_name]  
mycollection_name = "tasks"
mycollection_name = database[mycollection_name]
dblist = myclient.list_database_names()

if mydatabase_name in dblist:
  print(f"The database({mydatabase_name}) exists.")
else:
  print(f"The database({mydatabase_name}) does NOT exist.") 

pp = pprint.PrettyPrinter(indent=4)

def add_task(id, title, description, status="To Do"): 
    #TODO : check ids!!!!!
    print("Adding a task into my mongo dbase")
    mytask = { "_id": id, "title": title, "description": description, "status" : status }
    result = mycollection_name.insert_one(mytask)
    print(result.inserted_id)
    return result

def list_tasks():
    print("Listing all tasks in my mongo dbase") 
    for task in mycollection_name.find():
        pp.pprint("--------------------------")
        pp.pprint(task)
    pp.pprint("--------------------------")

def update_task_status(task_id, new_status): 
    print("Updating the task in my mongo dbase")
    toBeUpdated = { "_id": task_id }
    newvalues = { "$set" : { "status" : new_status } }
    mycollection_name.update_one(toBeUpdated, newvalues)

def delete_task(task_id): 
    print("Deleting the task in my mongo dbase")   
    toBeDeleted = { "_id": task_id }
    mycollection_name.delete_one(toBeDeleted) 
    
def main(): 
    print ("Hello MongoDB")
    id = 101
    title = "Pay the el. invoice" 
    description = "Ellevio invoice, last payment date: Friday"
    status = "Pending"                    
    add_task(id, title, description, status)

    id = 102
    title = "Meeting in the school" 
    description = "All parents have to join, Tuesday morning 8:30"
    status = "Planned"                    
    add_task(id, title, description, status)

    list_tasks() 

    #delete_task(101)
    update_task_status(102, "Done")
    update_task_status(101, "Cancelled")

    list_tasks()

    delete_task(101)

    list_tasks()

    delete_task(102)

    list_tasks() 

    id = 1021
    title = "Pay the el. invoice" 
    description = "Ellevio invoice, last payment date: Friday"
    status = "Pending"                    
    add_task(id, title, description, status)

    id = 1022
    title = "Meeting in the school" 
    description = "All parents have to join, Tuesday morning 8:30"
    status = "Planned"                    
    add_task(id, title, description, status)

    list_tasks()        

if __name__ == "__main__":
    main()