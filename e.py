import random
from json import load

import math
import requests
import re



from pymongo import MongoClient

client = MongoClient("mongodb://pretty:shop1234@ds139942.mlab.com:39942/moviebot")
db = client.moviebot

cursor = db.data.insert({"intent":"สามารถ",'question':['ถามอะไรได้','ทำอะไรได้บ้าง','การทำงาน','มีความสามารถไรบ้าง','มีความสามารถอะไรบ้าง','มีความสามารถไร','มีฟังก์ชันไร','มีฟังชันไรบ้าง'],'answer':['มีความสามารถดังนี้'],"contextSet" : ""})

