from logging import log
# from bcore.cruds import logout


logginServer = "172.20.236.55:8003"
logginHeaderz = {"Content-Type":"application/json"}
logginReqType =''
logginMethodType = "POST"
logginEndpoints = '/logrequest'

loggrRespdatasuccess = {
                    "status":200,
                    "respType":"Success",
                    "response": "Successfully Logged"
}

loggrRespdatafail = {
                    "status":500,
                    "respType":"Failure",
                    "response": "Failure in  Logging"
}



hashDataRespSuccess = {
                    "status":200,
                    "respType":"Success",
                    "response": "Successfully Logged"
}

hashDataRespdataFail = {
                    "status":500,
                    "respType":"Failure",
                    "response": "Failure in  Logging"
}

validateRespDataSuccess = {
    "respType":"Success",
    "response":"Successfully Logged"
}

validateRespDataFail = {
    "respType":"Failure",
    "response":"Failure in Logging"
}


successResp = {
    "resp_type":"SUCCESS",
    "status":"SUCCESS",
    "resp_code":"200",

}

failureResp = {
    "resp_type":"FAILED",
    "resp_code":"500",

}

validateServer = "172.20.236.55:8003"
validateHeaders = {"Content-Type":"application/json"}
validateEndpoint = "/validatereq"
validateReqType = ""
validateMethodType = "POST"




checkUserServer = "192.168.0.184:8003"
checkUserServer = "172.20.236.55:8003"
checkUserHeaders = {"Content-Type":"application/json"}
checkUserEndpoint = "/hashrequest"
checkUserReqType = ""
checkUserMethodType = "POST"



logoutServer = "172.20.236.55:8003"
logoutHeaders = {"Content-Type":"application/json"}
logoutEndpoints = "/checkLogout"
logoutReqType = ""
logoutMethodType = "POST"


INVALID_USER_PASS = {"Error-Response":"Invalid USERNAME, PASSWORD"}

postsuccessresp = {
                    "status":200,
                    "respType":"Success",
                    "response": "Successfully obtained result from POST request"
}
postfailresp = {
                    "status":500,
                    "respType":"Failure",
                    "response": "Failure in  recieving response from POST request"
}
