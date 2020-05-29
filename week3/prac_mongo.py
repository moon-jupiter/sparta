from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)
db = client.dbsparta  # mongoDB는 27017 포트로 돌아갑니다.

#doc = {'name':'JG', 'age':28}
#db.users.insert_one(doc)

db.users.delete_one({'name':'kay'})

db.users.delete_one({'name':'john'})
