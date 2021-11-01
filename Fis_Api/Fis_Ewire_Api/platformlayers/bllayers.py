import json,sys
import linecache
import logging
import traceback
from flask import request
from Fis_Ewire_Api.platformlayers.constantlayer import AuthApiImpl,CardOrderApiImpl,CardCancelApiImpl,CardEnqiuryApiImpl,CardStatusApiImpl,CustUpdateApiImpl,CardReplacementApiImpl,CardIssueApiImpl,CardActivationApiImpl,CardUpgradationApiImpl,CustDetailEnquiryApiImpl,VirtualCardApiImpl,Virtual2PhysicalApiImpl,AdjstAcntBlncApiImpl,AccountLoadApiImpl,ChangePinApiImpl,SetPinApiImpl,VerifyPinExeApiImpl,TnxEnqPinApiImpl,GiftCardApiImpl,CvvVerificationApiImpl,CardDetailsEnqApiImpl,ChannelUpateApiImpl,LimitUpateApiImpl,LimitChannelUpdateApiImpl


logging.basicConfig()
logger=logging.getLogger()
logger.setLevel(logging.DEBUG)


class AuthApiHandler:
    def authApiMapper(req):
        try:
            authObj = AuthApiImpl            
            print("=======================returning authObj to view=================")
            print(req.data.decode('utf-8'))
            respObj =  authObj.authenticateMethod(req.data.decode('utf-8').replace("'",'"'))
            # print(">>>>>>RESP OBJ "+ str(respObj['access_token']))
            return respObj
            
        except Exception as e:
          
           print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)

class CardOrderHandler:
    def cardOrderMapper(req):
        print("API MAPPER CALL RECIVED")

        try:
            # reqDataJson = json.loads(request.data.decode('utf-8'))
            # reqDataJson = request.get_json()
            reqDataJson = json.loads(req.data.decode('utf-8'))
            print("=================cardOrderMapper=============")
            print("API MAPPER CALL RECIVED, REQ DATA",reqDataJson)
            
            cardOrderObj = CardOrderApiImpl

            if reqDataJson['apiname'] == "CARD_VAL":
                respObj = cardOrderObj.cardOrderValidation(reqDataJson)
                return respObj

            elif reqDataJson['apiname'] == "CARD_EXE":
                respObj = cardOrderObj.cardOrderExecution(reqDataJson)
                return respObj
          
        except Exception as e:          
            print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
            return {"Error":str(e)}

class CardCancelHandler:
    def cardCancelMapper(req):
        print("Card Cancel Api method called")
        try:
            reqDataJson = json.loads(req.data.decode('utf-8'))
            print("=================cardOrderMapper=============")
            print("API MAPPER CALL RECIVED, REQ DATA",reqDataJson)
            
            cardCancelObj = CardCancelApiImpl

            if reqDataJson['apiname'] == "CARD_CNCL_VAL":
                respObj = cardCancelObj.cardCancelValidation(reqDataJson)
                return respObj

            elif reqDataJson['apiname'] == "CARD_CNCL_EXE":
                respObj = cardCancelObj.cardCancelExecution(reqDataJson)
                return respObj
          
        except Exception as e:          
            print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
            return {"Error":str(e)}

class CardEnquiryHandler:
    def cardEnquiryMapper(req):
        print("Card enquiry Api method called")
        try:
            reqDataJson = json.loads(req.data.decode('utf-8'))
            print("=================cardEnquiryMapper=============")
            print("API MAPPER CALL RECIVED, REQ DATA",reqDataJson)
            
            cardEquiryObj = CardEnqiuryApiImpl

            if reqDataJson['apiname'] == "CARD_CNCL_VAL":
                respObj =  cardEquiryObj.cardEnquiryValidation(reqDataJson)
                return respObj

            elif reqDataJson['apiname'] == "CARD_CNCL_EXE":
                respObj =  cardEquiryObj.cardEnquiryExecution(reqDataJson)
                return respObj
          
        except Exception as e:          
            print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
            return {"Error":str(e)}

class CardStatusHandler:
    def cardStatusMapper(req):
        print("Card status Api method called")
        try:
            reqDataJson = json.loads(req.data.decode('utf-8'))
            print("=================cardEnquiryMapper=============")
            print("API STATUS MAPPER CALL RECIVED, REQ DATA",reqDataJson)
            
            cardStatusObj = CardStatusApiImpl

            if reqDataJson['apiname'] == "CARD_CNCL_VAL":
                respObj =  cardStatusObj.cardStatusValidation(reqDataJson)
                return respObj

            elif reqDataJson['apiname'] == "CARD_CNCL_EXE":
                respObj =  cardStatusObj.cardStatusExecution(reqDataJson)
                return respObj
          
        except Exception as e:          
            print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
            return {"Error":str(e)}

