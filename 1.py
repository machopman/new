
'''
import random

from pymongo import MongoClient

client = MongoClient("mongodb://pretty:shop1234@ds139942.mlab.com:39942/moviebot")
db = client.moviebot

def general(question):
    doc = db.users
    for i in doc.find({'question'}):
        print(i)
print(general('ถามอะไรได้บ้าง'))
'''
'''
import difflib


def  match(event):

      a = difflib.get_close_matches(event, ['ทำอะไรได้บ้าง', 'การทำงาน', 'มีความสามารถไรบ้าง', 'ทำไรได้'])
      #a = difflib.get_close_matches(event, ['ไปไหนมา', 'กินข้าหรือยัง', 'ลาก่อนนะ', 'ทำอะไรอยู่'])

'''

a = [["สวัสดี","ดีจ้า","สวัสดีค่ะ","สวัสดีครับ","สวัส","ดีจร้า","ดีงับ","สวัดดี"] ,["ทำอะไรได้บ้าง","การทำงาน","มีความสามารถไรบ้าง","ทำไรได้"],["สบายดีไหม",""]]

