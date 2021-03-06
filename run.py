# coding=utf-8
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from PyQt4.Qt import *
from PyQt4.QtCore import *
from gui.guiQQ import Ui_login
from gui.guiMainQQ import Ui_Main
from gui.guiChatQQ import Ui_Chat
from api.qqapi import PyLinuxQQ
import sys
import thread
import time

# api
qq = PyLinuxQQ('', '')
# window
qqmain = None
qqchat = None
opened = False
trayhead = 'tmp/sys/QQ.png'
traymsg = False
# data
data_friends = None
data_group = None
data_discuss = None
data_recent = None
account = None
lnick = None
online = None
message = None
g_message = None
# Main


def load_group(main):
    global data_group
    data_group = qq.get_groups()
    # print data_group
    main.signal.emit(2)


def load_discuss(main):
    global data_discuss
    data_discuss = qq.get_discuss()
    main.signal.emit(6)


def load_recent(main):
    global data_recent
    data_recent = qq.get_recent()
    main.signal.emit(8)


def load_friend(main):
    global data_friends, online
    data_friends = qq.get_friends()
    # get onlinebody
    online = qq.get_online_uin()
    print 'online', online
    main.signal.emit(0)
    # get face
    main.signal.emit(1)
    for i in range(10):
        thread.start_new_thread(load_face, (main, 10, i))


def load_self(main):
    global account, lnick
    data = qq.get_self_info()
    account = data['account']
    lnick = data['lnick']
    qq.get_face(str(account))
    main.signal.emit(3)


def load_face(main, count, i):
    size = -1
    for user in data_friends['friends']:
        size += 1
        if size % count == i:
            qq.get_face(str(user['uin']))
            print 'loadding face..', user['uin']
            main.signal.emit(1)
    main.signal.emit(1)


def load_data(main):
    global data_friends, account, lnick, online
    # get hash
    qq.get_infoHash()
    # get friends
    thread.start_new_thread(load_friend, (main,))
    # get discuss
    thread.start_new_thread(load_discuss, (main,))
    # get group
    thread.start_new_thread(load_group, (main,))
    # get selfinfo
    thread.start_new_thread(load_self, (main,))


def load_msg(main):
    global message, g_message, d_message, trayhead, traymsg
    while True:
        time.sleep(0.3)
        data = qq.get_poll()
        if data is not None:
            print 'msg coming'
            if data[0]['poll_type'] == 'message':
                print 'user message'
                traymsg = True
                message = data[0]['value']
                trayhead = 'tmp/head/' + \
                    str(data[0]['value']['from_uin']) + '.jpg'
                main.signal.emit(4)
            if data[0]['poll_type'] == 'group_message':
                print 'group_message'
                traymsg = True
                g_message = data[0]['value']
                trayhead = 'tmp/sys/group.jpg'
                main.signal.emit(5)
            if data[0]['poll_type'] == 'discu_message':
                print 'discu_message'
                traymsg = True
                d_message = data[0]['value']
                trayhead = 'tmp/sys/discuss.png'
                main.signal.emit(7)
        else:
            print 'msg none'


def load_tray(main):
    global traymsg
    while True:
        
        if traymsg == True:
            main.signal.emit(9)
            time.sleep(0.5)
            main.signal.emit(10)
            time.sleep(0.5)
        else:
            time.sleep(2)
            main.signal.emit(9)


class qqMain(QtGui.QMainWindow, QtCore.QObject):

    signal = QtCore.pyqtSignal(int)
    chat = None

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.signal.connect(self.execute)
        self.ui = Ui_Main()
        self.ui.setupUi(self)
        self.show()
        thread.start_new_thread(load_data, (self,))
        thread.start_new_thread(load_msg, (self,))
        # trayicon
        self.trayicon = QtGui.QSystemTrayIcon(self)
        self.trayicon.setIcon(QtGui.QIcon(r'tmp/sys/QQ.png'))
        self.trayicon.setToolTip(u' QQ ')
        self.trayicon.show()
        self.trayicon.activated.connect(self.trayclick)
        # traymenu
        self.min = QAction(u' 最小化 ', self, triggered=self.hide)
        self.Hy = QAction(u' 还原 ', self, triggered=self.showNormal)
        self.qiuct = QAction(u' 退出 ', self, triggered=qApp.quit)
        self.traymen = QMenu(QApplication.desktop())
        self.traymen.addAction(self.min)
        self.traymen.addAction(self.Hy)
        self.traymen.addAction(self.qiuct)
        self.trayicon.setContextMenu(self.traymen)
        self.trayicon.activated.connect(self.trayclick)
        self.trayflash()

    def trayclick(self, res):
        global traymsg, trayhead
        if res == QSystemTrayIcon.DoubleClick:
            self.showNormal()
        if res == QSystemTrayIcon.Trigger:
            # print 'click', trayhead, traymsg
            qqchat.showNormal()
            traymsg = False
            trayhead = 'tmp/sys/QQ.png'

    def trayflash(self):
        thread.start_new_thread(load_tray, (self, ))

    def execute(self, arg):
        global opened, qqchat, trayhead
        self.chat = qqchat
        if arg == 0:
            self.ui.setupFriend(data_friends, online)
            # get recent
            thread.start_new_thread(load_recent, (self,))
        if arg == 2:
            self.ui.setupGroup(data_group)
        if arg == 6:
            self.ui.setupDiscuss(data_discuss)
        if arg == 8:
            self.ui.setupRecent(data_recent)
        if arg == 1:
            self.ui.setupFace(self, data_friends)
            self.ui.setupFace_recent(self, data_recent)
        if arg == 3:
            self.ui.setupSelf(self, account, lnick)
        if arg == 4:
            self.ui.openChat(self, opened, qqchat, message)
        if arg == 5:
            self.ui.openChat(self, opened, qqchat, g_message, 1)
        if arg == 7:
            self.ui.openChat(self, opened, qqchat, d_message, 2)
        if arg == 9:
            print trayhead
            self.trayicon.setIcon(QtGui.QIcon(trayhead))
        if arg == 10:
            print '10'
            self.trayicon.setIcon(QtGui.QIcon())

    def loadFace(self, id):
        qq.get_happyface(id)
