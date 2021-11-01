DB_NAME = 'fis'
ENCRYPTION_KEY = "WHENTHESKIESAREBLUESEEYOUONCEAGA"
# LOG_TABLE = 'log'
#user scheema
userSchema = {
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"},
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': {'keyAlias': {'type':'string'},
                     'institutionId': {'type':'string'},
                     'appId': {'type':'string'},
                     'signature': {'type':'string'},
                    'sessionKey': {'type':'string'},
                     },
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
    'hash': {'type':'string'},
    'checksum': {'type':'string'}}







