import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format="[%(asctime)s]: %(message)s:")

list_of_files = [
    ##constructer file innit file
    "src/__init__.py",
    "src/helper.py",
    ".env",
    "requirements.txt",
    "setup.py",
    "app.py",
    "research/trials.ipynb",
]
##looking through the list and convert each path to windows path
## /-forward slash and we us it in linux system,but windowos uses backslash \

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    ##it will automatically detect the operating system and convert this path to yopur operating system it
    ##it is used to avoid any path issues

    ##to create file directiory
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file :{filename}")

    ##it will check weather the file exist or not or is it empty or not
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file : {filepath}")

    ##if not it tells the file already exists
    else:
        logging.info(f"{filename} is already exists")
