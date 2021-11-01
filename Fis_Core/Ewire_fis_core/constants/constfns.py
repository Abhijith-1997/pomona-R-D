import datetime
from flask import request,Response
import requests,json
import logging
from Ewire_fis_core.constants.config import generic_consts
from Ewire_fis_core.statics import staticconstants
from Ewire_fis_core.constants import config
import hashlib
from hashlib import md5
from base64 import b64decode
from base64 import b64encode
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad


BLOCK_SIZE = 16



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
    print("Resp type in common response", str(resptype))
    print(type(resptype))
    if(resptype['status'] == "SUCCESS"):
        resptype['Response'] = {"request_status": "SUCCESS", "Status":" Transaction completed Successfully"}        
        return CommonResponse(resptype).__dict__
    elif (resptype['status'] == "FAIL"):
        respdata = resptype
        respdata["resp_code"] = "FAIL"
        respdata["resp_type"] = "APIRESP"
        respdata["message"] = "ACTIOON FAILED"
        respdata["request_status"] = "FAIL"
        respdata["Status"] = " Transaction failed with errors"
        print("RESPDATA",respdata)
        return CommonResponse(respdata).__dict__

def logger_srv(logData, configparams):
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


        logrequest = performRequest(generic_consts.logginServer,configparams['headerz'],configparams['endpoints'],logdata,configparams['reqtype'],configparams['methodtype'])
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

def performRequest(server, headerz, endpoint, reqdata, reqType, methodType):
   
    if(reqType == "SSL"):
        url = "https://" + server + endpoint

    else:
        url = "http://" + server + endpoint

    responseofreq = ""

    if(methodType == "POST"):
        
        print("DATA",str(reqdata))
        print("URL",str(url))
        print("HEADER",str(headerz))
        payload = json.dumps(reqdata)
        print(":::::::::::::",payload)

        try:
            r = requests.post(url, data = payload, headers=headerz)
            print(r)

            if(r.status_code == 200):

                return r.text
            else:
                return {"Error":"Api Failed"}
            responseofreq = r
        except Exception as e:
            return  str(e)
    else:
        if(methodType == "GET"):
            r = requests.get(url, data=reqdata, headers=headerz)
            if(r.status_code == 200):
                return "Success response to be created"
            else:
                return "failure response to be created"
            responseofreq = r
    return responseofreq


def validateReq(valdata):
    # VALIDATE REQUEST
    try:
        
        validatereq = performRequest(generic_consts.validateServer, generic_consts.validateHeaders, generic_consts.validateEndpoint, valdata, generic_consts.validateReqType, generic_consts.validateMethodType)
        validatereq = json.loads(validatereq)


        if(validatereq['response'] == 'success'):
            generic_consts.loggrRespdatasuccess["sourceoflog"] = "bcore-checklogin"
            valResp = generic_consts.loggrRespdatasuccess
        else:
            generic_consts.loggrRespdatafail["sourceoflog"] = "bcore-checklogin"
            valResp = generic_consts.loggrRespdatafail

    except ValueError as e:
        return str(e)
    except Exception as e:
        return str(e)

    logging.info(" :::VALIDATION SUCCESSFULL::: ")
    return valResp

def checkUser(chkdata):
    checkdata = chkdata
    # CHECK USER PROCESS
    try:
        if 'hash' in checkdata:
                
            checkdata.pop('hash')
            checkdata.pop('checksum')
            checkdata.pop('reqtype')
            checkdata.pop('status')
            checkdata.pop('authToken')

        requestDataJson = json.dumps(checkdata)
        print("REQDATAJSON",requestDataJson)
        print("REQDATAJSON",type(requestDataJson))
        checkUser = performRequest(generic_consts.checkUserServer, generic_consts.checkUserHeaders, generic_consts.checkUserEndpoint, requestDataJson, generic_consts.checkUserReqType, generic_consts.checkUserMethodType)
        print("checkUser", checkUser)
        checkUser = json.loads(checkUser)
        if(checkUser['status'] == 200):

            resp = generic_consts.hashDataRespSuccess
            resp["sourceoflog"] = "bcore-checklogin"
            resp["hash"] = checkUser['hash']
            return resp
        else:
            resp = generic_consts.hashDataRespdataFail
            resp["sourceoflog"] = "bcore-checklogin"
            
            return resp
      
    except ValueError as e:
        return str(e)
    except Exception as e:
        return str(e)

    logging.info(" :::CHECK USER SUCCESSFULL::: ")

