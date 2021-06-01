import re


class UkubukaValidator:

    @staticmethod
    def email(email):
        if isinstance(email, str):
            return bool(re.fullmatch(r'[^@]+@[^@]+', email))
        return False