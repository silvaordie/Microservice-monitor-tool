# Mercedes.io-Challenge

 The present repository includes the files necessary to run a Command Line Interface to check and monitor the state of several micro services such as GitHub, BitBucket, Slack, ... 

 ## Necessary modules

 The code was implemented using Pytoh with the folloawing modules

 ```
xml.dom
requests
bs4
time
threading
 ```

 ## Implementation

 The code was designed to allow the user to add/remove commands as well as services to monitor. This solution offers a class CLI where the interface is implemented as well as two abstract classes/interfaces that allow the user to add/remove services or commands from de CLI.

 ### Services 
To add a new service to the CLI, the user should create a new Python class and import it in the CLI.py script implementing the abstract methods defined in the 'Service' class and add the desired service to the configuration file 'services.xml' with it's respective URL. 
To remove a service from the CLI, the user chould remove it from the configuration file, or you may leave it and remove the "import NameOfDesiredService" line from the CLI script.

### Commands
To add a new command to the CLI, the procedure is similar to the one for services, simply implement the abstract methods of the Command.py class, import the newly created class in the CLI.py script and add the new command to the configuration file commands.xml.
To remove a command from the CLI, the procedure is the same as mentioned in the services.

## Default Build
The default build comes with two built-in commands, help and services, where both of them list all the available commands and services respectively. Also, four services have been made available (Slack.py, GitHub.py, BitLab.py and BitBucket.py) and five commands with optional arguments have been made available

```
 poll (only=ServiceName1,Servicename2, ...)/(exclude=ServiceName1,Servicename2, ...)
 fetch (PeriodInSeconds)
 history
 backup (path) name (--format=FORMAT)
 restore (path) name (--format=FORMAT)
```

## Authors

* **José Silva** :  - Fourth Year of Eletrical and Computer Engineering at Instituto Superior Técnico [Email](jose.ferreira.silva@junitec.tecnico.ulisboa.pt)