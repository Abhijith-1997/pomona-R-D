from Ewire_fis_be.maass import maasslogger
import json,jsonschema
import re
from Ewire_fis_be.statics import staticfunctions
from Ewire_fis_be.platformlayers import standardresponses
from Ewire_fis_be.statics import urlconstants
from jsonschema import validate

def parseRequestHCRD(request):
    try:
        #convert Request to dictionary
        reqdata = convinptodict(request)
    except Exception as e:
        #Log exception
        maasslogger(request,str(e))
        return str(e)
    #parse by predefined requestdata
    hashfrmInput = reqdata['hash']
    checksumfrmInput = reqdata['checksum']
    datafrmInput = reqdata['requestdata']
    #prepare a return dictionary
    retaftrParsed = {}
    retaftrParsed['hash'] = hashfrmInput
    retaftrParsed['checksum'] = checksumfrmInput
    retaftrParsed['datafrm'] = datafrmInput
    return retaftrParsed

def convinptodict(input):
    #check input data type
    if(isinstance(input,dict)):
        #it is already dict
        return input
    elif(isinstance(input,str)):
        #convert string to dictionary
        return json.loads(input)
    elif(isinstance(input,int)):
        #convert iny to dictionary
        return json.loads(input)
        
def backendapi(req):
    print("XXXXXX")
    request = req.get_json()
    try:
        datadict = {"req_type":request['req_type'],"req_code":request['req_code'],
                    "apiname":request['apiname'],"em_reqid":request['em_reqid'],
                    "partner_reqid":request['partner_reqid'],"requestdata":request['requestdata'],"authToken":request['authtoken'],"em_endpoint":request['em_endpoint'],
                    "em_custid":request['em_custid'],"txntype":request["txntype"],"hash":request['hash'],"checksum":request['checksum']}

        obj = standardresponses.commonValues[request['apiname']]  #eg:CORTEX
        print("datadict",datadict)
        otherdata = {}
        # modulename = 'LOGIN'
        otherdata['parameters'] = obj
        otherdata['data'] = datadict

        BuildBeResp = staticfunctions.performRequest(otherdata)
        print("ivide ethi 1",BuildBeResp)
        return BuildBeResp
    except ValueError as e:
        print("EXCEPTION1",str(e))
        return str(e)
    except Exception as e:
        print("EXCEPTION2",str(e))
        return str(e)
def validateJSON(jsonData, schemaname):
    str1 = {}
    try:
        validated = validate(instance=jsonData, schema=schemaname)
    except jsonschema.exceptions.ValidationError as err:
        return {"respType": "failure"}
    return {"respType": "success"}