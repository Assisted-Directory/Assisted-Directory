import logging as log
import sys
import tkinter as tk
import pandas as pd
import subprocess
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
    filename = os.getlogin() + ' @ ' + str(datetime.datetime.now().replace(microsecond=0)).replace(':', '_') + ".log"

    # setup log config
    log.basicConfig(encoding='utf-8',
                    filemode='w',
                    level=log.INFO,
                    format='%(asctime)s | %(name)s | %(levelname)s | %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename=os.path.join("%localappdata%\\AssistedDirectory\\logs", filename)
                    )
    return log.getLogger(__name__)


def get_textbox_contents():
    # TODO: build function
    print(None)


def import_file(path_to_file: str, logger):
    # TODO make sure this can open file selector
    if not os.path.exists(path_to_file):
        logger.warning("Unable to find file: " + path_to_file + " Please verify the path is correct! ")
        return None
    if len(get_textbox_contents()) > 0:
        file_contents = get_textbox_contents()
    elif '.csv' in path_to_file.lower():
        file_contents = pd.read_csv(path_to_file)
    elif '.xlsx' in path_to_file.lower():
        file_contents = pd.read_excel(path_to_file)
    elif '.txt' in path_to_file.lower():
        file_object = open(path_to_file, 'r')
        file_data = file_object.read()
        file_contents = file_data.split('\n')
    else:
        logger.warning("Wrong file type! Please verify the path is correct! " + path_to_file)
        return None
    return file_contents


def get_properties_from_ad():
    # TODO make sure this is the correct syntax
    sysp = subprocess.Popen(["powershell.exe",
                             "(get-aduser * -properties *).propertynames"],
                            stdout=sys.stdout)
    p.communicate()
    property_list = ['']
    return property_list


def add_additional_field(root, row, column):
    # TODO finish this function
    e = tk.Entry(root)
    e.grid(row=row, column=column)


def get_entry_values(entry):
    # TODO finish this function
    return entry.get()


def main():
    logger = init_logging()

    logical_operator_list = ['>', '>=', '<', '<=', '==', '!=', 'and', 'or', 'not', 'xor']

    # GUI initialize
    root = tk.Tk()

    # Title
    label_title = tk.Label(root, text="Assisted Directory")
    label_title.grid(row=0, column=0)

    # Entry Value fields
    entry1 = tk.Entry(root)
    entry1.grid(row=2, column=0)
    e1val = entry1.get()

    # Property dropdown
    returned_values = get_properties_from_ad
    prop_drop1 = tk.Spinbox(root, values=returned_values)
    prop_drop1.grid(row=2, column=1)
    p1val = prop_drop1.get()

    # Logical operators
    op_drop1 = tk.Spinbox(root, values=logical_operator_list)
    op_drop1.grid(row=2, column=2)
    o1val = op_drop1.get()

    # Buttons
    button_additional = tk.Button(root, text="Add additional field", command=add_additional_field(root, 3, 0))
    button_additional.grid(row=15, column=0)

    button_search = tk.Button(root, text="Search", command=get_entry_values(entry1))
    button_search.grid(row=16, column=0)

    # Import Buttons
    tk.Button(root, text="Import List (.xlsx, .csv, .txt)",
              command=import_file(path_to_file="test", logger=logger)).grid(row=20, column=0)

    root.mainloop()


main()
