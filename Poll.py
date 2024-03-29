from Command import Command

class Poll (Command):

    def __init__(self, id, desc):
        Command.__init__(self, id, desc)


    def execute(self, service, args):
 
        if(args):
            aux = args[0].split("=")
            arg = aux[0]
            if( arg == "only" or arg == "exclude"):
                params = aux[1].split(",")
                include = (arg == "only")

                for ser in service:
                    display=(include == False)
                    for element in params:
                        if( ser.getName()==element ):
                            display = include

                    if(display):
                        state = ser.getStatus(False)
                        name = ser.getName()
                        if(state):
                            print("[" + name + "]" + ":" + state)
                        else:
                            print("[" + name + "]" + ": No state information available")
            else:
                print("Unknown argument '" + arg + "'.")
        else:
            for ser in service:
                state = ser.getStatus(True)
                name = ser.getName()
                if(state):
                    print("[" + name + "]" + ":" + state)
                else:
                    print("[" + name + "]" + ": No state information available")