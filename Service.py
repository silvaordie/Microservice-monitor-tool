import time

class Service:

    status = ""
    id = ""
    name = ""
    url = ""

    def __init__(self, id , name, url):
        self.name = name
        self.id = id
        self.url = url

    def getName(self):
        return self.name

    def getStatus(self, update):
        pass  

    def getURL(self):
        return self.url  

    def setStatus(self, str):
        self.status = str



