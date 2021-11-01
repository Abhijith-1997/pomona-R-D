
class Constants:
    API_PLAID = ""
    
    API_SERVICE = "https://127.0.0.1:8005/app/rest/v1.0"
    AUTH_HOST = ""


    payload = {
        "KEY_ALIAS":"0kbOdd5Zc0ccbd7090PtMA==.t7SEZXtjq1vF9JEYUbBXPg==",
        "INSTITUTION_ID":"0w5xC29wvYvRqQeYBPtajg==.tyayfH/qZw4hfuxAEYlnCA==",
        "APP_ID":"",
        "SIGNATURE":"0sjqRg8nkKdxreZam16RgfZavEwEhY62uldUQQn/AjS33appwao6cbM2VlaJfIckl2LZHlVoTdANDHaZ4bLuPwhuStrROljeDeiZzyLVvhN69oM/9typX2qWrcH4x6UsoIX+kfp51YvxcYR4AiVyP8rTbINbBX//JMkv7XeTp+6tDfs+Efws0k+YqWqVouwnAnUf6+7HTn096ZsjN9uBWu5QcdDtpKOG2A99itfqtQ/O4HuGVwyUJIYB29yUU/Gmub/2mHnBSVu49KqYigLHGR3MpVTVMjNxdZELKLjDikdXVwDBe7UZEmS/y/5RriEy68T2bgTsRz6t84QLE6Heew==", 
        "SESSION_KEY":"mJpiCKZpCJG0dgS5EALL2HLKik+fOSW7MwtgytVQlmg="
    }

    #Authentication
    AUTH_TOKEN_URL ="https://127.0.0.1:8005/authman/v3_0/usersec/authenticate"
    TOKEN_HEADER={"Content-Type:application/json"}

    # card order
    CARD_ORDER_ENDPOINT ="/cardordernonperso"

    # card cancel 
    CARD_CANCEL_ENDPOINT="/cardordercancel"

    #card Equiry
    CARD_ENQ_ENDPOINT='/cardorderenq'

    # card Status
    CARD_STATUS_ENDPOINT="/changecardstatus"

    #customer status
    CUST_UPDATE_ENDPOINT="/updatecustprofile"

    #CARD REPLACEMENT
    CARD_REPLACEMENT_ENDPOINT="/cardreplacenonperso"

    #CARD ISSUE
    CARD_ISSUE_ENDPOINT="/cardorderstanperso"

    # card activation
    CARD_ACTIVE_ENDPOINT="/cardlink"

    # Card upgradation
    CARD_UPGRADE_ENDPOINT="/cardproductchng"

    #customer enquiry validation

    CUST_DETAIL_ENQ_ENDPOINT="/getcustomerdetails"

    # virtual card creation
    VIRTUALCARD_ENDPOINT="/virtualcardcreation"

    # virtual to physical card
    VIRTUAL_PHYSICAL_ENDPOINT="/virtual2physical"

    # adjust account validation
    ADJST_BLNC_ENDPOINT="/adjaccountbalance"

    # account load
    ACCOUNT_LOAD_ENDPOINT="/accountload"

    # set pin
    SET_PIN_ENDPOINT="/setpin"

    # change pin
    CHANGE_PIN_ENDPOINT="/changepin"

    # verify Pin
    VERIFY_PIN_ENDPOINT="/verifypin"

    #transaction details enquiry

    TNX_DET_ENQ_ENDPINT="/gettransactiondetails"

    #gidt card

    GIFT_CARD_ENDPOINT="/giftcardorder"

    #Cvv verification
    CVV_VERIFICATION_ENDPOINT="/verifycvv"


    #card details Enquiry
    CARD_DETAILS_ENQ_ENDPOINT="/carddetails"

    #channel update

    CHANNEL_UPDATE_ENDPOINT="/channelupdate"

    #limit update

    LIMIT_UPDATE_ENDPOINT="/cardlimit"

    #card details enquiry

    LIMIT_CHANNEL_UPDATE_ENDPOINT="/cardlimitandchannel"







