from requests.models import ProtocolError
PROTO="http://"
IP_DEV="192.168.0.238"
IP_UAT=""
IP_PROD=""
PORT="8003"
ENDPOINT="/cortex"
BASE_URL=PROTO+IP_DEV+':'+PORT+ENDPOINT

CORTEX=BASE_URL+"cortex"