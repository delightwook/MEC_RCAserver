from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse, abort

import json
import ast
app = Flask(__name__)
api = Api(app)



"""
Test Code
url = 'curl -i -H \"Content-Type: application/json\" -X POST -d ' + '\'' + total_request + '\'' + ' http://127.0.0.1:5050/Test'
os.system(url)
"""


@app.route('/MECrcaserver',methods=['POST','PUT'])
def rca_server():
    if not request.json:
        abort(400)
    data = request.json
    print(data)
    api_handler.start_action(data['action'],data)

    return ''

if __name__ == '__main__':
    app.run(host='127.0.0.1',port = 7070,debug = True)