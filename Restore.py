from Command import Command
from parse import *
class Restore (Command):

    def __init__(self, id, desc):
        Command.__init__(self, id, desc)


    def execute(self, service, args):
        hasformat=True
        if(len(args)==1):
            try:
                fd=open(args[0] + ".txt", "r")
                hasformat=False
            except:
                print("Unable to open input file")
                return
        elif(len(args)==2):
            aux = args[1].split("=")
            if(aux[0]=="--format"):
                form = aux[1]
                try:
                    fd=open(args[0] + "." + form, "r")  
                    hasformat=False
                except:
                    print("Unable to open input file")
                    return   
            else:
                print(args[1])
                try:
                    fd=open(args[1] + args[0] + ".txt", "r")  
                    hasformat=False
                except: 
                    print("Unable to open input file")
                    return
        elif(len(args)==3):
            try:
                aux = args[2].split("=")
                if(aux[0]=="--format"):
                    form = aux[1]
                else:
                    print("Unkown input criteria")
                    return

                try:
                    fd=open(args[1] + args[0] + "." + form, "r")
                except:
                    print("Unable to open input file")
                    return
            except:
                print("Unable to open input file")
                return
        else:
            print("Invalid number of input arguments")
            return

        lines = fd.readlines()
        
        for l in lines:
            found = False
            aux = l.split(":")
            r = parse("[{serv}]", aux[0])
            if(r == None):
                if(hasformat):
                    print('"' + l[0:-1] + '" is not a valid backup file line for the ' + form + " format.")
                else:
                    print('"' + l[0:-1] + " is not a valid backup file line for the txt format.")                   
            else:
                for ser in service:
                    if(ser.getName() == r['serv']):
                        ser.setStatus(aux[1][0:-1])
                        found = True

                if(not found):
                    print("Service " + r['serv'] + " isn't implemented")
             
     