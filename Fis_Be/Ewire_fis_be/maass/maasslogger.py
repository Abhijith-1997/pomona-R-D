from flask.globals import request
from Ewire_fis_be.statics import staticfunctions
from Ewire_fis_be.platformlayers import standardresponses
# Log the activity in Maass Logger Micro Service
def masslogger(data, error):
    maassdata = {"req_type":request['req_type'],"req_code":request['req_code'],
                        "apiname":request['apiname'],"em_reqid":request['em_reqid'],
                        "partner_reqid":request['partner_reqid'],"requestdata":request['requestdata'],"authToken":request['authtoken'],"em_endpoint":request['em_endpoint'],
                        "em_custid":request['em_custid'],"txntype":request["txntype"],"hash":request['hash'],"checksum":request['checksum']}
    #Log the error and the request data parameters
    maassobj=standardresponses.commonValues
    #core
    maaass=staticfunctions.performRequest(maassobj['CORELOGIN'],maassdata)
    return maaass