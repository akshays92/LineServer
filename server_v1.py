from flask import Flask
from flask import jsonify
from flask import request
from flask import json
from flask import Response
from flask_pymongo import PyMongo
import sys

dburi='mongodb://user1:ImUser!@ds117749.mlab.com:17749/lineserver'
# Create our Flask app
app = Flask(__name__)
# Add MONGO_DBNAME and MONGO_URI to our app config
app.config['MONGO_DBNAME'] = 'lineserver'
app.config['MONGO_URI'] = dburi

# Feed app into PyMongo() to generate a db connection
mongo = PyMongo(app)

@app.route('/lines/<int:id>', methods=['GET'])
def get_line(id):
    lines = mongo.db['lines']
    data = lines.find_one({"lineNumber": id})
    if data is not None:
    	js = json.dumps(data['text'])
    	resp = Response(js, status=200, mimetype='application/json')
    else:
    	data={
    	"ERROR":"Requested line is beyond the end of file"
    	}
    	js = json.dumps(data)
    	resp = Response(js, status=413, mimetype='application/json')
    return resp

# This has to be last because definition order matters in Python
if __name__ == '__main__':
    app.run(debug=False)

