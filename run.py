# coding=utf-8
from PyQt4 import QtCore, QtGui
from gui.gui import Ui_login
from api.qqapi import PyLinuxQQ
import sys
import thread

qq = PyLinuxQQ('', '')

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
    else:
        print 'login failed'
        login.signal_reLogin.emit()


class Login(QtGui.QMainWindow, QtCore.QObject):

    hasCode = False
    signal_showCode = QtCore.pyqtSignal()
    signal_reLogin = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        thread.start_new_thread(start_api,())
        self.signal_showCode.connect(self.showCode)
        self.signal_reLogin.connect(self.reLogin)
        self.loginGui()

    def reLogin(self):
        self.hideCode()
        self.ui.btn_login.setEnabled(True)
        self.ui.btn_login.setText(u'登陆')
        self.hasCode = False

    def loginGui(self):
        self.ui = Ui_login()
        self.ui.setupUi(self)
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
        if self.hasCode == True:
            return
        self.hasCode = True
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

# get friendslist
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    myqq = Login()
    sys.exit(app.exec_())
