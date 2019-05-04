from Command import Command
from parse import *
class Restore (Command):

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
            if(formating[:2] == "--" and arg == "format" and (doc == "txt" or doc == "csv") ):
                try:
                    fd= open(path + fil + "." + doc, "r")
                except:
                    print("Unnable to open input file")
                    return

                lines = fd.readlines()
                
                for l in lines:
                    found = False
                    aux = l.split(":")
                    r = parse("[{serv}]", aux[0])
                    if(r == None):
                        print('"' + l[0:-1] + '" is not a valid backup file line for the ' + doc + " format.")
                    else:
                        for ser in service:
                            if(ser.getName() == r['serv']):
                                ser.setStatus(aux[1][0:-1])
                                found = True

                        if(not found):
                            print("Service " + r['serv'] + " isn't implemented")
             
            else:
                print("Unknown format options (--format=csv or --format=txt)")
                return
        else:
            print("Not enough input arguments (restore path name --format=#)") 
            return       