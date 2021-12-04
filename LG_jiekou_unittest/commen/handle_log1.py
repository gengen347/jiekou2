import logging
from logging.handlers import TimedRotatingFileHandler
from commen.handle_config import conf
import os
from commen.handle_path import LOG_PATH

def log_get():
    log =logging.getLogger('ligen')
    log.setLevel(conf.get('logging','level'))

    sh = logging.StreamHandler()
    sh.setLevel(conf.get('logging','sh_level'))
    log.addHandler(sh)

    fh = TimedRotatingFileHandler(filename=os.path.join(LOG_PATH,'ligen.log'), when='d',
                                  interval=1, backupCount=3,
                                  encoding='utf-8')
    fh.setLevel(conf.get('logging','fh_level'))
    log.addHandler(fh)

    formatter = "%(asctime)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s"
    mate = logging.Formatter(formatter)
    sh.setFormatter(mate)
    fh.setFormatter(mate)

    return  log

log =log_get()

