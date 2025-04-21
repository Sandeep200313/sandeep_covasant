from fastapi import FastAPI
from pydantic import BaseModel
from dicttoxml import dicttoxml

class Info(BaseModel):
    name : str
    age : int

info_dict = {"sandeep":22}

app = FastAPI()

@app.get('/hello/get')
def get():
    data = {}
    for key in info_dict:
        data[key] = info_dict.get(key)
        
    return data
    
@app.get("/hello/get/{format}")
def get_format(format:str = "JSON"):
    data = info_dict
    
    if format=='XML':
        return dicttoxml(data, custom_root="data", attr_type=False)
    else:
        return data
    
    
@app.post('/hello/post')
def post(body:Info):
    age = body.age
    name = body.name
    
    if name in info_dict.keys():
        info_dict[name] = age
    else:
        info_dict[name] = age
    
    return {"updated":True}
