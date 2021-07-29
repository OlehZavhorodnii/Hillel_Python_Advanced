import json
import os
from datetime import datetime


def decorator_Logger(func):

    def wrapper(list_loggers, msg, **kwargs):
        for i in list_loggers:
            i.func(msg)
    return wrapper



@decorator_Logger
class Logger:

    """
    ДЗ 9. "Задекорировать" свой Logger с прошлого задания.
    Необходимо реализовать такой декоратор, который принимает список логгеров
    и каждое сообщение (инфо, ворнниг, эррор) ретранслирует каждому логгеру.
    Такой подход известен как fan-out.
    """

    def _config(self, level='ERROR', msg=None, time=datetime.today().isoformat(), **kwargs):
        params = {  # a dictionary that stores logging settings
            'level': level,
            'msg': msg,
            'time': time
        }
        params.update(kwargs)  # expanding the dictionary with additional logging parameters
        return params

    def _log(self, params):  # serialization the dictionary {params} to JSON
        json.dumps(params)

    # logging methods:
    def info(self, msg, **kwargs):  # **kwargs - additional logging parameters
        self._log(self._config('INFO', msg, **kwargs))

    def warn(self, msg, **kwargs):
        self._log(self._config('WARNING', msg, **kwargs))

    def error(self, msg, **kwargs):
        self._log(self._config('ERROR', msg, **kwargs))


class StdOutLogger(Logger):  # output logging to the console

    def _log(self, params):
        stdout = json.dumps(params)
        print(stdout)


class FileLogger(Logger):  # write logging to file

    def __init__(self, name_dir=os.getcwd(), name_file='log'):
        self.name_dir = name_dir
        self.name_file = name_file

    def _log(self, params):
        to_file = json.dumps(params)

        if os.path.isdir(self.name_dir):
            os.chdir(self.name_dir)
        else:
            os.makedirs(self.name_dir)
            os.chdir(self.name_dir)

        with open(f'{self.name_file}.json', 'a') as f:
            f.write(to_file + '\n')


log = StdOutLogger()

# log.info('Info', newparam='add new param')
# log.warn('Warn', newparam='add new param')
# log.error('Error', newparam='add new param')
#
# log_write = FileLogger('/home/oleh/Study/Write', 'My_log')
#
# log_write.info('Info', newparam='add new param')
# log_write.warn('Warn', newparam='add new param')
# log_write.error('Error', newparam='add new param')

# log = Logger()
# # log1 = Logger()
# # log2 = Logger()
#
# list_loggers = [log, log1, log2]