class CustUpdateHandler:
    def custUpdateMapper(req):
        print("Card update Api method called")
        try:
            reqDataJson = json.loads(req.data.decode('utf-8'))
            print("=================cardEnquiryMapper=============")
            print("API CUSTOMER UPDATE MAPPER CALL RECIVED, REQ DATA",reqDataJson)
            
            cardUpdateObj = CustUpdateApiImpl

            if reqDataJson['apiname'] == "CUST_UPDATE_VAL":
                respObj =  cardUpdateObj.custUpdateValidation(reqDataJson)
                return respObj

            elif reqDataJson['apiname'] == "CUST_UPDATE_EXE":
                respObj =  cardUpdateObj.custUpdateExecution(reqDataJson)
                return respObj
          
        except Exception as e:          
            print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
            return {"Error":str(e)}


#CARD REPLACEMENT
class CardReplacementHandler:
    def cardReplacementMapper(req):
        print("Card Replacement Api method called")
        try:
            reqDataJson = json.loads(req.data.decode('utf-8'))
            print("=================cardReplacementMapper=============")
            print("API CARD REPLACEMENT MAPPER CALL RECIVED, REQ DATA",reqDataJson)
            
            cardReplacementObj = CardReplacementApiImpl

            if reqDataJson['apiname'] == "CARD_REPLCMNT_VAL":
                respObj =   cardReplacementObj.CardReplacementValidation(reqDataJson)
                return respObj

            elif reqDataJson['apiname'] == "CARD_REPLCMNT_EXE":
                respObj =   cardReplacementObj.CardReplacementExecution(reqDataJson)
                return respObj
          
        except Exception as e:          
            print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
            return {"Error":str(e)}

class CardIssueHandler:
    def cardIssueMapper(req):
        print("Card issue Api method called")
        try:
            reqDataJson = json.loads(req.data.decode('utf-8'))
            print("=================cardReplacementMapper=============")
            print("API CARD ISSUE MAPPER CALL RECIVED, REQ DATA",reqDataJson)
            
            cardReplacementObj = CardIssueApiImpl

            if reqDataJson['apiname'] == "CARD_ISSUE_VAL":
                respObj =   cardReplacementObj.CardIssueValidation(reqDataJson)
                return respObj

            elif reqDataJson['apiname'] == "CARD_ISSUE_EXE":
                respObj =   cardReplacementObj.CardIssueExecutuion(reqDataJson)
                return respObj
          
        except Exception as e:          
            print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
            return {"Error":str(e)}

class CardActivationHandler:
    def cardActivationMapper(req):
        print("Card activation Api method called")
        try:
            reqDataJson = json.loads(req.data.decode('utf-8'))
            print("=================cardActivationMapper=============")
            print("API ACTIVATION MAPPER CALL RECIVED, REQ DATA",reqDataJson)
            
            cardActivationObj = CardActivationApiImpl

            if reqDataJson['apiname'] == "CARD_ACT_VAL":
                respObj =   cardActivationObj.CardActivationValidation(reqDataJson)
                return respObj

            elif reqDataJson['apiname'] == "CARD_ACT_EXE":
                respObj =   cardActivationObj.CardActivationExecutuion(reqDataJson)
                return respObj
          
        except Exception as e:          
            print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
            return {"Error":str(e)}

class CardUpgradationHandler:
    def cardUpgradationMapper(req):
        print("Card upgradation Api method called")
        try:
            reqDataJson = json.loads(req.data.decode('utf-8'))
            print("=================cardUpgradationMapper=============")
            print("API UPGRADATION MAPPER CALL RECIVED, REQ DATA",reqDataJson)
            
            cardUpgradationObj = CardUpgradationApiImpl

            if reqDataJson['apiname'] == "CARD_UPGRADE_VAL":
                respObj =   cardUpgradationObj.CardUpgradationValidation(reqDataJson)
                return respObj

            elif reqDataJson['apiname'] == "CARD_UPGRADE_EXE":
                respObj =   cardUpgradationObj.CardUpgradationExecution(reqDataJson)
                return respObj
          
        except Exception as e:          
            print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
            return {"Error":str(e)}

class CustDetailEnquiryHandler:
    def CustDetailEnquiryMapper(req):
        print("Customer detail enquiry Api method called")
        try:
            reqDataJson = json.loads(req.data.decode('utf-8'))
            print("=================customer detail enquiry Mapper=============")
            print("API customer detail enquiry MAPPER CALL RECIVED, REQ DATA",reqDataJson)
            
            CustDetailEnquiryObj = CustDetailEnquiryApiImpl

            if reqDataJson['apiname'] == "CUST_DET_ENQ":
                respObj =   CustDetailEnquiryObj.CustDetailEnquiry(reqDataJson)
                return respObj

        except Exception as e:          
            print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
            return {"Error":str(e)}

