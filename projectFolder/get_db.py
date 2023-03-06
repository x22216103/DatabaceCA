from pymongo import MongoClient

def get_db():
    CONNECTION_STRING= "mongodb+srv://cluster0.sqm88.mongodb.net/StormPredDb"
    client = MongoClient(CONNECTION_STRING)
    return client.get_database('my_db')

if __name__=='__main__':
    dbname = get_db()