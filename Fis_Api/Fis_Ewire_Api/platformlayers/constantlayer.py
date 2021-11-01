import requests
from flask import request
import logging,sys,json
from Fis_Ewire_Api.statics.urlconstants import Constants
from Fis_Ewire_Api.constants.validations import ValidateResp
from Fis_Ewire_Api.statics.staticfunctions import CommonResponse,CommonUtil



class AuthApiImpl:
    def authenticateMethod(req):
        respObj = {}
        try:
    
            URL = Constants.AUTH_TOKEN_URL        
                        
            header = {"Content-Type:application/json"}

            fisResp = CommonUtil.postrequestManager(URL,header,Constants.payload)
         
            print("End of aunthenticate method",fisResp)
            isValid = ValidateResp.validateObj(fisResp)
         # respObj['message']= "Successfully authenticated" 
            print("\n=====isValid====\n",isValid)
            return isValid

        except Exception as e:
            return {"resp_type":"FAILURE","resp_code":"9004","message":str(e)}
        # print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)


class CardOrderApiImpl:

    def cardOrderValidation(req):
        try:
            URL = Constants.API_SERVICE + Constants.CARD_ORDER_ENDPOINT
            print(">>>>><<<<<fwReqDATAJSON",req)
            fwReqJson = req['req_data']

            headers1 = CommonResponse.get_auth_head(CommonResponse,Constants.AUTH_TOKEN_URL,Constants.TOKEN_HEADER,1)
            print("header from authenticate : : : ",headers1)

            print("REQUESTS data",fwReqJson)
            print("REQUESTS data",type(fwReqJson))

            fwReqJson = json.dumps(fwReqJson)

            fisResp = CommonUtil.postrequestManager(URL,headers1,fwReqJson)
            print("End card order validation>>>>>>???????????",str(fisResp))
            isValid = ValidateResp.validateObj(fisResp)
            return isValid
        
        except Exception as e:
            return {"resp_type":"FAILURE","resp_code":"9004","message":str(e)}


    def cardOrderExecution(req):
        try:
            URL = Constants.API_SERVICE + Constants.CARD_ORDER_ENDPOINT
            print(">>>>><<<<<fwReqDATAJSON",req)
            fwReqJson = req['req_data']
            headers1 = CommonResponse.get_auth_head(CommonResponse,Constants.AUTH_TOKEN_URL,Constants.TOKEN_HEADER,1)
            print("header from authenticate : : : ",headers1)
            print("REQUESTS data",fwReqJson)
            print("REQUESTS data",type(fwReqJson))
            fwReqJson = json.dumps(fwReqJson)

            fisResp = CommonUtil.postrequestManager(URL,headers1,fwReqJson)
            print("End card order execution>>>>>>???????????",str(fisResp))
            isValid = ValidateResp.validateObj(fisResp)
            return isValid
        except Exception as e:
            return {"resp_type":"FAILURE","resp_code":"9004","message":str(e)}


#cancel
class CardCancelApiImpl:
    def cardCancelValidation(req):
        try:
            URL = Constants.API_SERVICE + Constants.CARD_CANCEL_ENDPOINT
            print(">>>>><<<<<fwReqDATAJSON",req)
            fwReqJson = req['req_data']
            headers1 = CommonResponse.get_auth_head(CommonResponse,Constants.AUTH_TOKEN_URL,Constants.TOKEN_HEADER,1)
            print("header from authenticate : : : ",headers1)
            print("REQUESTS data",fwReqJson)
            print("REQUESTS data",type(fwReqJson))
            fwReqJson = json.dumps(fwReqJson)

            fisResp = CommonUtil.postrequestManager(URL,headers1,fwReqJson)
            print("End cancel order validation>>>>>>???????????",str(fisResp))
            isValid = ValidateResp.validateObj(fisResp)
            return isValid
        except Exception as e:
            return {"resp_type":"FAILURE","resp_code":"9004","message":str(e)}

    def cardCancelExecution(req):
        try:
            URL = Constants.API_SERVICE + Constants.CARD_CANCEL_ENDPOINT
            print(">>>>><<<<<fwReqDATAJSON",req)
            fwReqJson = req['req_data']
            headers1 = CommonResponse.get_auth_head(CommonResponse,Constants.AUTH_TOKEN_URL,Constants.TOKEN_HEADER,1)
            print("header from authenticate : : : ",headers1)
            print("REQUESTS data",fwReqJson)
            print("REQUESTS data",type(fwReqJson))
            fwReqJson = json.dumps(fwReqJson)

            fisResp = CommonUtil.postrequestManager(URL,headers1,fwReqJson)
            print("End cancel order execution>>>>>>???????????",str(fisResp))
            isValid = ValidateResp.validateObj(fisResp)
            return isValid
        except Exception as e:
            return {"resp_type":"FAILURE","resp_code":"9004","message":str(e)}

