from repositories.repository_manager import get_all_keys

class UserInputError(Exception):
    pass

#Validator takes an array of params, checks that none of them are empty, otherwise a ValueError is thrown
def validate_not_empty(params):
    for param in params:
        if not param.strip():
            raise ValueError("Fill all fields")

def validate_length(params, min, max):
    for p in params:
        param = p.strip()
        if len(param) > max:
            raise ValueError("Field too long")
        if len(param) < min:
            raise ValueError("Field too short")    

def validate_key(key):
    keys = get_all_keys()
    for k in keys:
        if k==key:
            raise ValueError("Key already in use")
        
def validate(params : list):
    validate_not_empty(params)
    validate_length(params, 1, 255)
    validate_key(params[0])