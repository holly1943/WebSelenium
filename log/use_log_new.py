# coding: utf-8
# author: Holly

import logging

def log(msg):
    logger = logging.getLogger()
    # 设置日志级别
    logger.setLevel(logging.DEBUG)

    # 设置handler
    file_handler = logging.FileHandler(filename=r'E:\UI\log\logs\test_log.log',encoding='utf-8')
    # 设置格式
    file_format = logging.Formatter('%(asctime)s %(filename)s %(levelname)s %(message)s',
                                    datefmt='%Y-%m-%d %H:%M;%S %a')

    # 为handle加上格式
    file_handler.setFormatter(file_format)
    logger.addHandler(file_handler)
    # logger.debug('hello ,世界！')
    logger.info(msg)
    # 移除handler
    file_handler.close()
    logger.removeHandler(file_handler)


if __name__ == '__main__':
    log('泰拳警告')
    log('提示')
    log('错误')