class CardEnqiuryApiImpl:
    def cardEnquiryValidation(req):
        try:
            URL = Constants.API_SERVICE + Constants.CARD_ENQ_ENDPOINT
            print(">>>>><<<<<fwReqDATAJSON",req)
            fwReqJson = req['req_data']
            headers1 = CommonResponse.get_auth_head(CommonResponse,Constants.AUTH_TOKEN_URL,Constants.TOKEN_HEADER,1)
            print("header from authenticate : : : ",headers1)
            print("REQUESTS data",fwReqJson)
            print("REQUESTS data",type(fwReqJson))
            fwReqJson = json.dumps(fwReqJson)

            fisResp = CommonUtil.postrequestManager(URL,headers1,fwReqJson)
            print("End card enquiry>>>>>>???????????",str(fisResp))
            isValid = ValidateResp.validateObj(fisResp)
            return isValid
        except Exception as e:
            return {"resp_type":"FAILURE","resp_code":"9004","message":str(e)}

    def cardEnquiryExecution(req):
        try:
            URL = Constants.API_SERVICE + Constants.CARD_ENQ_ENDPOINT
            print(">>>>><<<<<fwReqDATAJSON",req)
            fwReqJson = req['req_data']
            headers1 = CommonResponse.get_auth_head(CommonResponse,Constants.AUTH_TOKEN_URL,Constants.TOKEN_HEADER,1)
            print("header from authenticate : : : ",headers1)
            print("REQUESTS data",fwReqJson)
            print("REQUESTS data",type(fwReqJson))
            fwReqJson = json.dumps(fwReqJson)

            fisResp = CommonUtil.postrequestManager(URL,headers1,fwReqJson)
            print("End card enquiry execution>>>>>>???????????",str(fisResp))
            isValid = ValidateResp.validateObj(fisResp)
            return isValid
        except Exception as e:
            return {"resp_type":"FAILURE","resp_code":"9004","message":str(e)}


class CardStatusApiImpl:
    def cardStatusValidation(req):
        try:
            URL = Constants.API_SERVICE + Constants.CARD_STATUS_ENDPOINT
            print(">>>>><<<<<fwReqDATAJSON",req)
            fwReqJson = req['req_data']
            headers1 = CommonResponse.get_auth_head(CommonResponse,Constants.AUTH_TOKEN_URL,Constants.TOKEN_HEADER,1)
            print("header from authenticate : : : ",headers1)
            print("REQUESTS data",fwReqJson)
            print("REQUESTS data",type(fwReqJson))
            fwReqJson = json.dumps(fwReqJson)

            fisResp = CommonUtil.postrequestManager(URL,headers1,fwReqJson)
            print("End card status change validation>>>>>>???????????",str(fisResp))
            isValid = ValidateResp.validateObj(fisResp)
            return isValid
        except Exception as e:
            return {"resp_type":"FAILURE","resp_code":"9004","message":str(e)}

    def cardStatusExecution(req):
        try:
            URL = Constants.API_SERVICE + Constants.CARD_STATUS_ENDPOINT
            print(">>>>><<<<<fwReqDATAJSON",req)
            fwReqJson = req['req_data']
            headers1 = CommonResponse.get_auth_head(CommonResponse,Constants.AUTH_TOKEN_URL,Constants.TOKEN_HEADER,1)
            print("header from authenticate : : : ",headers1)
            print("REQUESTS data",fwReqJson)
            print("REQUESTS data",type(fwReqJson))
            fwReqJson = json.dumps(fwReqJson)

            fisResp = CommonUtil.postrequestManager(URL,headers1,fwReqJson)
            print("End card status change execution validation>>>>>>???????????",str(fisResp))
            isValid = ValidateResp.validateObj(fisResp)
            return isValid
        except Exception as e:
            return {"resp_type":"FAILURE","resp_code":"9004","message":str(e)}


