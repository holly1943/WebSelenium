# coding: utf-8
# author: Holly


import logging
import time
import os
import datetime

'''
    %(name)s            Name of the logger (logging channel)
    %(levelno)s         Numeric logging level for the message (DEBUG, INFO,
                        WARNING, ERROR, CRITICAL)
    %(levelname)s       Text logging level for the message ("DEBUG", "INFO",
                        "WARNING", "ERROR", "CRITICAL")
    %(pathname)s        Full pathname of the source file where the logging
                        call was issued (if available)
    %(filename)s        Filename portion of pathname
    %(module)s          Module (name portion of filename)
    %(lineno)d          Source line number where the logging call was issued
                        (if available)
    %(funcName)s        Function name
    %(created)f         Time when the LogRecord was created (time.time()
                        return value)
    %(asctime)s         Textual time when the LogRecord was created
    %(msecs)d           Millisecond portion of the creation time
    %(relativeCreated)d Time in milliseconds when the LogRecord was created,
                        relative to the time the logging module was loaded
                        (typically at application startup time)
    %(thread)d          Thread ID (if available)
    %(threadName)s      Thread name (if available)
    %(process)d         Process ID (if available)
    %(message)s         The result of record.getMessage(), computed just as
                        the record is emitted
'''


class RecordLog(object):
    def __init__(self):
        self.logger = logging.getLogger()
        # 设置日志级别
        self.logger.setLevel(logging.INFO)
        # 日志文件名称
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))

        LOG_DIR = os.path.join(BASE_DIR, 'logs')
        log_file_name = datetime.datetime.now().strftime('%Y-%m-%d')+'.log'
        log_file_path = LOG_DIR + '/' + log_file_name

        # 输出格式
        format01 = logging.Formatter('%(asctime)s %(filename)s %(funcName)s %(levelname)s---->%(message)s')

        # 文件输出日志
        self.file_handler = logging.FileHandler(log_file_path, 'a', encoding='utf-8')
        self.file_handler.setFormatter(format01)
        self.logger.addHandler(self.file_handler)

    def get_log(self):
        return self.logger

    def close_handle(self):
        self.logger.removeHandler(self.file_handler)
        self.file_handler.close()


if __name__ == "__main__":
    rl = RecordLog()
    log_info = rl.get_log()
    log_info.debug('输出到文件中去')
    rl.close_handle()


