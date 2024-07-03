from flask import Flask, request
import json

#GLobal Vars
items = []

app = Flask(__name__)

@app.get("/")
def home():
    return "hello from flask"


#API endpoints
#JSON
# create an API to perform a get request this url: /api/about
#return your name as a message

@app.get("/api/about")
def about():
    me = {"name": "Heather"}
    return json.dumps(me)

products = []

@app.post("/api/products")
def saveProducts():
    product = request.get.json()
    print (product)
    #mock the save
    items.append(product)
    return json.dumps()



@app.get("/api/products")
def getProduct():
    return json.dumps(items)


app.run(debug = True)