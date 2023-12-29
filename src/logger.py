# we want to log/track all the executions into one file
# we want to save all the sception as well, even the custom exception
import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(
    os.getcwd(), "logs", LOG_FILE
)  # cwd = correct working directory
os.makedirs(logs_path, exist_ok=True)  # even though there is a file, keep appending into that folder

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# whenever we really need to create the log, we have to set it up in basic config

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
