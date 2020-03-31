# coding: utf-8
# author: Holly


import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s %(levelname)s %(message)s',
                    datefmt="%Y-%m-%d %H:%M;%S %a",
                    filename = r'E:\UI\log\logs\test_log.log')
logging.debug('hello world!')
logging.warning('hello world!')