class InternalServerError(Exception):
    pass

class SchemaValidationError(Exception):
    pass

class UserNotExistsError(Exception):
    pass

class NameAlreadyExistsError(Exception):
    pass

class UnauthorizedError(Exception):
    pass

errors = {
    "InternalServerError": {
        "message": "Something went wrong"
    },
     "SchemaValidationError": {
         "message": "Request is missing required fields",
         "status":400
     },
     "UserNotExistsError": {
         "message": "user with the given name doesn't exists",
         "status":400
     },
     "NameAlreadyExistsError": {
         "message": "User with given name already exists",
         "status":400
     },
     "UnauthorizedError": {
         "message": "Invalid username or password",
         "status":400
     }
}