def dpad(data):
    length = BLOCK_SIZE - (len(data) % BLOCK_SIZE)
    return (data + chr(length)*length).encode('utf8')

def dunpad(data):
    return data[:-data[-1]]

def r_pad(payload, block_size=16):
    length = block_size - (len(payload) % block_size)
    return payload + chr(length) * length

def decode_binary_string(s):
    return ''.join(chr(int(s[i*8:i*8+8],2)) for i in range(len(s)//8))

class AESCipher:
    def __init__(self, key):
        self.key = md5(key.encode('utf8')).digest()

    # def encrypt(self, payload):
    #     IV = Random.new().read(BLOCK_SIZE)
    #     return b64encode(AES.new(self.key, AES.MODE_CBC, IV).encrypt(r_pad(payload)))

    # def decrypt(self, payload):
    #     IV = Random.new().read(BLOCK_SIZE)
    #     return AES.new(self.key, AES.MODE_CBC, IV).decrypt(b64decode(payload))[:AES.block_size]

  

    # def encrypt(self, data):
    #     #IV = Random.new().read(BLOCK_SIZE)
    #     # aes = AES.new(self.key, AES.MODE_CBC, IV)
    #     # hassh = IV + aes.encrypt(dpad(data))
    #     # hasshret = b64encode(hassh).decode('utf-8')
    #     # return hasshret
    #     IV = Random.new().read(BLOCK_SIZE)
    #     aes = AES.new(self.key, AES.MODE_CBC, IV)
    #     return b64encode(IV + aes.encrypt(dpad(data))).decode('utf-8')

    def decrypt(self, data):
        encrypted = b64decode(data)
        IV = encrypted[:BLOCK_SIZE]
        aes = AES.new(self.key, AES.MODE_CBC, IV)
        return dunpad(aes.decrypt(encrypted[BLOCK_SIZE:]))

    def decrypt_from_cryptoJS(self, encrypted, iv = Random.new().read(BLOCK_SIZE)):
        aes = AES.new(self.key, AES.MODE_CBC, iv)           # Use CBC-mode
        encrypted = aes.decrypt(b64decode(encrypted))[AES.block_size:] # Remove Base64 decoding
        return encrypted

    def unpadPkcs7(self, data):
        return data[:-data[-1]]


def checkSum(value):
        # if  type(value)!= "Dict":
        #     value = json.dumps(value)
    hashvalue = hashlib.md5(str(value).encode('utf-8')).hexdigest()
    # hashValue = hashlib.sha512(value.encode('utf-8')).hexdigest().lower()
    return hashvalue

def prepareResp(prepareData,respdict):

    if respdict :
        Resp = generic_consts.successResp
        Resp['em_reqid'] = prepareData['em_reqid']   
        Resp['partner_reqid'] = prepareData['partner_reqid']
        Resp['timestamp'] = str(datetime.datetime.now())
        Resp['resp_frm_ewire'] = respdict
        Resp['em_custid'] = prepareData['em_custid']
        
    else:
        Resp = generic_consts.failureResp
        Resp['em_reqid'] = prepareData['em_reqid']
        Resp['partner_reqid'] = prepareData['partner_reqid']
        Resp['timestamp'] = str(datetime.datetime.now())
        Resp['resp_frm_ewire'] = {}
        Resp['em_custid'] = prepareData['em_custid']
    return Resp

    
# def getUrlsbyModule(modulename):
#    return standardresponses.commonValues[modulename]


def validateHash(requesthash,createdhash):

    decodehash2 = AESCipher(staticconstants.ENCRYPTION_KEY).decrypt(requesthash['hash'])

    #Decode hash from created hash
    checksum1 = request['checksum']

    checksum2 = checkSum(request['hash'])
    decodehash1 = AESCipher(staticconstants.ENCRYPTION_KEY).decrypt(createdhash['hash'])

    reqChecksum = checkSum(createdhash['hash'])

    #Compare Checksum and HASHES
    if decodehash1 == decodehash2:

        return "true"
    else:
        return "false"


def validatechecksum(requestchecksum,createdchecksum):
    checksum1 = checkSum(requestchecksum)
    checksum2 = checkSum(createdchecksum)
    if checksum1 == checksum2:
        return "true"
    else:
        return "false"





