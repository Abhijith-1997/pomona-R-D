from Ewire_fis_be.maass import maasslogger
import json,jsonschema
import re
from Ewire_fis_be.statics import staticfunctions
from Ewire_fis_be.statics.staticfunctions import PostRequestManager
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

        # response from core
        FisCoreResp = staticfunctions.performRequest(otherdata)        
        print("=========resposne from CORE is=====")
        print("TYPE====",type(FisCoreResp))
        print("VALUE===",FisCoreResp)
        FisCoreResp=json.loads(FisCoreResp)
        if FisCoreResp['resp_type'] == "FAILURE":
            return FisCoreResp

# for external api
        elif FisCoreResp['resp_type'] == "SUCCESS":
            print(" entered elif fiscoreresp")

            try:
                ewireReqData = {
                    "em_reqid": FisCoreResp['em_reqid'],
                    "timestamp" : str(urlconstants.TIME_NOW),
                    "em_custid" : FisCoreResp['em_custid'],
                    "apiname": FisCoreResp['api_name'],
                    "partner_id" : FisCoreResp['partner_id'],
                    "ext_base_url": FisCoreResp['ext_base_url'],
                    "ext_end_point_url": FisCoreResp['ext_end_point_url'],
                    
                    "api_header": FisCoreResp['api_header'], #Header for api provider
                    "req_data": FisCoreResp['req_data'] # req data for api provider
                }
            except Exception as e:
                print("exception",str(e))
                return str(e)
            except ValueError as e:
                print("exception2",str(e))
                return str(e)


        print("apiheader type "+str(type(FisCoreResp['api_header'])))
        print("===========ewireReqData======")
        print(ewireReqData)
        postToExternal = PostRequestManager 
        response = postToExternal.postrequestManagerExtApi(ewireReqData)
        print("==============RESPONSE FROM EXTERNAL============")
        print(response)
        response = json.loads(response)
        print("==============RESPONSE FROM EXTERNAL after loads============")
        print(response)
        try:
            if type(response['resp_frm_ext_api']) == list:                        
                print("++++RESP TYPE IS LIST++++")
                return response

            if 'Error' in response['resp_frm_ext_api'] or 'error desc' in response['resp_frm_ext_api']:
                response['resp_frm_ext_api']['resp_type'] = "FAILURE"
                return response
            else:
                response['resp_frm_ext_api']['resp_type'] = "SUCCESS"
                return response
        except KeyError:
            response['resp_frm_ext_api']['resp_type'] = "FAILURE"
        except Exception as e:
            return str(e)
        return response
                
    except Exception as e:
        return str(e)

        
        print("ivide ethi 1",FisCoreResp)
        return FisCoreResp
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
