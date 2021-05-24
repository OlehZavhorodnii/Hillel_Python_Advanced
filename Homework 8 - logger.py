import json
import os
import sys


class Logger:

    def _log(self, level='', msg=''):
        return json.dumps({'level': level, 'msg': msg})

    def info(self, msg):
        return self._log('INFO', msg)

    def warn(self, msg):
        return self._log('WARNING', msg)

    def error(self, msg):
        return self._log('ERROR', msg)


class StdOutLogger(Logger):

    def _log(self, level='', msg=''):
        stdout = json.dumps({'level': level, 'msg': msg})
        return sys.stdout.write(stdout + '\n')


class FileLogger(Logger):

    def _log(self, level='', msg=''):
        to_json = json.dumps({'level': level, 'msg': msg})
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


