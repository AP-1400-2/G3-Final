# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_register_2(object):
    def setupUi(self, register_2):
        register_2.setObjectName("register_2")
        register_2.resize(423, 721)
        self.gridLayout_2 = QtWidgets.QGridLayout(register_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.register_register = QtWidgets.QPushButton(register_2)
        self.register_register.setObjectName("register_register")
        self.verticalLayout.addWidget(self.register_register)
        self.operator_seller_login_page = QtWidgets.QPushButton(register_2)
        self.operator_seller_login_page.setObjectName("operator_seller_login_page")
        self.verticalLayout.addWidget(self.operator_seller_login_page)
        self.status_label = QtWidgets.QLabel(register_2)
        self.status_label.setObjectName("status_label")
        self.verticalLayout.addWidget(self.status_label)
        self.gridLayout.addLayout(self.verticalLayout, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(register_2)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.register_email = QtWidgets.QLineEdit(register_2)
        self.register_email.setObjectName("register_email")
        self.gridLayout_3.addWidget(self.register_email, 0, 2, 1, 1)
        self.register_password = QtWidgets.QLineEdit(register_2)
        self.register_password.setObjectName("register_password")
        self.gridLayout_3.addWidget(self.register_password, 1, 2, 1, 1)
        self.register_email_label = QtWidgets.QLabel(register_2)
        self.register_email_label.setObjectName("register_email_label")
        self.gridLayout_3.addWidget(self.register_email_label, 0, 0, 1, 1)
        self.register_pass_label = QtWidgets.QLabel(register_2)
        self.register_pass_label.setObjectName("register_pass_label")
        self.gridLayout_3.addWidget(self.register_pass_label, 1, 0, 1, 1)
        self.register_location_line = QtWidgets.QLineEdit(register_2)
        self.register_location_line.setObjectName("register_location_line")
        self.gridLayout_3.addWidget(self.register_location_line, 2, 2, 1, 1)
        self.register_location_label = QtWidgets.QLabel(register_2)
        self.register_location_label.setObjectName("register_location_label")
        self.gridLayout_3.addWidget(self.register_location_label, 2, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_3, 1, 0, 1, 1)
        self.location_input_help = QtWidgets.QLabel(register_2)
        self.location_input_help.setObjectName("location_input_help")
        self.gridLayout.addWidget(self.location_input_help, 2, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(register_2)
        QtCore.QMetaObject.connectSlotsByName(register_2)

    def retranslateUi(self, register_2):
        _translate = QtCore.QCoreApplication.translate
        register_2.setWindowTitle(_translate("register_2", "Form"))
        self.register_register.setText(_translate("register_2", "register"))
        self.operator_seller_login_page.setText(_translate("register_2", "I\'m Operator / seller"))
        self.status_label.setText(_translate("register_2", "TextLabel"))
        self.label.setText(_translate("register_2", "Welcome"))
        self.register_email_label.setText(_translate("register_2", "email"))
        self.register_pass_label.setText(_translate("register_2", "password"))
        self.register_location_label.setText(_translate("register_2", "location"))
        self.location_input_help.setText(_translate("register_2", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    register_2 = QtWidgets.QWidget()
    ui = Ui_register_2()
    ui.setupUi(register_2)
    register_2.show()
    sys.exit(app.exec_())

