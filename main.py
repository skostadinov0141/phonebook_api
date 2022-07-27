from fastapi import FastAPI, Response
from pymongo import MongoClient
from pprint import pprint
from fastapi.middleware.cors import CORSMiddleware
import os

# Import the phonebook model from the models directory
from models.phonebook_entry import PhoneBookEnrty

# Create a mongo client and connect it to the DB
client = MongoClient("172.17.0.2:27017")

db = client.admin
# Issue the serverStatus command and print the results
serverStatusResult=db.command("serverStatus")
pprint(serverStatusResult)

# Create a FastAPI app
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {'message':'Hello World!'}

# Add a phonebook entry to the database
@app.post("/create_phonebook_entry")
async def createPhonebookEntry(response:Response, entry : PhoneBookEnrty):
    phonebookDB = client.phonebook
    phonebookDB.entries.insert_one(entry.dict())
    response.headers["Access-Control-Allow-Origin"] = "*"
    return entry.dict()

# Get all phonebook entries contained within the database
@app.get("/get_phonebook_entries")
async def getPhonebookEntries(response:Response):
    returnList = []
    for document in client.phonebook.entries.find():
        returnList.append({
            "name":document["name"],
            "address":document["address"],
            "phoneNumber":document["phoneNumber"],
        })
    response.headers["Access-Control-Allow-Origin"] = "*"
    return {"data":returnList}