class VirtualCardHandler:
    def virtualCardMapper(req):
        print("Virtual Api method called")
        try:
            reqDataJson = json.loads(req.data.decode('utf-8'))
            print("=================VirtualCardMapper=============")
            print("API VIRTUAL CARD MAPPER CALL RECIVED, REQ DATA",reqDataJson)
            
            virtualCardObj = VirtualCardApiImpl

            if reqDataJson['apiname'] == "VIRTUAL_CARD_VAL":
                respObj =   virtualCardObj.virtualCardValidation(reqDataJson)
                return respObj

            elif reqDataJson['apiname'] == "VIRTUAL_CARD_EXE":
                respObj =   virtualCardObj.virtualCardExecution(reqDataJson)
                return respObj
          
        except Exception as e:          
            print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
            return {"Error":str(e)}

class VirtualToPhysicalHandler:
    def virtualToPhysicalMapper(req):
        print("Virtual To Physical Card method called")
        try:
            reqDataJson = json.loads(req.data.decode('utf-8'))
            print("=================VirtualCardMapper=============")
            print("API VIRTUAL TO PHYSICAL CARD MAPPER CALL RECIVED, REQ DATA",reqDataJson)
            
            virtualToPhysicalObj = Virtual2PhysicalApiImpl

            if reqDataJson['apiname'] == "VIRTUAL_PHYSCL_CARD":
                respObj =   virtualToPhysicalObj.virtual2PhysicalValidation(reqDataJson)
                return respObj

            elif reqDataJson['apiname'] == "VIRTUAL_PHYSCL_CARD_EXE":
                respObj =   virtualToPhysicalObj.virtual2PhysicalExecution(reqDataJson)
                return respObj
          
        except Exception as e:          
            print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
            return {"Error":str(e)}

class AdjsAccBlncHandler:
     def adjsAccBlncMapper(req):
        print("Account Balance Adjust called")
        try:
            reqDataJson = json.loads(req.data.decode('utf-8'))
            print("=================accAdjsBlncMapper Mapper=============")
            print("API ADJUST ACCNT BALANCE MAPPER CALL RECIVED, REQ DATA",reqDataJson)
            
            adjstacntblncObj = AdjstAcntBlncApiImpl

            if reqDataJson['apiname'] == "ADJST_ACC_BLNC_VAL":
                respObj =   adjstacntblncObj.adjstAcntBlncValidation(reqDataJson)
                return respObj

            elif reqDataJson['apiname'] == "ADJST_ACC_BLNC_EXE":
                respObj =   adjstacntblncObj.adjstAcntBlncExecution(reqDataJson)
                return respObj
          
        except Exception as e:          
            print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
            return {"Error":str(e)}


class AccountLoadHandler:
     def AccLoadMapper(req):
        print("Account Load")
        try:
            reqDataJson = json.loads(req.data.decode('utf-8'))
            print("=================account load Mapper=============")
            print("API ACCNT LOAD MAPPER CALL RECIVED, REQ DATA",reqDataJson)
            
            accloadObj = AccountLoadApiImpl

            if reqDataJson['apiname'] == "ACC_LOAD_VAL":
                respObj =   accloadObj.AccountLoadValidation(reqDataJson)
                return respObj

            elif reqDataJson['apiname'] == "ACC_LOAD_EXE":
                respObj =   accloadObj.AccountLoadExecution(reqDataJson)
                return respObj
          
        except Exception as e:          
            print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
            return {"Error":str(e)}


class SetPinHandler:
    def SetPinMapper(req):
        print("Set Pin")
        try:
            reqDataJson = json.loads(req.data.decode('utf-8'))
            print("=================account load Mapper=============")
            print("API SET PIN MAPPER CALL RECIVED, REQ DATA",reqDataJson)
            
            accloadObj = SetPinApiImpl

            if reqDataJson['apiname'] == "SET_PIN":
                respObj =   accloadObj.setPin(reqDataJson)
                return respObj

        except Exception as e:          
            print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
            return {"Error":str(e)}

class ChangePinHandler:
    def ChangePinMapper(req):
        print("Change Pin")
        try:
            reqDataJson = json.loads(req.data.decode('utf-8'))
            print("=================Change Pin Mapper=============")
            print("API CHANGE PIN MAPPER CALL RECIVED, REQ DATA",reqDataJson)
            
            accloadObj = ChangePinApiImpl

            if reqDataJson['apiname'] == "CHANGE_PIN":
                respObj =   accloadObj.changePin(reqDataJson)
                return respObj

        except Exception as e:          
            print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
            return {"Error":str(e)}

