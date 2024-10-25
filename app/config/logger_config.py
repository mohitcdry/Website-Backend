import logging
import os
from logging.handlers import TimedRotatingFileHandler

def get_logger():
    logger = logging.getLogger("fastapi_app")

    #check if the logger already has handlers to avoid duplicates
    if not logger.handlers:
        logger.setLevel(logging.DEBUG)

        #create logs directory if it doesn't exist
        log_directory = "logs"
        os.makedirs(log_directory, exist_ok=True)

        #creates a handler that writes log message to a file, rotating in every weak 
        log_file_path = os.path.join(log_directory, "fastapi_app.log")
        handler = TimedRotatingFileHandler (log_file_path, when="D", interval=7, backupCount=4)
        handler.setLevel(logging.DEBUG)

        #creates a logging format
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s ") 
        handler.setFormatter(formatter)

        #Adds the handler to the logger
        logger.addHandler(handler)

        #prevents the logger from propagating messages to the root logger
        logger.propagate = False

    return logger