class CustUpdateApiImpl:
    def custUpdateValidation(req):
        try:
            URL = Constants.API_SERVICE + Constants.CUST_UPDATE_ENDPOINT
            print(">>>>><<<<<fwReqDATAJSON",req)
            fwReqJson = req['req_data']
            headers1 = CommonResponse.get_auth_head(CommonResponse,Constants.AUTH_TOKEN_URL,Constants.TOKEN_HEADER,1)
            print("header from authenticate : : : ",headers1)
            print("REQUESTS data",fwReqJson)
            print("REQUESTS data",type(fwReqJson))
            fwReqJson = json.dumps(fwReqJson)

            fisResp = CommonUtil.postrequestManager(URL,headers1,fwReqJson)
            print("End customer update validation>>>>>>???????????",str(fisResp))
            isValid = ValidateResp.validateObj(fisResp)
            return isValid
        except Exception as e:
            return {"resp_type":"FAILURE","resp_code":"9004","message":str(e)}

    def custUpdateExecution(req):
        try:
            URL = Constants.API_SERVICE + Constants.CUST_UPDATE_ENDPOINT
            print(">>>>><<<<<fwReqDATAJSON",req)
            fwReqJson = req['req_data']
            headers1 = CommonResponse.get_auth_head(CommonResponse,Constants.AUTH_TOKEN_URL,Constants.TOKEN_HEADER,1)
            print("header from authenticate : : : ",headers1)
            print("REQUESTS data",fwReqJson)
            print("REQUESTS data",type(fwReqJson))
            fwReqJson = json.dumps(fwReqJson)

            fisResp = CommonUtil.postrequestManager(URL,headers1,fwReqJson)
            print("End customer update execution>>>>>>???????????",str(fisResp))
            isValid = ValidateResp.validateObj(fisResp)
            return isValid
        except Exception as e:
            return {"resp_type":"FAILURE","resp_code":"9004","message":str(e)}




class CardReplacementApiImpl:
    def CardReplacementValidation(req):
        try:
            URL = Constants.API_SERVICE + Constants.CARD_REPLACEMENT_ENDPOINT
            print(">>>>><<<<<fwReqDATAJSON",req)
            fwReqJson = req['req_data']
            headers1 = CommonResponse.get_auth_head(CommonResponse,Constants.AUTH_TOKEN_URL,Constants.TOKEN_HEADER,1)
            print("header from authenticate : : : ",headers1)
            print("REQUESTS data",fwReqJson)
            print("REQUESTS data",type(fwReqJson))
            fwReqJson = json.dumps(fwReqJson)

            fisResp = CommonUtil.postrequestManager(URL,headers1,fwReqJson)
            print("End card replacement validation>>>>>>???????????",str(fisResp))
            isValid = ValidateResp.validateObj(fisResp)
            return isValid
        except Exception as e:
            return {"resp_type":"FAILURE","resp_code":"9004","message":str(e)}

    def CardReplacementExecution(req):
        try:
            URL = Constants.API_SERVICE + Constants.CARD_REPLACEMENT_ENDPOINT
            print(">>>>><<<<<fwReqDATAJSON",req)
            fwReqJson = req['req_data']
            headers1 = CommonResponse.get_auth_head(CommonResponse,Constants.AUTH_TOKEN_URL,Constants.TOKEN_HEADER,1)
            print("header from authenticate : : : ",headers1)
            print("REQUESTS data",fwReqJson)
            print("REQUESTS data",type(fwReqJson))
            fwReqJson = json.dumps(fwReqJson)

            fisResp = CommonUtil.postrequestManager(URL,headers1,fwReqJson)
            print("End card replacement execution>>>>>>???????????",str(fisResp))
            isValid = ValidateResp.validateObj(fisResp)
            return isValid
        except Exception as e:
            return {"resp_type":"FAILURE","resp_code":"9004","message":str(e)}

class CardIssueApiImpl:
    def CardIssueValidation(req):
        try:
            URL = Constants.API_SERVICE + Constants.CARD_ISSUE_ENDPOINT
            print(">>>>><<<<<fwReqDATAJSON",req)
            fwReqJson = req['req_data']
            headers1 = CommonResponse.get_auth_head(CommonResponse,Constants.AUTH_TOKEN_URL,Constants.TOKEN_HEADER,1)
            print("header from authenticate : : : ",headers1)
            print("REQUESTS data",fwReqJson)
            print("REQUESTS data",type(fwReqJson))
            fwReqJson = json.dumps(fwReqJson)

            fisResp = CommonUtil.postrequestManager(URL,headers1,fwReqJson)
            print("End card issue validation>>>>>>???????????",str(fisResp))
            isValid = ValidateResp.validateObj(fisResp)
            return isValid
        except Exception as e:
            return {"resp_type":"FAILURE","resp_code":"9004","message":str(e)}
        
    def CardIssueExecutuion(req):
        try:
            URL = Constants.API_SERVICE + Constants.CARD_ISSUE_ENDPOINT
            print(">>>>><<<<<fwReqDATAJSON",req)
            fwReqJson = req['req_data']
            headers1 = CommonResponse.get_auth_head(CommonResponse,Constants.AUTH_TOKEN_URL,Constants.TOKEN_HEADER,1)
            print("header from authenticate : : : ",headers1)
            print("REQUESTS data",fwReqJson)
            print("REQUESTS data",type(fwReqJson))
            fwReqJson = json.dumps(fwReqJson)

            fisResp = CommonUtil.postrequestManager(URL,headers1,fwReqJson)
            print("End card issue execution>>>>>>???????????",str(fisResp))
            isValid = ValidateResp.validateObj(fisResp)
            return isValid
        except Exception as e:
            return {"resp_type":"FAILURE","resp_code":"9004","message":str(e)}