class VerifyPinExeHandler:
    def verifyPinExeMapper(req):
        print("Verify Pin")
        try:
            reqDataJson = json.loads(req.data.decode('utf-8'))
            print("=================VerifyPinMapper=============")
            print("API VERIFY PIN MAPPER CALL RECIVED, REQ DATA",reqDataJson)
            
            verifyObj = VerifyPinExeApiImpl

            if reqDataJson['apiname'] == "VERIFY_PIN_EXE":
                respObj =   verifyObj.verifyPinExe(reqDataJson)
                return respObj

        except Exception as e:          
            print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
            return {"Error":str(e)}


class txndetenqHandler:
    def txndetenqPinMapper(req):
        print("transaction enquiry pin")
        try:
            reqDataJson = json.loads(req.data.decode('utf-8'))
            print("=================VerifyPinMapper=============")
            print("API TRANSACTION DETAILS MAPPER CALL RECIVED, REQ DATA",reqDataJson)
            
            TnxDetENQObj = TnxEnqPinApiImpl

            if reqDataJson['apiname'] == "TXN_DET_ENQ":
                respObj =   TnxDetENQObj.tnxdetenq(reqDataJson)
                return respObj

        except Exception as e:          
            print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
            return {"Error":str(e)}


class GiftCardHandler:
     def GiftCardMapper(req):
        print("Account Load")
        try:
            reqDataJson = json.loads(req.data.decode('utf-8'))
            print("=================account load Mapper=============")
            print("API ADJUST ACCNT BALANCE MAPPER CALL RECIVED, REQ DATA",reqDataJson)
            
            accloadObj = GiftCardApiImpl

            if reqDataJson['apiname'] == "GIFT_CARD_VAL":
                respObj =   accloadObj.GiftCardValidation(reqDataJson)
                return respObj

            elif reqDataJson['apiname'] == "GIFT_CARD_EXE":
                respObj =   accloadObj.GiftCardExecution(reqDataJson)
                return respObj
          
        except Exception as e:          
            print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
            return {"Error":str(e)}



class CvvVerificationHandler:
    def CvvVerificationdMapper(req):
        print("Verify Pin")
        try:
            reqDataJson = json.loads(req.data.decode('utf-8'))
            print("=================CVV VERIFICATION=============")
            print("API VERIFY CVV MAPPER CALL RECIVED, REQ DATA",reqDataJson)
            
            verifyObj = CvvVerificationApiImpl

            if reqDataJson['apiname'] == "CVV2_VERFCTN":
                respObj =   verifyObj.CvvVerification(reqDataJson)
                return respObj

        except Exception as e:          
            print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
            return {"Error":str(e)}

class CardDetailEnqHandler:
    def CardDetailsEnqMapper(req):
        print("card details enquiry")
        try:
            reqDataJson = json.loads(req.data.decode('utf-8'))
            print("=================CARD DETAILS ENQUIRY=============")
            print("API CARD DETAILS MAPPER CALL RECIVED, REQ DATA",reqDataJson)
            
            verifyObj = CardDetailsEnqApiImpl

            if reqDataJson['apiname'] == "CARD_DET_ENQ":
                respObj =   verifyObj.CardDetailsEnq(reqDataJson)
                return respObj

        except Exception as e:          
            print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
            return {"Error":str(e)}

class channelupdateHandler:
    def ChannelUpdateMapper(req):
        print("channel update")
        try:
            reqDataJson = json.loads(req.data.decode('utf-8'))
            print("=================Channel update=============")
            print("API CHANNEL UPDATE MAPPER CALL RECIVED, REQ DATA",reqDataJson)
            
            verifyObj = ChannelUpateApiImpl

            if reqDataJson['apiname'] == "CHANNEL_UPDT":
                respObj =   verifyObj.ChannelUpadte(reqDataJson)
                return respObj

        except Exception as e:          
            print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
            return {"Error":str(e)}




class LimitUpdateHandler:
    def LimitUpdateMapper(req):
        print("limit update")
        try:
            reqDataJson = json.loads(req.data.decode('utf-8'))
            print("=================Channel update=============")
            print("API LIMIT UPDATE MAPPER CALL RECIVED, REQ DATA",reqDataJson)
            
            verifyObj = LimitUpateApiImpl

            if reqDataJson['apiname'] == "LIMIT_UPDT":
                respObj =   verifyObj.LimitUpadte(reqDataJson)
                return respObj

        except Exception as e:          
            print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
            return {"Error":str(e)}




class LimitChannelUpdateHandler:
    def LimitChannelUpdateMapper(req):
        print("CardDetailEnqMapper")
        try:
            reqDataJson = json.loads(req.data.decode('utf-8'))
            print("=================Channel update=============")
            print("API  MAPPER CALL RECIVED, REQ DATA",reqDataJson)
            
            verifyObj = LimitChannelUpdateApiImpl

            if reqDataJson['apiname'] == "LIMIT_CHANNEL_UPDT":
                respObj =   verifyObj.LimitChannelupadte(reqDataJson)
                return respObj

        except Exception as e:          
            print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
            return {"Error":str(e)}




