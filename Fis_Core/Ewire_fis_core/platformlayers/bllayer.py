from Ewire_fis_core.platformlayers import constantslayer
from Ewire_fis_core.responsemaster import responses
from Ewire_fis_core.maass import maasslogger
from Ewire_fis_core.statics import staticconstants
from Ewire_fis_core.constants import constfns
from Ewire_fis_core.statics import staticfunctions
from Ewire_fis_core.statics.dbconstants import MongoAPI
from Ewire_fis_core.constants.constfns import checkUser,checkSum,AESCipher,validateHash


def processLoginRequest(request):
    #Parse Request and  extract hash, checksum and data
    try:
        hashchecksumNdata = constantslayer.parseRequestHCRD(request)
    except Exception as e:
        maasslogger(request, str(e))
        return responses.s
        tandardErrorResponseToBE("LOGIN",str(e))
    #Create hash from data
    try:
        createdhash = constantslayer.createHashfromData(hashchecksumNdata['data'],"LOGIN")
    except Exception as ex:
        maasslogger(request, str(ex))
        return responses.standardErrorResponseToBE("CREATELOGINHASH",str(ex))
    #Decode hash obtained from input and from created hash and compare
    valHash = constfns.validateHash(hashchecksumNdata['hash'],createdhash)
    if(valHash == "true"):
        maasslogger(request, "Hashing Passed")
        # checking checksum
        createdchecksum = constfns.validateHash(hashchecksumNdata['hash'],createdhash)
        checksumcompare = constfns.validatechecksum(hashchecksumNdata['checksum'], createdchecksum)
        if(checksumcompare == "true"):
            try:

                comparedResults = constantslayer.getDetails(hashchecksumNdata)
            except Exception as exCompareUser:
                maasslogger(request, str(exCompareUser))
                return str(exCompareUser)
            # If success return success response
            if(comparedResults['result'] == "Success"):
                return comparedResults['respdata']
            else:
                maasslogger(request, "Wrong Credentials")
                return responses.standardErrorResponseToBE("LOGIN","Wrong Credentials")
    
    else:
        maasslogger(request, str("Hash Mismatch, Incorrect Request"))
        return responses.standardErrorResponseToBE("LOGIN","Hash Mismatch, Incorrect Request")