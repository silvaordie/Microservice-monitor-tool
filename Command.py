class Command:

    com = ""
    desc = ""

    def __init__(self, id, des):
        self.com = id
        self.desc = des

    def execute(self, service, args):
        pass

    def getComand(self):
        return self.com
    
    def getDesc(self):
        return self.desc
    