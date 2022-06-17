# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'total_login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_login(object):
    def setupUi(self, login):
        login.setObjectName("login")
        login.resize(423, 721)
        self.gridLayout_2 = QtWidgets.QGridLayout(login)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.login_push_button = QtWidgets.QPushButton(login)
        self.login_push_button.setObjectName("login_push_button")
        self.horizontalLayout.addWidget(self.login_push_button)
        self.register_push_button = QtWidgets.QPushButton(login)
        self.register_push_button.setObjectName("register_push_button")
        self.horizontalLayout.addWidget(self.register_push_button)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.login_password = QtWidgets.QLineEdit(login)
        self.login_password.setObjectName("login_password")
        self.gridLayout_3.addWidget(self.login_password, 1, 1, 1, 1)
        self.login_email = QtWidgets.QLineEdit(login)
        self.login_email.setObjectName("login_email")
        self.gridLayout_3.addWidget(self.login_email, 0, 1, 1, 1)
        self.login_email_label = QtWidgets.QLabel(login)
        self.login_email_label.setObjectName("login_email_label")
        self.gridLayout_3.addWidget(self.login_email_label, 0, 0, 1, 1)
        self.login_pass_label = QtWidgets.QLabel(login)
        self.login_pass_label.setObjectName("login_pass_label")
        self.gridLayout_3.addWidget(self.login_pass_label, 1, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_3, 1, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.operator_seller_login_page = QtWidgets.QPushButton(login)
        self.operator_seller_login_page.setObjectName("operator_seller_login_page")
        self.verticalLayout.addWidget(self.operator_seller_login_page)
        self.status_label = QtWidgets.QLabel(login)
        self.status_label.setObjectName("status_label")
        self.verticalLayout.addWidget(self.status_label)
        self.gridLayout.addLayout(self.verticalLayout, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(login)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(login)
        QtCore.QMetaObject.connectSlotsByName(login)

    def retranslateUi(self, login):
        _translate = QtCore.QCoreApplication.translate
        login.setWindowTitle(_translate("login", "Form"))
        self.login_push_button.setText(_translate("login", "login"))
        self.register_push_button.setText(_translate("login", "register"))
        self.login_email_label.setText(_translate("login", "email"))
        self.login_pass_label.setText(_translate("login", "password"))
        self.operator_seller_login_page.setText(_translate("login", "I\'m Operator / seller"))
        self.status_label.setText(_translate("login", "TextLabel"))
        self.label.setText(_translate("login", "Welcome"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    login = QtWidgets.QWidget()
    ui = Ui_login()
    ui.setupUi(login)
    login.show()
    sys.exit(app.exec_())

