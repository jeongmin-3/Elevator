from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 500)

        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")

        self.setupElevatorExternal(self.centralWidget)

        MainWindow.setCentralWidget(self.centralWidget)

        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1000, 26))
        self.menuBar.setObjectName("menuBar")

        self.menusdas = QtWidgets.QMenu(self.menuBar)
        self.menusdas.setObjectName("menusdas")
        MainWindow.setMenuBar(self.menuBar)

        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)

        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.actionaaa = QtWidgets.QAction(MainWindow)
        self.actionaaa.setObjectName("actionaaa")

        self.actionbbb = QtWidgets.QAction(MainWindow)
        self.actionbbb.setObjectName("actionbbb")

        self.menusdas.addAction(self.actionaaa)
        self.menusdas.addAction(self.actionbbb)
        self.menuBar.addAction(self.menusdas.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def setupElevatorExternal(self, parent):
        self.groupBox_2 = QtWidgets.QGroupBox(parent)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 20, 500, 421)) 
        self.groupBox_2.setObjectName("groupBox_2")

        self.layoutWidget2 = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget2.setGeometry(QtCore.QRect(50, 50, 195, 30))
        self.layoutWidget2.setObjectName("layoutWidget2")

        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")

        self.label_2 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_7.addWidget(self.label_2)

        self.comboBox = QtWidgets.QComboBox(self.layoutWidget2)
        self.comboBox.setObjectName("comboBox")
        for i in range(1, 15):
            self.comboBox.addItem(str(i))
        self.horizontalLayout_7.addWidget(self.comboBox)

        self.layoutWidget3 = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget3.setGeometry(QtCore.QRect(50, 110, 195, 30))
        self.layoutWidget3.setObjectName("layoutWidget3")

        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")

        self.pushButton_7 = QtWidgets.QPushButton(self.layoutWidget3)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_5.addWidget(self.pushButton_7)

        self.layoutWidget4 = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget4.setGeometry(QtCore.QRect(50, 150, 195, 30))
        self.layoutWidget4.setObjectName("layoutWidget4")

        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")

        self.pushButton_8 = QtWidgets.QPushButton(self.layoutWidget4)
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_6.addWidget(self.pushButton_8)

        self.layoutWidget5 = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget5.setGeometry(QtCore.QRect(280, 50, 151, 81))
        self.layoutWidget5.setObjectName("layoutWidget5")

        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.layoutWidget5)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")

        self.lcdNumber = QtWidgets.QLCDNumber(self.layoutWidget5)
        self.lcdNumber.setObjectName("lcdNumber")
        self.horizontalLayout_8.addWidget(self.lcdNumber)

        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.layoutWidget5)
        self.lcdNumber_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber_2.setLineWidth(1)
        self.lcdNumber_2.setDigitCount(2)
        self.lcdNumber_2.setProperty("value", 1.0)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.horizontalLayout_8.addWidget(self.lcdNumber_2)

        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(310, 150, 72, 15))
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(380, 150, 72, 15))
        self.label_5.setObjectName("label_5")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_2.setTitle(_translate("MainWindow", "엘리베이터"))
        self.label_2.setText(_translate("MainWindow", "층수    #"))
        self.pushButton_7.setText(_translate("MainWindow", "⬆"))
        self.pushButton_8.setText(_translate("MainWindow", "⬇"))
        self.label_4.setText(_translate("MainWindow", "0"))
        self.label_5.setText(_translate("MainWindow", "0"))
        self.menusdas.setTitle(_translate("MainWindow", "메뉴"))
        self.actionaaa.setText(_translate("MainWindow", "aaa"))
        self.actionbbb.setText(_translate("MainWindow", "bbb"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
