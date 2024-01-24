import os
import sys
from random import randint

import pymongo
from dotenv import load_dotenv

def test():
    load_dotenv()
    CONNECTION_STRING = os.environ.get("COSMOS_CONNECTION_STRING")

    DB_NAME = "azure-mongodb"
    COLLECTION_NAME = "students"

    client = pymongo.MongoClient(CONNECTION_STRING)

    # Create database if it doesn't exist
    db = client[DB_NAME]
    if DB_NAME not in client.list_database_names():
        # Create a database with 400 RU throughput that can be shared across
        # the DB's collections
        db.command({"customAction": "CreateDatabase", "offerThroughput": 400})
        print("Created db '{}' with shared throughput.\n".format(DB_NAME))
    else:
        print("Using database: '{}'.\n".format(DB_NAME))


    # Create collection if it doesn't exist
    collection = db[COLLECTION_NAME]
    if COLLECTION_NAME not in db.list_collection_names():
        # Creates a unsharded collection that uses the DBs shared throughput
        db.command(
            {"customAction": "CreateCollection", "collection": COLLECTION_NAME}
        )
        print("Created collection '{}'.\n".format(COLLECTION_NAME))
    else:
        print("Using collection: '{}'.\n".format(COLLECTION_NAME))


    indexes = [
        {"key": {"_id": 1}, "name": "_id_1"},
        {"key": {"name": 2}, "name": "_id_2"},
    ]
    db.command(
        {
            "customAction": "UpdateCollection",
            "collection": COLLECTION_NAME,
            "indexes": indexes,
        }
    )
    print("Indexes are: {}\n".format(sorted(collection.index_information())))


    """Create new document and upsert (create or replace) to collection"""
    students = [{
        "name": "Ahmet Celik",
        "age": 63,
        "email": "ahmetcelik@hotmail.tr",
    },
{
        "name": "Selim Turkmen",
        "age": 33,
        "email": "selim43@hotmail.gov",
    },
{
        "name": "Cenk Calik",
        "age": 37,
        "email": "cenkcelik@hotmail.se",
    },{
        "name": "Temel Ozmen",
        "age": 23,
        "email": "temelcelik@hotmail.se",
    },
    {
        "name": "Kamil Ovali",
        "age": 50,
        "email": "kamilcelik@hotmail.se",
    },
    {
        "name": "Hasan Dene3",
        "age": 23,
        "email": "hasan@hotmail.se",
    },   
]
    # hack writing
    students2 = []
    for student in students2:
        result = collection.update_one(
            {"name": student["name"]}, {"$set": student}, upsert=True
        )
        print("Upserted document with _id {}\n".format(result.upserted_id))

        doc = collection.find_one({"_id": result.upserted_id})
        print("Found a document with _id {}: {}\n".format(result.upserted_id, doc))



    """Query for student in the collection"""
    print(f"Student with age(23)':\n")
    allStudentsQuery = {"age": 23}
    for doc in collection.find().sort(
        "name", pymongo.ASCENDING):
        print("Found a student with _id {}: {}\n".format(doc["_id"], doc))
        
def main():
    test()

if __name__ == "__main__":
    main()
