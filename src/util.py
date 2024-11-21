class UserInputError(Exception):
    pass

#Validator takes an array of params, checks that none of them are empty, otherwise a ValueError is thrown
def validateNotEmpty(params):
    for param in params:
        #Also remove whitespace
        if not param.strip():
            raise ValueError("Fill all fields")

def validateLength(params, min, max):
    for p in params:
        #Remove whitespace
        param = p.strip()
        if len(param) > max:
            raise ValueError("Field too long")
        if len(param) < min:
            raise ValueError("Field too shot")    