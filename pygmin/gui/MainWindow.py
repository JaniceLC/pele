# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created: Wed Feb 13 17:31:40 2013
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
        MainWindow.resize(839, 623)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.BHTab = QtGui.QWidget()
        self.BHTab.setObjectName(_fromUtf8("BHTab"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.BHTab)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.widget = Show3D(self.BHTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout_3.addWidget(self.widget)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_2 = QtGui.QLabel(self.BHTab)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_3.addWidget(self.label_2)
        self.listWidget = QtGui.QListWidget(self.BHTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setMaximumSize(QtCore.QSize(200, 16777215))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.verticalLayout_3.addWidget(self.listWidget)
        self.pushTakestepExplorer = QtGui.QPushButton(self.BHTab)
        self.pushTakestepExplorer.setObjectName(_fromUtf8("pushTakestepExplorer"))
        self.verticalLayout_3.addWidget(self.pushTakestepExplorer)
        self.btnRun = QtGui.QPushButton(self.BHTab)
        self.btnRun.setObjectName(_fromUtf8("btnRun"))
        self.verticalLayout_3.addWidget(self.btnRun)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.tabWidget.addTab(self.BHTab, _fromUtf8(""))
        self.NEBTab = QtGui.QWidget()
        self.NEBTab.setObjectName(_fromUtf8("NEBTab"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.NEBTab)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setContentsMargins(5, -1, -1, -1)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.oglPath = Show3D(self.NEBTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.oglPath.sizePolicy().hasHeightForWidth())
        self.oglPath.setSizePolicy(sizePolicy)
        self.oglPath.setObjectName(_fromUtf8("oglPath"))
        self.verticalLayout.addWidget(self.oglPath)
        self.sliderFrame = QtGui.QSlider(self.NEBTab)
        self.sliderFrame.setOrientation(QtCore.Qt.Horizontal)
        self.sliderFrame.setObjectName(_fromUtf8("sliderFrame"))
        self.verticalLayout.addWidget(self.sliderFrame)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(6, -1, -1, -1)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.listMinima1 = QtGui.QListWidget(self.NEBTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listMinima1.sizePolicy().hasHeightForWidth())
        self.listMinima1.setSizePolicy(sizePolicy)
        self.listMinima1.setMaximumSize(QtCore.QSize(200, 16777215))
        self.listMinima1.setObjectName(_fromUtf8("listMinima1"))
        self.verticalLayout_5.addWidget(self.listMinima1)
        self.listMinima2 = QtGui.QListWidget(self.NEBTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listMinima2.sizePolicy().hasHeightForWidth())
        self.listMinima2.setSizePolicy(sizePolicy)
        self.listMinima2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.listMinima2.setObjectName(_fromUtf8("listMinima2"))
        self.verticalLayout_5.addWidget(self.listMinima2)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setContentsMargins(20, 0, 20, -1)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.btnAlign = QtGui.QPushButton(self.NEBTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnAlign.sizePolicy().hasHeightForWidth())
        self.btnAlign.setSizePolicy(sizePolicy)
        self.btnAlign.setMaximumSize(QtCore.QSize(100, 100))
        self.btnAlign.setObjectName(_fromUtf8("btnAlign"))
        self.gridLayout_2.addWidget(self.btnAlign, 1, 0, 1, 1)
        self.btnReconnect = QtGui.QPushButton(self.NEBTab)
        self.btnReconnect.setObjectName(_fromUtf8("btnReconnect"))
        self.gridLayout_2.addWidget(self.btnReconnect, 3, 1, 1, 1)
        self.btnInvert = QtGui.QPushButton(self.NEBTab)
        self.btnInvert.setObjectName(_fromUtf8("btnInvert"))
        self.gridLayout_2.addWidget(self.btnInvert, 1, 1, 1, 1)
        self.btnNEB = QtGui.QPushButton(self.NEBTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnNEB.sizePolicy().hasHeightForWidth())
        self.btnNEB.setSizePolicy(sizePolicy)
        self.btnNEB.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btnNEB.setObjectName(_fromUtf8("btnNEB"))
        self.gridLayout_2.addWidget(self.btnNEB, 2, 0, 1, 1)
        self.btnConnect = QtGui.QPushButton(self.NEBTab)
        self.btnConnect.setObjectName(_fromUtf8("btnConnect"))
        self.gridLayout_2.addWidget(self.btnConnect, 3, 0, 1, 1)
        self.btn_close_all = QtGui.QPushButton(self.NEBTab)
        self.btn_close_all.setObjectName(_fromUtf8("btn_close_all"))
        self.gridLayout_2.addWidget(self.btn_close_all, 2, 1, 1, 1)
        self.btnShowGraph = QtGui.QPushButton(self.NEBTab)
        self.btnShowGraph.setObjectName(_fromUtf8("btnShowGraph"))
        self.gridLayout_2.addWidget(self.btnShowGraph, 5, 0, 1, 1)
        self.btnDisconnectivity_graph = QtGui.QPushButton(self.NEBTab)
        self.btnDisconnectivity_graph.setObjectName(_fromUtf8("btnDisconnectivity_graph"))
        self.gridLayout_2.addWidget(self.btnDisconnectivity_graph, 5, 1, 1, 1)
        self.btnconnect_in_optim = QtGui.QPushButton(self.NEBTab)
        self.btnconnect_in_optim.setObjectName(_fromUtf8("btnconnect_in_optim"))
        self.gridLayout_2.addWidget(self.btnconnect_in_optim, 4, 1, 1, 1)
        self.btn_connect_all = QtGui.QPushButton(self.NEBTab)
        self.btn_connect_all.setObjectName(_fromUtf8("btn_connect_all"))
        self.gridLayout_2.addWidget(self.btn_connect_all, 4, 0, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout_5)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.tabWidget.addTab(self.NEBTab, _fromUtf8(""))
        self.TSTab = QtGui.QWidget()
        self.TSTab.setObjectName(_fromUtf8("TSTab"))
        self.gridLayout_8 = QtGui.QGridLayout(self.TSTab)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.oglTS = Show3DWithSlider(self.TSTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.oglTS.sizePolicy().hasHeightForWidth())
        self.oglTS.setSizePolicy(sizePolicy)
        self.oglTS.setObjectName(_fromUtf8("oglTS"))
        self.gridLayout_8.addWidget(self.oglTS, 0, 0, 1, 1)
        self.verticalLayout_9 = QtGui.QVBoxLayout()
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.list_TS = QtGui.QListWidget(self.TSTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list_TS.sizePolicy().hasHeightForWidth())
        self.list_TS.setSizePolicy(sizePolicy)
        self.list_TS.setMaximumSize(QtCore.QSize(200, 16777215))
        self.list_TS.setObjectName(_fromUtf8("list_TS"))
        self.verticalLayout_9.addWidget(self.list_TS)
        self.gridLayout_8.addLayout(self.verticalLayout_9, 0, 2, 1, 1)
        self.tabWidget.addTab(self.TSTab, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 839, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuSimulation = QtGui.QMenu(self.menubar)
        self.menuSimulation.setObjectName(_fromUtf8("menuSimulation"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuActions = QtGui.QMenu(self.menubar)
        self.menuActions.setObjectName(_fromUtf8("menuActions"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtGui.QAction(MainWindow)
        self.actionNew.setObjectName(_fromUtf8("actionNew"))
        self.actionClear = QtGui.QAction(MainWindow)
        self.actionClear.setObjectName(_fromUtf8("actionClear"))
        self.actionConnect = QtGui.QAction(MainWindow)
        self.actionConnect.setObjectName(_fromUtf8("actionConnect"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionDelete_Minimum = QtGui.QAction(MainWindow)
        self.actionDelete_Minimum.setObjectName(_fromUtf8("actionDelete_Minimum"))
        self.actionEditParams = QtGui.QAction(MainWindow)
        self.actionEditParams.setObjectName(_fromUtf8("actionEditParams"))
        self.actionMerge_Minima = QtGui.QAction(MainWindow)
        self.actionMerge_Minima.setObjectName(_fromUtf8("actionMerge_Minima"))
        self.menuSimulation.addAction(self.actionConnect)
        self.menuHelp.addAction(self.actionAbout)
        self.menuActions.addAction(self.actionDelete_Minimum)
        self.menuActions.addAction(self.actionMerge_Minima)
        self.menuActions.addAction(self.actionEditParams)
        self.menubar.addAction(self.menuSimulation.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuActions.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.listWidget, QtCore.SIGNAL(_fromUtf8("currentItemChanged(QListWidgetItem*,QListWidgetItem*)")), MainWindow.SelectMinimum)
        QtCore.QObject.connect(self.btnRun, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.StartBasinHopping)
        QtCore.QObject.connect(self.btnAlign, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.AlignMinima)
        QtCore.QObject.connect(self.btnNEB, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.ConnectMinima)
        QtCore.QObject.connect(self.listMinima1, QtCore.SIGNAL(_fromUtf8("currentItemChanged(QListWidgetItem*,QListWidgetItem*)")), MainWindow.SelectMinimum1)
        QtCore.QObject.connect(self.listMinima2, QtCore.SIGNAL(_fromUtf8("currentItemChanged(QListWidgetItem*,QListWidgetItem*)")), MainWindow.SelectMinimum2)
        QtCore.QObject.connect(self.sliderFrame, QtCore.SIGNAL(_fromUtf8("sliderMoved(int)")), MainWindow.showFrame)
        QtCore.QObject.connect(self.actionConnect, QtCore.SIGNAL(_fromUtf8("activated()")), MainWindow.connect)
        QtCore.QObject.connect(self.btnInvert, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.Invert)
        QtCore.QObject.connect(self.btnConnect, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.doubleEndedConnect)
        QtCore.QObject.connect(self.btnShowGraph, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.show_graph)
        QtCore.QObject.connect(self.actionDelete_Minimum, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.delete_minimum)
        QtCore.QObject.connect(self.btnDisconnectivity_graph, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.show_disconnectivity_graph)
        QtCore.QObject.connect(self.btnReconnect, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.doubleEndedReConnect)
        QtCore.QObject.connect(self.actionEditParams, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.edit_params)
        QtCore.QObject.connect(self.btnconnect_in_optim, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.connect_in_optim)
        QtCore.QObject.connect(self.actionMerge_Minima, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.merge_minima)
        QtCore.QObject.connect(self.list_TS, QtCore.SIGNAL(_fromUtf8("currentItemChanged(QListWidgetItem*,QListWidgetItem*)")), MainWindow.on_select_TS)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Energy (id)", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget.setSortingEnabled(True)
        self.pushTakestepExplorer.setText(QtGui.QApplication.translate("MainWindow", "Takestep explorer", None, QtGui.QApplication.UnicodeUTF8))
        self.btnRun.setToolTip(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p>Start a short basinhopping run</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.btnRun.setText(QtGui.QApplication.translate("MainWindow", "Run", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.BHTab), QtGui.QApplication.translate("MainWindow", "Basin Hopping", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAlign.setToolTip(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p>Find best alignment between two structures</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAlign.setText(QtGui.QApplication.translate("MainWindow", "Align", None, QtGui.QApplication.UnicodeUTF8))
        self.btnReconnect.setToolTip(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p>Start a fresh double ended connect run</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.btnReconnect.setText(QtGui.QApplication.translate("MainWindow", "Reconnect", None, QtGui.QApplication.UnicodeUTF8))
        self.btnInvert.setToolTip(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p>Invert one of the structures</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.btnInvert.setText(QtGui.QApplication.translate("MainWindow", "Invert", None, QtGui.QApplication.UnicodeUTF8))
        self.btnNEB.setToolTip(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p>Start an NEB run (no alignment is done)</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.btnNEB.setText(QtGui.QApplication.translate("MainWindow", "NEB", None, QtGui.QApplication.UnicodeUTF8))
        self.btnConnect.setToolTip(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p>Start a double ended connect run</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.btnConnect.setText(QtGui.QApplication.translate("MainWindow", "Connect", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_close_all.setText(QtGui.QApplication.translate("MainWindow", "Close Windows", None, QtGui.QApplication.UnicodeUTF8))
        self.btnShowGraph.setToolTip(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p>Show the graph of minima and transition states</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.btnShowGraph.setText(QtGui.QApplication.translate("MainWindow", "show graph", None, QtGui.QApplication.UnicodeUTF8))
        self.btnDisconnectivity_graph.setToolTip(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p>Show the disconnectivity graph</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.btnDisconnectivity_graph.setText(QtGui.QApplication.translate("MainWindow", "disconnectivity graph", None, QtGui.QApplication.UnicodeUTF8))
        self.btnconnect_in_optim.setToolTip(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p>Spawn an external OPTIM job</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.btnconnect_in_optim.setText(QtGui.QApplication.translate("MainWindow", "Connect in OPTIM", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_connect_all.setText(QtGui.QApplication.translate("MainWindow", "Connect All", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.NEBTab), QtGui.QApplication.translate("MainWindow", "Connect", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TSTab), QtGui.QApplication.translate("MainWindow", "Transition States", None, QtGui.QApplication.UnicodeUTF8))
        self.menuSimulation.setTitle(QtGui.QApplication.translate("MainWindow", "Database", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menuActions.setTitle(QtGui.QApplication.translate("MainWindow", "Actions", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setText(QtGui.QApplication.translate("MainWindow", "New", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClear.setText(QtGui.QApplication.translate("MainWindow", "Clear Database", None, QtGui.QApplication.UnicodeUTF8))
        self.actionConnect.setText(QtGui.QApplication.translate("MainWindow", "Connect to Database", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDelete_Minimum.setText(QtGui.QApplication.translate("MainWindow", "Delete Minimum", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEditParams.setText(QtGui.QApplication.translate("MainWindow", "Edit default parameters", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMerge_Minima.setText(QtGui.QApplication.translate("MainWindow", "Merge Minima", None, QtGui.QApplication.UnicodeUTF8))

from show3d import Show3DWithSlider
from pygmin.gui.show3d import Show3D
