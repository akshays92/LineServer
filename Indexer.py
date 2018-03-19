import sys
from pymongo import MongoClient
import pickle
#print(str(sys.argv[1]))
filename = str(sys.argv[1])
file = open(filename, "r")
lineNumber=0

#retriving the credentials
with open('credentials.pickle', 'rb') as handle:
    cred = pickle.load(handle)

#client = MongoClient('mongodb://user1:ImUser!@ds117749.mlab.com:17749/lineserver')
client = MongoClient(cred['protocol']+cred['user']+':'+cred['password']+cred['link']+cred['db'])
db = client[cred['db']]
db.drop_collection(cred['collection'])
for line in file:
   #print (str(lineNumber)+": "+line)
   post = {"lineNumber": lineNumber,
   "text": line}
   lines = db[cred['collection']]
   post_id = lines.insert_one(post).inserted_id
   #print(lineNumber)
   lineNumber+=1
print ("Number of lines indexed: "+str(lineNumber-1))