from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow2(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(557, 565)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 0, 201, 181))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(r"Interfaces\Logo framework.jpg"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, 210, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(85, 0, 127);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(160, 350, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(85, 0, 127);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 390, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(85, 0, 127);")
        self.label_4.setObjectName("label_4")
        self.lineEdit_user = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_user.setGeometry(QtCore.QRect(220, 210, 221, 31))
        self.lineEdit_user.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: black;\n"
"")
        self.lineEdit_user.setObjectName("lineEdit_user")
        self.lineEdit_senha1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_senha1.setGeometry(QtCore.QRect(220, 340, 221, 31))
        self.lineEdit_senha1.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: black;")
        self.lineEdit_senha1.setObjectName("lineEdit_senha1")
        self.lineEdit_senha2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_senha2.setGeometry(QtCore.QRect(220, 390, 221, 31))
        self.lineEdit_senha2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: black;")
        self.lineEdit_senha2.setObjectName("lineEdit_senha2")
        self.pushButton_cfcadastro = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_cfcadastro.setGeometry(QtCore.QRect(380, 470, 141, 51))
        self.pushButton_cfcadastro.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 0, 127);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: black;")
        self.pushButton_cfcadastro.setObjectName("pushButton_cfcadastro")
        self.label_error = QtWidgets.QLabel(self.centralwidget)
        self.label_error.setGeometry(QtCore.QRect(200, 440, 251, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_error.setFont(font)
        self.label_error.setStyleSheet("color: rgb(85, 0, 127);")
        self.label_error.setText("")
        self.label_error.setObjectName("label_error")
        self.pushButton_voltar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_voltar.setGeometry(QtCore.QRect(30, 30, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_voltar.setFont(font)
        self.pushButton_voltar.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 0, 127);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: black;")
        self.pushButton_voltar.setObjectName("pushButton_voltar")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(160, 270, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(85, 0, 127);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(120, 310, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(85, 0, 127);")
        self.label_6.setObjectName("label_6")
        self.lineEdit_nome = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_nome.setGeometry(QtCore.QRect(220, 260, 221, 31))
        self.lineEdit_nome.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: black;\n"
"")
        self.lineEdit_nome.setObjectName("lineEdit_nome")
        self.lineEdit_sobrenome = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_sobrenome.setGeometry(QtCore.QRect(220, 300, 221, 31))
        self.lineEdit_sobrenome.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: black;\n"
"")
        self.lineEdit_sobrenome.setObjectName("lineEdit_sobrenome")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 557, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Cadastro"))
        self.label_2.setText(_translate("MainWindow", "Login:"))
        self.label_3.setText(_translate("MainWindow", "Senha:"))
        self.label_4.setText(_translate("MainWindow", "Confirmação de senha:"))
        self.pushButton_cfcadastro.setText(_translate("MainWindow", "Confirmar Cadastro"))
        self.pushButton_voltar.setText(_translate("MainWindow", "VOLTAR"))
        self.label_5.setText(_translate("MainWindow", "Nome:"))
        self.label_6.setText(_translate("MainWindow", "Sobrenome:"))