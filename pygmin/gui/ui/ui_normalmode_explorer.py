# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_normalmode_explorer.ui'
#
# Created: Wed Apr 24 11:48:11 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(863, 613)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.splitter)
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.view3D = Show3DWithSlider(self.verticalLayoutWidget_2)
        self.view3D.setObjectName(_fromUtf8("view3D"))
        self.verticalLayout_2.addWidget(self.view3D)
        self.verticalLayoutWidget = QtGui.QWidget(self.splitter)
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.listNormalmodes = QtGui.QListWidget(self.verticalLayoutWidget)
        self.listNormalmodes.setObjectName(_fromUtf8("listNormalmodes"))
        self.verticalLayout.addWidget(self.listNormalmodes)
        self.pushClose = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushClose.setObjectName(_fromUtf8("pushClose"))
        self.verticalLayout.addWidget(self.pushClose)
        self.horizontalLayout.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 863, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionRun = QtGui.QAction(MainWindow)
        self.actionRun.setCheckable(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/run.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/run.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/run.png")), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        self.actionRun.setIcon(icon)
        self.actionRun.setObjectName(_fromUtf8("actionRun"))
        self.actionSave = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/save.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon1)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionParameters = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/preferences.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionParameters.setIcon(icon2)
        self.actionParameters.setObjectName(_fromUtf8("actionParameters"))
        self.toolBar.addAction(self.actionRun)
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addAction(self.actionParameters)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.pushClose, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Normalmodes", None, QtGui.QApplication.UnicodeUTF8))
        self.pushClose.setText(QtGui.QApplication.translate("MainWindow", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRun.setText(QtGui.QApplication.translate("MainWindow", "Play", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionParameters.setText(QtGui.QApplication.translate("MainWindow", "Parameters", None, QtGui.QApplication.UnicodeUTF8))

from pygmin.gui.show3d_with_slider import Show3DWithSlider
import resources_rc