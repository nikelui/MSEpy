# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'startWin.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_startWindow(object):
    def setupUi(self, startWindow):
        startWindow.setObjectName("startWindow")
        startWindow.resize(500, 350)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(startWindow.sizePolicy().hasHeightForWidth())
        startWindow.setSizePolicy(sizePolicy)
        startWindow.setMinimumSize(QtCore.QSize(500, 350))
        startWindow.setMaximumSize(QtCore.QSize(500, 350))
        startWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedKingdom))
        self.centralwidget = QtWidgets.QWidget(startWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(240, 247, 255);")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setStyleSheet("padding-right:20px;")
        self.titleLabel.setText("")
        self.titleLabel.setPixmap(QtGui.QPixmap(":/start/resource/about.png"))
        self.titleLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.titleLabel.setObjectName("titleLabel")
        self.gridLayout.addWidget(self.titleLabel, 0, 0, 1, 2)
        self.versionLabel = QtWidgets.QLabel(self.centralwidget)
        self.versionLabel.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.versionLabel.setObjectName("versionLabel")
        self.gridLayout.addWidget(self.versionLabel, 3, 1, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_new = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_new.setMinimumSize(QtCore.QSize(150, 60))
        self.pushButton_new.setMaximumSize(QtCore.QSize(150, 60))
        self.pushButton_new.setStyleSheet("font: 14pt \"Ubuntu\";\n"
"text-align: left;\n"
"padding-left: 10px")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/start/resource/welcome_new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_new.setIcon(icon)
        self.pushButton_new.setIconSize(QtCore.QSize(64, 64))
        self.pushButton_new.setObjectName("pushButton_new")
        self.verticalLayout.addWidget(self.pushButton_new)
        self.pushButton_open = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_open.setMinimumSize(QtCore.QSize(150, 60))
        self.pushButton_open.setMaximumSize(QtCore.QSize(150, 60))
        self.pushButton_open.setStyleSheet("font: 14pt \"Ubuntu\";\n"
"text-align: left;\n"
"padding-left: 10px")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/start/resource/welcome_open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_open.setIcon(icon1)
        self.pushButton_open.setIconSize(QtCore.QSize(64, 64))
        self.pushButton_open.setObjectName("pushButton_open")
        self.verticalLayout.addWidget(self.pushButton_open)
        self.pushButton_last = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_last.setMinimumSize(QtCore.QSize(150, 60))
        self.pushButton_last.setMaximumSize(QtCore.QSize(150, 60))
        self.pushButton_last.setStyleSheet("font: 14pt \"Ubuntu\";\n"
"text-align: left;\n"
"padding-left: 10px")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/start/resource/welcome_last.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_last.setIcon(icon2)
        self.pushButton_last.setIconSize(QtCore.QSize(64, 64))
        self.pushButton_last.setObjectName("pushButton_last")
        self.verticalLayout.addWidget(self.pushButton_last)
        self.gridLayout.addLayout(self.verticalLayout, 3, 0, 1, 1)
        self.linkLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("cmr10")
        font.setPointSize(12)
        self.linkLabel.setFont(font)
        self.linkLabel.setStyleSheet("padding-right:20px;")
        self.linkLabel.setTextFormat(QtCore.Qt.RichText)
        self.linkLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.linkLabel.setOpenExternalLinks(True)
        self.linkLabel.setObjectName("linkLabel")
        self.gridLayout.addWidget(self.linkLabel, 1, 1, 1, 1)
        startWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(startWindow)
        self.pushButton_open.clicked.connect(startWindow.openFile)
        QtCore.QMetaObject.connectSlotsByName(startWindow)
        startWindow.setTabOrder(self.pushButton_new, self.pushButton_open)
        startWindow.setTabOrder(self.pushButton_open, self.pushButton_last)

    def retranslateUi(self, startWindow):
        _translate = QtCore.QCoreApplication.translate
        startWindow.setWindowTitle(_translate("startWindow", "Magic Set Editor"))
        self.versionLabel.setText(_translate("startWindow", "Version 0.1"))
        self.pushButton_new.setText(_translate("startWindow", "New Set"))
        self.pushButton_open.setText(_translate("startWindow", "Open Set"))
        self.pushButton_last.setText(_translate("startWindow", "Last Set"))
        self.linkLabel.setText(_translate("startWindow", "<html><head/><body><p><a href=\"https://github.com/nikelui/MSEpy\"><span style=\" text-decoration: underline; color:#0000ff;\">follow on Github</span></a></p></body></html>"))

import res_rc
