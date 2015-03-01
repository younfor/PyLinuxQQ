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
        self.main=Main
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
        self.scrollArea = QtGui.QScrollArea(self.tab_3)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setGeometry(QtCore.QRect(0, 7, 261, 361))
        self.scrollArea.setWidgetResizable(False)
        self.toolBox_group = QtGui.QToolBox()
        self.scrollArea.setWidget(self.toolBox_group)
        self.toolBox_group.setGeometry(QtCore.QRect(0, 7, 250, 400))
        self.tabWidget.addTab(self.tab_3, _fromUtf8("    群   组   "))
        self.tabWidget.setCurrentIndex(1)
        self.toolBox_group.currentChanged.connect(self.onToolBoxChanged_group)
            #discuss
        self.listWidget_discuss = QtGui.QListWidget()
        self.toolBox_group.addItem(self.listWidget_discuss, _fromUtf8('讨论组'))
        self.listWidget_discuss.setGeometry(QtCore.QRect(0, 1, 238, 301))
        #QtCore.QObject.connect(self.listWidget_discuss, QtCore.SIGNAL(_fromUtf8("itemDoubleClicked(QListWidgetItem*)")), self.itemOnDoubleClickedDiscuss)
            #group
        self.listWidget_group = QtGui.QListWidget()
        self.toolBox_group.addItem(self.listWidget_group, _fromUtf8('群 组'))
        self.toolBox_group.setCurrentIndex(1)
        self.listWidget_group.setGeometry(QtCore.QRect(0, 1, 238, 301))
        self.toolsize_group=[0,0]
        self.graphicsView_group = {}
        #QtCore.QObject.connect(self.listWidget_group, QtCore.SIGNAL(_fromUtf8("itemDoubleClicked(QListWidgetItem*)")), self.itemOnDoubleClickedDiscuss)
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
            self.graphicsView[data['friends'][i]['uin']].setScene(scene)
            self.graphicsView[data['friends'][i]['uin']].resize(50,50)
    def itemOnDoubleClicked(self,item):
        print 'double itemDoubleClicked'
        print item.listWidget().itemWidget(item)
        widget=item.listWidget().itemWidget(item)
        uin=int(widget.property('uin').toString())
        print uin
        self.main.chat.ui.createMsg(self,uin,None)
        self.main.chat.showNormal()
    def createImg(self,flag,uin):
        pixmap = QtGui.QPixmap()
        if flag=='discuss':
            url='tmp/sys/discuss.png'
        if flag=='group':
            url='tmp/sys/group.jpg'
        pixmap.load(url)
        scene = QtGui.QGraphicsScene()
        item = QtGui.QGraphicsPixmapItem(pixmap)
        scene.addItem(item)
        return scene
    def setupGroup(self,data):
        print 'group' 
        self.groupdict={}
        for g in data['gnamelist']:
            info={'name':g['name'],'gid':g['gid'],'code':g['code']}
            self.groupdict[g['gid']]=info
            item,widget=self.createWidget_group(self.listWidget_group,g['name'],g['gid'],'group')
            self.listWidget_group.setItemWidget(item, widget)
        self.toolsize_group[1]=len(data['gnamelist'])
        self.toolBox_group.resize(QtCore.QSize(250,self.toolsize_group[1]*48+len(self.toolsize_group)*34))
    def onToolBoxChanged_group(self,index):
        self.toolBox_group.resize(QtCore.QSize(250,self.toolsize_group[index]*48+len(self.toolsize_group)*34))
    def onToolBoxChanged(self,index):
        self.toolBox.resize(QtCore.QSize(250,self.toolsize[index]*48+len(self.toolsize)*34))

    def setupDiscuss(self,data):
        print 'discuss' 
        self.discussdict={}
        for g in data['dnamelist']:
            info={'name':g['name'],'did':g['did']}
            self.discussdict[g['did']]=info
            item,widget=self.createWidget_group(self.listWidget_discuss,g['name'],g['did'],'discuss')
            self.listWidget_discuss.setItemWidget(item, widget)
        self.toolsize_group[0]=len(data['dnamelist'])
        
    def setupFriend(self, data,online):
        print 'type',type(data['friends'][0]['uin'])
        # categories
        if data['categories'][0]['index'] == 0:
            self.listWidget = {}
        else:
            self.listWidget = {0: QtGui.QListWidget()}
            self.toolBox.addItem(self.listWidget[0], _fromUtf8('我的好友'))
            self.listWidget[0].setGeometry(QtCore.QRect(0, 1, 238, 301))
            QtCore.QObject.connect(self.listWidget[0], QtCore.SIGNAL(_fromUtf8("itemDoubleClicked(QListWidgetItem*)")), self.itemOnDoubleClicked)
            #QtCore.QObject.connect(self.listWidget, QtCore.SIGNAL(_fromUtf8("itemDoubleClicked(QListWidgetItem*)")), self.listWidget.scrollToBottom)
        for cat in data['categories']:
            self.listWidget[cat['index']] = QtGui.QListWidget()
            self.toolBox.addItem(
                self.listWidget[cat['index']], _fromUtf8(cat['name']))
            self.listWidget[cat['index']].setGeometry(
                QtCore.QRect(0, 1, 238, 301))
            QtCore.QObject.connect(self.listWidget[cat['index']], QtCore.SIGNAL(_fromUtf8("itemDoubleClicked(QListWidgetItem*)")), self.itemOnDoubleClicked)
        self.graphicsView = {}
        # userlist
        self.userdict={}
        for i in range(len(data['friends'])):
            info={'markname':'None','nickname':data['info'][i]['nick'],'online':False,'cat':data['friends'][i]['categories']}
            print info
            self.userdict[data['friends'][i]['uin']]=info
        # markname   
        for mark in data['marknames']:
            self.userdict[mark['uin']]['markname']=mark['markname']
        # online
        cat_count={}
        for on in online:
            self.userdict.get(on['uin'])['online']=True
            arg1=self.listWidget[self.userdict[on['uin']].get('cat')]
            arg2=self.userdict[on['uin']].get('nickname')
            arg3=self.userdict[on['uin']].get('markname')
            arg4=on['uin']
            self.item, self.widget = self.createWidget(arg1,arg2,arg3,arg4)
            arg1.setItemWidget(
                self.item, self.widget)
            #count
            if cat_count.get(self.userdict[on['uin']].get('cat')):
                print True
                cat_count[self.userdict[on['uin']].get('cat')]+=1
            else:
                cat_count[self.userdict[on['uin']].get('cat')]=1
            print 'cat:',self.userdict[on['uin']].get('cat'),'value:',cat_count[self.userdict[on['uin']].get('cat')]
        # widget
        for user in data['friends']:
            if self.userdict[user['uin']].get('online')==True:
                continue
            arg1=self.listWidget[self.userdict[user['uin']].get('cat')]
            arg2=self.userdict[user['uin']].get('nickname')
            arg3=self.userdict[user['uin']].get('markname')
            arg4=user['uin']
            self.item, self.widget = self.createWidget(arg1,arg2,arg3,arg4)
            arg1.setItemWidget(
                self.item, self.widget)
        # size
        self.toolsize = []
        j=-1
        for key,val in self.listWidget.items():
            j+=1
            size = len(val)
            print size
            self.toolsize.append(size)
            self.toolBox.setItemText(j,self.toolBox.itemText(j)+'('+str(cat_count.get(key,0))+'/'+str(size)+')')
        self.toolBox.setCurrentIndex(j)
        self.toolBox.currentChanged.connect(self.onToolBoxChanged)
        self.toolBox.resize(QtCore.QSize(250,self.toolsize[0]*48+len(self.toolsize)*34))
    def onToolBoxChanged(self,index):
        self.toolBox.resize(QtCore.QSize(250,self.toolsize[index]*48+len(self.toolsize)*34))
    
    def createWidget_group(self,listWidget,title,guin,flag):
        self.listWidgetItem = QtGui.QListWidgetItem(listWidget)
        self.listWidgetItem.setSizeHint(QtCore.QSize(0, 48))
        self.widget = QtGui.QWidget()
        self.widget.setProperty('guin',guin)
        self.widget.setGeometry(QtCore.QRect(0, 0, 238, 51))
        self.graphicsView_group[guin] = QtGui.QGraphicsView(self.widget)
        self.graphicsView_group[guin].setGeometry(QtCore.QRect(1, 1, 60, 60))
        self.graphicsView_group[guin].setScene(self.createImg(flag,guin))
        self.graphicsView_group[guin].resize(50,50)
        self.lbl_title = QtGui.QLabel(self.widget)
        self.lbl_title.setGeometry(QtCore.QRect(60, 10, 181, 18))
        self.lbl_title.setFont(self.font2)
        self.lbl_title.setText(_translate("Main", title, None))
        return self.listWidgetItem, self.widget
    def createWidget(self,listWidget, title,markname,uin):
        self.listWidgetItem = QtGui.QListWidgetItem(listWidget)
        self.listWidgetItem.setSizeHint(QtCore.QSize(0, 48))
        self.widget = QtGui.QWidget()
        self.widget.setProperty('uin',uin)
        self.widget.setGeometry(QtCore.QRect(0, 0, 238, 51))
        self.graphicsView[uin] = QtGui.QGraphicsView(self.widget)
        self.graphicsView[uin].setGeometry(QtCore.QRect(1, 1, 38, 38))
        self.lbl_title = QtGui.QLabel(self.widget)
        self.lbl_title.setGeometry(QtCore.QRect(60, 10, 181, 18))
        self.lbl_title.setFont(self.font2)
        if markname != 'None':
            title=markname+'('+title+')'
        self.lbl_title.setText(_translate("Main", title, None))
        self.lbl_comment = QtGui.QLabel(self.widget)
        self.lbl_comment.setGeometry(QtCore.QRect(60, 30, 181, 18))
        info=self.userdict.get(uin)
        if info['online']:
            self.lbl_comment.setText(_translate("Main", '[在线]', None))
        else:
            self.lbl_comment.setText(_translate("Main", '[离线]', None))
        self.lbl_comment.setFont(self.font3)
        return self.listWidgetItem, self.widget
    def openChat(self,main,opened,qqchat,msg,flag=0):
        '''
        content: [["font", {size: 10, color: "000000", style: [0, 0, 0], name: "宋体"}], "你好啊，", ["face", 3], "嘿嘿 "]
        0: ["font", {size: 10, color: "000000", style: [0, 0, 0], name: "宋体"}]
        1: "你好啊，"
        2: ["face", 3]
        3: "嘿嘿 "
        from_uin: 603579481
        msg_id: 54156
        msg_id2: 138519
        msg_type: 9
        reply_ip: 176488600
        time: 1424938754
        to_uin: 28762822
        '''
        # flag 0qq, 1group, 2discuss
        if opened==False:
            opened==True
            qqchat.show()
        chat_from_uin=msg['from_uin']
        chat_msg=''
        for i in range(1,len(msg['content'])):
            if type(msg['content'][i]) is list:
                chat_msg+='<img src="tmp/face/'+str(msg['content'][i][1])+'.gif" />'
                main.loadFace(msg['content'][i][1])
                print 'loadface:',msg['content'][i][1]
            else:
                chat_msg+=msg['content'][i]
        print chat_from_uin,':',chat_msg
        qqchat.ui.createMsg(self,chat_from_uin,chat_msg)