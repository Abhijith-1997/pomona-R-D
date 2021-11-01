from Ewire_fis_core.maass import maasslogger
import json
from Ewire_fis_core.statics import staticfunctions,staticconstants
from Ewire_fis_core.platformlayers import standardresponses
from Ewire_fis_core.constants import constfns
import re
import datetime

def parseRequestHCRD(request):
    try:
        #Convert Request to dictionary
        reqdata = convinptodict(request)
    except Exception as e:
        #Log exception
        maasslogger(request, str(e))
        return str(e)

    #parse by pre defined request data
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
    if(isinstance(input, dict)):
        #it is already dict
        return input
    elif(isinstance(input, str)):
        #convert string to dictionary
        return json.loads(input)
    elif(isinstance(input, int)):
        #convert int to dictionary
        return json.loads(input)

def createHashfromData(request, modulename):
    #Extract Data
    hashabledata = convinptodict(request)
    rethashableonly = hashabledata['requestdata']
    #Prepare Data
    hashinput = preparehash(rethashableonly)
    #Convert to Hash
    hashh = callmaass4hashing(hashinput, modulename)
    #Return Hash
    return hashh

def preparehash(dataset):
    # print("request",request)
    hashstr = re.sub("{","||||",str(dataset)) # replace open brackets
    hashstr = re.sub("}","||||",hashstr) # replace close brackets
    hashstr = re.sub(":","|",hashstr) # replace semicolons
    hashstr = re.sub(" ","",hashstr) # replace spaces
    hashifyrequestdata = re.sub(",","||",hashstr) # replace commasz
    return hashifyrequestdata


def callmaass4hashing(hashinput, modulename):
    print("inside callmaass4hashing")
    urls = staticfunctions.getUrlsbyModule(modulename)
    print("urls:",urls)
    configparams = staticfunctions.commonValues
    print("configparams:",configparams)
    respfrmmasshash = constfns.performRequest(standardresponses.checkUserHeaders,standardresponses.checkUserReqType,standardresponses.checkUserMethodType,standardresponses.checkUserEndpoint)
    print("respfrmmasshash:",respfrmmasshash)


timeStamp = str(datetime.datetime.now())
def getDetails(request):
    print("inside  getDetails")
    
    try: 
        modPartyObj = staticfunctions.CommonUtil
        resp = modPartyObj.getByApiName(request)
        print("RESPONSE FROM GET API BY NAME ==> ",resp)


        print("request from be",request)
        print("request from DB",resp)
        

        if bool(resp):
            print("bool resp")
            respdata= staticconstants.success_resp(request,resp)
            print("respdata",respdata)

            # make dictionary and pass it inside the commonresponse
            responseObj = staticfunctions.CommonResponse(respdata)
            print("success responseobject",responseObj)
                
        else:
            response_dict = {"resp_from_core":"request attribute does not exist"}
            respdata= staticconstants.failure_resp(request,resp)

            responseObj = staticfunctions.CommonResponse(respdata)



    except Exception as e:
        response_dict = {"resp_from_core":str(e)}
        respdata= staticconstants.failure_resp(request,resp)

        responseObj = staticfunctions.CommonResponse(respdata)

    commonRespObj = staticfunctions.CommonResponse
    response = commonRespObj.classToJsonObj(responseObj)

    print("RESPONSE @ CORE ",response )

    return response

