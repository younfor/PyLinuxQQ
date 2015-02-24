# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/guiMain.ui'
#
# Created: Tue Feb 24 13:58:32 2015
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

class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName(_fromUtf8("Main"))
        Main.resize(268, 513)
        self.img_head = QtGui.QGraphicsView(Main)
        self.img_head.setGeometry(QtCore.QRect(10, 10, 71, 61))
        self.img_head.setObjectName(_fromUtf8("img_head"))
        self.lbl_head = QtGui.QLabel(Main)
        self.lbl_head.setGeometry(QtCore.QRect(110, 17, 131, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Helvetica"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_head.setFont(font)
        self.lbl_head.setObjectName(_fromUtf8("lbl_head"))
        self.lbl_content = QtGui.QLabel(Main)
        self.lbl_content.setGeometry(QtCore.QRect(110, 50, 151, 18))
        self.lbl_content.setObjectName(_fromUtf8("lbl_content"))
        self.text_search = QtGui.QLineEdit(Main)
        self.text_search.setGeometry(QtCore.QRect(0, 80, 268, 28))
        self.text_search.setToolTip(_fromUtf8(""))
        self.text_search.setInputMethodHints(QtCore.Qt.ImhNone)
        self.text_search.setInputMask(_fromUtf8(""))
        self.text_search.setText(_fromUtf8(""))
        self.text_search.setObjectName(_fromUtf8("text_search"))
        self.tabWidget = QtGui.QTabWidget(Main)
        self.tabWidget.setGeometry(QtCore.QRect(0, 110, 268, 401))
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.listWidget = QtGui.QListWidget(self.tab)
        self.listWidget.setGeometry(QtCore.QRect(0, 11, 261, 351))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.toolBox = QtGui.QToolBox(self.tab_2)
        self.toolBox.setGeometry(QtCore.QRect(0, 7, 261, 361))
        self.toolBox.setObjectName(_fromUtf8("toolBox"))
        self.page = QtGui.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 261, 297))
        self.page.setObjectName(_fromUtf8("page"))
        self.listWidget_2 = QtGui.QListWidget(self.page)
        self.listWidget_2.setGeometry(QtCore.QRect(0, 1, 261, 301))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget_2.sizePolicy().hasHeightForWidth())
        self.listWidget_2.setSizePolicy(sizePolicy)
        self.listWidget_2.setMinimumSize(QtCore.QSize(200, 0))
        self.listWidget_2.setResizeMode(QtGui.QListView.Adjust)
        self.listWidget_2.setObjectName(_fromUtf8("listWidget_2"))
        self.widget = QtGui.QWidget(self.page)
        self.widget.setGeometry(QtCore.QRect(0, 0, 261, 51))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.graphicsView = QtGui.QGraphicsView(self.widget)
        self.graphicsView.setGeometry(QtCore.QRect(10, 7, 38, 38))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(70, 10, 121, 18))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Helvetica"))
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(70, 30, 191, 18))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Helvetica"))
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.scrollArea = QtGui.QScrollArea(self.page)
        self.scrollArea.setGeometry(QtCore.QRect(50, 100, 171, 151))
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 163, 143))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.toolBox.addItem(self.page, _fromUtf8(""))
        self.page_2 = QtGui.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 92, 22))
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.toolBox.addItem(self.page_2, _fromUtf8(""))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))

        self.retranslateUi(Main)
        self.tabWidget.setCurrentIndex(1)
        self.toolBox.setCurrentIndex(0)
        QtCore.QObject.connect(self.toolBox, QtCore.SIGNAL(_fromUtf8("currentChanged(int)")), self.toolBox.showMaximized)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        Main.setWindowTitle(_translate("Main", "PyLinuxQQ", None))
        self.lbl_head.setText(_translate("Main", "稻草人", None))
        self.lbl_content.setText(_translate("Main", "悄悄留下，生肖别离", None))
        self.text_search.setPlaceholderText(_translate("Main", "搜索好友...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Main", "Tab 1", None))
        self.label.setText(_translate("Main", "稻草人", None))
        self.label_2.setText(_translate("Main", "[在线]流年似水。。", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("Main", "Page 1", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("Main", "Page 2", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Main", "Tab 2", None))

