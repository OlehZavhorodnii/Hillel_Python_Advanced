import json
import os
from datetime import datetime


class Logger:

    def _construct_params(self, level, msg, log_time=datetime.now().isoformat(), **kwargs):
        # **kwargs - additional logging parameters
        params = {  # a dictionary that stores logging settings
            'level': level,
            'msg': msg,
            'time': log_time
        }
        params.update(kwargs)  # expanding the dictionary with additional logging parameters
        return params

    def _log(self, params):
        json.dumps(params)
        return

    # logging methods:
    def info(self, msg, **kwargs):
        self._log(self._construct_params('INFO', msg, **kwargs))

    def warn(self, msg, **kwargs):
        self._log(self._construct_params('WARNING', msg, **kwargs))

    def error(self, msg, **kwargs):
        self._log(self._construct_params('ERROR', msg, **kwargs))


class StdOutLogger(Logger):  # output logging to the console

    def _log(self, params):
        text = json.dumps(params)
        print(text)


class FileLogger(Logger):  # write logging to file

    def __init__(self, abs_path_dir, filename):
        self.__file = open(f'{os.path.join(abs_path_dir, filename)}.json', 'a', buffering=-1)

    def _log(self, params):
        to_file = json.dumps(params)
        self.__file.write(to_file + os.linesep)

    def __call__(self):
        try:
            pass
        finally:
            self.__file.close()


class Decorator(Logger):

    def __init__(self, list_logs, info_msg, warn_msg, error_msg):
        self.__list_logs = list_logs
        self.__info_msg = info_msg
        self.__warn_msg = warn_msg
        self.__error_msg = error_msg

    def __call__(self):
        for i in self.__list_logs:
            i.info(self.__info_msg)
            i.warn(self.__warn_msg)
            i.error(self.__error_msg)
        return


log1 = StdOutLogger()
log2 = StdOutLogger()
log3 = StdOutLogger()

list_logs = [log1, log2, log3]

log4 = StdOutLogger()

list_logs.append(log4)

StdOutLogger = Decorator(list_logs, 'This is info msg', 'This is warn msg', 'This is error msg')
StdOutLogger()

