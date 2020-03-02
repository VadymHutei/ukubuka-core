class Response():

    def __init__(self, response):
        self.data = response.json()

    def getData(self):
        return self.data
