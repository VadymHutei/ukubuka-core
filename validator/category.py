import re


def categoryID(category_id):
    if isinstance(category_id, str):
        return bool(re.fullmatch(r'[0-9]{1,8}', category_id))
    if isinstance(category_id, int):
        return 1 <= len(str(category_id)) <= 8
    return False


def alias(alias):
    if isinstance(alias, str):
        pattern = r'[0-9a-zA-Z_]{1,64}'
        return bool(re.fullmatch(pattern, alias))
    return False


def categoryName(name):
    if isinstance(name, str):
        return re.fullmatch(r'\w{1,64}', name)
    return False


def categoryDescription(description):
    if isinstance(description, str):
        return len(description) <= 1024
    return False
