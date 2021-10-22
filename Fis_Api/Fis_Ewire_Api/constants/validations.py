import flask
from flask import request
import json
# from Fis_Ewire_Api.responsemaster.responses import Responses

class ValidateResp:
    # respMesg = {"Error":"Exception occured during validation"}
    
    def validateObj(reqData):
        respMesg ={}
        try:
            if type(reqData) != list:
                if "status" in reqData.keys():
                    print("\n===inside bool val===\n")
                    if reqData['status'] == 400:
                        respMesg['Error']=reqData['errors']
                        return respMesg
                    elif reqData['status'] == 500:
                        respMesg['Error']=reqData['errors']
                        return respMesg
                else:
                # respMesg['status'] = Responses.SUCCESS
                    return reqData
            else:
                return json.dumps(reqData)
        except Exception as e:
            print("\n====inside val exception===\n",str(e))
            return respMesg