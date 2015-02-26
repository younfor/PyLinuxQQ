# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/guiChat.ui'
#
# Created: Wed Feb 25 21:11:06 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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


class Ui_Chat(object):

    def setupUi(self, Chat):
        Chat.setWindowTitle(_translate("Chat", "聊天", None))
        Chat.resize(575, 524)
        self.line = QtGui.QFrame(Chat)
        self.line.setGeometry(QtCore.QRect(90, 0, 21, 521))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        # font
        self.font = QtGui.QFont()
        self.font.setFamily(_fromUtf8("Helvetica"))
        self.font.setPointSize(13)
        self.font.setBold(True)
        self.font.setItalic(False)
        self.font.setWeight(75)
        self.font2 = QtGui.QFont()
        self.font2.setFamily(_fromUtf8("Helvetica"))
        self.font2.setPointSize(9)
        # side bar
        self.groupBox = QtGui.QGroupBox(Chat)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 111, 521))
        # side button
        self.button_chat = QtGui.QPushButton(self.groupBox)
        self.button_chat.setGeometry(QtCore.QRect(0, 0, 101, 27))
        self.button_chat.setText(_translate("Chat", "稻草人", None))
        self.button_chat.setStyleSheet("QPushButton{color:red;}")
        # stack widget
        self.stackedWidget = QtGui.QStackedWidget(Chat)
        self.stackedWidget.setGeometry(QtCore.QRect(100, 0, 471, 521))
        # page
        uin = '28762822'
        self.stack = {}
        self.stack[uin] = self.createPage()
        self.stackedWidget.addWidget(self.stack[uin])

        QtCore.QMetaObject.connectSlotsByName(Chat)

    def createPage(self):
        self.page = QtGui.QWidget()
        line = QtGui.QFrame(self.page)
        line.setGeometry(QtCore.QRect(-3, 40, 471, 20))
        line.setFrameShape(QtGui.QFrame.HLine)
        line.setFrameShadow(QtGui.QFrame.Sunken)
        # head
        self.img_head = QtGui.QGraphicsView(self.page)
        self.img_head.setGeometry(QtCore.QRect(5, 5, 43, 43))
        self.label_head = QtGui.QLabel(self.page)
        self.label_head.setGeometry(QtCore.QRect(70, 10, 251, 18))
        self.label_head.setText(_translate("Chat", "稻草人(28762822)", None))
        self.label_head.setFont(self.font)
        self.label_content = QtGui.QLabel(self.page)
        self.label_content.setGeometry(QtCore.QRect(70, 30, 381, 18))
        self.label_content.setFont(self.font2)
        self.label_content.setText(
            _translate("Chat", "[在线]悄悄是别离的生肖。。。。。", None))
        line_1 = QtGui.QFrame(self.page)
        line_1.setGeometry(QtCore.QRect(0, 440, 481, 16))
        line_1.setFrameShape(QtGui.QFrame.HLine)
        line_1.setFrameShadow(QtGui.QFrame.Sunken)
        # send
        self.textEdit = QtGui.QTextEdit(self.page)
        self.textEdit.setGeometry(QtCore.QRect(0, 450, 391, 71))
        self.button_send = QtGui.QPushButton(self.page)
        self.button_send.setGeometry(QtCore.QRect(392, 450, 81, 71))
        self.button_send.setText(_translate("Chat", "发送", None))
        # chat
        #self.scrollArea = QtGui.QScrollArea(self.page)
        #self.scrollArea.setGeometry(QtCore.QRect(0, 50, 471, 391))
        #self.scrollArea.setWidgetResizable(False)
        self.listWidget = QtGui.QListWidget(self.page)
        #self.scrollArea.setWidget(self.listWidget)
        self.listWidget.setGeometry(QtCore.QRect(0, 50, 470, 391))
        # 1
        self.item, self.widget = self.createWidget(0, self.listWidget)
        self.listWidget.setItemWidget(self.item, self.widget)
        self.item, self.widget = self.createWidget(0, self.listWidget)
        self.listWidget.setItemWidget(self.item, self.widget)
        self.item, self.widget = self.createWidget(1, self.listWidget)
        self.listWidget.setItemWidget(self.item, self.widget)
        self.item, self.widget = self.createWidget(0, self.listWidget)
        self.listWidget.setItemWidget(self.item, self.widget)
    
       
        return self.page

    def createWidget(self, style, listWidget):
        self.listWidgetItem = QtGui.QListWidgetItem(listWidget)
        self.listWidgetItem.setSizeHint(QtCore.QSize(0, 50))
        self.widget = QtGui.QWidget()
        self.graphicsView = QtGui.QGraphicsView(self.widget)
        self.label = QtGui.QTextBrowser(self.widget)
        self.label.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        if style == 0:
            self.widget.setGeometry(QtCore.QRect(0, 10, 455, 50))
            self.graphicsView.setGeometry(QtCore.QRect(5, 5, 41, 41))
            self.label.setGeometry(QtCore.QRect(50, 5, 390, 50))
        elif style == 1:
            self.widget.setGeometry(QtCore.QRect(0, 10, 455, 50))
            self.graphicsView.setGeometry(QtCore.QRect(398, 10, 41, 41))
            self.label.setGeometry(QtCore.QRect(10, 5, 390, 50))
            self.label.setAlignment(QtCore.Qt.AlignRight)
            self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        content=u'''
<html><body>
你好你好啊,嘿嘿<img src="/home/younfor/project/PyLinuxQQ/tmp/head/qq.jpg" />嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿</body></html>
        '''
        doc=QtGui.QTextDocument(self.label)
        doc.setHtml(content)
        self.label.setDocument(doc)
        # resize
        size=max(self.label.document().size().height()+5,50)
        print size
        self.listWidgetItem.setSizeHint(QtCore.QSize(445, size))
        self.widget.resize(455,size)
        self.label.resize(380,size)
        return self.listWidgetItem, self.widget
