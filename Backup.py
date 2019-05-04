from Command import Command

class Backup (Command):

    def __init__(self, id, desc):
        Command.__init__(self, id, desc)


    def execute(self, service, args):
            
        if(len(args)==1):
            try:
                fd=open(args[0] + ".txt", "w+")
                hasformat=False
                haspath=False
            except:
                print("Unable to open input file")
                return
        elif(len(args)==2):
            aux = args[1].split("=")
            if(aux[0]=="--format"):
                form = aux[1]
                hasformat=True
                haspath=False
                try:
                    fd=open(args[0] + "." + form, "w+")  
                except:
                    print("Unable to open input file")
                    return   
            else:
                print(args[1])
                try:
                    fd=open(args[1] + args[0] + ".txt", "w+")  
                    hasformat=False
                    haspath=True
                except: 
                    print("Unable to open input file")
                    return
        elif(len(args)==3):
            try:
                aux = args[2].split("=")
                if(aux[0]=="--format"):
                    form = aux[1]
                    hasformat=True
                    haspath = True
                else:
                    print("Unkown input criteria")
                    return

                try:
                    fd=open(args[1] + args[0] + "." + form, "w+")
                except:
                    print("Unable to open input file")
                    return
            except:
                print("Unable to open input file")
                return
        else:
            print("Invalid number of input arguments")
            return

        for ser in service:
            state = ser.getStatus(False)
            name = ser.getName()
            if(state):
                fd.write("[" + name + "]" + ":" + state + "\n")
            else:
                fd.write("[" + name + "]" + ": No state information available" + "\n")

        if(hasformat and haspath):
            print("Backup file named " + args[0] + "." + form + " is located at " + args[1])
        elif(haspath):
            print("Backup file named " + args[0] + ".txt" + " is located at " + args[1])
        elif(hasformat):
            print("Backup file named " + args[0] + "." + form + " created")
        else:
            print("Backup file named " + args[0] + ".txt created")


        fd.close()    