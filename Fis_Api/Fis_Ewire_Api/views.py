from flask import Flask,request
import json
from Fis_Ewire_Api import app
from Fis_Ewire_Api.platformlayers.bllayers import AuthApiHandler,CardOrderHandler,CardCancelHandler,CardEnquiryHandler,CardStatusHandler,CustUpdateHandler,CardReplacementHandler,CardIssueHandler,CardActivationHandler,CardUpgradationHandler,CustDetailEnquiryHandler,VirtualCardHandler,VirtualToPhysicalHandler,AdjsAccBlncHandler,AccountLoadHandler,SetPinHandler,ChangePinHandler, VerifyPinExeHandler,txndetenqHandler,GiftCardHandler,CvvVerificationHandler,CardDetailEnqHandler,channelupdateHandler,LimitUpdateHandler,LimitChannelUpdateHandler

baseUrl = '/api/v1/ewire/fis' 


@app.route('/', methods = ['GET'])
def response():
    return "API:FIS RUNNING....V.1.0.0"

# from ewire_fis.authenticate import token_required
@app.route(baseUrl+'/tokenAccess', methods = ['GET','POST'])
def authResponse():
    authObj = AuthApiHandler
    print("authentication view Final")
    temp =  authObj.authApiMapper(request)
    # Constants.ACCESS_TOKEN = str(temp['access_token'])
     
    return temp

#Card Order – Non-perso (Insta-kit)
@app.route(baseUrl+'/cardorder', methods = ['POST'])
def cardorder():
    print("enterd card order views")
    print("///////////////////////////////")
    print("request",request)
    print("///////////////////////////////")

    cardOrderRespObj = CardOrderHandler
    temp = cardOrderRespObj.cardOrderMapper(request)
    return temp

#card cancellation

@app.route(baseUrl+'/cardcancel', methods = ['POST'])
def cardcancel():
    cardCancelRespObj = CardCancelHandler
    temp = cardCancelRespObj.cardCancelMapper(request)
    return temp

#card enquiry
@app.route(baseUrl+'/cardenquiry', methods = ['POST'])
def cardenq():
    cardEnquiryRespObj = CardEnquiryHandler
    temp = cardEnquiryRespObj.cardEnquiryMapper(request)
    return temp

#card status
@app.route(baseUrl+'/cardstatus', methods = ['POST'])
def cardstatus():
    cardStatusRespObj = CardStatusHandler
    temp = cardStatusRespObj.cardStatusMapper(request)
    return temp

#customer update
@app.route(baseUrl+'/custupdate', methods = ['POST'])
def custupdate():
    custUpdateRespObj = CustUpdateHandler
    temp = custUpdateRespObj.custUpdateMapper(request)
    return temp

# card replacement

@app.route(baseUrl+'/cardreplacement', methods = ['POST'])
def cardreplacement():
    cardReplacementRespObj = CardReplacementHandler
    temp = cardReplacementRespObj.cardReplacementMapper(request)
    return temp

#card issue exe
@app.route(baseUrl+'/cardissue', methods = ['POST'])
def cardissue():
    cardIssueRespObj = CardIssueHandler
    temp = cardIssueRespObj.cardIssueMapper(request)
    return temp

# card activation validation
@app.route(baseUrl+'/cardactivation', methods = ['POST'])
def cardactivate():
    cardActivationRespObj = CardActivationHandler
    temp = cardActivationRespObj.cardActivationMapper(request)
    return temp

# Card Upgrade
@app.route(baseUrl+'/cardupgrade', methods = ['POST'])
def cardupgradation():
    cardUpgradationRespObj = CardUpgradationHandler
    temp = cardUpgradationRespObj.cardUpgradationMapper(request)
    return temp 

# customer detail enquiry
@app.route(baseUrl+'/custdetailenq', methods = ['POST'])
def custdetailenq():
    custdetailenquiryRespObj = CustDetailEnquiryHandler
    temp = custdetailenquiryRespObj.CustDetailEnquiryMapper(request)
    return temp 

# virtual  card  creation
@app.route(baseUrl+'/virtualcard', methods = ['POST'])
def virtualcard_create():
    virtualCardRespObj = VirtualCardHandler
    temp = virtualCardRespObj.virtualCardMapper(request)
    return temp 

# virtual to physical  card  
@app.route(baseUrl+'/virtualtophysical', methods = ['POST'])
def virtual_physical_card():
    virtualToPhysicalRespObj = VirtualToPhysicalHandler
    temp = virtualToPhysicalRespObj.virtualToPhysicalMapper(request)
    return temp

# adjust account balance 
@app.route(baseUrl+'/adjaccbalance', methods = ['POST'])
def accadjs_blc():
    adjsaccblncRespObj = AdjsAccBlncHandler
    temp = adjsaccblncRespObj.adjsAccBlncMapper(request)
    return temp
    
# load account  

@app.route(baseUrl+'/accountload', methods = ['POST'])
def account_load():
    accountloadRespObj = AccountLoadHandler
    temp = accountloadRespObj.AccLoadMapper(request)
    return temp

@app.route(baseUrl+'/setpin', methods = ['POST'])
def set_pin():
    setpinRespObj = SetPinHandler
    temp = setpinRespObj.SetPinMapper(request)
    return temp


@app.route(baseUrl+'/changepin', methods = ['POST'])
def change_pin():
    changepinRespObj = ChangePinHandler
    temp = changepinRespObj.ChangePinMapper(request)
    return temp

@app.route(baseUrl+'/verifypin', methods = ['POST'])
def verify_pin():
    verifypinRespObj = VerifyPinExeHandler
    temp = verifypinRespObj.verifyPinExeMapper(request)
    return temp

@app.route(baseUrl+'/txndetenq', methods = ['POST'])
def txn_detenq():
    txndetenqRespObj = txndetenqHandler
    temp = txndetenqRespObj.txndetenqPinMapper(request)
    return temp


@app.route(baseUrl+'/giftcard', methods = ['POST'])
def gift_card():
    giftcardRespObj = GiftCardHandler
    temp = giftcardRespObj.GiftCardMapper(request)
    return temp


@app.route(baseUrl+'/cvv', methods = ['POST'])
def cvv_verification():
    cvvverificationRespObj = CvvVerificationHandler
    temp = cvvverificationRespObj.CvvVerificationdMapper(request)
    return temp

@app.route(baseUrl+'/carddetailenq', methods = ['POST'])
def card_det_enq():
    carddetailsenqRespObj = CardDetailEnqHandler
    temp = carddetailsenqRespObj.CardDetailsEnqMapper(request)
    return temp

@app.route(baseUrl+'/channel_update', methods = ['POST'])
def channel_update():
    channelupdateRespObj = channelupdateHandler
    temp = channelupdateRespObj.ChannelUpdateMapper(request)
    return temp


@app.route(baseUrl+'/limit_update', methods = ['POST'])
def limit_update():
    limitupdateRespObj = LimitUpdateHandler
    temp = limitupdateRespObj.LimitUpdateMapper(request)
    return temp


@app.route(baseUrl+'/limitchannelupdate', methods = ['POST'])
def limitchannelupdate():
    limitchannelupdateRespObj = LimitChannelUpdateHandler
    temp = limitchannelupdateRespObj.LimitChannelUpdateMapper(request)
    return temp

