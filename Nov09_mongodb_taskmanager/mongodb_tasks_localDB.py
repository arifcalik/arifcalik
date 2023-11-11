import pymongo
from getpass import getpass
import pprint
import sys
from bson import ObjectId

pp = pprint.PrettyPrinter(indent=4)

def setup(database_name, collection_name):   
    uri = "mongodb://localhost:27017/"
    # Connect!
    myclient = pymongo.MongoClient(uri)
    try:
        myclient.admin.command('ping')
        print("You successfully connected to your local MongoDB!")
    except Exception as e:
        print(e)

    mydatabase = myclient[database_name]
    mycollection = mydatabase[collection_name]        
    dblist = myclient.list_database_names()
    if database_name in dblist:
        print(f"The database({database_name}) exists.")
    else:
        print(f"The database({database_name}) does NOT exist.") 

    return mycollection

def add_task(mycollection, title, description, status="To Do"): 
    print("Adding a task into my mongo dbase")
    mytask = { "title": title, "description": description, "status" : status }
    # check there is totally same document in case repetition!
    document_retrieved = mycollection.find_one(mytask)
    if document_retrieved:
        print("\nThere is totaly same document in the database, wont add it!!!\n")
        return -1
    else:
        try:
            result = mycollection.insert_one(mytask)
        except pymongo.errors.OperationFailure:
            print("Authentication error! Sure your database user is authorized for writing?")
            sys.exit(1)   
        else:       
            print(f"Added documents id is {result.inserted_id}") 
        return result.inserted_id

def list_tasks(mycollection):
    print("Listing all tasks in my mongo dbase") 
    for task in mycollection.find():
        pp.pprint("--------------------------")
        pp.pprint(task)
    pp.pprint("--------------------------")

def update_task_status(mycollection, task_id, new_status): 
    print("Updating the task in my mongo dbase")
    toBeUpdated = { "_id": ObjectId(task_id) }
    newvalues = { "$set" : { "status" : new_status } }
    mycollection.update_one(toBeUpdated, newvalues)

def delete_task(mycollection, task_id): 
    print("Deleting the task in my mongo dbase")   
    toBeDeleted = { "_id": ObjectId(task_id) }

    try:
        result = mycollection.delete_one(toBeDeleted)
    except pymongo.errors.OperationFailure:
        print("Aauthentication error! Sure your database user is authorized for writing?")
        sys.exit(1)   
    else:          
        print("Deletion Summary: %x documents deleted." %(result.deleted_count))
    return result.deleted_count    
    
def main(): 
    collection = setup("taskmanager3", "tasks")
    title = "Pay the el. invoice" 
    description = "Fortum invoice, last payment date: Friday"
    status = "Pending"                    
    add_task(collection, title, description, status)

    title = "Meeting in the school" 
    description = "All parents have to join, Tuesday morning 8:30"
    status = "Planned"                    
    add_task(collection, title, description, status)

    list_tasks(collection) 

    update_task_status(collection, '102732489293939439433aaa', "Done")
    update_task_status(collection, '654d51b016a82cf868119c27', "Cancelled")

    list_tasks(collection)

    #TODO: instead of hardcoded ids choose random one from list via find!
    id =  '654d51b016a82cf868119c26'
    delete_task(collection, id)
    list_tasks(collection)
    delete_task(collection, '1025123456abc67890234cbe')
    list_tasks(collection) 

    title = "Pay the el invoice" 
    description = "Ellevio invoice, last payment date: Mondag"
    status = "Pending"                    
    add_task(collection, title, description, status)

    title = "Meeting - Wednesday" 
    description = "All parents have to join, Wednesday morning 8:30"
    status = "Planned"                    
    add_task(collection, title, description, status)

    print("\nTry adding same task!\n")
    title = "Meeting - Wednesday" 
    description = "All parents have to join, Wednesday morning 8:30"
    status = "Planned"                    
    add_task(collection, title, description, status)

    title = "Shopping" 
    description = "Ett par skor till Gunnar!"                 
    add_task(collection, title, description)

    list_tasks(collection)        

if __name__ == "__main__":
    main()
