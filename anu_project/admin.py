# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sqlite3, sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from other_window import *
from signup import *
from forget_password import *
from sqlite3 import Error


class Ui_AdminLogin(object):
    def OpenWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        AdminLogin.hide()
        self.window.show()

    def SearchRows(self):
        sqlStatement = "SELECT Username, Password FROM Users where Username like'" + self.lineEditUsername.text() + "'and Password like '" + self.lineEditPassword.text() + "'"
        try:
            conn = sqlite3.connect("admin.db")
            cur = conn.cursor()
            cur.execute(sqlStatement)
            row = cur.fetchone()
            if (row == None):
                msg = QMessageBox()
                msg.setWindowTitle("Warning!")
                msg.setText("Account Not Found! Please Sign up")
                msg.setDefaultButton(QMessageBox.Ok)
                msg.exec()
            else:
                self.OpenWindow()
        except Error as e:
            msg = QMessageBox()
            msg.setWindowTitle("Alert!")
            msg.setText("Error! Couldn't access the user")
            msg.setDefaultButton(QMessageBox.Ok)
            msg.exec()
        finally:
            conn.close()

    def SignUpWindow(self):
        self.dialog = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.dialog)
        self.dialog.show()

    def ForgetPasswordWindow(self):
        self.dialog_1 = QtWidgets.QDialog()
        self.ui = Ui_Dialog1()
        self.ui.setupUi(self.dialog_1)
        self.dialog_1.show()

    def setupUi(self, AdminLogin):
        AdminLogin.setObjectName("AdminLogin")
        AdminLogin.resize(569, 455)
        self.centralwidget = QtWidgets.QWidget(AdminLogin)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(80, 100, 401, 211))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labelAdmin = QtWidgets.QLabel(self.layoutWidget)
        self.labelAdmin.setObjectName("labelAdmin")
        self.verticalLayout_2.addWidget(self.labelAdmin)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelUsername = QtWidgets.QLabel(self.layoutWidget)
        self.labelUsername.setObjectName("labelUsername")
        self.horizontalLayout.addWidget(self.labelUsername)
        self.lineEditUsername = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEditUsername.setObjectName("lineEditUsername")
        self.horizontalLayout.addWidget(self.lineEditUsername)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelPassword = QtWidgets.QLabel(self.layoutWidget)
        self.labelPassword.setEnabled(True)
        self.labelPassword.setObjectName("labelPassword")
        self.horizontalLayout_2.addWidget(self.labelPassword)
        self.lineEditPassword = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.horizontalLayout_2.addWidget(self.lineEditPassword)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButtonLogin = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButtonLogin.setObjectName("pushButtonLogin")

        self.pushButtonLogin.clicked.connect(self.SearchRows)

        self.horizontalLayout_3.addWidget(self.pushButtonLogin)
        self.pushButtonForgetPassword = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButtonForgetPassword.setObjectName("pushButtonForgetPassword")

        self.pushButtonForgetPassword.clicked.connect(self.ForgetPasswordWindow)

        self.horizontalLayout_3.addWidget(self.pushButtonForgetPassword)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.pushButtonSignUp = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButtonSignUp.setObjectName("pushButtonSignUp")

        self.pushButtonSignUp.clicked.connect(self.SignUpWindow)

        self.verticalLayout_4.addWidget(self.pushButtonSignUp)
        AdminLogin.setCentralWidget(self.centralwidget)

        self.retranslateUi(AdminLogin)
        QtCore.QMetaObject.connectSlotsByName(AdminLogin)

    def retranslateUi(self, AdminLogin):
        _translate = QtCore.QCoreApplication.translate
        AdminLogin.setWindowTitle(_translate("AdminLogin", "Admin Window"))
        self.labelAdmin.setText(_translate("AdminLogin", "ADMIN LOGIN"))
        self.labelUsername.setText(_translate("AdminLogin", "Username"))
        self.labelPassword.setText(_translate("AdminLogin", "Password"))
        self.pushButtonLogin.setText(_translate("AdminLogin", "Login"))
        self.pushButtonForgetPassword.setText(_translate("AdminLogin", "Forget Password"))
        self.pushButtonSignUp.setText(_translate("AdminLogin", "Sign Up"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AdminLogin = QtWidgets.QMainWindow()
    ui = Ui_AdminLogin()
    ui.setupUi(AdminLogin)
    AdminLogin.show()
    sys.exit(app.exec_())