# login


def start_api():
    qq.login_sig()


def check_user(username, login):
    qq.username = username
    if qq.login_check() == True:
        print 'check code True'
        login.signal_showCode.emit()


def check_pwd(username, pwd, code, login):
    qq.username = username
    qq.password = pwd
    qq.code1 = code
    if qq.login_on() == True:
        print 'login success'
        login.signal_exit.emit()
    else:
        print 'login failed'
        login.signal_reLogin.emit()


class qqLogin(QtGui.QMainWindow, QtCore.QObject):

    hasCode = False
    signal_showCode = QtCore.pyqtSignal()
    signal_reLogin = QtCore.pyqtSignal()
    signal_exit = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.signal_showCode.connect(self.showCode)
        self.signal_reLogin.connect(self.reLogin)
        self.signal_exit.connect(self.startMain)
        self.loginGui()

    def startMain(self):
        self.close()
        global qqmain
        qqmain = qqMain()

    def reLogin(self):
        self.hideCode()
        self.ui.btn_login.setEnabled(True)
        self.ui.btn_login.setText(u'登陆')
        self.ui.text_pwd.setText(u'')
        self.hasCode = False
        thread.start_new_thread(
            check_user, (str(self.ui.text_user.text()), self))

    def loginGui(self):
        self.ui = Ui_login()
        self.ui.setupUi(self)
        self.ui.text_user.setText(u'28762822')
        self.ui.text_pwd.setText(u'199288@920808')
        self.hideCode()
        self.show()
        thread.start_new_thread(start_api, ())
        print 'start login'

    def checkLogin(self):
        self.ui.btn_login.setDisabled(True)
        self.ui.btn_login.setText(u'登陆中')
        uname = str(self.ui.text_user.text())
        pwd = str(self.ui.text_pwd.text())
        if qq.check == '1':
            code = str(self.ui.text_code.text())
            qq.code1 = code
        else:
            code = qq.code1
        thread.start_new_thread(check_pwd, (uname, pwd, code, self))

    def loadCode(self):
        # check user
        uname = str(self.ui.text_user.text())
        print uname
        thread.start_new_thread(check_user, (uname, self))

    def hideCode(self):
        self.resize(257, 150)
        self.ui.lbl_code.hide()
        self.ui.text_code.hide()
        self.ui.img_code.hide()
        self.ui.btn_login.setGeometry(QtCore.QRect(20, 110, 93, 27))
        self.ui.btn_cancel.setGeometry(QtCore.QRect(140, 110, 93, 27))

    def showCode(self):
        pixmap = QtGui.QPixmap()
        pixmap.load("api/code.jpg")
        pixmap.scaledToHeight(60)
        pixmap.scaledToWidth(120)
        self.scene_code = QtGui.QGraphicsScene(self)
        item = QtGui.QGraphicsPixmapItem(pixmap)
        self.scene_code.addItem(item)
        self.ui.img_code.setScene(self.scene_code)
        self.resize(257, 235)
        self.ui.lbl_code.setGeometry(QtCore.QRect(20, 110, 63, 18))
        self.ui.text_code.setGeometry(QtCore.QRect(70, 100, 113, 28))
        self.ui.img_code.setGeometry(QtCore.QRect(60, 130, 120, 50))
        self.ui.btn_login.setGeometry(QtCore.QRect(20, 190, 93, 27))
        self.ui.btn_cancel.setGeometry(QtCore.QRect(140, 190, 93, 27))
        self.ui.lbl_code.show()
        self.ui.text_code.show()
        self.ui.img_code.show()

# chat


def sendMsg(uin, msg, flag):
    if flag == 0:
        qq.send_msg(uin, msg)
    if flag == 1:
        qq.send_group_msg(uin, msg)
    if flag == 2:
        qq.send_discuss_msg(uin, msg)


def loadFace(uin):
    qq.get_face(uin)


class qqChat(QtGui.QMainWindow, QtCore.QObject):

    myuin = None

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Chat()
        self.ui.setupUi(self)
        # self.show()

    def sendMsg(self, uin, msg, flag):
        self.myuin = account
        thread.start_new_thread(sendMsg, (uin, msg, flag))

    def loadFace(self, uin):
        thread.start_new_thread(loadFace, (uin,))

    def loadGroupInfo(self, gcode):
        result = {}
        ginfo = qq.get_group_info(gcode)
        for item in ginfo['minfo']:
            result[item['uin']] = item
        print result
        return result

    def loadDiscussInfo(self, did):
        result = {}
        dinfo = qq.get_discuss_info(did)
        for item in dinfo['mem_info']:
            result[item['uin']] = item
        print result
        return result
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    QtGui.QApplication.setQuitOnLastWindowClosed(False)
    qqlogin = qqLogin()
    qqchat = qqChat()
    sys.exit(app.exec_())
