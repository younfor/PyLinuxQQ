# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/guiChat.ui'
#
# Created: Wed Feb 25 21:11:06 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import functools,os
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
        self.main=Chat
        Chat.setWindowTitle(_translate("Chat", "聊天", None))
        Chat.resize(575, 524)
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
        self.listWidget_Users = QtGui.QListWidget(Chat)
        self.listWidget_Users.setGeometry(QtCore.QRect(0, 0, 94, 521))
        self.listWidget_Users.setSpacing(2)
        self.line = QtGui.QFrame(Chat)
        self.line.setGeometry(QtCore.QRect(97, 0, 10, 521))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        # stack widget
        self.stackedWidget = QtGui.QStackedWidget(Chat)
        self.stackedWidget.setGeometry(QtCore.QRect(100, 0, 471, 521))
        # page
        self.stack = {}
        self.listWidget = {}
        self.sideButton = {}
        self.button_send = {}
        self.textEdit = {}
        QtCore.QMetaObject.connectSlotsByName(Chat)
        # data
        self.groupInfo={}  #gcode
        self.discussInfo={}

    def createSideButton(self, uin, title):
        # side button
        self.sideButton[uin] = QtGui.QPushButton()
        self.sideButton[uin].setGeometry(QtCore.QRect(0, 0, 101, 27))
        self.sideButton[uin].setText(_translate("Chat", title, None))
        self.sideButton[uin].setStyleSheet("QPushButton{color:red;font-size:10px;}")
        self.button_item = QtGui.QListWidgetItem(self.listWidget_Users)
        self.button_item.setSizeHint(QtCore.QSize(0, 30))
        self.listWidget_Users.setItemWidget(
            self.button_item, self.sideButton[uin])
        # click
        self.sideButton[uin].clicked.connect(
            functools.partial(self.sideButtonOnClick, uin))

    def sideButtonOnClick(self, uin):
        print 'uin-click:', uin
        self.stackedWidget.setCurrentWidget(self.stack[uin])
        self.sideButton[uin].setStyleSheet("QPushButton{color:black;font-size:10px;}")
    def createMsg(self, main, chat_from_uin, chat_msg,flag=0,g_sender=None):
        # check new
        if self.stack.get(chat_from_uin) is None:
            # user0  group1 discuss2
            if flag==0:
                self.stack[chat_from_uin] = self.createPage(chat_from_uin,main.userdict[chat_from_uin],flag)
            if flag==1:
                self.stack[chat_from_uin] = self.createPage(chat_from_uin,main.groupdict[chat_from_uin],flag)
            if flag==2:
                self.stack[chat_from_uin] = self.createPage(chat_from_uin,main.discussdict[chat_from_uin],flag)
            self.stackedWidget.addWidget(self.stack[chat_from_uin])
            if flag==0:
                self.createSideButton(
                    chat_from_uin, main.userdict[chat_from_uin]['nickname'])
                print 'add user:', chat_from_uin
            if flag==1:
                self.createSideButton(
                    chat_from_uin, main.groupdict[chat_from_uin]['name'])
                print 'add group :', chat_from_uin
            if flag==2:
                self.createSideButton(
                    chat_from_uin, main.discussdict[chat_from_uin]['name'])
                print 'add discuss :', chat_from_uin
        # change color tips
        if self.stackedWidget.currentWidget()!=self.stack[chat_from_uin]:
            self.sideButton[chat_from_uin].setStyleSheet("QPushButton{color:red;font-size:10px;}")
        # add msg
        if chat_msg is not None:
            if flag==0:
                self.item, self.widget = self.createWidget(
                    0, self.listWidget[chat_from_uin], chat_msg,chat_from_uin,flag)
            else:
                self.item, self.widget = self.createWidget(
                    0, self.listWidget[chat_from_uin], chat_msg,chat_from_uin,flag,g_sender)
            self.listWidget[chat_from_uin].setItemWidget(self.item, self.widget)
            self.listWidget[chat_from_uin].scrollToBottom()

    def createImg(self,uin,flag=0,g_sender=None):
        ex='head'
        if flag==0:
            name = str(uin)
        else:
            if flag==1 and g_sender is None:
                ex='sys'
                name='group.jpg'
            elif flag==2 and g_sender is None:
                ex='sys'
                name='discuss.png'
            else:
                name = str(g_sender)+'.jpg'
        pixmap = QtGui.QPixmap()

        if not os.path.exists('tmp/'+ex+'/' + name ):
            if flag!=0:
                self.main.loadFace(g_sender)
                print 'load group face'
            name = 'qq.jpg'
        print 'pic:','tmp/',ex,'/',name
        pixmap.load('tmp/'+ex+'/' + name )
        scene = QtGui.QGraphicsScene()
        item = QtGui.QGraphicsPixmapItem(pixmap)
        scene.addItem(item)
        return scene
    def createPage(self, chat_from_uin,userinfo,flag=0):
        # load groupInfo
        if flag==1:
            if self.groupInfo.get(userinfo['code']) is None:
                self.groupInfo[chat_from_uin]=self.main.loadGroupInfo(userinfo['code'])
        if flag==2:
            if self.discussInfo.get(userinfo['did']) is None:
                self.discussInfo[chat_from_uin]=self.main.loadDiscussInfo(userinfo['did'])
        self.page = QtGui.QWidget()
        line = QtGui.QFrame(self.page)
        line.setGeometry(QtCore.QRect(-3, 40, 471, 20))
        line.setFrameShape(QtGui.QFrame.HLine)
        line.setFrameShadow(QtGui.QFrame.Sunken)
        # head
        self.img_head = QtGui.QGraphicsView(self.page)
        self.img_head.setGeometry(QtCore.QRect(1, 1, 60, 60))
        if flag==0:
            self.img_head.setScene(self.createImg(chat_from_uin))
        if flag!=0:
            self.img_head.setScene(self.createImg(chat_from_uin,flag))
        self.img_head.resize(50,50)
        self.label_head = QtGui.QLabel(self.page)
        self.label_head.setGeometry(QtCore.QRect(70, 10, 251, 18))
        # nickname
        if flag==0:
            title=userinfo['nickname']
            if userinfo['markname'] != 'None':
                title=userinfo['markname']+'('+title+')'
        else:
            title=userinfo['name']
        self.label_head.setText(_translate("Chat", title, None))
        self.label_head.setFont(self.font)
        self.label_content = QtGui.QLabel(self.page)
        self.label_content.setGeometry(QtCore.QRect(70, 30, 381, 18))
        self.label_content.setFont(self.font2)
        # content
        if flag==0:
            self.label_content.setText(
                _translate("Chat", "[在线]", None))
        line_1 = QtGui.QFrame(self.page)
        line_1.setGeometry(QtCore.QRect(0, 440, 481, 16))
        line_1.setFrameShape(QtGui.QFrame.HLine)
        line_1.setFrameShadow(QtGui.QFrame.Sunken)
        # send
        self.textEdit[chat_from_uin] = QtGui.QTextEdit(self.page)
        self.textEdit[chat_from_uin].setGeometry(QtCore.QRect(0, 450, 391, 71))
        self.button_send[chat_from_uin] = QtGui.QPushButton(self.page)
        self.button_send[chat_from_uin].setGeometry(QtCore.QRect(392, 450, 81, 71))
        self.button_send[chat_from_uin].setText(_translate("Chat", "发送", None))
        self.button_send[chat_from_uin].clicked.connect(
            functools.partial(self.sendButtonOnClick, chat_from_uin))
        # chat
        self.listWidget[chat_from_uin] = QtGui.QListWidget(self.page)
        self.listWidget[chat_from_uin].setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget[chat_from_uin].setGeometry(
            QtCore.QRect(0, 50, 470, 391))
        self.listWidget[chat_from_uin].setSpacing(3)
        return self.page
    def sendButtonOnClick(self,uin):
        print 'ready to send msg'
        msg=u'{0}'.format(self.textEdit[uin].toPlainText ()).replace(b'\n',b' ')
        if msg != '':
            print 'ready:',msg
            self.textEdit[uin].setPlainText('')
            # add msg
            self.main.sendMsg(uin,msg)
            print 'myuin:',self.main.myuin
            self.item, self.widget = self.createWidget(
                1, self.listWidget[uin], msg,self.main.myuin)
            self.listWidget[uin].setItemWidget(self.item, self.widget)
            self.listWidget[uin].scrollToBottom()
            
        else:
            print 'null msg'
    def createWidget(self, style, listWidget, chat_msg,uin,flag=0,g_sender=None):
        self.listWidgetItem = QtGui.QListWidgetItem(listWidget)
        self.listWidgetItem.setSizeHint(QtCore.QSize(0, 50))
        self.widget = QtGui.QWidget()
        self.graphicsView = QtGui.QGraphicsView(self.widget)
        self.label = QtGui.QTextBrowser(self.widget)
        self.label.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        orient=''
        if flag==0:
            ruin=uin
        else:
            ruin=g_sender
            print 'img senderuin:',ruin
        if style == 0:
            self.widget.setGeometry(QtCore.QRect(0, 10, 455, 50))
            self.graphicsView.setGeometry(QtCore.QRect(5, 5, 60, 60))
            self.graphicsView.setScene(self.createImg(ruin,flag,g_sender))
            self.graphicsView.resize(50,50)
            self.label.setGeometry(QtCore.QRect(50, 5, 390, 50))
            orient='left'
        elif style == 1:
            self.widget.setGeometry(QtCore.QRect(0, 10, 455, 50))
            self.graphicsView.setGeometry(QtCore.QRect(392, 5, 60, 60))
            self.graphicsView.setScene(self.createImg(ruin,flag,g_sender))
            self.graphicsView.resize(50,50)
            self.label.setGeometry(QtCore.QRect(10, 5, 390, 50))
            orient='right'
        # msg edit
        if flag==1:
            nick=self.groupInfo[uin][g_sender]['nick']
        if flag==2:
            nick=self.discussInfo[uin][g_sender]['nick']
        if flag==1 or flag==2:
            chat_msg=u'<p><b>'+nick+'</b></p><p>'+chat_msg+'</p>'
        content = u'''
<html><body><p align="'''+orient+'''"> ''' + chat_msg + '''</p></body></html>
        '''
        doc = QtGui.QTextDocument(self.label)
        doc.setHtml(content)
        self.label.setDocument(doc)
        # resize
        size = max(self.label.document().size().height() + 5, 50)
        self.listWidgetItem.setSizeHint(QtCore.QSize(445, size))
        self.widget.resize(455, size)
        self.label.resize(380, size)
        return self.listWidgetItem, self.widget
