import pymysql


class Repository:

    DBCredentialKeys = (
        'host',
        'user',
        'password',
        'database',
    )

    def __init__(self):
        self.dbCredentials = {
            'cursorclass': pymysql.cursors.DictCursor,
        }

    def getConnection(self):
        return pymysql.connect(**self.dbCredentials)

    def _setCredentials(self, credentials):
        for key, value in credentials.items():
            if key in self.DBCredentialKeys:
                self.dbCredentials[key] = value