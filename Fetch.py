from Command import Command
import threading
import time

class Fetch (Command):

    period = 5
    run = False

    def __init__(self, id, desc):
        Command.__init__(self, id, desc)


    def checkStop(self):
        while(self.run):
            i=input()
            self.run = False

    def execute(self, service, args):
        
        self.run = True
        if(args):
            try:
                self.period = float(args[0])
                if(self.period < 0):
                    print(print("Invalid polling interval"))
                    return
            except:
                print("Invalid polling interval")
                return


        threading.Thread(target=self.checkStop).start()
        print("Polling every " + str(self.period) + " seconds:  (Press enter to stop)")
        for ser in service:
            state = ser.getStatus(True)
            name = ser.getName()

            print("[" + name + "]" + ":" + state)
        print("------")
        start = time.time()

        while(self.run):
            if(time.time()-start > self.period):
                for ser in service:
                    state = ser.getStatus(True)
                    name = ser.getName()

                    print("[" + name + "]" + ":" + state)
                
                print("------")
                start = time.time()
            
