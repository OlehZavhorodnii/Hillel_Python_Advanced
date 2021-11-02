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


log = StdOutLogger()

log.info('This is info msg', newparam='add new param')
log.warn('This is warn msg', newparam='add new param')
log.error('This is error msg', newparam='add new param')

log_write = FileLogger('/home/oleh/Study/Write', 'My_log')

log_write.info('This is Info msg', newparam='add new param')
log_write.warn('This is Warn msg', newparam='add new param')
log_write.error('This is Error msg', newparam='add new param')
