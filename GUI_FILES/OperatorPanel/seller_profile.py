# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'seller_profile.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(762, 486)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.toolBox = QtWidgets.QToolBox(Form)
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 740, 402))
        self.page.setObjectName("page")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.seller_profile_information_table = QtWidgets.QTableWidget(self.page)
        self.seller_profile_information_table.setObjectName("seller_profile_information_table")
        self.seller_profile_information_table.setColumnCount(0)
        self.seller_profile_information_table.setRowCount(0)
        self.gridLayout_2.addWidget(self.seller_profile_information_table, 1, 0, 1, 1)
        self.toolBox.addItem(self.page, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 740, 402))
        self.page_2.setObjectName("page_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.page_2)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.gridLayout_5.addLayout(self.horizontalLayout_4, 0, 1, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.seller_profile_products_table = QtWidgets.QTableWidget(self.page_2)
        self.seller_profile_products_table.setObjectName("seller_profile_products_table")
        self.seller_profile_products_table.setColumnCount(0)
        self.seller_profile_products_table.setRowCount(0)
        self.horizontalLayout_9.addWidget(self.seller_profile_products_table)
        self.gridLayout_5.addLayout(self.horizontalLayout_9, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.page_2)
        self.label_2.setMaximumSize(QtCore.QSize(400, 16777215))
        self.label_2.setObjectName("label_2")
        self.gridLayout_5.addWidget(self.label_2, 1, 0, 1, 1)
        self.toolBox.addItem(self.page_2, "")
        self.gridLayout.addWidget(self.toolBox, 0, 0, 1, 1)

        self.retranslateUi(Form)
        self.toolBox.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "SL ID"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("Form", "Information"))
        self.label_5.setText(_translate("Form", "product list"))
        self.label_2.setText(_translate("Form", "wallet inventory"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("Form", "Product list"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
