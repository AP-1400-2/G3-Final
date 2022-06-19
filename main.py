# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'operator.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import * 
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
        self.new_buy_request_table.setColumnCount(7)
        self.new_buy_request_table.setRowCount(0)
    #_________________________ buy request table fill __________________________
        self.new_buy_request_table.setColumnWidth(0,60)
        self.new_buy_request_table.setColumnWidth(1,60)
        self.new_buy_request_table.setColumnWidth(2,100)
        self.new_buy_request_table.setColumnWidth(3,150)
        self.new_buy_request_table.setColumnWidth(4,150)
        self.new_buy_request_table.setColumnWidth(5,150)
        self.new_buy_request_table.setColumnWidth(6,150)


        self.buy_request_load_data()
        self.new_buy_request_table.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers) # make table un editable

        self.new_buy_request_table.setHorizontalHeaderLabels(['accept', 'reject', 'CU_ID','SL_ID', 'ORDER LIST', 'DATE', 'STATUS' ])
        self.new_buy_request_table.verticalHeader().hide()
        self.new_buy_request_table.cellClicked.connect(self.print_test)

        for index in range(self.new_buy_request_table.rowCount()):
            self.buy_request_accept  = QPushButton("✅")
                
            self.new_buy_request_table.setCellWidget(index, 0, self.buy_request_accept )

        for index in range(self.new_buy_request_table.rowCount()):
            self.buy_request_reject  = QPushButton("❌")
            

            self.new_buy_request_table.setCellWidget(index, 1, self.buy_request_reject )

            # self.show_seller_profile.clicked.connect(self.get_buy_id)
        

        
        #________________________________________________________________________  

        
        self.gridLayout_3.addWidget(self.new_buy_request_table, 1, 0, 1, 1)
        self.new_product_tabel = QtWidgets.QTableWidget(Form)
        self.new_product_tabel.setObjectName("new_product_tabel")
        self.new_product_tabel.setColumnCount(8)
        self.new_product_tabel.setRowCount(0)

    #_________________________ buy request table fill __________________________
        self.new_product_tabel.setColumnWidth(0,60)
        self.new_product_tabel.setColumnWidth(1,60)
        self.new_product_tabel.setColumnWidth(2,100)
        self.new_product_tabel.setColumnWidth(3,150)
        self.new_product_tabel.setColumnWidth(4,150)
        self.new_product_tabel.setColumnWidth(5,150)
        self.new_product_tabel.setColumnWidth(6,150)
        self.new_product_tabel.setColumnWidth(7,150)

        self.new_product_request_load_data()
        self.new_buy_request_table.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers) # make table un editable

        self.new_product_tabel.setHorizontalHeaderLabels(['accept', 'reject', 'PR_ID','NAME', 'NUMBER', 'PRICE', 'SELLER LIST', 'STATUS' ])
        self.new_product_tabel.verticalHeader().hide()
        self.new_product_tabel.cellClicked.connect(self.print_test)

        for index in range(self.new_product_tabel.rowCount()):
            self.product_request_accept  = QPushButton("✅")
                
            self.new_product_tabel.setCellWidget(index, 0, self.product_request_accept )

        for index in range(self.new_product_tabel.rowCount()):
            self.product_request_reject  = QPushButton("❌")
            

            self.new_product_tabel.setCellWidget(index, 1, self.product_request_reject )

            # self.show_seller_profile.clicked.connect(self.get_buy_id)
    #________________________________________________________________________


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
        self.seller_list_table.setColumnCount(4)
        self.seller_list_table.setRowCount(0)
        #_________________________ seller table fill __________________________
        self.seller_list_table.setColumnWidth(0,60)
        self.seller_list_table.setColumnWidth(1,100)
        self.seller_list_table.setColumnWidth(2,150)
        self.seller_list_table.setColumnWidth(3,100)



        self.seller_load_data()
        self.seller_list_table.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers) # make table un editable

        self.seller_list_table.setHorizontalHeaderLabels(['profile', 'SL_ID', 'EMAIL', 'SCORE'])
        self.seller_list_table.verticalHeader().hide()
        self.seller_list_table.cellClicked.connect(self.print_test)

        for index in range(self.seller_list_table.rowCount()):
            self.show_seller_profile  = QPushButton("🙍")
            self.seller_list_table.setCellWidget(index, 0, self.show_seller_profile )

            self.show_seller_profile.clicked.connect(self.get_SL_ID)
            self.show_seller_profile.setStyleSheet("background-color : #c9c9c9")

        
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
        #_________________________ sell table fill __________________________
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
        self.shop_report_table.setColumnCount(4)
        self.shop_report_table.setRowCount(0)
        #_____________________shop report table fill_________________
        self.shop_report_table.setColumnWidth(0, 100)
        self.shop_report_table.setColumnWidth(1, 200)
        self.shop_report_table.setColumnWidth(2, 200)
        self.shop_report_table.setColumnWidth(3, 200)
        self.shop_report_table.setHorizontalHeaderLabels(['Name', 'Products', 'Costumers', 'Sellers'])

        self.shop_report_load_data()
        #____________________________________________________________

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
        self.refresh_costumer_list_table_button = QtWidgets.QPushButton(self.tab_2)
        self.refresh_costumer_list_table_button.setObjectName("refresh_costumer_list_table_button")
        self.gridLayout_8.addWidget(self.refresh_costumer_list_table_button, 7, 0, 1, 1)
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
        self.costumerlist_table.setColumnWidth(0,60)
        self.costumerlist_table.setColumnWidth(1,100)
        self.costumerlist_table.setColumnWidth(2,200)
        self.costumerlist_table.setColumnWidth(3,100)

        
        self.costumerlist_table.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers) # make table un editable

        self.costumerlist_table.setHorizontalHeaderLabels(['profile', 'CU_ID', 'EMAIL', 'LOCATION'])
        self.costumerlist_table.verticalHeader().hide()
        self.costumer_load_data()
        self.costumerlist_table.cellClicked.connect(self.print_test)

        for index in range(self.costumerlist_table.rowCount()):
            self.show_costumer_profile  = QPushButton("🙍")
            self.costumerlist_table.setCellWidget(index, 0, self.show_costumer_profile )

            self.show_costumer_profile .clicked.connect(self.get_CU_ID)
            self.show_costumer_profile.setStyleSheet("background-color : #c9c9c9")
        
        #________________________________________________________________________ 
        self.gridLayout_8.addWidget(self.costumerlist_table, 1, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout_8.addWidget(self.label_7, 0, 0, 1, 1)
        self.costumer_report_table = QtWidgets.QTableWidget(self.tab_2)
        self.costumer_report_table.setObjectName("costumer_report_table")
        self.costumer_report_table.setColumnCount(0)
        self.costumer_report_table.setRowCount(0)
      #_________________________ costumer report table fill __________________________
        self.costumer_report_table.setColumnWidth(0,100)
        self.costumer_report_table.setColumnWidth(1,100)
        self.costumer_report_table.setColumnWidth(2,200)

        
        self.costumer_report_table.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers) # make table un editable

        # self.costumerlist_table.setHorizontalHeaderLabels(['Show profile', 'CU_ID', 'EMAIL', 'LOCATION'])
        # self.costumerlist_table.verticalHeader().hide()
        # self.costumer_load_data()
        # self.costumerlist_table.cellClicked.connect(self.print_test)

        # for index in range(self.costumerlist_table.rowCount()):
        #     self.show_costumer_profile  = QPushButton("Profile")
        #     self.costumerlist_table.setCellWidget(index, 0, self.show_costumer_profile )

        #     self.show_costumer_profile .clicked.connect(self.get_CU_ID)
        #     self.show_costumer_profile.setStyleSheet("background-color : #00A693")
        
        #________________________________________________________________________ 


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
        self.product_table.setColumnCount(4)
        self.product_table.setRowCount(0)
    #_________________________ product table fill __________________________
        self.product_table.setColumnWidth(0,100)
        self.product_table.setColumnWidth(1,200)
        self.product_table.setColumnWidth(2,50)
        self.product_table.setColumnWidth(3,80)

        
        self.product_table.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers) # make table un editable

        self.product_table.setHorizontalHeaderLabels(['PR_ID', 'NAME', 'NUMBER', 'PRICE'])
        
        self.product_table_load_data()
        
        
        #________________________________________________________________________ 

        self.gridLayout_8.addWidget(self.product_table, 1, 2, 6, 1)
        self.gridLayout_7.addLayout(self.gridLayout_8, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout_2.addWidget(self.tabWidget, 0, 2, 2, 1)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    #____________________ test _____________________________________
    def print_test(self):
        # self.costumerlist_table.
        print("test done!")
    
    def get_CU_ID(self):
        current_row = self.costumerlist_table.currentRow()
        current_column = self.costumerlist_table.currentColumn()
        cell_value = self.costumerlist_table.item(current_row, current_column + 1).text()
        print(cell_value)
    def get_SL_ID(self):
        current_row = self.seller_list_table.currentRow()
        current_column = self.seller_list_table.currentColumn()
        cell_value = self.seller_list_table.item(current_row, current_column + 1).text()
        print(cell_value)
    #_______________________________________________________________

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Operator panel"))
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
        self.refresh_costumer_list_table_button.setText(_translate("Form", "refresh"))
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
        cursor = conn.execute("SELECT count(*) FROM '{}';" .format(table_name))
        for row in cursor:
            return row[0]
    def __row_count_SPECIAL(self, table_name:str, SPECIAL):
        conn = sqlite3.connect('database.sqlite3')
        cursor = conn.execute("SELECT count(*) FROM '{}' WHERE STATUS = '{}'".format(table_name, SPECIAL))
        for row in cursor:
            return row[0]



    #_____________________ product load data function _____________________
    def product_table_load_data(self):
        row_count = self.__row_count('PRODUCT')
        self.product_table.setRowCount(row_count)
        tablerow = 0 
        for row in the_operator.product_report():
            self.product_table.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.product_table.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.product_table.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.product_table.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[3]))
            tablerow +=1

    #______________________________________________________________________


    #_____________________ new product request load data function _____________________
    def new_product_request_load_data(self):
        row_count = self.__row_count_SPECIAL('PRODUCT','NEW' )
        self.new_product_tabel.setRowCount(row_count)
        tablerow = 0 
        for row in the_operator.check_product():
            self.new_product_tabel.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[0]))
            self.new_product_tabel.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[1]))
            self.new_product_tabel.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row[2]))
            self.new_product_tabel.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(row[3]))
            self.new_product_tabel.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(row[4]))
            self.new_product_tabel.setItem(tablerow, 7, QtWidgets.QTableWidgetItem(row[5]))
            tablerow +=1

    #__________________________________________________________________________________

    #_____________________ new buy request load data function _____________________
    def buy_request_load_data(self):
        row_count = self.__row_count_SPECIAL('ORDER','NEW' )
        self.new_buy_request_table.setRowCount(row_count)
        tablerow = 0 
        for row in the_operator.check_order():
            self.new_buy_request_table.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[0]))
            self.new_buy_request_table.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[1]))
            self.new_buy_request_table.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row[2]))
            self.new_buy_request_table.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(row[3]))
            self.new_buy_request_table.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(row[4]))
            tablerow +=1

    #_____________________ costumer load data function _____________________
    def costumer_load_data(self):
        row_count = self.__row_count('COSTUMER')
        self.costumerlist_table.setRowCount(row_count)
        tablerow = 0 
        for row in the_operator.costumer_report():
            self.costumerlist_table.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[0]))
            self.costumerlist_table.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[1]))
            self.costumerlist_table.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[2]))
            tablerow +=1
        
    #________________________________________________________________________


    #_____________________ seller load data function ________________________
    def seller_load_data(self):
        
        row_count = self.__row_count('SELLER')

        self.seller_list_table.setRowCount(row_count)
        tablerow = 0 
        for row in the_operator.seller_report():
            self.seller_list_table.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[0]))
            self.seller_list_table.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[1]))
            self.seller_list_table.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[2]))
            tablerow +=1
    #________________________________________________________________________

    #_____________________ shop load data function ________________________
    def shop_report_load_data(self):
        row_count = self.__row_count('SHOP')
        self.shop_report_table.setRowCount(row_count)
        result = the_operator.shop_reports()
        tablerow = 0 
        for row in result:
            self.shop_report_table.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.shop_report_table.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.shop_report_table.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.shop_report_table.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[3]))
            tablerow +=1

    #________________________________________________________________________


    #_____________________ sell report load data function ________________________
    def sell_report_load_data(self):
        row_count = self.__row_count('SELL_REPORT')
        self.sell_report_table.setRowCount(row_count)
        result = the_operator.sell_report()
        tablerow = 0 
        for row in result:
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
        self.load_off_data()
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

