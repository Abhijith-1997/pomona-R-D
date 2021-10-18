from Ewire_fis_be.statics.urlconstants import LOGIN
from Ewire_fis_be.statics import ipconstants
commonValues = {}
commonValues['LOGIN'] = {
                            "modulename":"checkUser",
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/user",
                            "reqtype" : "LOGINREQ",
                            "methodtype" : "POST"
                        }
commonValues['CORELOGIN']={
                            "checkUserServer": "",
                            "checkUserHeader":{"Content-Type":"application/json"},
                            "checkUserReqType":"",
                            "checkUserMethodType":"POST",
                            "checkUserEndpoint":"/login"
                            }