class CardActivationApiImpl:
    def CardActivationValidation(req):
        try:
            URL = Constants.API_SERVICE + Constants.CARD_ACTIVE_ENDPOINT
            print(">>>>><<<<<fwReqDATAJSON",req)
            fwReqJson = req['req_data']
            headers1 = CommonResponse.get_auth_head(CommonResponse,Constants.AUTH_TOKEN_URL,Constants.TOKEN_HEADER,1)
            print("header from authenticate : : : ",headers1)
            print("REQUESTS data",fwReqJson)
            print("REQUESTS data",type(fwReqJson))
            fwReqJson = json.dumps(fwReqJson)

            fisResp = CommonUtil.postrequestManager(URL,headers1,fwReqJson)
            print("End card activation/linking validation>>>>>>???????????",str(fisResp))
            isValid = ValidateResp.validateObj(fisResp)
            return isValid
        except Exception as e:
            return {"resp_type":"FAILURE","resp_code":"9004","message":str(e)}

    def CardActivationExecutuion(req):
        try:
            URL = Constants.API_SERVICE + Constants.CARD_ACTIVE_ENDPOINT
            print(">>>>><<<<<fwReqDATAJSON",req)
            fwReqJson = req['req_data']
            headers1 = CommonResponse.get_auth_head(CommonResponse,Constants.AUTH_TOKEN_URL,Constants.TOKEN_HEADER,1)
            print("header from authenticate : : : ",headers1)
            print("REQUESTS data",fwReqJson)
            print("REQUESTS data",type(fwReqJson))
            fwReqJson = json.dumps(fwReqJson)

            fisResp = CommonUtil.postrequestManager(URL,headers1,fwReqJson)
            print("End card activation/linking execution>>>>>>???????????",str(fisResp))
            isValid = ValidateResp.validateObj(fisResp)
            return isValid
        except Exception as e:
            return {"resp_type":"FAILURE","resp_code":"9004","message":str(e)}

class CardUpgradationApiImpl:
    def CardUpgradationValidation(req):
        try:
            URL = Constants.API_SERVICE + Constants.CARD_UPGRADE_ENDPOINT
            print(">>>>><<<<<fwReqDATAJSON",req)
            fwReqJson = req['req_data']
            headers1 = CommonResponse.get_auth_head(CommonResponse,Constants.AUTH_TOKEN_URL,Constants.TOKEN_HEADER,1)
            print("header from authenticate : : : ",headers1)
            print("REQUESTS data",fwReqJson)
            print("REQUESTS data",type(fwReqJson))
            fwReqJson = json.dumps(fwReqJson)

            fisResp = CommonUtil.postrequestManager(URL,headers1,fwReqJson)
            print("End card upgradation validation>>>>>>???????????",str(fisResp))
            isValid = ValidateResp.validateObj(fisResp)
            return isValid
        except Exception as e:
            return {"resp_type":"FAILURE","resp_code":"9004","message":str(e)}

    def CardUpgradationExecution(req):
        try:
            URL = Constants.API_SERVICE + Constants.CARD_UPGRADE_ENDPOINT
            print(">>>>><<<<<fwReqDATAJSON",req)
            fwReqJson = req['req_data']
            headers1 = CommonResponse.get_auth_head(CommonResponse,Constants.AUTH_TOKEN_URL,Constants.TOKEN_HEADER,1)
            print("header from authenticate : : : ",headers1)
            print("REQUESTS data",fwReqJson)
            print("REQUESTS data",type(fwReqJson))
            fwReqJson = json.dumps(fwReqJson)

            fisResp = CommonUtil.postrequestManager(URL,headers1,fwReqJson)
            print("End card upgradation execution>>>>>>???????????",str(fisResp))
            isValid = ValidateResp.validateObj(fisResp)
            return isValid
        except Exception as e:
            return {"resp_type":"FAILURE","resp_code":"9004","message":str(e)}

class CustDetailEnquiryApiImpl:
    def CustDetailEnquiry(req):
        try:
            URL = Constants.API_SERVICE + Constants.CUST_DETAIL_ENQ_ENDPOINT
            print(">>>>><<<<<fwReqDATAJSON",req)
            fwReqJson = req['req_data']
            headers1 = CommonResponse.get_auth_head(CommonResponse,Constants.AUTH_TOKEN_URL,Constants.TOKEN_HEADER,1)
            print("header from authenticate : : : ",headers1)
            print("REQUESTS data",fwReqJson)
            print("REQUESTS data",type(fwReqJson))
            fwReqJson = json.dumps(fwReqJson)

            fisResp = CommonUtil.postrequestManager(URL,headers1,fwReqJson)
            print(" END CUST DETAIL ENQUIRY>>>>>???????????",str(fisResp))
            isValid = ValidateResp.validateObj(fisResp)
            return isValid
        except Exception as e:
            return {"resp_type":"FAILURE","resp_code":"9004","message":str(e)}

