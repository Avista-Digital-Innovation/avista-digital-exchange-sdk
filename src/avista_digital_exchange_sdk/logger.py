import datetime


class Logger:
    """If a log file for today already exist, open it in append mode.
    Else, create a new log file for today, and open it in append mode.
    """
    DEBUG = False
    PADDING = 9
    FORMAT = "|{type:< {self.PADDING}}|{datetime:%I:%M}| {msg}\n"
    FILE = open(f"logs/log{datetime.datetime.now():%d-%m-%Y}.txt", "w+")

    def __init__(self, debug: bool) -> None:
        self.DEBUG = debug

    @classmethod
    def log(self, msg, level):
        if not self.DEBUG and level == "DEBUG":
            return
        print(self.FORMAT.format(
            type=level,
            msg=msg,
            datetime=datetime.datetime.now(),
        ))

    @classmethod
    def info(self, msg):
        """Log info"""
        self.log(msg, "INFO")

    @classmethod
    def exception(self, msg):
        self.log(msg, "EXCEPTION")

    @classmethod
    def debug(self, msg):
        "Only logs if the static variable {DEBUG} is set to True."
        self.log(msg, "DEBUG")
