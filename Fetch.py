from Command import Command
import threading
import time

class Fetch (Command):

    period = 5
    run = False

    def __init__(self):
        Command.__init__(self, "fetch", "Retrieves the status from of all configured services")


    def checkStop(self):
        while(self.run):
            i=input()

            if(i=="q" or i=="exit"):
                self.run = False

    def execute(self, service):
        
        self.run = True

        threading.Thread(target=self.checkStop).start()
        print("Polling every " + str(self.period) + " seconds:  (Press 'q' to stop)")
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
            
