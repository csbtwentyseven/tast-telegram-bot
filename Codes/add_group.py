# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import main

class Ui_AddGroup(object):
    def setupUi(self, AddGroupWindow, MainWindow):
        AddGroupWindow.setObjectName("MainWindow")
        AddGroupWindow.resize(746, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AddGroupWindow.sizePolicy().hasHeightForWidth())
        AddGroupWindow.setSizePolicy(sizePolicy)
        AddGroupWindow.setMinimumSize(QtCore.QSize(746, 400))
        AddGroupWindow.setMaximumSize(QtCore.QSize(746, 400))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../Downloads/telegram.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AddGroupWindow.setWindowIcon(icon)
        AddGroupWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(AddGroupWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(80, 40, 591, 312))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(20, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMinimumSize(QtCore.QSize(200, 100))
        self.lineEdit.setMaximumSize(QtCore.QSize(300, 100))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.lineEdit.setFont(font)
        self.lineEdit.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.lineEdit.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEdit.setStyleSheet("\n"
"QLineEdit{\n"
"border: 2px solid rgb(34, 158, 217);\n"
"border-radius: 10px; \n"
"padding: 0 8px; \n"
"selection-background-color: darkgray; \n"
"font-size: 16px;\n"
"}\n"
"\n"
"")
        self.lineEdit.setText("")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setMinimumSize(QtCore.QSize(250, 100))
        self.label_2.setMaximumSize(QtCore.QSize(250, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(34, 158, 217);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(200, 100))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(300, 100))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("\n"
"QLineEdit{\n"
"border: 2px solid rgb(34, 158, 217);\n"
"border-radius: 10px; \n"
"padding: 0 8px; \n"
"selection-background-color: darkgray; \n"
"font-size: 16px;\n"
"}\n"
"\n"
"")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(250, 100))
        self.label.setMaximumSize(QtCore.QSize(200, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(34, 158, 217);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(0, 170, 255);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.pushButton = QtWidgets.QPushButton(self.formLayoutWidget, clicked = lambda: self.addGroup(MainWindow))
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 300))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
"  background-color: #229ED9;\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 20px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 16px;\n"
"  margin: 4px 2px;\n"
"  border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
" background-color: white;\n"
" color:#229ED9\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.pushButton)
        AddGroupWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(AddGroupWindow)
        self.statusbar.setObjectName("statusbar")
        AddGroupWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AddGroupWindow)
        QtCore.QMetaObject.connectSlotsByName(AddGroupWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle("Add Group")
        self.label_2.setText(_translate("MainWindow", "GROUP ID: "))
        self.label.setText(_translate("MainWindow", "GROUP NAME:  "))
        self.label_3.setText(_translate("MainWindow", "PLEASE MAKE SURE \n"
"YOUR BOT IS ALREADY \n"
"MEMBER OF THE\n"
"GROUP YOU WANT TO ADD"))
        self.pushButton.setText(_translate("MainWindow", "ADD GROUP"))


    def addGroup(self, main_w):
        print("Add group eklendi")
        main_w.hide()  #REFRESH -BASLANGIC
        groupName = self.lineEdit.text()
        groupIdStr = self.lineEdit_2.text()
        groupsFile = open("Group List.txt","a")


        try:
            groupDataSet = {"Name": groupName, "Id": groupIdStr}
            groupId = int(groupIdStr)
            if(groupId >= 0):
                raise ValueError

            groupInfoGeneral = "{}".format(groupDataSet)
            groupsFile.write(groupInfoGeneral + "\n")
            groupsFile.close()

            self.window = QtWidgets.QMainWindow()
            self.ui = main.Ui_MainWindow()
            self.ui.setupUi(self.window)
            self.ui.fillTable()
            self.window.show() #REFRESH BITIS


        except ValueError:
            self.label_3.setText("PLEASE ADD \n VALID GROUP ID")



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    addGroupWindow = QtWidgets.QMainWindow()
    ui = Ui_AddGroup()
    ui.setupUi(addGroupWindow)
    addGroupWindow.show()
    sys.exit(app.exec_())
