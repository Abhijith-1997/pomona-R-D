def success_resp(request,resp):
    try:

        success_data={}
        success_data['resp_type']="SUCCESS"
        success_data['resp_code']="800"
        success_data['em_reqid']=request['em_reqid']
        success_data['em_custid']=request['em_custid']

        # success_data['timestamp']=timeStamp
        success_data['api_name']=request['apiname']
        success_data['partner_reqid']=resp['partner_reqid']
        success_data['ext_base_url']=resp['ext_base_url']
        success_data['ext_end_point_url']=resp['ext_end_point_name']
        success_data['api_header']=resp['api_header']
        success_data['resp_frm_database']={}
        success_data['req_data']=resp['req_data']
        success_data['is_revert']=False
        return success_data

    except Exception as e:
        print("exception",str(e))
        return str(e)
    except ValueError as e:
        print("exception2",str(e))
        return str(e)

def failure_resp(request,resp):
    failure_data={}
    failure_data['resp_type']="FAILURE"
    failure_data['resp_code']="802"
    failure_data['em_reqid']=request['em_reqid']
    # failure_data['timestamp']=timeStamp
    failure_data['em_custid']=""
    failure_data['api_name']=request['apiname']
    failure_data['partner_id']=""
    failure_data['ext_base_url']=""
    failure_data['ext_end_point_url']=""
    failure_data['api_header']={}
    failure_data['resp_frm_database']={}
    failure_data['req_data']={}
    failure_data['is_revert']=False
    return failure_data