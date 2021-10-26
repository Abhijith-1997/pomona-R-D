import requests,json
import logging
from Ewire_fis_core.constants.config import generic_consts
from Ewire_fis_core.platformlayers import standardresponses
from Ewire_fis_core.constants import config
from Ewire_fis_core.constants import constfns
from Ewire_fis_core.statics.dbconstants import MongoAPI
from Ewire_fis_core.statics import staticconstants
from json import JSONEncoder
from requests import request

import hashlib
from hashlib import md5
from base64 import b64decode
from base64 import b64encode

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import datetime

logging.basicConfig(level=logging.DEBUG)
logger= logging.getLogger('GET API DETAILS BY API NAME::')


class CommonUtil:
    def getByApiName(data):
        print("entered getApiByName")
        
        try:
            dataDupe={}
            dataDupe['database']="pomona_maass"
            dataDupe['collection']="apix"
            apiDict = False

            # Database = MongoAPI()
         
            logger.info("REQUEST FOR GET API BY NAME : " + str(data))

            #ToDO validations of request parameters
            # if 'partner_id' in data.keys():
            if 'partner_reqid' in data.keys():

                try:
                    queryDict = {"partnerid":data['partner_reqid'],"apiName":data['apiname']}
                    print(queryDict)
                    try:
                                                
                        apiDict=MongoAPI(dataDupe).readOne(queryDict)

                        print("apiDict",apiDict)
                    except:
                        apiDict = False
                except:
                    apiDict = False

            elif 'em_custid' in data.keys():
                try:
                    custDict = MongoAPI.readOne('ccp_customers',{"custId":data['em_custid']})
                    custID = data['em_custid']
                    try:
                        queryDict = {"partnerid":custDict['partner_reqid'],"apiName":data['apiname']}
                        try:
                            # apiDict = Database.readOne('apix',queryDict)
                            apiDict=MongoAPI(dataDupe).readOne(queryDict)
                        except:
                            apiDict = False
                    except:
                        apiDict = False
                except:
                    apiDict = False


            print("apiDict ==>", apiDict)

            if apiDict:

                req_data = dict()
                if 'req_data' in data:
                    req_data = data['req_data']


                print("success apiDict")
                response = {
                    "cust_id": apiDict["em_custid"],
                    "partner_reqid": apiDict['partnerid'],
                    "ext_base_url": apiDict['apiURL'],
                    "ext_end_point_name": apiDict['apiEndpoint'],
                    # "api_header": api_header,
                    "api_header":apiDict["apiHeader"],
                    "req_data": req_data
                } 

                # print("success apiDict")
                # response = {
                #     "cust_id": apiDict["id"],
                #     "partner_id": apiDict['partnerid'],
                #     "ext_base_url": apiDict['apiURL'],
                #     "ext_end_point_name": apiDict['apiEndpoint'],
                #     # "api_header": api_header,
                #     "api_header":apiDict["apiHeader"],
                #     "req_data": req_data
                # } 
            else:
                print("failed apiDict")
                response = False
            
            print("RESPONSE @CORE getByApiName ",response)
            return response

        except Exception as e:
            return e 
            
# COMMON RESPONSE CLASS
class CommonResponse:
    em_reqid : str
    timestamp : datetime
    em_custid : str
    resp_code : str
    message : str
    resp_type : str
    resp_frm_yesb : dict
    resp_frm_ewire : dict

    def __init__(self, respdata):

        print("DATARESp",respdata)
        print("DATAAA",type(respdata))

        self.em_reqid= ""
        self.timestamp= ""
        self.em_custid= ""
        self.resp_code= ""
        self.message= ""
        self.resp_type= ""
        self.resp_frm_yesb=""
        self.resp_frm_ewire=""
        
        self.resp_code = respdata["resp_code"]
        self.resp_type = respdata["resp_type"]
        self.message = respdata["message"]
       
        try:
            if respdata["em_reqid"] is None or respdata["em_reqid"] is None:
                 raise Exception("Attribute error,request param null")
                    
            self.em_reqid = respdata["em_reqid"]
            self.em_custid = respdata["em_custid"]
            self.resp_frm_bank = respdata["resp_frm_bank"]
            self.resp_frm_ewire = respdata["resp_frm_ewire"]
            self.resp_frm_cbs = respdata["resp_frm_cbs"]
            self.resp_frm_ext = respdata["resp_frm_ext"]
            self.resp_frm_maass = respdata["resp_frm_maass"]
            self.resp_frm_blockc = respdata["resp_frm_blockc"]
            self.resp_frm_mojaloop = respdata["resp_frm_mojaloop"]
            self.resp_frm_rulengn = respdata["resp_frm_rulengn"]
            self.timestamp = str(datetime.datetime.now())

        except ValueError :
            raise Exception("ValueError exception  while assigning timeStamp")
        except TypeError:
            raise Exception("TypeError exception while assigning timeStamp")
        except Exception as e:
            print(e)
            raise Exception(e)
            
    @staticmethod
    def classToJsonObj(obj):
    # apiRespStr = json.dumps(obj.__dict__)
        apiRespStr = json.dumps(obj.__dict__ ,
                sort_keys=False,
                indent=1,
                cls=DjangoJSONEncoder)
        return apiRespStr

