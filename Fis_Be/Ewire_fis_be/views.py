
from flask.globals import session
from flask.json import jsonify
from flask.wrappers import Request
from flask import Response,request
from Ewire_fis_be import app
import json
from Ewire_fis_be.platformlayers import bllayer, constantslayer
from Ewire_fis_be.responsemaster import responses
from Ewire_fis_be.statics.staticfunctions import uitobe_response, validateReq
from flask_cors import CORS
baseUrl = '/api/v1/fis'
@app.route('/', methods=['POST','GET'])
def base():
    
    return responses.upGetResponse(request)

@app.route(baseUrl+'/login', methods = ['POST'])
def user():
    valdata=validateReq(request)
    print("valdata",valdata)

    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.checklogin(request)
        print("checklog",checklog)
        checklog['resp_type']=="SUCCESS"
        return jsonify(uitobe_response(checklog))
    else:
        request['resp_type']="FAIL"
        return jsonify(uitobe_response())




