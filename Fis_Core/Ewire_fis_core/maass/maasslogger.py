# Log the activity in Maass Logger Micro Service
from re import M
from Ewire_fis_core.statics import staticfunctions
from Ewire_fis_core.platformlayers import standardresponses
def maasslogger(data, msg, modulename, logtype):
    #Log the error and the request data parameters
    config = {}
    reqdta = {}
    reqdta['data'] = data
    reqdta['msg'] = msg
    config[modulename]["requestdata"] = reqdta
    config[modulename]["loggr"] = logtype

    maasslog = staticfunctions.performRequest(config[modulename])
    return maasslog