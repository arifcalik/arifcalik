import pymongo
import pprint
from datetime import datetime
import re
from getpass import getpass
from bson import ObjectId

pp = pprint.PrettyPrinter(indent=4)


def setup(database_name, collection_names):
    uri = "mongodb://localhost:27017/"
    mongo_client = pymongo.MongoClient(uri)
    try:
        mongo_client.admin.command('ping')
        print("You successfully connected to your local MongoDB!")
    except Exception as e:
        print(e)

    database = mongo_client[database_name]
    users_collection, posts_collection = database[collection_names[0]], database[collection_names[1]]
    dblist = mongo_client.list_database_names()
    if database_name in dblist:
        print(f"The database({database_name}) exists.")
    else:
        print(f"The database({database_name}) does NOT exist.")
    return users_collection, posts_collection


def login(users_col, active_user):
    correct_user_info = False
    while not correct_user_info:
        pp.pprint("Provide your username and password")
        username = input("username ::")
        # security
        # username = getpass()
        password = input("enter your password ::")

        for doc in users_col.find():
            if doc["username"] == username and doc["password"] == password:
                pp.pprint("Successfully you logged in.")
                correct_user_info = True
                active_user = username
                break
        else:
            pp.pprint("Incorrect username or password!")
        return correct_user_info, active_user


def register(users_col):
    pp.pprint("Welcome for registration, good choice")

    correct_email_format = False
    email = None
    while not correct_email_format:
        email = input("valid email address ::")
        regex_expression = r"[^@]+@[^@]+\.[^@]+"
        correct_email_format = re.match(regex_expression, email)
        if email.lower() == "q":
            exit()

    username = input("username ::")
    password = input("create a password ::")
    # TODO :
    # security
    # username = getpass()

    # TODO : check username
    # do not accept same username in users

    user_info = {"username": username, "password": password, "email": email, "followers": [], "following": []}
    result = users_col.insert_one(user_info)
    pp.pprint(result.inserted_id)

    return True, username


def follow(users_col, active_user):
    follow_user = input("Who do you want to follow:: ")
    follow_user_doc = users_col.find_one({"username": follow_user})
    if not follow_user_doc:
        pp.pprint("No such user in the users collection!!!")
    else:
        pp.pprint("There is such a user and you can sure follow!")
        active_user_doc = users_col.find_one({"username": active_user})
        if active_user_doc:
            if not active_user_doc["following"]:    # empty list
                users_col.update_one({"username": active_user}, {"$push": {"following": follow_user}})
            else:
                users_col.update_one({"username": active_user}, {"$addToSet": {"following": follow_user}})

            if not follow_user_doc["followers"]:    # empty list
                users_col.update_one({"username": follow_user}, {"$push": {"followers": active_user}})
            else:
                users_col.update_one({"username": follow_user}, {"$addToSet": {"followers": active_user}})


def unfollow(users_col, active_user):
    unfollow_user = input("Who do you want to unfollow:: ")
    unfollow_user_doc = users_col.find_one({"username": unfollow_user})
    if not unfollow_user_doc:
        pp.pprint("No such user in the users collection!!!")
    else:
        pp.pprint("There is such a user and you can sure unfollow!")
        active_user_doc = users_col.find_one({"username": active_user})
        if active_user_doc:
            if unfollow_user in active_user_doc["following"]:    # in the list
                users_col.update_one({"username": active_user}, {"$pull": {"following": unfollow_user}})
                users_col.update_one({"username": unfollow_user}, {"$pull": {"followers": active_user}})


def view(users_col, posts_col, active_user):
    # TODO : only view the followings posts not all posts!
    print("Listing all posts of my followings and mines :")
    following = users_col.find_one({"username": active_user})["following"]
    for _post in posts_col.find():
        if _post["owner"] in following or _post["owner"] == active_user:
            pp.pprint("--------------------------")
            pp.pprint(_post)
            pp.pprint("--------------------------")
            post_id = _post["_id"]
            if _post["owner"] != active_user:
                to_be_updated = {"_id": ObjectId(post_id)}
                new_values = {"$inc": {"view": 1}}
                posts_col.update_one(to_be_updated, new_values)


def like(posts_col):
    post_id = input("Enter the post id you want to LIKE:: ")
    print("Updating the post likes in my mongo dbase")
    to_be_updated = {"_id": ObjectId(post_id)}
    new_values = {"$inc": {"like": 1}}
    posts_col.update_one(to_be_updated, new_values)
    return


def quit_app():
    exit()


def post(posts_col, active_user):
    datetime_now = datetime.utcnow()  

    # TODO : $currentDate
    title = input("Enter the title here for the post::")
    content = input("Enter the text for the posts body::")
    post_info = {"owner": active_user, "title": title, "content": content, "like": 0, "view": 0, "date": datetime_now}
    result = posts_col.insert_one(post_info)
    pp.pprint(result.inserted_id)
    pp.pprint("")


def intro(users_col, posts_col, active_user):
    pp.pprint("Welcome to Facelook")
    # choice = input("Do you want to register(r) or login(l) or quit(q) : ")
    logged_in = False
    empty_user = {}
    database_up_and_running = users_col.count_documents(empty_user)  # {}could be directly in call instead empty_user
    while True:
        if logged_in:
            choice = input("Do you want to (q)uit (p)ost (f)ollow like(heart) (u)nfollow or (v)iew: ")
        elif not database_up_and_running:
            choice = input("Do you want to (r)egister or (q)uit:: ")
        elif not logged_in:
            choice = input("Do you want to (r)egister, (l)ogin or (q)uit:: ")
        else:
            choice = None

        match choice:
            case 'r':
                logged_in, active_user = register(users_col)
            case 'l':
                if database_up_and_running and not logged_in:
                    logged_in, active_user = login(users_col, active_user)
            case 'f':
                if database_up_and_running and logged_in:
                    follow(users_col, active_user)
            case 'u':
                if database_up_and_running and logged_in:
                    unfollow(users_col, active_user)
            case 'h':
                if database_up_and_running and logged_in:
                    like(posts_col)
            case 'v':
                if database_up_and_running and logged_in:
                    view(users_col, posts_col, active_user)
            case 'p':
                if database_up_and_running and logged_in:
                    post(posts_col, active_user)
            case 'q':
                quit_app()
              
            case _:
                print("Something's wrong with your choice!")


def main():
    active_user = None
    users_collection, posts_collection = setup("social_media", ["users", "posts"])
    intro(users_collection, posts_collection, active_user)


if __name__ == "__main__":
    main()
