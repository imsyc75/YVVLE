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
            raise ValueError("Field too shot")    

def validate_key(key, keys):
    for k in keys:
        print(k)
        if k==key:
            raise ValueError("Key already in use")