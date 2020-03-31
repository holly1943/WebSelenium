# coding: utf-8
# author: Holly


import unittest
from selenium import webdriver
from utils.openXml import *
from log.user_log import RecordLog


class Init(unittest.TestCase, OperationXml):
    def setUp(self):
        self.log = RecordLog()
        self.logger = self.log.get_log()
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(self.getXmlData('url'))
        self.driver.implicitly_wait(30)
        self.frame = self.driver.find_elements_by_tag_name('iframe')[0]
        self.driver.switch_to.frame(0)

    def tearDown(self):
        self.driver.quit()
        self.log.close_handle()