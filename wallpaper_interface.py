from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(542, 417)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setStyleSheet("background-color: rgb(51, 46, 61);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 40, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(23)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(193, 185, 209);")
        self.label.setObjectName("label")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 120, 498, 117))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout_3 = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setStyleSheet("color: rgb(193, 185, 209);\n"
                                   "font: 75 14pt \"Verdana\";\n"
                                   "padding: 5px;")
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(
            0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox.setStyleSheet("color: rgb(193, 185, 209);\n"
                                    "font: 75 12pt \"Verdana\";\n"
                                    "padding: 5px;")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.formLayout.setWidget(
            0, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.formLayout_2.setLayout(
            0, QtWidgets.QFormLayout.SpanningRole, self.formLayout)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setStyleSheet("color: rgb(193, 185, 209);\n"
                                   "font: 75 14pt \"Verdana\";\n"
                                   "padding: 5px;")
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(
            1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.comboBox_2 = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_2.setStyleSheet("color: rgb(193, 185, 209);\n"
                                      "font: 75 12pt \"Verdana\";\n"
                                      "padding: 5px;")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.formLayout_2.setWidget(
            1, QtWidgets.QFormLayout.FieldRole, self.comboBox_2)
        self.formLayout_3.setLayout(
            0, QtWidgets.QFormLayout.SpanningRole, self.formLayout_2)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setStyleSheet("color: rgb(193, 185, 209);\n"
                                   "font: 75 10pt \"Verdana\";\n"
                                   "padding: 5px;")
        self.label_5.setObjectName("label_5")
        self.formLayout_3.setWidget(
            1, QtWidgets.QFormLayout.FieldRole, self.label_5)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(430, 310, 91, 31))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("color: rgb(243, 243, 243);\n"
                                      "background-color: rgb(51, 153, 0);\n"
                                      "font: 75 14pt \"Verdana\";\n"
                                      "padding: 5px;")
        self.pushButton.setObjectName("pushButton")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(28, 310, 281, 31))
        self.checkBox.setStyleSheet("color: rgb(193, 185, 209);\n"
                                    "font: 75 12pt \"Verdana\";\n"
                                    "padding: 5px;")
        self.checkBox.setObjectName("checkBox")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(32, 250, 191, 31))
        self.pushButton_2.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("color: rgb(243, 243, 243);\n"
                                        "background-color: rgb(51, 153, 0);\n"
                                        "font: 75 14pt \"Verdana\";\n"
                                        "padding: 5px;")
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 542, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "WallpaperPy"))
        self.label_2.setText(_translate("MainWindow", "Category:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Category name"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Category name"))
        self.label_3.setText(_translate("MainWindow", "Update frequency:"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "One day"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Two days"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "Three days"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "Week"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "Month"))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "Never"))
        self.label_5.setText(_translate("MainWindow", ""))
        self.pushButton.setText(_translate("MainWindow", "Save"))
        self.checkBox.setText(_translate(
            "MainWindow", "Don\'t delete current wallpaper"))
        self.pushButton_2.setText(_translate("MainWindow", "Update wallpaper"))
