# coding: utf-8
# author: Holly


from selenium.webdriver.common.by import By
from base.basePage import *


class WY(WebUI):
    username_loc = (By.NAME, 'email')
    password_loc = (By.NAME, 'password')
    # //*[@id="dologin"]
    login_loc = (By.XPATH,'//*[@id="dologin"]')
    loginError_loc = (By.XPATH, '//*[@id="nerror"]/div[2]')

    def typeUserName(self, username):
        self.findElement(*self.username_loc).send_keys(username)

    def typePassword(self, password):
        self.findElement(*self.password_loc).send_keys(password)

    # @property将类的方法变成可直接调用的属性 https://www.liaoxuefeng.com/wiki/897692888725344/923030547069856
    @property
    def clickLogin(self):
        self.findElement(*self.login_loc).click()

    def login(self, username=None, password=None):
        self.typeUserName(username)
        self.typePassword(password)
        self.clickLogin

    @property
    def getLoginError(self):
        '''获取错误信息'''
        return self.findElement(*self.loginError_loc).text