class VirtualCardApiImpl:
    def virtualCardValidation(req):
        try:
            URL = Constants.API_SERVICE + Constants.VIRTUALCARD_ENDPOINT
            print(">>>>><<<<<fwReqDATAJSON",req)
            fwReqJson = req['req_data']
            headers1 = CommonResponse.get_auth_head(CommonResponse,Constants.AUTH_TOKEN_URL,Constants.TOKEN_HEADER,1)
            print("header from authenticate : : : ",headers1)
            print("REQUESTS data",fwReqJson)
            print("REQUESTS data",type(fwReqJson))
            fwReqJson = json.dumps(fwReqJson)

            fisResp = CommonUtil.postrequestManager(URL,headers1,fwReqJson)
            print(" end virtual card validation>>>>>???????????",str(fisResp))
            isValid = ValidateResp.validateObj(fisResp)
            return isValid
        except Exception as e:
            return {"resp_type":"FAILURE","resp_code":"9004","message":str(e)}
    
    def virtualCardExecution(req):
        try:
            URL = Constants.API_SERVICE + Constants.VIRTUALCARD_ENDPOINT
            print(">>>>><<<<<fwReqDATAJSON",req)
            fwReqJson = req['req_data']
            headers1 = CommonResponse.get_auth_head(CommonResponse,Constants.AUTH_TOKEN_URL,Constants.TOKEN_HEADER,1)
            print("header from authenticate : : : ",headers1)
            print("REQUESTS data",fwReqJson)
            print("REQUESTS data",type(fwReqJson))
            fwReqJson = json.dumps(fwReqJson)

            fisResp = CommonUtil.postrequestManager(URL,headers1,fwReqJson)
            print(" end virtual card execution>>>>>???????????",str(fisResp))
            isValid = ValidateResp.validateObj(fisResp)
            return isValid
        except Exception as e:
            return {"resp_type":"FAILURE","resp_code":"9004","message":str(e)}
        
class Virtual2PhysicalApiImpl:
    def virtual2PhysicalValidation(req):
        try:
            URL = Constants.API_SERVICE + Constants.VIRTUAL_PHYSICAL_ENDPOINT
            print(">>>>><<<<<fwReqDATAJSON",req)
            fwReqJson = req['req_data']
            headers1 = CommonResponse.get_auth_head(CommonResponse,Constants.AUTH_TOKEN_URL,Constants.TOKEN_HEADER,1)
            print("header from authenticate : : : ",headers1)
            print("REQUESTS data",fwReqJson)
            print("REQUESTS data",type(fwReqJson))
            fwReqJson = json.dumps(fwReqJson)

            fisResp = CommonUtil.postrequestManager(URL,headers1,fwReqJson)
            print(" end virtual 2 physical card validation>>>>>???????????",str(fisResp))
            isValid = ValidateResp.validateObj(fisResp)
            return isValid
        except Exception as e:
            return {"resp_type":"FAILURE","resp_code":"9004","message":str(e)}
    
    def virtual2PhysicalExecution(req):
        try:
            URL = Constants.API_SERVICE + Constants.VIRTUAL_PHYSICAL_ENDPOINT
            print(">>>>><<<<<fwReqDATAJSON",req)
            fwReqJson = req['req_data']
            headers1 = CommonResponse.get_auth_head(CommonResponse,Constants.AUTH_TOKEN_URL,Constants.TOKEN_HEADER,1)
            print("header from authenticate : : : ",headers1)
            print("REQUESTS data",fwReqJson)
            print("REQUESTS data",type(fwReqJson))
            fwReqJson = json.dumps(fwReqJson)

            fisResp = CommonUtil.postrequestManager(URL,headers1,fwReqJson)
            print(" end virtual 2 physical card execution>>>>>???????????",str(fisResp))
            isValid = ValidateResp.validateObj(fisResp)
            return isValid
        except Exception as e:
            return {"resp_type":"FAILURE","resp_code":"9004","message":str(e)}

