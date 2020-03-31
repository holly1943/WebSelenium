# coding: utf-8
# author: Holly

import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait


class Factory(object):
    def __init__(self, driver):
        self.driver = driver

    def createDriver(self,driver):
        if driver == 'web':
            return WebUI(self.driver)
        elif driver == 'app':
            return APPUI(self.driver)


class Webdriver(object):
    def __init__(self, driver):
        self.driver = driver

    def findElement(self, *loc):
        '''定位单个元素的方法'''
        try:
            return WebDriverWait(self.driver,20).until(lambda x: x.find_element(*loc))
            # return self.driver.find_element(*loc)
        except NoSuchElementException as e:
            print('error details{0}'.format(e.args[0]))

    def findElements(self,*loc):
        '''多个元素的定位'''
        try:
            return WebDriverWait(self.driver, 20).until(lambda x: x.find_element(*loc))
            # return self.driver.find_elements(*loc)
        except NoSuchElementException as e:
            print('error details{0}'.format(e.args[0]))


class WebUI(Webdriver):
    def __str__(self):
        return 'WebUI'


class APPUI(Webdriver):
    def __str__(self):
        return 'APPUI'

