from .exceptions import *

API_URL = "https://yoomoney.ru/api/"
ERROR_CODES = {
    "illegal_param_type": IllegalParamType,
    "illegal_param_start_record": IllegalParamStartRecord,
    "illegal_param_records": IllegalParamRecords,
    "illegal_param_label": IllegalParamLabel,
    "illegal_param_from": IllegalParamFromDate,
    "illegal_param_till": IllegalParamTillDate,
    "illegal_param_details": IllegalParamDetails,
    "illegal_param_operation_id": IllegalParamOperationId,
    
    "invalid_request": InvalidRequest,
    "unauthorized_client": UnauthorizedClient,
    "invalid_grant": InvalidGrant
}
