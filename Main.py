import logging as log
import tkinter as tk
import datetime
import os


# function to create folder locations if none found
def init_filepath():
    if not os.path.exists("%localappdata%\\AssistedDirectory"):
        os.makedirs("%localappdata%\\AssistedDirectory")
    if not os.path.exists("%localappdata%\\AssistedDirectory\\logs"):
        os.makedirs("%localappdata%\\AssistedDirectory\\logs")


# function to setup logging capabilities
def init_logging():
    # create path for logs
    init_filepath()

    # creates log file in the format '<username> @ <datetime>.log
    filename = os.getlogin() + ' @ ' + str(datetime.now().replace(microsecond=0)).replace(':', '_') + ".log"

    # setup log config
    log.basicConfig(encoding='utf-8',
                    filemode='w',
                    level=log.INFO,
                    format='%(asctime)s | %(name)s | %(levelname)s | %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename=os.path.join("%localappdata%\\AssistedDirectory\\logs", filename)
                    )


init_logging()
