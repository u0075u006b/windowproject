# -*- coding: utf-8 -*-

import logging
from logging.handlers import RotatingFileHandler
import os.path

class Log:

    def __init__(self):
        pass

    @staticmethod
    def mainlogfun():
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        if not logger.handlers:
            formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - 线程ID%(thread)s - 模块：%(module)s - %(message)s',
                                          datefmt='%Y-%m-%d  %H:%M:%S')
            log_file_handler = RotatingFileHandler(filename=os.path.join(os.getcwd(), 'logs/main.log'),
                                                   mode='a',
                                                   maxBytes=1024,
                                                   backupCount=1)
            log_file_handler.setFormatter(formatter)
            logger.addHandler(log_file_handler)
        return logger