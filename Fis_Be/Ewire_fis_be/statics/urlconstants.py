from requests.models import ProtocolError
import datetime
PROTO="http://"
IP_DEV="192.168.0.238"
IP_UAT=""
IP_PROD=""
PORT="8003"
ENDPOINT="/cortex"
BASE_URL=PROTO+IP_DEV+':'+PORT+ENDPOINT

CORTEX=BASE_URL+"cortex"

CORE_END_POINT = "/api/v1/ewire/core/fis/apiDetails/byApiName"
EXT_API_END_POINT_NAME = "api/v1/ewire/extApi"



LOCAL_FIS_URL_CORE = "http://localhost:8002"
DEV_FIS_URL_CORE = "http://192.168.0.160.8000"

UAT_FIS_URL_CORE = LOCAL_FIS_URL_CORE
PROD_FIS_URL_CORE = "https://core.ewirecards.com/fis"

EXT_API_SERVER_URL_LOCAL = "http://localhost:7020/"  #192.168.0.200
UAT_FIS_URL_EXT = EXT_API_SERVER_URL_LOCAL

TIME_NOW = datetime.datetime.now()

class FisConfig():
    def getMWUrl():
        return UAT_FIS_URL_CORE + CORE_END_POINT

    def getExtApiUrl():
        return UAT_FIS_URL_EXT + EXT_API_END_POINT_NAME

    def getHeader():
        return {'Content-Type': 'application/json'}