class AdjstAcntBlncApiImpl:
    def adjstAcntBlncValidation(req):
        try:
            URL = Constants.API_SERVICE + Constants.ADJST_BLNC_ENDPOINT
            print(">>>>><<<<<fwReqDATAJSON",req)
            fwReqJson = req['req_data']
            headers1 = CommonResponse.get_auth_head(CommonResponse,Constants.AUTH_TOKEN_URL,Constants.TOKEN_HEADER,1)
            print("header from authenticate : : : ",headers1)
            print("REQUESTS data",fwReqJson)
            print("REQUESTS data",type(fwReqJson))
            fwReqJson = json.dumps(fwReqJson)

            fisResp = CommonUtil.postrequestManager(URL,headers1,fwReqJson)
            print(" adjust balance validation>>>>>???????????",str(fisResp))
            isValid = ValidateResp.validateObj(fisResp)
            return isValid
        except Exception as e:
            return {"resp_type":"FAILURE","resp_code":"9004","message":str(e)}
    
    def adjstAcntBlncExecution(req):
        try:
            URL = Constants.API_SERVICE + Constants.ADJST_BLNC_ENDPOINT
            print(">>>>><<<<<fwReqDATAJSON",req)
            fwReqJson = req['req_data']
            headers1 = CommonResponse.get_auth_head(CommonResponse,Constants.AUTH_TOKEN_URL,Constants.TOKEN_HEADER,1)
            print("header from authenticate : : : ",headers1)
            print("REQUESTS data",fwReqJson)
            print("REQUESTS data",type(fwReqJson))
            fwReqJson = json.dumps(fwReqJson)

            fisResp = CommonUtil.postrequestManager(URL,headers1,fwReqJson)
            print(" adjust balance execution>>>>>???????????",str(fisResp))
            isValid = ValidateResp.validateObj(fisResp)
            return isValid
        except Exception as e:
            return {"resp_type":"FAILURE","resp_code":"9004","message":str(e)}

            
class AccountLoadApiImpl:
    def AccountLoadValidation(req):
        try:
            URL = Constants.API_SERVICE + Constants.ACCOUNT_LOAD_ENDPOINT
            print(">>>>><<<<<fwReqDATAJSON",req)
            fwReqJson = req['req_data']
            headers1 = CommonResponse.get_auth_head(CommonResponse,Constants.AUTH_TOKEN_URL,Constants.TOKEN_HEADER,1)
            print("header from authenticate : : : ",headers1)
            print("REQUESTS data",fwReqJson)
            print("REQUESTS data",type(fwReqJson))
            fwReqJson = json.dumps(fwReqJson)

            fisResp = CommonUtil.postrequestManager(URL,headers1,fwReqJson)
            print(" account load>>>>>???????????",str(fisResp))
            isValid = ValidateResp.validateObj(fisResp)
            return isValid
        except Exception as e:
            return {"resp_type":"FAILURE","resp_code":"9004","message":str(e)}

        
    
    def AccountLoadExecution(req):
        try:
            URL = Constants.API_SERVICE + Constants.ACCOUNT_LOAD_ENDPOINT
            print(">>>>><<<<<fwReqDATAJSON",req)
            fwReqJson = req['req_data']
            headers1 = CommonResponse.get_auth_head(CommonResponse,Constants.AUTH_TOKEN_URL,Constants.TOKEN_HEADER,1)
            print("header from authenticate : : : ",headers1)
            print("REQUESTS data",fwReqJson)
            print("REQUESTS data",type(fwReqJson))
            fwReqJson = json.dumps(fwReqJson)

            fisResp = CommonUtil.postrequestManager(URL,headers1,fwReqJson)
            print(" account load execution>>>>>???????????",str(fisResp))
            isValid = ValidateResp.validateObj(fisResp)
            return isValid
        except Exception as e:
            return {"resp_type":"FAILURE","resp_code":"9004","message":str(e)}

class SetPinApiImpl:
    def setPin(req):
        try:
            URL = Constants.API_SERVICE + Constants.SET_PIN_ENDPOINT
            print(">>>>><<<<<fwReqDATAJSON",req)
            fwReqJson = req['req_data']
            headers1 = CommonResponse.get_auth_head(CommonResponse,Constants.AUTH_TOKEN_URL,Constants.TOKEN_HEADER,1)
            print("header from authenticate : : : ",headers1)
            print("REQUESTS data",fwReqJson)
            print("REQUESTS data",type(fwReqJson))
            fwReqJson = json.dumps(fwReqJson)

            fisResp = CommonUtil.postrequestManager(URL,headers1,fwReqJson)
            print(" set pin >>>>>???????????",str(fisResp))
            isValid = ValidateResp.validateObj(fisResp)
            return isValid
        except Exception as e:
            return {"resp_type":"FAILURE","resp_code":"9004","message":str(e)}


