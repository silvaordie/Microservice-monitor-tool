from Command import Command

class Poll (Command):

    def __init__(self):
        Command.__init__(self, "poll", "Retrieves the status from of all configured services")


    def execute(self, service):
        for ser in service:
            state = ser.getStatus(True)
            name = ser.getName()

            print("[" + name + "]" + ":" + state)