def checkrequest(request):
    data = request
    if data is None or data == {}:
        return {"response" : json.dumps({"Error": "Please provide connection information"}),
                        "status" : 500,
                        "mimetype" : 'application/json'}
    else:
        return {"response" : json.dumps({"Success": "It Works"}),
                        "status" : 200,
                        "mimetype" : 'application/json'}

def coretobe_response(resptype): 
    print("eneterd coretobe response")
    print("Resp type in common response", str(resptype))
    print(type(resptype))
    if(resptype['status'] == "SUCCESS"):
        resptype['Response'] = {"request_status": "SUCCESS", "Status":" Transaction completed Successfully"}        
        # return CommonResponse(resptype).__dict__
        return CommonResponse(resptype)
    elif (resptype['resp_type'] == "FAIL"):
        respdata = resptype
        respdata["resp_code"] = "FAIL"
        respdata["resp_type"] = "APIRESP"
        respdata["message"] = "ACTIOON FAILED"
        respdata["request_status"] = "FAIL"
        respdata["Status"] = " Transaction failed with errors"
        print("RESPDATA",respdata)
        return CommonResponse(respdata).__dict__

def logger_srv(logData, configparams):
    print("entered logger srv")
    if(logData['reqtype'] == "SUCCESS"):
        resp = successlogreq(logData, configparams)
    else:
        if(logData['reqtype'] == "FAIL"):
            resp = faillogreq(logData)
            print("")
        else:
            print("FAIL")
    print("Response: " + str(resp))
    return resp

def successlogreq(reqdata, configparams):
    print("enterd successlog req")
    # REQUEST LOGGING
    try:
        logdata = {}
        
        logdata['apiname'] =  configparams['apiname']
        logdata['level'] = "SUCCESS"
        logdata['logtype'] = "SUCCESS LOG"
        logdata['logdata'] = json.dumps(reqdata)
        logdata['reqtype'] = reqdata['req_type']
        logdata['timestamp'] = str(datetime.datetime.now())
        logdata['collection'] = config.LOG_TABLE

        logdata['datalog'] = reqdata


        logrequest = constfns.performRequest(generic_consts.logginServer,configparams['headerz'],configparams['endpoints'],logdata,configparams['reqtype'],configparams['methodtype'])
        logrequest = json.loads(logrequest)

        
        if(logrequest['respType'] == 'Success'):
            generic_consts.loggrRespdatasuccess["sourceoflog"] = "bcore-checklogin"
            logResp = generic_consts.loggrRespdatasuccess
            print("LOGGIN SUCCESSFULL")
        else:
            generic_consts.loggrRespdatafail["sourceoflog"] = "bcore-checklogin"
            logResp = generic_consts.loggrRespdatafail
            print(" :::LOGGING FAILED::: ")

    except ValueError as e:
        return str(e)
    except Exception as e:
        return str(e)
    
    logResp = reqdata
    print("Log Response ", logResp)
    logResp['status'] = "SUCCESS"
    return logResp

def faillogreq(reqdata):
    reqst = "" + reqdata + ""
    return reqst




# class AESCipher:
#     def __init__(self, key):
#         self.key = md5(key.encode('utf8')).digest()

#     def encrypt(self, data):
#         iv = get_random_bytes(AES.block_size)
#         print(iv)
#         self.cipher = AES.new(self.key, AES.MODE_CBC,iv)
#         return b64encode(self.cipher.encrypt(pad(data.encode('utf-8'),AES.block_size))).decode('utf-8')

#     def decrypt(self, data):
#         raw = b64decode(data)
#         self.cipher = AES.new(self.key, AES.MODE_CBC, raw[:AES.block_size])
#         return unpad(self.cipher.decrypt(raw[AES.block_size:]), AES.block_size).decode('utf-8')





        