class ChangePinApiImpl:
    def changePin(req):
        try:
            URL = Constants.API_SERVICE + Constants.CHANGE_PIN_ENDPOINT
            print(">>>>><<<<<fwReqDATAJSON",req)
            fwReqJson = req['req_data']
            headers1 = CommonResponse.get_auth_head(CommonResponse,Constants.AUTH_TOKEN_URL,Constants.TOKEN_HEADER,1)
            print("header from authenticate : : : ",headers1)
            print("REQUESTS data",fwReqJson)
            print("REQUESTS data",type(fwReqJson))
            fwReqJson = json.dumps(fwReqJson)

            fisResp = CommonUtil.postrequestManager(URL,headers1,fwReqJson)
            print(" change pin >>>>>???????????",str(fisResp))
            isValid = ValidateResp.validateObj(fisResp)
            return isValid
        except Exception as e:
            return {"resp_type":"FAILURE","resp_code":"9004","message":str(e)}

class VerifyPinExeApiImpl:
    def verifyPinExe(req):
        try:
            URL = Constants.API_SERVICE + Constants.VERIFY_PIN_ENDPOINT
            print(">>>>><<<<<fwReqDATAJSON",req)
            fwReqJson = req['req_data']
            headers1 = CommonResponse.get_auth_head(CommonResponse,Constants.AUTH_TOKEN_URL,Constants.TOKEN_HEADER,1)
            print("header from authenticate : : : ",headers1)
            print("REQUESTS data",fwReqJson)
            print("REQUESTS data",type(fwReqJson))
            fwReqJson = json.dumps(fwReqJson)

            fisResp = CommonUtil.postrequestManager(URL,headers1,fwReqJson)
            print(" verify pin >>>>>???????????",str(fisResp))
            isValid = ValidateResp.validateObj(fisResp)
            return isValid
        except Exception as e:
            return {"resp_type":"FAILURE","resp_code":"9004","message":str(e)}

class TnxEnqPinApiImpl:
    def tnxdetenq(req):
        try:
            URL = Constants.API_SERVICE + Constants.TNX_DET_ENQ_ENDPINT
            print(">>>>><<<<<fwReqDATAJSON",req)
            fwReqJson = req['req_data']
            headers1 = CommonResponse.get_auth_head(CommonResponse,Constants.AUTH_TOKEN_URL,Constants.TOKEN_HEADER,1)
            print("header from authenticate : : : ",headers1)
            print("REQUESTS data",fwReqJson)
            print("REQUESTS data",type(fwReqJson))
            fwReqJson = json.dumps(fwReqJson)

            fisResp = CommonUtil.postrequestManager(URL,headers1,fwReqJson)
            print(" TRANSACTION DETAIL ENQUIRY >>>>>???????????",str(fisResp))
            isValid = ValidateResp.validateObj(fisResp)
            return isValid
        except Exception as e:
            return {"resp_type":"FAILURE","resp_code":"9004","message":str(e)}





class GiftCardApiImpl:
    def GiftCardValidation(req):
        try:
            URL = Constants.API_SERVICE + Constants.GIFT_CARD_ENDPOINT
            print(">>>>><<<<<fwReqDATAJSON",req)
            fwReqJson = req['req_data']
            headers1 = CommonResponse.get_auth_head(CommonResponse,Constants.AUTH_TOKEN_URL,Constants.TOKEN_HEADER,1)
            print("header from authenticate : : : ",headers1)
            print("REQUESTS data",fwReqJson)
            print("REQUESTS data",type(fwReqJson))
            fwReqJson = json.dumps(fwReqJson)

            fisResp = CommonUtil.postrequestManager(URL,headers1,fwReqJson)
            print(" GIFT CARD VALIDATION>>>>???????????",str(fisResp))
            isValid = ValidateResp.validateObj(fisResp)
            return isValid
        except Exception as e:
            return {"resp_type":"FAILURE","resp_code":"9004","message":str(e)}


        
    def GiftCardExecution(req):
        try:
            URL = Constants.API_SERVICE + Constants.GIFT_CARD_ENDPOINT
            print(">>>>><<<<<fwReqDATAJSON",req)
            fwReqJson = req['req_data']
            headers1 = CommonResponse.get_auth_head(CommonResponse,Constants.AUTH_TOKEN_URL,Constants.TOKEN_HEADER,1)
            print("header from authenticate : : : ",headers1)
            print("REQUESTS data",fwReqJson)
            print("REQUESTS data",type(fwReqJson))
            fwReqJson = json.dumps(fwReqJson)

            fisResp = CommonUtil.postrequestManager(URL,headers1,fwReqJson)
            print(" GIFT CARD EXECUTION>>>>???????????",str(fisResp))
            isValid = ValidateResp.validateObj(fisResp)
            return isValid
        except Exception as e:
            return {"resp_type":"FAILURE","resp_code":"9004","message":str(e)}


    
