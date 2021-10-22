from flask import Flask
from flask.globals import session
from flask.wrappers import Request
from flask import Response, request
from Ewire_fis_core import app
from Ewire_fis_core.statics import urlconstants
import json
from Ewire_fis_core.platformlayers import bllayer, constantslayer
from Ewire_fis_core.responsemaster import responses


@app.route('/', methods=['POST','GET'])
def base():
    return responses.upGetResponse(request)

@app.route(urlconstants.endpoint+'/authapi', methods = ['POST'])
def authapi():
    
    # Check User credentials and perform login operation
    return bllayer.processLoginRequest(request.json)

@app.route('/api/v1/ewire/core/fis/apiDetails/byApiName', methods = ['POST'])
def getApiName():

    resp = dict()
    resp['resp_type'] = "FAILURE @ Core didnt enter try"

    try:
        print("RECEIVED REQ FROM BE")
        reqDataJson = request.get_json()
        # reqData = request.data.decode('utf-8').replace("'",'"')
        reqDataJson = json.loads(reqDataJson)
        print("RECEIVED DATA :: ", type(reqDataJson))

        print("REQUEST FOR URLS FOR API NAME : ", reqDataJson)

        if reqDataJson["api_name"] == "Authenticate":
            return constantslayer.getDetails(reqDataJson)

        elif reqDataJson["api_name"] == "CARD_VAL":
            return constantslayer.getDetails(reqDataJson)
        
        elif reqDataJson["api_name"] == "CARD_EXE":
            return constantslayer.getDetails(reqDataJson)

        elif reqDataJson["api_name"] == "CARD_CNCL_VAL":
            return constantslayer.getDetails(reqDataJson)
        
        elif reqDataJson["api_name"] == "CARD_CNCL_EXE":
            return constantslayer.getDetails(reqDataJson)

        elif reqDataJson["api_name"] == "CARD_ENQ_VAL":
            return constantslayer.getDetails(reqDataJson)
        
        elif reqDataJson["api_name"] == "CARD_ENQ_EXE":
            return constantslayer.getDetails(reqDataJson)

        elif reqDataJson["api_name"] == "CARD_STATUS_VAL":
            return constantslayer.getDetails(reqDataJson)

        elif reqDataJson["api_name"] == "CARD_STATUS_EXE":
            return constantslayer.getDetails(reqDataJson)

        elif reqDataJson["api_name"] == "CUST_UPDATE_VAL":
            return constantslayer.getDetails(reqDataJson)

        elif reqDataJson["api_name"] == "CUST_UPDATE_EXE":
            return constantslayer.getDetails(reqDataJson)
        
        elif reqDataJson["api_name"] == "CARD_REPLCMNT_VAL":
            return constantslayer.getDetails(reqDataJson)
        
        elif reqDataJson["api_name"] == "CUST_REPLCMNT_EXE":
            return constantslayer.getDetails(reqDataJson)
        

        elif reqDataJson["api_name"] == "CARD_ISSUE_VAL'":
            return constantslayer.getDetails(reqDataJson)

        elif reqDataJson["api_name"] == "CARD_ISSUE_EXE":
            return constantslayer.getDetails(reqDataJson)

        elif reqDataJson["api_name"] == "CARD_ACT_VAL":
            return constantslayer.getDetails(reqDataJson)


        elif reqDataJson["api_name"] == "CARD_ACT_EXE":
            return constantslayer.getDetails(reqDataJson)


        elif reqDataJson["api_name"] == "CARD_UPGRADE_VAL":
            return constantslayer.getDetails(reqDataJson)

        elif reqDataJson["api_name"] == "CARD_UPGRADE_EXE":
            return constantslayer.getDetails(reqDataJson)

        elif reqDataJson["api_name"] == "CUST_DET_ENQ":
            return constantslayer.getDetails(reqDataJson)


        elif reqDataJson["api_name"] == "VIRTUAL_CARD_VAL":
            return constantslayer.getDetails(reqDataJson)

        
        elif reqDataJson["api_name"] == "VIRTUAL_CARD_EXE":
            return constantslayer.getDetails(reqDataJson)


        elif reqDataJson["api_name"] == "VIRTUAL_PHYSCL_CARD":
            return constantslayer.getDetails(reqDataJson)


        elif reqDataJson["api_name"] == "VIRTUAL_PHYSCL_CARD_EXE":
            return constantslayer.getDetails(reqDataJson)


        elif reqDataJson["api_name"] == "ADJST_ACC_BLNC_VAL":
            return constantslayer.getDetails(reqDataJson)

        elif reqDataJson["api_name"] == "ADJST_ACC_BLNC_EXE":
            return constantslayer.getDetails(reqDataJson)
        
        elif reqDataJson["api_name"] == "ACC_LOAD_EXE":
            return constantslayer.getDetails(reqDataJson)

        elif reqDataJson["api_name"] == "SET_PIN":
            return constantslayer.getDetails(reqDataJson)

        elif reqDataJson["api_name"] == "CHANGE_PIN":
            return constantslayer.getDetails(reqDataJson)

        elif reqDataJson["api_name"] == "VERIFY_PIN_EXE":
            return constantslayer.getDetails(reqDataJson)

        elif reqDataJson["api_name"] == "TXN_DET_ENQ":
            return constantslayer.getDetails(reqDataJson)

        elif reqDataJson["api_name"] == "GIFT_CARD_VAL":
            return constantslayer.getDetails(reqDataJson)

        elif reqDataJson["api_name"] == "GIFT_CARD_EXE":
            return constantslayer.getDetails(reqDataJson)

        elif reqDataJson["api_name"] == "CVV2_VERFCTN":
            return constantslayer.getDetails(reqDataJson)
 
        elif reqDataJson["api_name"] == "CARD_DET_ENQ":
            return constantslayer.getDetails(reqDataJson)

        elif reqDataJson["api_name"] == "CHANNEL_UPDT":
            return constantslayer.getDetails(reqDataJson)

        elif reqDataJson["api_name"] == "LIMIT_UPDT":
            return constantslayer.getDetails(reqDataJson)

        elif reqDataJson["api_name"] == "CARD_DET_ENQ":
            return constantslayer.getDetails(reqDataJson)



        elif reqDataJson["api_name"] == "LIMIT_CHANNEL_UPDT":
            return constantslayer.getDetails(reqDataJson)


        else:
            resp['resp_msg'] = "Api name not found in records"
            print("RESPONSE @ CORE ",resp )
            return resp


    except Exception as e:
        print("RESPONSE @ CORE "+str(e),resp )
        resp['resp_msg'] = str(e)
        return resp


