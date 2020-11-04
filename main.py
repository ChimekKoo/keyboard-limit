# keyboard_limit 0.1
# Copyright (c) 2020 ChimekKoo
# https://github.com/ChimekKoo/keyboard_limit
# https://chimekkoo.github.io/keyboard_limit

import re
from datetime import datetime
from os import system
from sys import exit, argv
from time import perf_counter
from tkinter.messagebox import showerror, showinfo

from pynput.keyboard import Listener


def write_log(text, log_type):
    logfile = open("log.log", "w")
    now = datetime.now()
    if text == "":
        logfile.write("{datetime} => ==== {type} ====\n".format(
            datetime=now.strftime("%d/%m/%Y %H:%M:%S"),
            type=log_type,
        ))
    else:
        logfile.write("{datetime} => {type}: {text}\n".format(
            datetime=now.strftime("%d/%m/%Y %H:%M:%S"),
            type=log_type,
            text=text
        ))


# define click listener variables #######################################

time_stamp = 0
time_now = 0
i = 0


def main():

    write_log("", log_type="RESTART")

    # Read data from config file ########################################

    file = open("config", "r")
    raw = file.read()
    file.close()

    raw = raw.split("\n")

    if raw[1].count("=") != 1:
        write_log("ERROR", "config: Command cannot contain equal sign (\"=\").")
        showerror("Keyboard Limit 0.1", "config: Command cannot contain equal sign (\"=\"). %s")
        exit()

    config_regex = re.compile(r'([a-zA-Z]*)=([a-zA-Z0-9]*)')

    mo = config_regex.search(raw[0])

    try:
        limit = int(mo.group(2))
    except ValueError:
        write_log("ERROR", "config: Limit must be an integer.")
        showerror("Keyboard Limit 0.1", "config: \"limit\" option must be an integer.")
        exit()

    mo = config_regex.search(raw[1])
    command = mo.group(2)

    # listen clicks #####################################################

    def click():
        i += 1
        if i == 1:
            time_stamp = perf_counter()
        else:
            time_now = perf_counter()
            if (time_now - time_stamp) > limit:
                showinfo("l", "l")
                system(command)

    Listener(on_press=click)


if __name__ == '__main__':
    if "--gui" in argv:
        import gui
    else:
        main()
