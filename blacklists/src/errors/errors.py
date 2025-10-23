class ApiError(Exception):
    code = 422
    description = "Default message"

class IncompleteParams(ApiError):
    code = 400
    description = "Bad request"


class InvalidParams(ApiError):
    code = 400
    description = "Bad request"


class Unauthorized(ApiError):
    code = 401
    description = "Unauthorized"


class NotFoundError(ApiError):
    code = 404
    description = "Item does not exist"

class EmailExist(ApiError):
    code = 400
    description = "Email exist"

class NotToken(ApiError):
    code = 403
    description = "Token not present in headers"
    
class TokenInvalid(ApiError):
    code = 401
    description = "The token is invalid or expired"
