import random
import hashlib

import config
from vendor.Ukubuka.exceptions.WrongPassword import WrongPassword


def getSecret(abc, length):
    if not isinstance(length, int) or 1 > length > 128:
        return None
    if not isinstance(abc, str) or 1 > len(abc) > 128:
        return None
    return ''.join([random.choice(abc) for _ in range(length)])

def getHash(string):
    if not isinstance(string, str):
        return None
    m = hashlib.sha512(string.encode('utf-8'))
    return m.hexdigest()

def getPassword(password=None, length=None, salt=None):
    if length is None:
        length = config.PASSWORD_LENGTH
    elif config.PASSWORD_LENGTH_MIN >= length >= config.PASSWORD_LENGTH_MAX:
        raise WrongPassword('Wrong length of the password')
    if password is None:
        password = getSecret(config.PASSWORD_ABC_FULL_SAFE, length)
    if salt is None:
        salt = getSecret(config.PASSWORD_ABC_FULL, config.PASSWORD_SALT_LENGTH)

    passwordHash = getHash(password)
    passwordHash = getHash(passwordHash + salt)
    passwordHash = getHash(passwordHash + config.PASSWORD_SALT)

    return password, salt, passwordHash