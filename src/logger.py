import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"                 #log file is created
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)                            #  whetaver log file is created , it will be wrt to current wrking directoy
os.makedirs(logs_path,exist_ok=True)                                           # this says that even if there is a  file already, keep on appending those files

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,


)