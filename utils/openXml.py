# coding: utf-8
# author: Holly


import os
import xml.dom.minidom


class OperationXml(object):
    def dir_base(self, filename, filepath='data'):
        '''获取data文件夹下的文件'''
        return os.path.join(os.path.dirname(os.path.dirname(__file__)),filepath,filename)

    def getXmlData(self, value):
        '''获取xml单节点中的数据'''
        dom = xml.dom.minidom.parse(self.dir_base('ui.xml'))
        db = dom.documentElement
        name = db.getElementsByTagName(value)
        nameValue = name[0]
        return nameValue.firstChild.data

    def getXmlUser(self,parent,child):
        '''获取xml子节点中的数据'''
        dom = xml.dom.minidom.parse(self.dir_base('ui.xml'))
        db = dom.documentElement
        itemlist = db.getElementsByTagName(parent)
        item = itemlist[0]
        return item.getAttribute(child)

