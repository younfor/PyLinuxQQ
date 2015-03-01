# coding=utf-8
from PyQt4 import QtCore, QtGui
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
# data
data_friends = None
data_group = None
data_discuss = None
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


def load_data(main):
    global data_friends, account, lnick, online
    # get hash
    qq.get_infoHash()
    # get friends
    data_friends = qq.get_friends()
    # get group
    thread.start_new_thread(load_group, (main,))
    # get discuss
    thread.start_new_thread(load_discuss, (main,))
    # get selfinfo
    data = qq.get_self_info()
    account = data['account']
    lnick = data['lnick']
    main.signal.emit(3)
    # get onlinebody
    online = qq.get_online_uin()
    print 'online', online
    main.signal.emit(0)
    # get face
    qq.get_face(str(account))
    main.signal.emit(1)
    # faces
    size = 0
    for user in data_friends['friends']:
        size += 1
        qq.get_face(str(user['uin']))
        if size % 20 == 0:
            main.signal.emit(1)
        print 'loadding face..', user['uin']


def load_msg(main):
    global message, g_message, d_message
    while True:
        time.sleep(0.2)
        data = qq.get_poll()
        if data is not None:
            print 'msg coming'
            if data[0]['poll_type'] == 'message':
                print 'user message'
                message = data[0]['value']
                main.signal.emit(4)
            if data[0]['poll_type'] == 'group_message':
                print 'group_message'
                g_message = data[0]['value']
                # main.signal.emit(5)
            if data[0]['poll_type'] == 'discu_message':
                print 'discu_message'
                d_message = data[0]['value']
                # main.signal.emit()
        else:
            print 'msg none'


class qqMain(QtGui.QMainWindow, QtCore.QObject):

    signal = QtCore.pyqtSignal(int)
    chat = None

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        thread.start_new_thread(load_data, (self,))
        thread.start_new_thread(load_msg, (self,))
        self.signal.connect(self.execute)
        self.ui = Ui_Main()
        self.ui.setupUi(self)
        self.show()

    def execute(self, arg):
        global opened, qqchat
        self.chat = qqchat
        if arg == 0:
            self.ui.setupFriend(data_friends, online)
        if arg == 2:
            self.ui.setupGroup(data_group)
        if arg == 6:
            self.ui.setupDiscuss(data_discuss)
        if arg == 1:
            self.ui.setupFace(self, data_friends)
        if arg == 3:
            self.ui.setupSelf(self, account, lnick)
        if arg == 4:
            self.ui.openChat(self, opened, qqchat, message)
        if arg == 5:
            self.ui.openChat(self, opened, qqchat, g_message, 1)

    def loadFace(self, id):
        qq.get_happyface(id)
# login


def start_api():
    pass


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
        qq.login_sig()

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


def sendMsg(uin, msg):
    qq.send_msg(uin, msg)


class qqChat(QtGui.QMainWindow, QtCore.QObject):

    myuin = None

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Chat()
        self.ui.setupUi(self)
        # self.show()

    def sendMsg(self, uin, msg):
        self.myuin = account
        thread.start_new_thread(sendMsg, (uin, msg))

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    qqlogin = qqLogin()
    qqchat = qqChat()
    sys.exit(app.exec_())