class CvvVerificationApiImpl:
    def CvvVerification(req):
        try:
            URL = Constants.API_SERVICE + Constants.CVV_VERIFICATION_ENDPOINT
            print(">>>>><<<<<fwReqDATAJSON",req)
            fwReqJson = req['req_data']
            headers1 = CommonResponse.get_auth_head(CommonResponse,Constants.AUTH_TOKEN_URL,Constants.TOKEN_HEADER,1)
            print("header from authenticate : : : ",headers1)
            print("REQUESTS data",fwReqJson)
            print("REQUESTS data",type(fwReqJson))
            fwReqJson = json.dumps(fwReqJson)

            fisResp = CommonUtil.postrequestManager(URL,headers1,fwReqJson)
            print(" CVV VALIDATION>>>>???????????",str(fisResp))
            isValid = ValidateResp.validateObj(fisResp)
            return isValid
        except Exception as e:
            return {"resp_type":"FAILURE","resp_code":"9004","message":str(e)}


class CardDetailsEnqApiImpl:
    def CardDetailsEn(req):
        try:
            URL = Constants.API_SERVICE + Constants.CARD_DETAILS_ENQ_ENDPOINT
            print(">>>>><<<<<fwReqDATAJSON",req)
            fwReqJson = req['req_data']
            headers1 = CommonResponse.get_auth_head(CommonResponse,Constants.AUTH_TOKEN_URL,Constants.TOKEN_HEADER,1)
            print("header from authenticate : : : ",headers1)
            print("REQUESTS data",fwReqJson)
            print("REQUESTS data",type(fwReqJson))
            fwReqJson = json.dumps(fwReqJson)

            fisResp = CommonUtil.postrequestManager(URL,headers1,fwReqJson)
            print(" CARD_DETAILS_ENQ>>>>???????????",str(fisResp))
            isValid = ValidateResp.validateObj(fisResp)
            return isValid
        except Exception as e:
            return {"resp_type":"FAILURE","resp_code":"9004","message":str(e)}

class ChannelUpateApiImpl:
    def ChannelUpadte(req):
        try:
            URL = Constants.API_SERVICE + Constants.CHANNEL_UPDATE_ENDPOINT
            print(">>>>><<<<<fwReqDATAJSON",req)
            fwReqJson = req['req_data']
            headers1 = CommonResponse.get_auth_head(CommonResponse,Constants.AUTH_TOKEN_URL,Constants.TOKEN_HEADER,1)
            print("header from authenticate : : : ",headers1)
            print("REQUESTS data",fwReqJson)
            print("REQUESTS data",type(fwReqJson))
            fwReqJson = json.dumps(fwReqJson)

            fisResp = CommonUtil.postrequestManager(URL,headers1,fwReqJson)
            print(" CHANNEL UPDATE>>>>???????????",str(fisResp))
            isValid = ValidateResp.validateObj(fisResp)
            return isValid
        except Exception as e:
            return {"resp_type":"FAILURE","resp_code":"9004","message":str(e)}


class LimitUpateApiImpl:
    def LimitUpadte(req):
        try:
            URL = Constants.API_SERVICE + Constants.LIMIT_UPDATE_ENDPOINT
            print(">>>>><<<<<fwReqDATAJSON",req)
            fwReqJson = req['req_data']
            headers1 = CommonResponse.get_auth_head(CommonResponse,Constants.AUTH_TOKEN_URL,Constants.TOKEN_HEADER,1)
            print("header from authenticate : : : ",headers1)
            print("REQUESTS data",fwReqJson)
            print("REQUESTS data",type(fwReqJson))
            fwReqJson = json.dumps(fwReqJson)

            fisResp = CommonUtil.postrequestManager(URL,headers1,fwReqJson)
            print(" LIMIT UPDATE>>>>???????????",str(fisResp))
            isValid = ValidateResp.validateObj(fisResp)
            return isValid
        except Exception as e:
            return {"resp_type":"FAILURE","resp_code":"9004","message":str(e)}

class LimitChannelUpdateApiImpl:
    def LimitChannelupadte(req):
        try:
            URL = Constants.API_SERVICE + Constants.LIMIT_CHANNEL_UPDATE_ENDPOINT
            print(">>>>><<<<<fwReqDATAJSON",req)
            fwReqJson = req['req_data']
            headers1 = CommonResponse.get_auth_head(CommonResponse,Constants.AUTH_TOKEN_URL,Constants.TOKEN_HEADER,1)
            print("header from authenticate : : : ",headers1)
            print("REQUESTS data",fwReqJson)
            print("REQUESTS data",type(fwReqJson))
            fwReqJson = json.dumps(fwReqJson)

            fisResp = CommonUtil.postrequestManager(URL,headers1,fwReqJson)
            print(" LIMIT CHANNEL UPDATE>>>>???????????",str(fisResp))
            isValid = ValidateResp.validateObj(fisResp)
            return isValid
        except Exception as e:
            return {"resp_type":"FAILURE","resp_code":"9004","message":str(e)}

    


    



        









    


  

