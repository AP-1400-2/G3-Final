# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'operator.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import * 



from ingredients.customer import customer
from ingredients.shop_oprator import operators
from ingredients.shop_oprator import shop
from ingredients.shop_seller import seller
from ingredients.shop_seller import products


import sqlite3

################################ start operator panel ###################################

the_operator = operators('hello', 1234)
class operator_panel(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1582, 921)
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_19 = QtWidgets.QLabel(Form)
        self.label_19.setText("")
        self.label_19.setObjectName("label_19")
        self.gridLayout_2.addWidget(self.label_19, 2, 2, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.profile_button = QtWidgets.QPushButton(Form)
        self.profile_button.setObjectName("profile_button")
        self.verticalLayout_2.addWidget(self.profile_button)
        self.log_out_button = QtWidgets.QPushButton(Form)
        self.log_out_button.setObjectName("log_out_button")
        self.verticalLayout_2.addWidget(self.log_out_button)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 2, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_20 = QtWidgets.QLabel(Form)
        self.label_20.setObjectName("label_20")
        self.gridLayout_3.addWidget(self.label_20, 0, 1, 1, 1)
        self.new_product_refresh = QtWidgets.QPushButton(Form)
        self.new_product_refresh.setObjectName("new_product_refresh")
        self.gridLayout_3.addWidget(self.new_product_refresh, 2, 1, 1, 1)
        self.accept_button = QtWidgets.QPushButton(Form)
        self.accept_button.setObjectName("accept_button")
        self.gridLayout_3.addWidget(self.accept_button, 8, 0, 1, 4)
        self.new_seller_table_refresh = QtWidgets.QPushButton(Form)
        self.new_seller_table_refresh.setObjectName("new_seller_table_refresh")
        self.gridLayout_3.addWidget(self.new_seller_table_refresh, 2, 2, 1, 1)
        self.new_buy_table_refresh = QtWidgets.QPushButton(Form)
        self.new_buy_table_refresh.setObjectName("new_buy_table_refresh")
        self.gridLayout_3.addWidget(self.new_buy_table_refresh, 2, 0, 1, 1)
        self.new_buy_request_table = QtWidgets.QTableWidget(Form)
        self.new_buy_request_table.setObjectName("new_buy_request_table")
        self.new_buy_request_table.setColumnCount(0)
        self.new_buy_request_table.setRowCount(0)
        self.gridLayout_3.addWidget(self.new_buy_request_table, 1, 0, 1, 1)
        self.new_product_tabel = QtWidgets.QTableWidget(Form)
        self.new_product_tabel.setObjectName("new_product_tabel")
        self.new_product_tabel.setColumnCount(0)
        self.new_product_tabel.setRowCount(0)
        self.gridLayout_3.addWidget(self.new_product_tabel, 1, 1, 1, 1)
        self.new_seller_request_table = QtWidgets.QTableWidget(Form)
        self.new_seller_request_table.setObjectName("new_seller_request_table")
        self.new_seller_request_table.setColumnCount(0)
        self.new_seller_request_table.setRowCount(0)
        self.gridLayout_3.addWidget(self.new_seller_request_table, 1, 2, 1, 1)
        self.label_18 = QtWidgets.QLabel(Form)
        self.label_18.setText("")
        self.label_18.setObjectName("label_18")
        self.gridLayout_3.addWidget(self.label_18, 9, 0, 1, 3)
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 3, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 0, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 0, 2, 1, 1)
        self.CU_ID_SL_ID_line_accept = QtWidgets.QLineEdit(Form)
        self.CU_ID_SL_ID_line_accept.setObjectName("CU_ID_SL_ID_line_accept")
        self.gridLayout_3.addWidget(self.CU_ID_SL_ID_line_accept, 3, 1, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout_3, 1, 4, 1, 1)
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_15.addWidget(self.label_11)
        self.off_code_table = QtWidgets.QTableWidget(Form)
        self.off_code_table.setObjectName("off_code_table")
        self.off_code_table.setColumnCount(6)
        self.off_code_table.setRowCount(0)
        #_____________________ OFF CODE TABLE ______________________
        self.off_code_table.setColumnWidth(0,100)
        self.off_code_table.setColumnWidth(1,100)
        self.off_code_table.setColumnWidth(2,100)
        self.off_code_table.setColumnWidth(3,100)
        self.off_code_table.setColumnWidth(4,100)
        self.off_code_table.setColumnWidth(5,100)

        self.off_code_table.setHorizontalHeaderLabels(['CODE','PR_ID', 'EXP', 'CU_ID', 'NUMBER', 'PERCENTAGE'])

        self.load_off_data()
        #___________________________________________________________

        self.verticalLayout_15.addWidget(self.off_code_table)
        self.refresh_off_table = QtWidgets.QPushButton(Form)
        self.refresh_off_table.setObjectName("refresh_off_table")

    #______________ OFF CODE TABLE refresh button ______________
        self.refresh_off_table.clicked.connect(self.load_off_data)
    #___________________________________________________________
        self.verticalLayout_15.addWidget(self.refresh_off_table)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.off_num = QtWidgets.QLineEdit(Form)
        self.off_num.setObjectName("off_num")

        self.gridLayout_5.addWidget(self.off_num, 1, 1, 1, 1)
        self.off_EXP_date = QtWidgets.QLineEdit(Form)
        self.off_EXP_date.setObjectName("off_EXP_date")

        self.gridLayout_5.addWidget(self.off_EXP_date, 0, 1, 1, 1)
        self.off_percentage = QtWidgets.QLineEdit(Form)
        self.off_percentage.setObjectName("off_percentage")

        self.gridLayout_5.addWidget(self.off_percentage, 4, 1, 1, 1)
        self.off_CU_ID = QtWidgets.QLineEdit(Form)
        self.off_CU_ID.setObjectName("off_CU_ID")

        self.gridLayout_5.addWidget(self.off_CU_ID, 2, 1, 1, 1)
        self.off_PR_ID = QtWidgets.QLineEdit(Form)
        self.off_PR_ID.setObjectName("off_PR_ID")

        self.gridLayout_5.addWidget(self.off_PR_ID, 3, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setObjectName("label_12")
        self.gridLayout_5.addWidget(self.label_12, 0, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(Form)
        self.label_16.setObjectName("label_16")
        self.gridLayout_5.addWidget(self.label_16, 4, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(Form)
        self.label_14.setObjectName("label_14")
        self.gridLayout_5.addWidget(self.label_14, 2, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setObjectName("label_13")
        self.gridLayout_5.addWidget(self.label_13, 1, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(Form)
        self.label_15.setObjectName("label_15")
        self.gridLayout_5.addWidget(self.label_15, 3, 0, 1, 1)
        self.verticalLayout_15.addLayout(self.gridLayout_5)
        self.generate_off = QtWidgets.QPushButton(Form)
        self.generate_off.setObjectName("generate_off")
        #____________________________ home button _______________________
        self.generate_off.clicked.connect(self.generate_off_code)
        #________________________________________________________________
        self.verticalLayout_15.addWidget(self.generate_off)
        self.gridLayout_2.addLayout(self.verticalLayout_15, 0, 4, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.seller_list_add_button = QtWidgets.QPushButton(self.tab)
        self.seller_list_add_button.setObjectName("seller_list_add_button")
        self.gridLayout_6.addWidget(self.seller_list_add_button, 7, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setObjectName("label_3")
        self.gridLayout_6.addWidget(self.label_3, 0, 3, 1, 1)
        self.seller_list_sort_button = QtWidgets.QPushButton(self.tab)
        self.seller_list_sort_button.setObjectName("seller_list_sort_button")
        self.gridLayout_6.addWidget(self.seller_list_sort_button, 2, 2, 1, 1)
        self.seller_list_delete_button = QtWidgets.QPushButton(self.tab)
        self.seller_list_delete_button.setObjectName("seller_list_delete_button")
        self.gridLayout_6.addWidget(self.seller_list_delete_button, 5, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setObjectName("label_2")
        self.gridLayout_6.addWidget(self.label_2, 0, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setObjectName("label_4")
        self.gridLayout_6.addWidget(self.label_4, 0, 4, 1, 1)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.seller_list_table = QtWidgets.QTableWidget(self.tab)
        self.seller_list_table.setObjectName("seller_list_table")
        self.seller_list_table.setColumnCount(3)
        self.seller_list_table.setRowCount(0)
        #_________________________ seller table fill __________________________
        self.seller_list_table.setColumnWidth(0,100)
        self.seller_list_table.setColumnWidth(1,150)
        self.seller_list_table.setColumnWidth(2,100)

        self.seller_list_table.setHorizontalHeaderLabels(['SL_ID', 'EMAIL', 'SCORE'])

        self.seller_load_data()
        #________________________________________________________________________  
        self.verticalLayout_7.addWidget(self.seller_list_table)
        self.gridLayout_6.addLayout(self.verticalLayout_7, 1, 2, 1, 1)
        self.sell_report_refresh_button = QtWidgets.QPushButton(self.tab)
        self.sell_report_refresh_button.setObjectName("sell_report_refresh_button")
        self.gridLayout_6.addWidget(self.sell_report_refresh_button, 7, 0, 1, 1)
        self.seller_list_refresh_button = QtWidgets.QPushButton(self.tab)
        self.seller_list_refresh_button.setObjectName("seller_list_refresh_button")
        self.gridLayout_6.addWidget(self.seller_list_refresh_button, 3, 2, 1, 1)
        self.seller_rate_refresh_button = QtWidgets.QPushButton(self.tab)
        self.seller_rate_refresh_button.setObjectName("seller_rate_refresh_button")
        self.gridLayout_6.addWidget(self.seller_rate_refresh_button, 7, 4, 1, 1)
        self.sell_report_table = QtWidgets.QTableWidget(self.tab)
        self.sell_report_table.setObjectName("sell_report_table")
        self.sell_report_table.setColumnCount(5)
        self.sell_report_table.setRowCount(0)
        #_________________________ seller table fill __________________________
        self.sell_report_table.setColumnWidth(0,100)
        self.sell_report_table.setColumnWidth(1,100)
        self.sell_report_table.setColumnWidth(2,100)
        self.sell_report_table.setColumnWidth(3,100)
        self.sell_report_table.setColumnWidth(4,100)

        self.sell_report_table.setHorizontalHeaderLabels(['PR_ID', 'SHOP_NAME','SL_ID', 'DATE', 'CU_ID'])

        self.sell_report_load_data()
        #________________________________________________________________________ 
        self.gridLayout_6.addWidget(self.sell_report_table, 1, 0, 5, 1)
        self.pushButton_18 = QtWidgets.QPushButton(self.tab)
        self.pushButton_18.setObjectName("pushButton_18")
        self.gridLayout_6.addWidget(self.pushButton_18, 7, 5, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.tab)
        self.label_17.setObjectName("label_17")
        self.gridLayout_6.addWidget(self.label_17, 0, 5, 1, 1)
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label.setObjectName("label")
        self.gridLayout_6.addWidget(self.label, 0, 0, 1, 1)
        self.shop_report_table = QtWidgets.QTableWidget(self.tab)
        self.shop_report_table.setObjectName("shop_report_table")
        self.shop_report_table.setColumnCount(0)
        self.shop_report_table.setRowCount(0)
        self.gridLayout_6.addWidget(self.shop_report_table, 1, 5, 5, 1)
        self.sallerrate_list = QtWidgets.QTableWidget(self.tab)
        self.sallerrate_list.setObjectName("sallerrate_list")
        self.sallerrate_list.setColumnCount(0)
        self.sallerrate_list.setRowCount(0)
        self.gridLayout_6.addWidget(self.sallerrate_list, 1, 4, 5, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_6.addWidget(self.lineEdit_3, 4, 2, 1, 1)
        self.seller_report_refresh_button = QtWidgets.QPushButton(self.tab)
        self.seller_report_refresh_button.setObjectName("seller_report_refresh_button")
        self.gridLayout_6.addWidget(self.seller_report_refresh_button, 7, 3, 1, 1)
        self.seller_report_list = QtWidgets.QTableWidget(self.tab)
        self.seller_report_list.setObjectName("seller_report_list")
        self.seller_report_list.setColumnCount(2)
        self.seller_report_list.setRowCount(0)

        #_________________________ seller report table fill __________________________
        self.seller_report_list.setColumnWidth(0,100)
        self.seller_report_list.setColumnWidth(1,150)
        self.seller_report_list.setHorizontalHeaderLabels([])

        # self.seller_report_load_data()
        #________________________________________________________________________ 

        self.gridLayout_6.addWidget(self.seller_report_list, 1, 3, 5, 1)
        self.gridLayout.addLayout(self.gridLayout_6, 0, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.delete_costumer = QtWidgets.QPushButton(self.tab_2)
        self.delete_costumer.setObjectName("delete_costumer")
        self.gridLayout_8.addWidget(self.delete_costumer, 4, 0, 1, 1)
        self.costumer_ID_line = QtWidgets.QLineEdit(self.tab_2)
        self.costumer_ID_line.setObjectName("costumer_ID_line")
        self.gridLayout_8.addWidget(self.costumer_ID_line, 3, 0, 1, 1)
        self.costumer_list_refresh_button = QtWidgets.QPushButton(self.tab_2)
        self.costumer_list_refresh_button.setObjectName("costumer_list_refresh_button")
        self.gridLayout_8.addWidget(self.costumer_list_refresh_button, 7, 0, 1, 1)
        self.refresh_costumer_list_table = QtWidgets.QPushButton(self.tab_2)
        self.refresh_costumer_list_table.setObjectName("refresh_costumer_list_table")
        self.gridLayout_8.addWidget(self.refresh_costumer_list_table, 7, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_8.addWidget(self.pushButton_5, 6, 0, 1, 1)
        self.addcostumer = QtWidgets.QPushButton(self.tab_2)
        self.addcostumer.setObjectName("addcostumer")
        self.gridLayout_8.addWidget(self.addcostumer, 6, 0, 1, 1)
        self.costumer_list_sort = QtWidgets.QPushButton(self.tab_2)
        self.costumer_list_sort.setObjectName("costumer_list_sort")
        self.gridLayout_8.addWidget(self.costumer_list_sort, 2, 0, 1, 1)
        self.costumerlist_table = QtWidgets.QTableWidget(self.tab_2)
        self.costumerlist_table.setObjectName("costumerlist_table")
        self.costumerlist_table.setColumnCount(4)
        self.costumerlist_table.setRowCount(0)

        #_________________________ costumer table fill __________________________
        self.costumerlist_table.setColumnWidth(0,100)
        self.costumerlist_table.setColumnWidth(1,200)
        self.costumerlist_table.setColumnWidth(2,80)
        self.costumerlist_table.setColumnWidth(3,100)


        self.costumerlist_table.setHorizontalHeaderLabels(['', 'CU_ID', 'EMAIL', 'LOCATION'])
        self.costumerlist_table.verticalHeader().hide()
        self.costumer_load_data()
        for index in range(self.costumerlist_table.rowCount()):
            self.btn = QPushButton("show")
            self.costumerlist_table.setCellWidget(index, 0, self.btn)
        self.btn.clicked.connect(self.costumer_load_data)
        #________________________________________________________________________ 
        self.gridLayout_8.addWidget(self.costumerlist_table, 1, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout_8.addWidget(self.label_7, 0, 0, 1, 1)
        self.costumer_report_table = QtWidgets.QTableWidget(self.tab_2)
        self.costumer_report_table.setObjectName("costumer_report_table")
        self.costumer_report_table.setColumnCount(0)
        self.costumer_report_table.setRowCount(0)
        self.gridLayout_8.addWidget(self.costumer_report_table, 1, 1, 6, 1)
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout_8.addWidget(self.label_8, 0, 1, 1, 1)
        self.costumer_report_refresh = QtWidgets.QPushButton(self.tab_2)
        self.costumer_report_refresh.setObjectName("costumer_report_refresh")
        self.gridLayout_8.addWidget(self.costumer_report_refresh, 7, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout_8.addWidget(self.label_5, 0, 2, 1, 1)
        self.product_table_refresh = QtWidgets.QPushButton(self.tab_2)
        self.product_table_refresh.setObjectName("product_table_refresh")
        self.gridLayout_8.addWidget(self.product_table_refresh, 7, 2, 1, 1)
        self.product_table = QtWidgets.QTableWidget(self.tab_2)
        self.product_table.setObjectName("product_table")
        self.product_table.setColumnCount(0)
        self.product_table.setRowCount(0)
        self.gridLayout_8.addWidget(self.product_table, 1, 2, 6, 1)
        self.gridLayout_7.addLayout(self.gridLayout_8, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout_2.addWidget(self.tabWidget, 0, 2, 2, 1)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.profile_button.setText(_translate("Form", "Profile"))
        self.log_out_button.setText(_translate("Form", "logout"))
        self.label_20.setText(_translate("Form", "new product"))
        self.new_product_refresh.setText(_translate("Form", "refresh"))
        self.accept_button.setText(_translate("Form", "accept"))
        self.new_seller_table_refresh.setText(_translate("Form", "refresh"))
        self.new_buy_table_refresh.setText(_translate("Form", "refresh"))
        self.label_6.setText(_translate("Form", "ID"))
        self.label_9.setText(_translate("Form", "new buy request"))
        self.label_10.setText(_translate("Form", "new seller request"))
        self.label_11.setText(_translate("Form", "off_code"))
        self.refresh_off_table.setText(_translate("Form", "refresh"))
        self.label_12.setText(_translate("Form", "EXP"))
        self.label_16.setText(_translate("Form", "%"))
        self.label_14.setText(_translate("Form", "CU_ID"))
        self.label_13.setText(_translate("Form", "NUM"))
        self.label_15.setText(_translate("Form", "PR_ID"))
        self.generate_off.setText(_translate("Form", "generate"))
        self.seller_list_add_button.setText(_translate("Form", "add"))
        self.label_3.setText(_translate("Form", "Seller report"))
        self.seller_list_sort_button.setText(_translate("Form", "sort"))
        self.seller_list_delete_button.setText(_translate("Form", "delete"))
        self.label_2.setText(_translate("Form", "Seller list"))
        self.label_4.setText(_translate("Form", "seller rate"))
        self.sell_report_refresh_button.setText(_translate("Form", "refresh"))
        self.seller_list_refresh_button.setText(_translate("Form", "refresh"))
        self.seller_rate_refresh_button.setText(_translate("Form", "refresh"))
        self.pushButton_18.setText(_translate("Form", "refresh"))
        self.label_17.setText(_translate("Form", "shop report"))
        self.label.setText(_translate("Form", "Sell report"))
        self.seller_report_refresh_button.setText(_translate("Form", "refresh"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "SELLER"))
        self.delete_costumer.setText(_translate("Form", "delete"))
        self.costumer_list_refresh_button.setText(_translate("Form", "sort"))
        self.refresh_costumer_list_table.setText(_translate("Form", "refresh"))
        self.pushButton_5.setText(_translate("Form", "refresh"))
        self.addcostumer.setText(_translate("Form", "add"))
        self.costumer_list_sort.setText(_translate("Form", "sort"))
        self.label_7.setText(_translate("Form", "costumer list"))
        self.label_8.setText(_translate("Form", "costumer report"))
        self.costumer_report_refresh.setText(_translate("Form", "refresh"))
        self.label_5.setText(_translate("Form", "products"))
        self.product_table_refresh.setText(_translate("Form", "refresh"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "COSTUMER / PRODUCTS"))

    def __row_count(self, table_name:str):
        conn = sqlite3.connect('database.sqlite3')
        cursor = conn.execute("SELECT count(*) FROM %s"%(table_name))
        for row in cursor:
            return row[0]
    def __row_count_SPECIAL(self, table_name:str, SPECIAL):
        conn = sqlite3.connect('database.sqlite3')
        cursor = conn.execute("SELECT count(%s) FROM %s"%(SPECIAL ,table_name))
        for row in cursor:
            return row[0]

    #_____________________ costumer load data function _____________________
    def costumer_load_data(self):
        conn = sqlite3.connect('database.sqlite3')
        cur = conn.cursor()
        query = 'SELECT CU_ID, EMAIL, LOCATION FROM CUSTOMER'
        row_count = self.__row_count('CUSTOMER')

        self.costumerlist_table.setRowCount(row_count)
        tablerow = 0 
        for row in cur.execute(query):
            self.costumerlist_table.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.costumerlist_table.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.costumerlist_table.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            tablerow +=1
        
    #________________________________________________________________________


    #_____________________ seller load data function ________________________
    def seller_load_data(self):
        conn = sqlite3.connect('database.sqlite3')
        cur = conn.cursor()
        query = 'SELECT SL_ID,EMAIL,SCORE FROM SELLER'
        row_count = self.__row_count('SELLER')

        self.seller_list_table.setRowCount(row_count)
        tablerow = 0 
        for row in cur.execute(query):
            self.seller_list_table.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.seller_list_table.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.seller_list_table.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))

            tablerow +=1
    #________________________________________________________________________


    #_____________________ sell report load data function ________________________
    def sell_report_load_data(self):
        conn = sqlite3.connect('database.sqlite3')
        cur = conn.cursor()
        query = 'SELECT PR_ID, SHOP_NAME, SL_ID, DATE_TIME, CU_ID FROM SELL_REPORT'
        row_count = self.__row_count('SELL_REPORT')

        self.sell_report_table.setRowCount(row_count)
        tablerow = 0 
        for row in cur.execute(query):
            self.sell_report_table.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.sell_report_table.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.sell_report_table.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.sell_report_table.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[3]))
            self.sell_report_table.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row[4]))
            tablerow +=1
    #________________________________________________________________________


    #____________________________new_seller_refresh __________________________
    # def new_seller_refresh(self):
    #     conn = sqlite3.connect('database.sqlite3')
    #     cur = conn.cursor()
    #     query = "SELECT SL_ID FROM SELLER WHERE STATUS = 'NEW'"
    #     row_count = self.__row_count_SPECIAL('SELLER','STATUS')
    #     self.new_seller_request_table.setRowCount(row_count)
    #     tablerow = 0 
    #     for row in cur.execute(query):
    #         self.new_seller_request_table.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
    #         self.new_seller_request_table.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
    #         tablerow +=1
    # #_________________________________________________________________________


    #_________________________________generate off code ____________________________
    def generate_off_code(self):
        exp = self.off_EXP_date.text()
        num = self.off_num.text()
        perecentage = self.off_percentage.text()
        off_cu_id = self.off_CU_ID.text()
        off_pr_id = self.off_PR_ID.text()

        the_operator.off_code_generator(exp, off_pr_id,off_cu_id,num,perecentage)
    #_______________________________________________________________________________


    #____________________________________ load off data______________________________
    def load_off_data(self):
        conn = sqlite3.connect('database.sqlite3')
        cur = conn.cursor()
        query = "SELECT CODE,PR_ID,EXP_DATE,CU_ID,NUMBER, PERCENTAGE FROM OFF"
        row_count = self.__row_count('OFF')

        self.off_code_table.setRowCount(row_count)
        tablerow = 0 
        for row in cur.execute(query):
            self.off_code_table.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.off_code_table.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.off_code_table.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.off_code_table.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[3]))
            self.off_code_table.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row[4]))
            self.off_code_table.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(row[5]))
            tablerow +=1

    #________________________________________________________________________________
################################ end operator panel #####################################


################################ start login panel ###################################

#__________________________________ main login _______________________________________
class main_login(object):
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
       #_________________________ change page to operator seller __________________________
        self.operator_seller_login_page.clicked.connect(self.change_to_operator_seller_page)
       #___________________________________________________________________________________

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

#_____________________________________________________________________________________

#__________________________________ register  ________________________________________

#_____________________________________________________________________________________

#__________________________________ seller register  _________________________________

#_____________________________________________________________________________________

#__________________________________ operator register  _______________________________

#_____________________________________________________________________________________

#__________________________________ operator & seller login  _________________________
class oprator_seller_login(object):
    def setupUi(self, login):
        login.setObjectName("login")
        login.resize(441, 777)
        self.gridLayout_2 = QtWidgets.QGridLayout(login)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(login)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.layoutWidget = QtWidgets.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 401, 699))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.login_push_button = QtWidgets.QPushButton(self.layoutWidget)
        self.login_push_button.setObjectName("login_push_button")
        self.horizontalLayout.addWidget(self.login_push_button)
        self.register_push_button = QtWidgets.QPushButton(self.layoutWidget)
        self.register_push_button.setObjectName("register_push_button")
        self.horizontalLayout.addWidget(self.register_push_button)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.login_password = QtWidgets.QLineEdit(self.layoutWidget)
        self.login_password.setObjectName("login_password")
        self.gridLayout_3.addWidget(self.login_password, 1, 1, 1, 1)
        self.login_email = QtWidgets.QLineEdit(self.layoutWidget)
        self.login_email.setObjectName("login_email")
        self.gridLayout_3.addWidget(self.login_email, 0, 1, 1, 1)
        self.login_email_label = QtWidgets.QLabel(self.layoutWidget)
        self.login_email_label.setObjectName("login_email_label")
        self.gridLayout_3.addWidget(self.login_email_label, 0, 0, 1, 1)
        self.login_pass_label = QtWidgets.QLabel(self.layoutWidget)
        self.login_pass_label.setObjectName("login_pass_label")
        self.gridLayout_3.addWidget(self.login_pass_label, 1, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.status_label = QtWidgets.QLabel(self.layoutWidget)
        self.status_label.setObjectName("status_label")
        self.verticalLayout.addWidget(self.status_label)
        self.gridLayout.addLayout(self.verticalLayout, 2, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.layoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 10, 401, 699))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.layoutWidget_2)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.login_password_2 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.login_password_2.setObjectName("login_password_2")
        self.gridLayout_5.addWidget(self.login_password_2, 1, 1, 1, 1)
        self.login_email_2 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.login_email_2.setObjectName("login_email_2")
        self.gridLayout_5.addWidget(self.login_email_2, 0, 1, 1, 1)
        self.login_email_label_2 = QtWidgets.QLabel(self.layoutWidget_2)
        self.login_email_label_2.setObjectName("login_email_label_2")
        self.gridLayout_5.addWidget(self.login_email_label_2, 0, 0, 1, 1)
        self.login_pass_label_2 = QtWidgets.QLabel(self.layoutWidget_2)
        self.login_pass_label_2.setObjectName("login_pass_label_2")
        self.gridLayout_5.addWidget(self.login_pass_label_2, 1, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.status_label_2 = QtWidgets.QLabel(self.layoutWidget_2)
        self.status_label_2.setObjectName("status_label_2")
        self.verticalLayout_2.addWidget(self.status_label_2)
        self.gridLayout_4.addLayout(self.verticalLayout_2, 2, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.login_push_button_2 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.login_push_button_2.setObjectName("login_push_button_2")
        self.horizontalLayout_2.addWidget(self.login_push_button_2)
        self.register_push_button_2 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.register_push_button_2.setObjectName("register_push_button_2")
        self.horizontalLayout_2.addWidget(self.register_push_button_2)
        self.gridLayout_4.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout_2.addWidget(self.tabWidget, 0, 1, 1, 1)

        self.retranslateUi(login)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(login)

    def retranslateUi(self, login):
        _translate = QtCore.QCoreApplication.translate
        login.setWindowTitle(_translate("login", "Form"))
        self.login_push_button.setText(_translate("login", "login"))
        self.register_push_button.setText(_translate("login", "register"))
        self.login_email_label.setText(_translate("login", "email"))
        self.login_pass_label.setText(_translate("login", "password"))
        self.status_label.setText(_translate("login", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("login", "seller"))
        self.login_email_label_2.setText(_translate("login", "email"))
        self.login_pass_label_2.setText(_translate("login", "password"))
        self.status_label_2.setText(_translate("login", "TextLabel"))
        self.login_push_button_2.setText(_translate("login", "login"))
        self.register_push_button_2.setText(_translate("login", "register"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("login", "operator"))

#_____________________________________________________________________________________

################################ end login panel #####################################

################################ start shop ###################################

################################ end   shop ###################################


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = operator_panel()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

