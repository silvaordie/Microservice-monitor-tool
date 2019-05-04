import Service
from BitBucket import BitBucket
from GitHub import GitHub
from Slack import Slack

import Command
from Poll import Poll
from Fetch import Fetch
from History import History
from Backup import Backup
from Restore import Restore

from xml.dom import minidom

run = True
serv = []
com = []

mydoc = minidom.parse("services.xml")
items = mydoc.getElementsByTagName("service")

for i in items :
    try:
        serv.append( eval(i.attributes["name"].value + '("' + i.firstChild.data + '")' ) ) 
    except:
        print("Unknown service: " + i.attributes["name"].value)

mydoc = minidom.parse("commands.xml")
items = mydoc.getElementsByTagName("command")
items2 = mydoc.getElementsByTagName("call")
items3 = mydoc.getElementsByTagName("description")

for i in range(0,len(items)) :
    try:
        com.append( eval(items[i].attributes["name"].value + '("' +  items2[i].firstChild.data + '","' + items3[i].firstChild.data + '")') ) 
    except:
        print("erro")

while(run):

    print(">>", end= " ")
    entry = input()
    i = entry.split()
    found = False

    if( i and i[0]== "help") :
        found = True
        for c in com:
            print(c.getComand() + " - " + c.getDesc() )
    elif( i and i[0] == "services"):
        found = True
        for s in serv:
            print(s.getName() + " - " + s.getURL() )  
    else:
        for c in com:
            if( i and i[0] == c.getComand() ):

                c.execute(serv, i[1:])

                found = True

    if(found):
        found = False
    else:
        print("Unknown command, type 'help' for the list of available commands")



