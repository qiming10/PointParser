# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PointParser.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(300, 456)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.gbox_input = QGroupBox(self.centralwidget)
        self.gbox_input.setObjectName(u"gbox_input")
        self.verticalLayout_2 = QVBoxLayout(self.gbox_input)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.ptext_input = QPlainTextEdit(self.gbox_input)
        self.ptext_input.setObjectName(u"ptext_input")

        self.verticalLayout_2.addWidget(self.ptext_input)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.chkbox_auto_copy = QCheckBox(self.gbox_input)
        self.chkbox_auto_copy.setObjectName(u"chkbox_auto_copy")
        self.chkbox_auto_copy.setChecked(True)

        self.horizontalLayout_2.addWidget(self.chkbox_auto_copy)

        self.chkbox_auto_clear = QCheckBox(self.gbox_input)
        self.chkbox_auto_clear.setObjectName(u"chkbox_auto_clear")
        self.chkbox_auto_clear.setCheckable(True)
        self.chkbox_auto_clear.setChecked(False)

        self.horizontalLayout_2.addWidget(self.chkbox_auto_clear)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout_4.addWidget(self.gbox_input)

        self.gbox_output = QGroupBox(self.centralwidget)
        self.gbox_output.setObjectName(u"gbox_output")
        self.verticalLayout_3 = QVBoxLayout(self.gbox_output)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.ptext_output = QPlainTextEdit(self.gbox_output)
        self.ptext_output.setObjectName(u"ptext_output")

        self.verticalLayout_3.addWidget(self.ptext_output)

        self.btn_save_output = QPushButton(self.gbox_output)
        self.btn_save_output.setObjectName(u"btn_save_output")

        self.verticalLayout_3.addWidget(self.btn_save_output)


        self.verticalLayout_4.addWidget(self.gbox_output)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line)

        self.gbox_save = QGroupBox(self.centralwidget)
        self.gbox_save.setObjectName(u"gbox_save")
        self.verticalLayout = QVBoxLayout(self.gbox_save)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tbl_save = QTableWidget(self.gbox_save)
        self.tbl_save.setObjectName(u"tbl_save")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbl_save.sizePolicy().hasHeightForWidth())
        self.tbl_save.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.tbl_save)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_save2txt = QPushButton(self.gbox_save)
        self.btn_save2txt.setObjectName(u"btn_save2txt")

        self.horizontalLayout.addWidget(self.btn_save2txt)

        self.btn_save2xls = QPushButton(self.gbox_save)
        self.btn_save2xls.setObjectName(u"btn_save2xls")

        self.horizontalLayout.addWidget(self.btn_save2xls)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_4.addWidget(self.gbox_save)

        self.verticalLayout_4.setStretch(0, 2)
        self.verticalLayout_4.setStretch(1, 2)
        self.verticalLayout_4.setStretch(3, 6)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 300, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Point Parser", None))
        self.gbox_input.setTitle(QCoreApplication.translate("MainWindow", u"\u7c98\u8d34\u6846", None))
        self.chkbox_auto_copy.setText(QCoreApplication.translate("MainWindow", u"\u81ea\u52a8\u590d\u5236", None))
        self.chkbox_auto_clear.setText(QCoreApplication.translate("MainWindow", u"\u81ea\u52a8\u6e05\u9664", None))
        self.gbox_output.setTitle(QCoreApplication.translate("MainWindow", u"\u89e3\u6790\u7ed3\u679c", None))
        self.btn_save_output.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u5230\u8868\u683c\u4e2d", None))
        self.gbox_save.setTitle(QCoreApplication.translate("MainWindow", u"\u5df2\u4fdd\u5b58\u6570\u636e", None))
        self.btn_save2txt.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u6210txt", None))
        self.btn_save2xls.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u6210excel", None))
    # retranslateUi

