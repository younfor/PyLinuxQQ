# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/guiMain.ui'
#
# Created: Mon Feb 23 17:19:12 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import json,os
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_Main(object):

    def setupFont(self):
        self.font1 = QtGui.QFont()
        self.font1.setFamily(_fromUtf8("Helvetica"))
        self.font1.setPointSize(14)
        self.font1.setBold(True)
        self.font1.setWeight(75)
        self.font2 = QtGui.QFont()
        self.font2.setFamily(_fromUtf8("Helvetica"))
        self.font2.setPointSize(13)
        self.font2.setBold(False)
        self.font2.setWeight(50)
        self.font3 = QtGui.QFont()
        self.font3.setFamily(_fromUtf8("Helvetica"))
        self.font3.setPointSize(9)

    def setupUi(self, Main):
        # font
        self.setupFont()
        # head
        Main.setWindowTitle(_translate("Main", "PyLinuxQQ", None))
        Main.resize(268, 513)
        self.img_head = QtGui.QGraphicsView(Main)
        self.img_head.setGeometry(QtCore.QRect(10, 10, 71, 61))
        self.lbl_head = QtGui.QLabel(Main)
        self.lbl_head.setGeometry(QtCore.QRect(90, 17, 131, 21))
        self.lbl_head.setFont(self.font1)
        self.lbl_content = QtGui.QLabel(Main)
        self.lbl_content.setGeometry(QtCore.QRect(90, 50, 151, 18))
        self.text_search = QtGui.QLineEdit(Main)
        self.text_search.setGeometry(QtCore.QRect(0, 80, 268, 28))
        self.text_search.setPlaceholderText(
            _translate("Main", "搜索好友...", None))
        # tabwidget

        self.tabWidget = QtGui.QTabWidget(Main)
        self.tabWidget.setGeometry(QtCore.QRect(0, 110, 268, 401))
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        # 会话
        self.tab = QtGui.QWidget()
        self.listWidget = QtGui.QListWidget(self.tab)
        self.listWidget.setGeometry(QtCore.QRect(0, 11, 261, 351))
        self.tabWidget.addTab(self.tab, _fromUtf8("    会   话   "))
        # 好友
        self.tab_2 = QtGui.QWidget()
        self.scrollArea = QtGui.QScrollArea(self.tab_2)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setGeometry(QtCore.QRect(0, 7, 261, 361))
        self.scrollArea.setWidgetResizable(False)
        self.toolBox = QtGui.QToolBox()
        self.scrollArea.setWidget(self.toolBox)
        self.toolBox.setGeometry(QtCore.QRect(0, 7, 250, 600))
        self.toolBox.setCurrentIndex(0)
        self.tabWidget.addTab(self.tab_2, _fromUtf8("    好   友   "))
        # 群组
        self.tab_3 = QtGui.QWidget()
        self.listWidget = QtGui.QListWidget(self.tab_3)
        self.listWidget.setGeometry(QtCore.QRect(0, 11, 261, 351))
        self.tabWidget.addTab(self.tab_3, _fromUtf8("    群   组   "))
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Main)
    def setupSelf(self,main,account,lnick):
        pixmap = QtGui.QPixmap()
        pixmap.load('tmp/head/' + str(account) + '.jpg')
        scene = QtGui.QGraphicsScene(main)
        item = QtGui.QGraphicsPixmapItem(pixmap)
        scene.addItem(item)
        self.img_head.setScene(scene)
        self.lbl_head.setText(_translate("Main", str(account), None))
        self.lbl_content.setText(_translate("Main", lnick, None))
    def setupFace(self, main,data):
        
        for i in range(len(data['friends'])):
            name = str(data['friends'][i]['uin'])
            pixmap = QtGui.QPixmap()
            if not os.path.exists('tmp/head/'+name+'.jpg'):
                name = 'qq'
            pixmap.load('tmp/head/' + name + '.jpg')
            scene = QtGui.QGraphicsScene(main)
            item = QtGui.QGraphicsPixmapItem(pixmap)
            scene.addItem(item)
            self.graphicsView[i].setScene(scene)
            self.graphicsView[i].resize(50,50)

    def setupFriend(self, data,online):
        # categories
        if data['categories'][0]['index'] == 0:
            self.listWidget = {}
        else:
            self.listWidget = {0: QtGui.QListWidget()}
            self.toolBox.addItem(self.listWidget[0], _fromUtf8('我的好友'))
            self.listWidget[0].setGeometry(QtCore.QRect(0, 1, 238, 301))
        for cat in data['categories']:
            self.listWidget[cat['index']] = QtGui.QListWidget()
            self.toolBox.addItem(
                self.listWidget[cat['index']], _fromUtf8(cat['name']))
            self.listWidget[cat['index']].setGeometry(
                QtCore.QRect(0, 1, 238, 301))
        # markname  
        self.uindict={}
        for mark in data['marknames']:
            info=[mark['markname'],None,None]
            self.uindict[mark['uin']]=info
        # online
        for on in online:
            u=self.uindict.get(on['uin'])
            if u is None:
                info=[None,True,None]
                self.uindict[on['uin']]=info
            else:
                u[1]=True
        # widget
        loc = -1
        self.graphicsView = {}
        for user in data['friends']:
            loc += 1
            if self.uindict.get(user['uin']):
                markname=self.uindict.get(user['uin'])[0]
            else:
                markname=None
            self.item, self.widget = self.createWidget(
                loc, self.listWidget[user['categories']], data['info'][loc]['nick'],markname,user['uin'])
            self.listWidget[user['categories']].setItemWidget(
                self.item, self.widget)
        # size
        self.toolsize = []
        for key,val in self.listWidget.items():
            size = len(val)
            print size
            self.toolsize.append(size)
        self.toolBox.currentChanged.connect(self.onToolBoxChanged)
        self.toolBox.resize(QtCore.QSize(250,self.toolsize[0]*48+len(self.toolsize)*34))
    def onToolBoxChanged(self,index):
        self.toolBox.resize(QtCore.QSize(250,self.toolsize[index]*48+len(self.toolsize)*34))
    def createWidget(self, loc, listWidget, title,markname,uin):
        self.listWidgetItem = QtGui.QListWidgetItem(listWidget)
        self.listWidgetItem.setSizeHint(QtCore.QSize(0, 48))
        self.widget = QtGui.QWidget()
        self.widget.setGeometry(QtCore.QRect(0, 0, 238, 51))
        self.graphicsView[loc] = QtGui.QGraphicsView(self.widget)
        self.graphicsView[loc].setGeometry(QtCore.QRect(1, 1, 38, 38))
        self.lbl_title = QtGui.QLabel(self.widget)
        self.lbl_title.setGeometry(QtCore.QRect(60, 10, 181, 18))
        self.lbl_title.setFont(self.font2)
        if markname is not None:
            title=markname+'('+title+')'
        self.lbl_title.setText(_translate("Main", title, None))
        self.lbl_comment = QtGui.QLabel(self.widget)
        self.lbl_comment.setGeometry(QtCore.QRect(60, 30, 181, 18))
        info=self.uindict.get(uin)
        if info and info[1]:
            self.lbl_comment.setText(_translate("Main", '[在线]', None))
        else:
            self.lbl_comment.setText(_translate("Main", '[离线]', None))
        self.lbl_comment.setFont(self.font3)
        return self.listWidgetItem, self.widget
