import logging
import sys
import shutil


# https://github.com/sergey-shirnin/LoggingStd_In-Out
class LoggerOut:
    def __init__(self):
        self.terminal = sys.stdout
        self.filename = 'temp_log.txt'

    def write(self, message):
        self.terminal.write(message)
        with open(self.filename, "a") as file:
            print(message, file=file, flush=True, end='')

    def flush(self):
        pass


class LoggerIn:
    def __init__(self):
        self.terminal = sys.stdin
        self.filename = 'temp_log.txt'

    def readline(self):
        entry = self.terminal.readline()
        with open(self.filename, "a") as file:
            print(entry.rstrip(), file=file, flush=True)
        return entry


def save_log():
    try:
        f_name = input("File name:\n")
        shutil.copy('temp_log.txt', f_name)
        print("The log has been saved.")
    except OSError:
        print("Could not save log.")
