import pickle

a = {
'db': 'lineserver',
'user':'user1',
'password':'ImUser!',
'adminUserName':'circleProjectAdmin',
'adminPassword':'I<3BlockChain',
'email':'d1070103@nwytg.com',
'collection':'lines',
'DatabaseName':'myMongoDatabase',
'link':'@ds117749.mlab.com:17749/',
'protocol':'mongodb://'
}

with open('credentials.pickle', 'wb') as handle:
    pickle.dump(a, handle, protocol=pickle.HIGHEST_PROTOCOL)
