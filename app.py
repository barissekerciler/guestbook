from flask import Flask
from flask import request
from flask import jsonify
from db_operations import DbOperations
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['POST', 'GET'])
def insert_data():
    db_ = DbOperations()
    if request.method == 'POST':
        return jsonify(result=db_.insert_message_to_db(request.json['username'], request.json['message']))
    if request.method == 'GET':
        return jsonify(result=db_.get_data())


if __name__ == '__main__':
    app.run(host=os.environ.get('APPHOST'), port=os.environ.get('APPPORT'), debug=os.environ.get('APPDEBUG'))
