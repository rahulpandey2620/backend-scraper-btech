from pymongo import MongoClient
local_connection_str= "mongodb://localhost:27017/test"
remote_connection_str = "mongodb+srv://rahul:<password>@cluster0.hem9w.mongodb.net/?retryWrites=true&w=majority"
conn=MongoClient(remote_connection_str)