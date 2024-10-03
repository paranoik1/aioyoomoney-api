class YooMoneyError(Exception):
    """Basic class"""


class IllegalParamError(YooMoneyError):
    message = "Invalid parameter value {}"


class IllegalParamType(IllegalParamError):
    def __init__(self, ):
        super().__init__(self.message.format("type"))


class IllegalParamStartRecord(IllegalParamError):
    def __init__(self, ):
        super().__init__(self.message.format("start_record"))


class IllegalParamRecords(IllegalParamError):
    def __init__(self, ):
        super().__init__(self.message.format("records"))


class IllegalParamLabel(IllegalParamError):
    def __init__(self, ):
        super().__init__(self.message.format("label"))


class IllegalParamFromDate(IllegalParamError):
    def __init__(self, ):
        super().__init__(self.message.format("from_date"))


class IllegalParamTillDate(IllegalParamError):
    def __init__(self, ):
        super().__init__(self.message.format("till_date"))


class IllegalParamOperationId(IllegalParamError):
    def __init__(self, ):
        super().__init__(self.message.format("operation_id"))


class IllegalParamDetails(IllegalParamError):
    def __init__(self):
        super().__init__(self.message.format('details'))


class TechnicalError(YooMoneyError):
    message = "Technical error, try calling the operation again later. Error code - {error_code}"

    def __init__(self, error_code: str):
        super().__init__(self.message.format(error_code=error_code))


class InvalidRequest(YooMoneyError):
    message = "Required query parameters are missing or have incorrect or invalid values"

    def __init__(self, ):
        super().__init__(self.message)


class UnauthorizedClient(YooMoneyError):
    message = "Invalid parameter value 'client_id' or 'client_secret', or the application" \
              " does not have the right to request authorization (for example, YooMoney blocked it 'client_id')"

    def __init__(self, ):
        super().__init__(self.message)


class InvalidGrant(YooMoneyError):
    message = "In issue 'access_token' denied. YuMoney did not issue a temporary token, " \
              "the token is expired, or this temporary token has already been issued " \
              "'access_token' (repeated request for an authorization token with the same temporary token)"

    def __init__(self, ):
        super().__init__(self.message)


class EmptyToken(YooMoneyError):
    message = "Response token is empty. Repeated request for an authorization token"

    def __init__(self, ):
        super().__init__(self.message)


class InvalidToken(YooMoneyError):
    message = "Token is not valid, or does not have the appropriate rights"

    def __init__(self, ):
        super().__init__(self.message)
