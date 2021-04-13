import pymysql


class Repository:

    def __init__(self):
        self.dbCredentials = {}

    def getConnection(self):
        return pymysql.connect(**self.dbCredentials)