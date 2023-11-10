import pymongo
import pprint
from datetime import datetime
import re
from getpass import getpass
from bson import ObjectId

#TODO : def setup! 
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydatabase_name = "socialmedia" 
database = myclient [mydatabase_name]  
mycollection_name_users = "users"
mycollection_name_users = database[mycollection_name_users]
mycollection_name_posts = "posts"
mycollection_name_posts = database[mycollection_name_posts]
#TODO: fix those here too
dblist = myclient.list_database_names()
if mydatabase_name in dblist:
  print(f"The database({mycollection_name_users}) exists.")
else:
  print(f"The database({mycollection_name_users}) does NOT exist.") 

if mycollection_name_posts in dblist:
  print(f"The database({mycollection_name_posts}) exists.")
else:
  print(f"The database({mycollection_name_posts}) does NOT exist.") 

pp = pprint.PrettyPrinter(indent=4)

#TODO : remove global thing
active_user = None

def login():
   correct_user_info = False
   while not correct_user_info:
    pp.pprint("Provide your username and password")
    username = input("username ::")
    #security
    #username = getpass()
    password = input("enter your password ::")
    user_info = { "username": username, "password": password }

    for user_info in mycollection_name_users.find():
        if user_info["username"] == username and user_info["password"] == password:
            pp.pprint("Successfully you logged in.") 
            correct_user_info = True
            #active_user = user_info["username"]
            global active_user 
            active_user = username
            break
    else:
        pp.pprint("")   
    return correct_user_info 

def register():
   pp.pprint("Welcome for registeration, good choice")

   correct_email_format = False
   while not correct_email_format:   
    email = input("valid email address ::")
    reGex = '[^@]+@[^@]+\.[^@]+'
    if re.match(reGex, email): 
       correct_email_format = True

   username = input("username ::")
   password = input("create a password ::")
   #TODO :
   #security
   #username = getpass()

   user_info = { "username": username, "password": password, "email" : email, "followers": [], "following" : [] }
   result = mycollection_name_users.insert_one(user_info)
   pp.pprint(result.inserted_id)

   return True

def follow():
        follow = input("Who do you want to follow:: ")
        result = mycollection_name_users.find({"username": follow})
        mycollection_name_users.find_one_and_update({ "username": active_user }, )

        if not result:
            pp.pprint("No such user in the users collection!!!")
        else:
            pp.pprint("There is such a user and you can sure follow!")   

        toBeUpdated = {"username": active_user}
        #TODO :append must be called / improve later
        followings_list = [follow]

        toBeUpdated = { "username": active_user }
        newvalues = { "$set" : { "following" : followings_list } }
        mycollection_name_users.update_one(toBeUpdated, newvalues)

def unfollow():
   pass

def view():
    print("Listing all post in my mongo posts collection:") 
    for post in mycollection_name_posts.find():
        pp.pprint("--------------------------")
        pp.pprint(post)
        pp.pprint("--------------------------")
        post_id = post["_id"]
        toBeUpdated = { "_id": ObjectId(post_id) }
        newvalues = { "$inc" : { "view" : 1 } }
        result = mycollection_name_posts.update_one(toBeUpdated, newvalues)     

def like():
    post_id = input("Enter the post id you want to LIKE:: ")
    print("Updating the post likes in my mongo dbase")
    toBeUpdated = { "_id": ObjectId(post_id) }
    newvalues = { "$inc" : { "like" : 1 } }
    result = mycollection_name_posts.update_one(toBeUpdated, newvalues)   
    return 

def quit():
   exit()

def post():
    datetime_now = datetime.utcnow()  

    #TODO : $currentDate
    title = input("Enter the title here for the post::")
    content = input("Enter the text for the posts body::")
    post_info = { "title": title, "content": content, "like": 0, "view" : 0 , "date": datetime_now}
    result = mycollection_name_posts.insert_one(post_info)
    pp.pprint(result.inserted_id)
    pp.pprint("")

def intro():
   pp.pprint("Welcome to Facelook")
   choice = input("Do you want to register(r) or login(l) or quit(q) : ")
   loggedin = False
   while True:
    if loggedin == True:
        choice = input("Do you want to (q)uit (p)ost (f)ollow like(heart) (u)nfollow or (v)iew: ")
    match choice:
            case 'r':
                loggedin = register()
            case 'l':
                if loggedin == False: 
                    loggedin = login()
            case 'f':
                if loggedin == True:            
                    follow()
            case 'u':
                if loggedin == True:            
                    unfollow()            
            case 'h':
                if loggedin == True:            
                    like()
            case 'v':
                if loggedin == True:            
                    view()
            case 'p':
                if loggedin == True:
                    post()
            case 'q':
                #if loggedin == True:
                quit()
              
            case _:
                print("Something's wrong with your choice!")

def main(): 
    intro()
 
if __name__ == "__main__":
    main()