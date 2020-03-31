# coding: utf-8
# author: Holly

import unittest
from page.wy import *
from selenium import webdriver
import time as t
from utils.openXml import *
from page.init import Init
from page.mail import Mail


class WYTest(Init, WY,Mail):
    def test_wyLogin_001(self, parent='divText', value='emailNull'):
        self.login('','')
        self.logger.info('Hello, World!')
        self.assertEqual(self.getLoginError,self.getXmlUser(parent,value))

    def test_wyLogin_002(self, parent='divText',value='passwdNull'):
        self.login('admin', '')
        self.assertEqual(self.getLoginError, self.getXmlUser(parent, value))

    def test_write_mail(self):
        self.login('','')
        self.write_mail()


if __name__ == '__main__':
    unittest.main(verbosity=2)