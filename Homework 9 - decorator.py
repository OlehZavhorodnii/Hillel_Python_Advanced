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


log1 = StdOutLogger()
log2 = StdOutLogger()
log3 = StdOutLogger()

list_logs = [log1, log2, log3]


def decorator_Logger(Cls, list_logs, info_msg, warn_msg, error_msg):
    """
    ДЗ 9. "Задекорировать" свой Logger с прошлого задания.
    Необходимо реализовать такой декоратор, который принимает список логгеров
    и каждое сообщение (инфо, ворнниг, эррор) ретранслирует каждому логгеру.
    Такой подход известен как fan-out.
    """

    def wrapper():
        map(Cls.info(info_msg), list_logs)
        map(Cls.warn(warn_msg), list_logs)
        map(Cls.error(error_msg), list_logs)
        return

    return wrapper


decorator_Logger(StdOutLogger(), list_logs, 'This is info msg', 'This is warn msg', 'This is error msg')

log = StdOutLogger()
log.info('This is info msg')

