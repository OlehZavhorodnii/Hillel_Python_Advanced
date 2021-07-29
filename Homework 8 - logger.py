import json
import os
import sys
from datetime import datetime


class Logger:

    def _config(self, level, msg, log_time, **kwargs):  # **kwargs - additional logging parameters
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
    def info(self, msg, log_time, **kwargs):
        self._log(self._config('INFO', msg, log_time, **kwargs))

    def warn(self, msg, log_time, **kwargs):
        self._log(self._config('WARNING', msg, log_time, **kwargs))

    def error(self, msg, log_time, **kwargs):
        self._log(self._config('ERROR', msg, log_time, **kwargs))


class StdOutLogger(Logger):  # output logging to the console

    def _log(self, params):
        text = json.dumps(params)
        print(text)


class FileLogger(Logger):  # write logging to file

    def __init__(self, abs_path_dir, filename):
        self.__abs_path_dir = abs_path_dir
        self.__filename = filename
        self.__file = open(f'{os.path.join(self.__abs_path_dir, self.__filename)}.json', 'a')
        self.__write_to_file = str()

    def _log(self, params):
        to_file = list()
        to_file.append(json.dumps(params))
        self.__write_to_file = ''.join(to_file)
        print(sys.getsizeof(self.__write_to_file))
        if sys.getsizeof(self.__write_to_file) >= 2048:
            self.__file.write(self.__write_to_file + os.linesep)
        else:
            self.__file.write(self.__write_to_file + os.linesep)


log = StdOutLogger()

log.info('This is info msg', datetime.today().isoformat(), newparam='add new param')
log.warn('This is warn msg', datetime.today().isoformat(), newparam='add new param')
log.error('This is error msg', datetime.today().isoformat(), newparam='add new param')

log_write = FileLogger('/home/oleh/Study/Write', 'My_log')


for i in range(3):
    log_write.info('This is Info msg', datetime.today().isoformat(), newparam='add new param')
    log_write.warn('This is Warn msg', datetime.today().isoformat(), newparam='add new param')
    log_write.error('This is Error msg', datetime.today().isoformat(), newparam='add new param')
