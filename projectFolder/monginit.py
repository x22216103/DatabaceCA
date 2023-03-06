from get_db import get_db
from dateutil import parser
dbname = get_db()
collection_name = dbname["initial_null_values"]

test_event = {
  "_id" : "U1IT00001",
  "event_name" : "test_weather",
  "humidity" : "0%",
  "feels_like" : 10,
  "real_temp" : 34,
  "category" : "test_extreme_event"
}
collection_name.insert_one(test_event)