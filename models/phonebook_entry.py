from pydantic import BaseModel

class PhoneBookEnrty(BaseModel):
    name:str
    address:str
    phoneNumber:str