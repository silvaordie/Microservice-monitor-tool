import Service
from BitBucket import BitBucket
from GitHub import GitHub

import Command
from Poll import Poll
from Fetch import Fetch

from xml.dom import minidom

run = True
com = [Poll(), Fetch()]
serv = []

mydoc = minidom.parse("services.xml")
items = mydoc.getElementsByTagName("service")

for i in items :
    if(i.attributes["name"].value == "GitHub"):
        serv.append( GitHub(i.data))
    elif(i.attributes["name"].value == "BitBucket"):
        serv.append( BitBucket(i.data))
    else:
        print("Unknown service:" + i.attributes["name"].value)


while(run):

    print(">>", end= " ")
    i = input()
    found = False

    if( i== "help") :
        found = True
        for c in com:
            print(c.getComand() + " - " + c.getDesc() )
    elif(i == "services"):
        found = True
        for s in serv:
            print(s.getName() + " - " + s.getURL() )  
    else:
        for c in com:
            if(i == c.getComand() ):
                c.execute(serv)
                found = True
          
    
    if(found):
        found = False
    else:
        print("Unknown command, type 'help' for the list of available commands")



