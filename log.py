import os

ROOT_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)))
LOG_DIR = os.path.join(ROOT_DIR, 'logs')
LOG_FILE = os.path.join(LOG_DIR, 'log.log')


def _write(msg):
    print(msg)
    with open(LOG_FILE, 'a') as f:
        f.write(msg + '\n')


def response(status_code, data):
    msg = '[RSP] [{}] {}'.format(status_code, data)
    _write(msg)


def sql(*args):
    query = args[0]
    msg = '[SQL] ' + query
    if len(args) > 1:
        args_list = ','.join(map(str, args[1]))
        msg += ' (' + args_list + ')'
    _write(msg)


def log(msg):
    _write('[LOG] ' + msg)