class login_register(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(445, 692)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.toolBox = QtWidgets.QToolBox(self.tab)
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 395, 526))
        self.page.setObjectName("page")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.costumer_login_push_button = QtWidgets.QPushButton(self.page)
        self.costumer_login_push_button.setObjectName("costumer_login_push_button")
        self.horizontalLayout.addWidget(self.costumer_login_push_button)
        self.gridLayout_4.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.costumer_login_password_line = QtWidgets.QLineEdit(self.page)
        self.costumer_login_password_line.setObjectName("costumer_login_password_line")
        self.gridLayout_5.addWidget(self.costumer_login_password_line, 1, 1, 1, 1)
        self.costumer_login_email_line = QtWidgets.QLineEdit(self.page)
        self.costumer_login_email_line.setObjectName("costumer_login_email_line")
        self.gridLayout_5.addWidget(self.costumer_login_email_line, 0, 1, 1, 1)
        self.login_email_label = QtWidgets.QLabel(self.page)
        self.login_email_label.setObjectName("login_email_label")
        self.gridLayout_5.addWidget(self.login_email_label, 0, 0, 1, 1)
        self.login_pass_label = QtWidgets.QLabel(self.page)
        self.login_pass_label.setObjectName("login_pass_label")
        self.gridLayout_5.addWidget(self.login_pass_label, 1, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_5, 1, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.costumer_login_status = QtWidgets.QLabel(self.page)
        self.costumer_login_status.setObjectName("costumer_login_status")
        self.verticalLayout.addWidget(self.costumer_login_status)
        self.gridLayout_4.addLayout(self.verticalLayout, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.page)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.toolBox.addItem(self.page, "")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.page_3)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.seller_password_login_line = QtWidgets.QLineEdit(self.page_3)
        self.seller_password_login_line.setObjectName("seller_password_login_line")
        self.gridLayout_7.addWidget(self.seller_password_login_line, 1, 1, 1, 1)
        self.seller_email_login_line = QtWidgets.QLineEdit(self.page_3)
        self.seller_email_login_line.setObjectName("seller_email_login_line")
        self.gridLayout_7.addWidget(self.seller_email_login_line, 0, 1, 1, 1)
        self.login_email_label_2 = QtWidgets.QLabel(self.page_3)
        self.login_email_label_2.setObjectName("login_email_label_2")
        self.gridLayout_7.addWidget(self.login_email_label_2, 0, 0, 1, 1)
        self.login_pass_label_2 = QtWidgets.QLabel(self.page_3)
        self.login_pass_label_2.setObjectName("login_pass_label_2")
        self.gridLayout_7.addWidget(self.login_pass_label_2, 1, 0, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_7, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.seler_login_push_button = QtWidgets.QPushButton(self.page_3)
        self.seler_login_push_button.setObjectName("seler_login_push_button")
        self.horizontalLayout_2.addWidget(self.seler_login_push_button)
        self.gridLayout_8.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.seller_login_status = QtWidgets.QLabel(self.page_3)
        self.seller_login_status.setObjectName("seller_login_status")
        self.gridLayout_8.addWidget(self.seller_login_status, 2, 0, 1, 1)
        self.toolBox.addItem(self.page_3, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 395, 526))
        self.page_2.setObjectName("page_2")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.operator_login_password_line = QtWidgets.QLineEdit(self.page_2)
        self.operator_login_password_line.setObjectName("operator_login_password_line")
        self.gridLayout_9.addWidget(self.operator_login_password_line, 1, 1, 1, 1)
        self.operator_login_email_line = QtWidgets.QLineEdit(self.page_2)
        self.operator_login_email_line.setObjectName("operator_login_email_line")
        self.gridLayout_9.addWidget(self.operator_login_email_line, 0, 1, 1, 1)
        self.login_email_label_3 = QtWidgets.QLabel(self.page_2)
        self.login_email_label_3.setObjectName("login_email_label_3")
        self.gridLayout_9.addWidget(self.login_email_label_3, 0, 0, 1, 1)
        self.login_pass_label_3 = QtWidgets.QLabel(self.page_2)
        self.login_pass_label_3.setObjectName("login_pass_label_3")
        self.gridLayout_9.addWidget(self.login_pass_label_3, 1, 0, 1, 1)
        self.gridLayout_10.addLayout(self.gridLayout_9, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.operator_login_push_button = QtWidgets.QPushButton(self.page_2)
        self.operator_login_push_button.setObjectName("operator_login_push_button")
        self.horizontalLayout_3.addWidget(self.operator_login_push_button)
        self.gridLayout_10.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.operator_login_status = QtWidgets.QLabel(self.page_2)
        self.operator_login_status.setObjectName("operator_login_status")
        self.gridLayout_10.addWidget(self.operator_login_status, 2, 0, 1, 1)
        self.toolBox.addItem(self.page_2, "")
        self.gridLayout_2.addWidget(self.toolBox, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.toolBox_2 = QtWidgets.QToolBox(self.tab_2)
        self.toolBox_2.setObjectName("toolBox_2")
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setGeometry(QtCore.QRect(0, 0, 400, 536))
        self.page_4.setObjectName("page_4")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.page_4)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.gridLayout_11 = QtWidgets.QGridLayout()
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.costumer_register_button = QtWidgets.QPushButton(self.page_4)
        self.costumer_register_button.setObjectName("costumer_register_button")
        self.verticalLayout_2.addWidget(self.costumer_register_button)
        self.costumer_register_status = QtWidgets.QLabel(self.page_4)
        self.costumer_register_status.setObjectName("costumer_register_status")
        self.verticalLayout_2.addWidget(self.costumer_register_status)
        self.gridLayout_11.addLayout(self.verticalLayout_2, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.page_4)
        self.label_2.setObjectName("label_2")
        self.gridLayout_11.addWidget(self.label_2, 0, 0, 1, 1)
        self.gridLayout_12 = QtWidgets.QGridLayout()
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.costumer_register_email_line = QtWidgets.QLineEdit(self.page_4)
        self.costumer_register_email_line.setObjectName("costumer_register_email_line")
        self.gridLayout_12.addWidget(self.costumer_register_email_line, 0, 2, 1, 1)
        self.costumer_register_password_line = QtWidgets.QLineEdit(self.page_4)
        self.costumer_register_password_line.setObjectName("costumer_register_password_line")
        self.gridLayout_12.addWidget(self.costumer_register_password_line, 1, 2, 1, 1)
        self.register_email_label = QtWidgets.QLabel(self.page_4)
        self.register_email_label.setObjectName("register_email_label")
        self.gridLayout_12.addWidget(self.register_email_label, 0, 0, 1, 1)
        self.register_pass_label = QtWidgets.QLabel(self.page_4)
        self.register_pass_label.setObjectName("register_pass_label")
        self.gridLayout_12.addWidget(self.register_pass_label, 1, 0, 1, 1)
        self.costumer_register_location_line = QtWidgets.QLineEdit(self.page_4)
        self.costumer_register_location_line.setObjectName("costumer_register_location_line")
        self.gridLayout_12.addWidget(self.costumer_register_location_line, 2, 2, 1, 1)
        self.register_location_label = QtWidgets.QLabel(self.page_4)
        self.register_location_label.setObjectName("register_location_label")
        self.gridLayout_12.addWidget(self.register_location_label, 2, 0, 1, 1)
        self.gridLayout_11.addLayout(self.gridLayout_12, 1, 0, 1, 1)
        self.location_input_help = QtWidgets.QLabel(self.page_4)
        self.location_input_help.setObjectName("location_input_help")
        self.gridLayout_11.addWidget(self.location_input_help, 2, 0, 1, 1)
        self.gridLayout_13.addLayout(self.gridLayout_11, 0, 0, 1, 1)
        self.toolBox_2.addItem(self.page_4, "")
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setGeometry(QtCore.QRect(0, 0, 400, 536))
        self.page_5.setObjectName("page_5")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.page_5)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.gridLayout_14 = QtWidgets.QGridLayout()
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.seller_register_button = QtWidgets.QPushButton(self.page_5)
        self.seller_register_button.setObjectName("seller_register_button")
        self.verticalLayout_3.addWidget(self.seller_register_button)
        self.seller_rgister_status_label = QtWidgets.QLabel(self.page_5)
        self.seller_rgister_status_label.setObjectName("seller_rgister_status_label")
        self.verticalLayout_3.addWidget(self.seller_rgister_status_label)
        self.gridLayout_14.addLayout(self.verticalLayout_3, 3, 0, 1, 1)
        self.welcome_label = QtWidgets.QLabel(self.page_5)
        self.welcome_label.setObjectName("welcome_label")
        self.gridLayout_14.addWidget(self.welcome_label, 0, 0, 1, 1)
        self.gridLayout_15 = QtWidgets.QGridLayout()
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.seller_register_email_line = QtWidgets.QLineEdit(self.page_5)
        self.seller_register_email_line.setObjectName("seller_register_email_line")
        self.gridLayout_15.addWidget(self.seller_register_email_line, 0, 2, 1, 1)
        self.seller_register_password_line = QtWidgets.QLineEdit(self.page_5)
        self.seller_register_password_line.setObjectName("seller_register_password_line")
        self.gridLayout_15.addWidget(self.seller_register_password_line, 1, 2, 1, 1)
        self.seller_register_email_label = QtWidgets.QLabel(self.page_5)
        self.seller_register_email_label.setObjectName("seller_register_email_label")
        self.gridLayout_15.addWidget(self.seller_register_email_label, 0, 0, 1, 1)
        self.seller_register_pass_label = QtWidgets.QLabel(self.page_5)
        self.seller_register_pass_label.setObjectName("seller_register_pass_label")
        self.gridLayout_15.addWidget(self.seller_register_pass_label, 1, 0, 1, 1)
        self.seller_register_location_line = QtWidgets.QLineEdit(self.page_5)
        self.seller_register_location_line.setObjectName("seller_register_location_line")
        self.gridLayout_15.addWidget(self.seller_register_location_line, 2, 2, 1, 1)
        self.seller_register_location_label = QtWidgets.QLabel(self.page_5)
        self.seller_register_location_label.setObjectName("seller_register_location_label")
        self.gridLayout_15.addWidget(self.seller_register_location_label, 2, 0, 1, 1)
        self.gridLayout_14.addLayout(self.gridLayout_15, 1, 0, 1, 1)
        self.seller_location_input_help = QtWidgets.QLabel(self.page_5)
        self.seller_location_input_help.setObjectName("seller_location_input_help")
        self.gridLayout_14.addWidget(self.seller_location_input_help, 2, 0, 1, 1)
        self.gridLayout_16.addLayout(self.gridLayout_14, 0, 0, 1, 1)
        self.toolBox_2.addItem(self.page_5, "")
        self.gridLayout_3.addWidget(self.toolBox_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(1)
        self.toolBox.setCurrentIndex(2)
        self.toolBox_2.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.costumer_login_push_button.setText(_translate("Form", "login"))
        self.login_email_label.setText(_translate("Form", "email"))
        self.login_pass_label.setText(_translate("Form", "password"))
        self.costumer_login_status.setText(_translate("Form", "Status"))
        self.label.setText(_translate("Form", "Welcome"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("Form", "Costumer"))
        self.login_email_label_2.setText(_translate("Form", "email"))
        self.login_pass_label_2.setText(_translate("Form", "password"))
        self.seler_login_push_button.setText(_translate("Form", "login"))
        self.seller_login_status.setText(_translate("Form", "Status"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), _translate("Form", "Seller"))
        self.login_email_label_3.setText(_translate("Form", "email"))
        self.login_pass_label_3.setText(_translate("Form", "password"))
        self.operator_login_push_button.setText(_translate("Form", "login"))
        self.operator_login_status.setText(_translate("Form", "Status"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("Form", "Operator"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Login"))
        self.costumer_register_button.setText(_translate("Form", "register"))
        self.costumer_register_status.setText(_translate("Form", "Status"))
        self.label_2.setText(_translate("Form", "Welcome"))
        self.register_email_label.setText(_translate("Form", "email"))
        self.register_pass_label.setText(_translate("Form", "password"))
        self.register_location_label.setText(_translate("Form", "location"))
        self.location_input_help.setText(_translate("Form", "Please enter first four letter of your state name in location section\n"
"example: tehran = tehr"))
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.page_4), _translate("Form", "Costumer"))
        self.seller_register_button.setText(_translate("Form", "register"))
        self.seller_rgister_status_label.setText(_translate("Form", "Status"))
        self.welcome_label.setText(_translate("Form", "Welcome"))
        self.seller_register_email_label.setText(_translate("Form", "email"))
        self.seller_register_pass_label.setText(_translate("Form", "password"))
        self.seller_register_location_label.setText(_translate("Form", "location"))
        self.seller_location_input_help.setText(_translate("Form", "Please enter first four letter of your state name in location section\n"
"example: tehran = tehr"))
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.page_5), _translate("Form", "Seller"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Register"))

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

