# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'costumer_profile.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(657, 413)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.toolBox = QtWidgets.QToolBox(Form)
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 635, 267))
        self.page.setObjectName("page")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.costumer_profile_information_table = QtWidgets.QTableWidget(self.page)
        self.costumer_profile_information_table.setObjectName("costumer_profile_information_table")
        self.costumer_profile_information_table.setColumnCount(0)
        self.costumer_profile_information_table.setRowCount(0)
        self.gridLayout_2.addWidget(self.costumer_profile_information_table, 1, 0, 1, 1)
        self.toolBox.addItem(self.page, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 635, 267))
        self.page_2.setObjectName("page_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.costumer_profile_wallet_label = QtWidgets.QLabel(self.page_2)
        self.costumer_profile_wallet_label.setMaximumSize(QtCore.QSize(400, 16777215))
        self.costumer_profile_wallet_label.setObjectName("costumer_profile_wallet_label")
        self.gridLayout_5.addWidget(self.costumer_profile_wallet_label, 1, 0, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.costumer_profile_order_table = QtWidgets.QTableWidget(self.page_2)
        self.costumer_profile_order_table.setObjectName("costumer_profile_order_table")
        self.costumer_profile_order_table.setColumnCount(0)
        self.costumer_profile_order_table.setRowCount(0)
        self.horizontalLayout_9.addWidget(self.costumer_profile_order_table)
        self.gridLayout_5.addLayout(self.horizontalLayout_9, 1, 1, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.page_2)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.gridLayout_5.addLayout(self.horizontalLayout_4, 0, 1, 1, 1)
        self.toolBox.addItem(self.page_2, "")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setGeometry(QtCore.QRect(0, 0, 635, 267))
        self.page_3.setObjectName("page_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.page_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.costumer_profile_basket_table = QtWidgets.QTableWidget(self.page_3)
        self.costumer_profile_basket_table.setObjectName("costumer_profile_basket_table")
        self.costumer_profile_basket_table.setColumnCount(0)
        self.costumer_profile_basket_table.setRowCount(0)
        self.horizontalLayout_7.addWidget(self.costumer_profile_basket_table)
        self.costumer_profile_favorite_table = QtWidgets.QTableWidget(self.page_3)
        self.costumer_profile_favorite_table.setObjectName("costumer_profile_favorite_table")
        self.costumer_profile_favorite_table.setColumnCount(0)
        self.costumer_profile_favorite_table.setRowCount(0)
        self.horizontalLayout_7.addWidget(self.costumer_profile_favorite_table)
        self.gridLayout_3.addLayout(self.horizontalLayout_7, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.page_3)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.label_3 = QtWidgets.QLabel(self.page_3)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.toolBox.addItem(self.page_3, "")
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setGeometry(QtCore.QRect(0, 0, 635, 267))
        self.page_4.setObjectName("page_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.page_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_6 = QtWidgets.QLabel(self.page_4)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.gridLayout_4.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.tableWidget_5 = QtWidgets.QTableWidget(self.page_4)
        self.tableWidget_5.setObjectName("tableWidget_5")
        self.tableWidget_5.setColumnCount(0)
        self.tableWidget_5.setRowCount(0)
        self.horizontalLayout_6.addWidget(self.tableWidget_5)
        self.gridLayout_4.addLayout(self.horizontalLayout_6, 1, 0, 1, 1)
        self.toolBox.addItem(self.page_4, "")
        self.gridLayout.addWidget(self.toolBox, 0, 0, 1, 1)

        self.retranslateUi(Form)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "CU ID "))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("Form", "Information"))
        self.costumer_profile_wallet_label.setText(_translate("Form", "wallet inventory"))
        self.label_5.setText(_translate("Form", "order list"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("Form", "Order list "))
        self.label_4.setText(_translate("Form", "Basket"))
        self.label_3.setText(_translate("Form", "favorit"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), _translate("Form", "Basket / Favorite"))
        self.label_6.setText(_translate("Form", "Comments list"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_4), _translate("Form", "Comments"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
