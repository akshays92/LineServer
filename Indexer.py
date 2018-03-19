import sys
from pymongo import MongoClient
#print(str(sys.argv[1]))
filename = str(sys.argv[1])
file = open(filename, "r")
lineNumber=0
client = MongoClient('mongodb://user1:ImUser!@ds117749.mlab.com:17749/lineserver')
db = client['lineserver']
db.drop_collection('lines')
for line in file:
   #print (str(lineNumber)+": "+line)
   post = {"lineNumber": lineNumber,
   "text": line}
   lines = db.lines
   post_id = lines.insert_one(post).inserted_id
   #print(lineNumber)
   lineNumber+=1
print ("Number of lines indexed: "+str(lineNumber-1))