# coding: utf-8
# author: Holly


import os
import HTMLTestRunner
import time
import unittest


def allTests():
    '''获取所有要执行的测试用例'''
    suite = unittest.defaultTestLoader.discover(
        start_dir = os.path.join(os.path.dirname(__file__),'testCase'),
        pattern='test*.py',
        top_level_dir=None
    )
    return suite


def getNowTime():
    '''获取当前时间'''
    return time.strftime('%Y-%m-%d_%H_%M_%S', time.localtime(time.time()))


def run():
    filename = os.path.join(os.path.dirname(__file__),'report',getNowTime()+'report.html')
    with open(filename, 'wb') as fp:
        runner = HTMLTestRunner.HTMLTestRunner(
            stream = fp,
            title = 'UI自动化测试',
            description='自动化测试详细信息',
        )
        runner.run(allTests())


if __name__ == '__main__':
    run()