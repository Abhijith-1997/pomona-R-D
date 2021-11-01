import requests
import json


class CommonUtil:

    # Error handled post requests 
    def postrequestManager(URL,headers,fwReqJson):
        print("code is postrequestManager")
        
        try:
            
            print("postrequestManager PAYLOAD ==>"+ str(fwReqJson))
            print("postrequestManager HEADERS ==>"+ str(headers))
            print("postrequestManager HIT URL ==>"+ str(URL))

            r = requests.post(URL, headers=headers, data=fwReqJson)
            print("AFTER HIT FIS ==>", r.json())    
            return r.json()

        except requests.exceptions.HTTPError as err:
            return str(err)
        except requests.Timeout as e:
            return "Request Timed Out"
        except requests.RequestException as e:
            return "Request Exception detected :"
        except requests.ConnectionError as e:
            return str(e)
        except Exception as e:
            return {"status":"error","message":str(e)}

class CommonResponse:
    
    reqDict = dict()
    # This method provides the data necessary to generate a valid token
    def __init__(self,reqDict = None):
        if reqDict is None:
            self.reqDict = dict()
            self.reqDict["KEY_ALIAS"] = "0kbOdd5Zc0ccbd7090PtMA==.t7SEZXtjq1vF9JEYUbBXPg=="
            self.reqDict["INSTITUTION_ID"] = "0w5xC29wvYvRqQeYBPtajg==.tyayfH/qZw4hfuxAEYlnCA=="
            self.reqDict["APP_ID"] = ""
            self.reqDict["SIGNATURE"] = "0sjqRg8nkKdxreZam16RgfZavEwEhY62uldUQQn/AjS33appwao6cbM2VlaJfIckl2LZHlVoTdANDHaZ4bLuPwhuStrROljeDeiZzyLVvhN69oM/9typX2qWrcH4x6UsoIX+kfp51YvxcYR4AiVyP8rTbINbBX//JMkv7XeTp+6tDfs+Efws0k+YqWqVouwnAnUf6+7HTn096ZsjN9uBWu5QcdDtpKOG2A99itfqtQ/O4HuGVwyUJIYB29yUU/Gmub/2mHnBSVu49KqYigLHGR3MpVTVMjNxdZELKLjDikdXVwDBe7UZEmS/y/5RriEy68T2bgTsRz6t84QLE6Heew=="
            self.reqDict["SESSION_KEY"] = "mJpiCKZpCJG0dgS5EALL2HLKik+fOSW7MwtgytVQlmg="
            
    def get_auth_head(self,url,headers,status):
        payload = dict()
        payload["KEY_ALIAS"] = "0kbOdd5Zc0ccbd7090PtMA==.t7SEZXtjq1vF9JEYUbBXPg=="
        payload["INSTITUTION_ID"] = "0w5xC29wvYvRqQeYBPtajg==.tyayfH/qZw4hfuxAEYlnCA=="
        payload["APP_ID"]=""
        payload["SIGNATURE"] = "0sjqRg8nkKdxreZam16RgfZavEwEhY62uldUQQn/AjS33appwao6cbM2VlaJfIckl2LZHlVoTdANDHaZ4bLuPwhuStrROljeDeiZzyLVvhN69oM/9typX2qWrcH4x6UsoIX+kfp51YvxcYR4AiVyP8rTbINbBX//JMkv7XeTp+6tDfs+Efws0k+YqWqVouwnAnUf6+7HTn096ZsjN9uBWu5QcdDtpKOG2A99itfqtQ/O4HuGVwyUJIYB29yUU/Gmub/2mHnBSVu49KqYigLHGR3MpVTVMjNxdZELKLjDikdXVwDBe7UZEmS/y/5RriEy68T2bgTsRz6t84QLE6Heew=="
        payload["SESSION_KEY"] = "mJpiCKZpCJG0dgS5EALL2HLKik+fOSW7MwtgytVQlmg="

        print("payload===get_auth_head====",payload)
        common_util = CommonUtil
        auth_head = common_util.postrequestManager(url,headers,payload)
        # auth_head = common_util.getRequestManager(url,headers,payload)
        if(status==1):
            auth_token = "Bearer " + auth_head["access_token"]
            headers = {"Authorization":auth_token,"Content-Type": "applicaton/json"}
            print("headers staus 1 =====",headers)
            return headers
        elif status==2:
            auth_token = "Bearer " + auth_head["access_token"]
            headers = {"Authorization":auth_token}
            print("headers staus 2 =====",headers)
            return headers
        return {"Error":"invalid header status"}
        