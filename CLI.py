from BitBucket import BitBucket
from GitHub import GitHub

import Command
from Poll import Poll

import Service


run = True
com = [Poll()]
serv = [GitHub("https://status.github.com/") , BitBucket("https://status.bitbucket.org/")]

while(run):
    print(">>", end= " ")
    i = input()

    for c in com:
        if(i == c.getComand() ):
            c.execute(serv)
        elif( i== "help") :
            for c in com:
                print(c.getComand() + " - " + c.getDesc() )
        else:    
            print("Unknown command, for list of available comands type 'help' ")

