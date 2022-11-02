# python-logging-model
Purpose study and implement basic logging funcionalities, using logging module.

Logging
Purpose: Record progress and problems...
Levels: Debug, Info, Warning, Error, Critical
It is possible to implement new Levels.

Logging Levels

Level	    Integer  Value	
NOTSET	    0	
DEBUG	    10	
INFO	    20	
WARNING	    30	Default
ERROR	    40	
CRITICAL	50	

If not set the default level is 30 or default
The log level is set on .basicConfig(level = logging.DEBUG)

Logging will only register loglevel >= loglevel set

# Log messages information
Python gives a wide selection of information to include in log messages. 
They can be viewed at  python.org website: 
https://docs.python.org/3/library/logging.html#logrecord-attributes
https://peps.python.org/pep-0282/#formatters




