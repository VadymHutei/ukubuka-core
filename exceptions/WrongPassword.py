class WrongPassword(Exception):

    def __init__(self, message=None):
        if message is None:
            message = 'Wrong password'
        super().__init__(message)