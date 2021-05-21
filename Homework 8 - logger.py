import json
import os


class Logger:

    def _log(self, level='', msg=''):
        return json.dumps({level: msg}, sort_keys=True)

    def info(self, msg):
        return self._log('INFO', msg)

    def warn(self, msg):
        return self._log('WARNING', msg)

    def error(self, msg):
        return self._log('ERROR', msg)


class StdOutLogger(Logger):

    def _log(self, level='', msg=''):
        return print(json.dumps({level: msg}))


class FileLogger(Logger):

    def _log(self, level='', msg=''):
        to_json = json.dumps({level: msg})
        if os.getcwd():
            logfile = open('log.json', 'a')
            logfile.write(to_json + '\n')


log = StdOutLogger()

log.info('This is sparta info')
log.warn('This is sparta warn')
log.error('This is sparta error')

log = FileLogger()

log.info('This is sparta info')
log.warn('This is sparta warn')
log.error('This is sparta error')


