import logging


# Create and configure logger
# What will be shown on log file
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"

''' basicConfig parameters
filename = "test.log",  # creates a file if it doesnt exist
level = logging.DEBUG,
format = LOG_FORMAT,  # comes from constant above
filemode = 'w'  # default is append , 'w' writes a new file every log )
'''

logging.basicConfig(filename = "test.log",
                    level = logging.DEBUG,
                    format = LOG_FORMAT,)
                    # filemode = 'w')
logger = logging.getLogger()

# Test the logger
logger.info("Our FIRST message.")
print(logger.level)     # shows the loglevel

# it will only log the info with log >= level
logger.debug("This is a harmless debug message.")
logger.info("Just some useful info.")
logger.warning("I'm sorry, but I can't do that, Dave.")
logger.error("Did you just try to divide by zero?")
logger.critical("The entire internet is down!!")
