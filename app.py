from flask import Flask, request, jsonify, render_template, Response
from db_operations import DbOperations
from flask_cors import CORS
import os

app = Flask(__name__)

CORS(app)


@app.route('/', methods=['POST', 'GET'])
def insert_data():
    db_ = DbOperations()
    if request.method == 'POST':
        print(request.form['username'], request.form['message'])
        db_.insert_message_to_db(request.form['username'], request.form['message'])
        return render_template('index.html', data=db_.get_data())
    if request.method == 'GET':
        #return jsonify(result=db_.get_data())
        return render_template('index.html', data=db_.get_data())


@app.route('/health', methods=['GET'])
def health_check():
    return Response(status=200)


if __name__ == '__main__':
    app.run(host=os.environ.get('APPHOST'), port=os.environ.get('APPPORT'), debug=os.environ.get('APPDEBUG'))
