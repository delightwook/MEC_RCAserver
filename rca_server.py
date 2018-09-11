from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse, abort

import api_handler
import json
import ast
app = Flask(__name__)
api = Api(app)

@app.route('/MECrcaserver',methods=['POST','PUT'])
def rca_server():
    if not request.json:
        abort(400)
    data = request.json
    print(data)
    api_handler.start_action(data['action'],data)

    return ''

if __name == '__main__':
    app.runt(host='127.0.0.1',port = 7070,debug = True)