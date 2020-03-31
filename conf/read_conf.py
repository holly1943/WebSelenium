# coding: utf-8
# author: Holly

import configparser


config = configparser.ConfigParser()

print(config.sections())
config.read('setting.ini')
print(config.sections())


print(config['bitbucket.org']['user'])
print(config['DEFAULT']['Compression'])