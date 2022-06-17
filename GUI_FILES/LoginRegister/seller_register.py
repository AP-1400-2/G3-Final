# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'seller_register.ui'
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
        self.seller_register_register = QtWidgets.QPushButton(register_2)
        self.seller_register_register.setObjectName("seller_register_register")
        self.verticalLayout.addWidget(self.seller_register_register)
        self.seller_rgister_status_label = QtWidgets.QLabel(register_2)
        self.seller_rgister_status_label.setObjectName("seller_rgister_status_label")
        self.verticalLayout.addWidget(self.seller_rgister_status_label)
        self.gridLayout.addLayout(self.verticalLayout, 3, 0, 1, 1)
        self.welcome_label = QtWidgets.QLabel(register_2)
        self.welcome_label.setObjectName("welcome_label")
        self.gridLayout.addWidget(self.welcome_label, 0, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.seller_register_email = QtWidgets.QLineEdit(register_2)
        self.seller_register_email.setObjectName("seller_register_email")
        self.gridLayout_3.addWidget(self.seller_register_email, 0, 2, 1, 1)
        self.seller_register_password = QtWidgets.QLineEdit(register_2)
        self.seller_register_password.setObjectName("seller_register_password")
        self.gridLayout_3.addWidget(self.seller_register_password, 1, 2, 1, 1)
        self.seller_register_email_label = QtWidgets.QLabel(register_2)
        self.seller_register_email_label.setObjectName("seller_register_email_label")
        self.gridLayout_3.addWidget(self.seller_register_email_label, 0, 0, 1, 1)
        self.seller_register_pass_label = QtWidgets.QLabel(register_2)
        self.seller_register_pass_label.setObjectName("seller_register_pass_label")
        self.gridLayout_3.addWidget(self.seller_register_pass_label, 1, 0, 1, 1)
        self.seller_register_location_line = QtWidgets.QLineEdit(register_2)
        self.seller_register_location_line.setObjectName("seller_register_location_line")
        self.gridLayout_3.addWidget(self.seller_register_location_line, 2, 2, 1, 1)
        self.seller_register_location_label = QtWidgets.QLabel(register_2)
        self.seller_register_location_label.setObjectName("seller_register_location_label")
        self.gridLayout_3.addWidget(self.seller_register_location_label, 2, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_3, 1, 0, 1, 1)
        self.seller_location_input_help = QtWidgets.QLabel(register_2)
        self.seller_location_input_help.setObjectName("seller_location_input_help")
        self.gridLayout.addWidget(self.seller_location_input_help, 2, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(register_2)
        QtCore.QMetaObject.connectSlotsByName(register_2)

    def retranslateUi(self, register_2):
        _translate = QtCore.QCoreApplication.translate
        register_2.setWindowTitle(_translate("register_2", "Form"))
        self.seller_register_register.setText(_translate("register_2", "register"))
        self.seller_rgister_status_label.setText(_translate("register_2", "TextLabel"))
        self.welcome_label.setText(_translate("register_2", "Welcome"))
        self.seller_register_email_label.setText(_translate("register_2", "email"))
        self.seller_register_pass_label.setText(_translate("register_2", "password"))
        self.seller_register_location_label.setText(_translate("register_2", "location"))
        self.seller_location_input_help.setText(_translate("register_2", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    register_2 = QtWidgets.QWidget()
    ui = Ui_register_2()
    ui.setupUi(register_2)
    register_2.show()
    sys.exit(app.exec_())

