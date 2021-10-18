import flask
from flask import Response
import json
def upGetResponse():
    print("resppp")
    resp = Response(response=json.dumps({"Status":"UP"}),status=200,mimetype='application/json')
    print("resppp")
    return resp
def standardErrorResponseToUI(src,error):
    resp = Response(response=json.dumps({"Source":src},{"ERROR":str(error)}),status=200,mimetype='application/json')
    return resp