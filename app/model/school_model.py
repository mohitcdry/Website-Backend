from pydantic import BaseModel

class Address(BaseModel):
    ward_no:int
    muncipality:str
    province_no:int
    address:str

class School(BaseModel):
    name:str
    address:Address
    email_address:str
    phone_number:int

