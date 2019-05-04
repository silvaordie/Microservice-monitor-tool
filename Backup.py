from Command import Command

class Backup (Command):

    def __init__(self, id, desc):
        Command.__init__(self, id, desc)


    def execute(self, service, args):
            
        if(len(args)  == 2):
            path = ""
        elif(len(args) == 3 ):
            
            path = args[0]
            fil = args[1]
            formating = args[2]

            aux = formating[2:].split("=")
            
            arg = aux[0]
            doc = aux[1]
            if(formating[:2] == "--" and arg == "format" ):
                try:
                    fd= open(path + fil + "." + doc, "w+")
                except:
                    print("Unnable to open output file")
                    return

                for ser in service:
                    state = ser.getStatus(False)
                    name = ser.getName()
                    if(state):
                        fd.write("[" + name + "]" + ":" + state + "\n")
                    else:
                        fd.write("[" + name + "]" + ": No state information available" + "\n")

                print("Backup file named " + fil + "." + doc + " is located at " + path)
                fd.close()
            else:
                print("Unknown format options (--format=csv or --format=txt)")
                return
        else:
            print("Not enough input arguments (backup path name --format=#)") 
            return       