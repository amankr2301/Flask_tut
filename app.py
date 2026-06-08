from flask import Flask , request 

app = Flask(__name__)
    

# for now just making stores list later will setup into the database 
stores = [
    {
        "name": "store1" , 
        "items" : [
            {
            "name" : "chair" , 
            "price" : 1200
        }
        ]
    }
]

@app.get("/store")  #http://127.0.0.1:5000/store
def get_stores():
    return {"Stores" : stores} ; 

@app.post("/store")
def create_store():
    request_data = request.get_json() ;  
    new_store = {"name" : request_data["name"] , "items" : []}
    stores.append(new_store) ; 
    return new_store , 201


@app.post("/store/<string:name>/additems")
def add_items(name):
    request_data = request.get_json() ; 
    store_name = name ; 
    new_items = request_data["items"]
    for i in stores:
        if (i["name"] == store_name):
            i["items"].append(new_items) ; 
            return new_items , 201 ; 
    return f"store with name {name} not found " , 404


@app.get("/store/<string:storename>")
def get_store(storename):
    for i in stores:
        if (i["name"] == storename):
            return i , 201
        
    return f"store with storename {storename} not found" , 404

@app.get("/store/<string:name>/items")
def items_in_store(name):
    for i in stores:
        if(i["name"] == name):
            return i["items"] , 201
    return f"Store with name {name} not found"


    



