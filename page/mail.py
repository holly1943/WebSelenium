# coding: utf-8
# author: Holly


from base.basePage import *
from selenium.webdriver.common.by import By


class Mail(WebUI):
    # 写邮件元素属性 /html/body/div[1]/nav/div[1]/ul/li[2]/span[2]
    writeMail_loc = (By.XPATH, '/html/body/div[1]/nav/div[1]/ul/li[2]/span[2]')
    # //*[@title="发给多人时地址请以分号隔开"]
    # 收件人 /html/body/div[2]/div[1]/div[2]/div[1]/section/header/div[1]/div[1]/div/div[2]
    reciver_loc = (By.XPATH, '/html/body/div[2]/div[1]/div[2]/div[1]/section/header/div[1]/div[1]/div/div[2]/div/input')
    # 主题 /html/body/div[2]/div[1]/div[2]/div[1]/section/header/div[2]/div[1]/div/div/input
    title_loc = (By.XPATH, '/html/body/div[2]/div[1]/div[2]/div[1]/section/header/div[2]/div[1]/div/div/input')
    # 存草稿 //*[@id="_mail_button_4_188"]/span
    save_loc = (By.XPATH, '/html/body/div[2]/div[1]/div[2]/header/div/div[3]/div/span')

    @property
    def clickWriteMail(self):
        '''点击写信按钮'''
        return self.findElement(*self.writeMail_loc).click()

    def typeReciver(self, reciver):
        '''输入主题'''
        return self.findElement(*self.reciver_loc).send_keys(reciver)

    def typeSubject(self, subject):
        '''输入主题'''
        return self.findElement(*self.title_loc).send_keys(subject)

    @property
    def save(self):
        '''存为草稿'''
        return self.findElement(*self.save_loc).click()

    def write_mail(self, reciver='123@163.com', subject='123456'):
        # self.findElement(*self.writeMail_loc).click()
        # self.findElement(*self.reciver_loc).send_keys(reciver)
        # self.findElement(*self.title_loc).send_keys(subject)
        # self.findElement(*self.save_loc).click()
        self.clickWriteMail
        self.typeReciver(reciver)
        self.typeSubject(subject)
        self.save


