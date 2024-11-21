class UserInputError(Exception):
    pass

#Validator takes an array of params, checks that none of them are empty, otherwise a ValueError is thrown
def validateNotEmpty(params):
    for param in params:
        if not param:
            raise ValueError("Fill all fields")
