from fastapi import FastAPI
from pymongo import MongoClient
from pprint import pprint
import os

# Import the phonebook model from the models directory
from models.phonebook_entry import PhoneBookEnrty

# Create a mongo client and connect it to the DB
client = MongoClient(os.environ["MONGO_ADDRESS"] + ":" + os.environ["MONGO_PORT"])

db = client.admin
# Issue the serverStatus command and print the results
serverStatusResult=db.command("serverStatus")
pprint(serverStatusResult)

# Create a FastAPI app
app = FastAPI()

@app.get("/")
async def root():
    return {'message':'Hello World!'}

# Add a phonebook entry to the database
@app.post("/create_phonebook_entry")
async def createPhonebookEntry(entry : PhoneBookEnrty):
    phonebookDB = client.phonebook
    phonebookDB.entries.insert_one(entry.dict())
    return entry.dict()

# Get all phonebook entries contained within the database
@app.get("/get_phonebook_entries")
async def getPhonebookEntries():
    returnList = []
    for document in client.phonebook.entries.find():
        returnList.append({
            "name":document["name"],
            "address":document["address"],
            "phoneNumber":document["phoneNumber"],
        })
    return returnList