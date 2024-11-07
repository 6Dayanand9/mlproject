
import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
#print(log_file)

log_path=os.path.join(os.getcwd(),'logs',LOG_FILE)
os.makedirs(log_path,exist_ok=True)

Log_File_PATH = os.path.join(log_path,LOG_FILE)

logging.basicConfig(
    filename=Log_File_PATH,
    format="[%(asctime)s]-%(lineno)d-%(levelname)s-%(message)s",
    level=logging.INFO
)

if __name__=="__main__":
    logging.info("logging has started")



"""import logging
import os
from datetime import datetime

# Define the log file name with a timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define the log directory path
log_dir = os.path.join(os.getcwd(), 'logs')
os.makedirs(log_dir, exist_ok=True)  # Ensure the logs directory exists

# Full path for the log file
Log_File_PATH = os.path.join(log_dir, LOG_FILE)

# Configure logging settings
logging.basicConfig(
    filename=Log_File_PATH,
    format="[%(asctime)s] - %(lineno)d - %(levelname)s - %(message)s",
    level=logging.INFO
)

# Test logging setup
if __name__ == "__main__":
    logging.info("Logging has started")
"""