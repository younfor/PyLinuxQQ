# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/gui.ui'
#
# Created: Fri Feb 20 19:05:42 2015
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

class Ui_login(object):
    def setupUi(self, login):
        login.setObjectName(_fromUtf8("login"))
        login.setEnabled(True)
        login.resize(257, 235)
        login.setSizeIncrement(QtCore.QSize(0, 0))
        login.setWindowOpacity(1.0)
        self.text_user = QtGui.QLineEdit(login)
        self.text_user.setGeometry(QtCore.QRect(70, 20, 113, 28))
        self.text_user.setObjectName(_fromUtf8("text_user"))
        self.text_pwd = QtGui.QLineEdit(login)
        self.text_pwd.setGeometry(QtCore.QRect(70, 60, 113, 28))
        self.text_pwd.setObjectName(_fromUtf8("text_pwd"))
        self.text_code = QtGui.QLineEdit(login)
        self.text_code.setGeometry(QtCore.QRect(70, 100, 113, 28))
        self.text_code.setObjectName(_fromUtf8("text_code"))
        self.btn_login = QtGui.QPushButton(login)
        self.btn_login.setGeometry(QtCore.QRect(20, 190, 93, 27))
        self.btn_login.setObjectName(_fromUtf8("btn_login"))
        self.btn_cancel = QtGui.QPushButton(login)
        self.btn_cancel.setGeometry(QtCore.QRect(140, 190, 93, 27))
        self.btn_cancel.setObjectName(_fromUtf8("btn_cancel"))
        self.lbl_user = QtGui.QLabel(login)
        self.lbl_user.setGeometry(QtCore.QRect(30, 30, 51, 21))
        self.lbl_user.setObjectName(_fromUtf8("lbl_user"))
        self.lbl_pwd = QtGui.QLabel(login)
        self.lbl_pwd.setGeometry(QtCore.QRect(30, 70, 63, 18))
        self.lbl_pwd.setObjectName(_fromUtf8("lbl_pwd"))
        
        self.lbl_code = QtGui.QLabel(login)
        self.lbl_code.setGeometry(QtCore.QRect(20, 110, 63, 18))
        self.lbl_code.setObjectName(_fromUtf8("lbl_code"))
        
        self.img_code = QtGui.QGraphicsView(login)
        self.img_code.setEnabled(True)
        self.img_code.setGeometry(QtCore.QRect(60, 130, 120, 50))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.img_code.sizePolicy().hasHeightForWidth())
        self.img_code.setSizePolicy(sizePolicy)
        self.img_code.setMaximumSize(QtCore.QSize(120, 50))
        self.img_code.setAutoFillBackground(True)
        self.img_code.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.img_code.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.img_code.setObjectName(_fromUtf8("img_code"))

        self.retranslateUi(login)
        QtCore.QObject.connect(self.text_user, QtCore.SIGNAL(_fromUtf8("editingFinished()")), login.loadCode)
        QtCore.QObject.connect(self.btn_login, QtCore.SIGNAL(_fromUtf8("clicked()")), login.checkLogin)
        QtCore.QObject.connect(self.btn_cancel, QtCore.SIGNAL(_fromUtf8("clicked()")), login.close)
        QtCore.QMetaObject.connectSlotsByName(login)

    def retranslateUi(self, login):
        login.setWindowTitle(_translate("login", "登陆", None))
        self.btn_login.setText(_translate("login", "登陆", None))
        self.btn_cancel.setText(_translate("login", "取消", None))
        self.lbl_user.setText(_translate("login", "Q Q:", None))
        self.lbl_pwd.setText(_translate("login", "密码:", None))
        self.lbl_code.setText(_translate("login", "验证码:", None))

