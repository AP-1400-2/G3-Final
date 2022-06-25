import sqlite3
from random import randint as rint
# operator sql table

'''CREATE TABLE "OPERATOR" (
	"ID"	INTEGER NOT NULL UNIQUE,
	"EMAIL"	TEXT NOT NULL UNIQUE,
	"PASSWORD"	TEXT NOT NULL,
	PRIMARY KEY("ID" AUTOINCREMENT)
);'''

class operators:
    def __init__(self, email, password):
        self.__email = email
        self.__password = password
    
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, value):
        print('error use changeemail method')

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, value):
        print('error use changepassword method')


    def changepassword(self, oldpassword, newpassword):
        conn = sqlite3.connect('database.sqlite3')
        old_password = conn.execute("SELECT PASSWORD FROM OPERATOR WHERE EMAIL = '{}' " .format(self.__email))
        if old_password == oldpassword:
            try:
                conn.execute("UPDATE OPERATOR PASSWORD = '{}' WHERE EMAIL = '{}'" .format(newpassword, self.__email))
                conn.commit()            
            except sqlite3.Error:
                print("error! something went wrong")
            else:
                print("Done!")


    def changeemail(self, newewmail, password):
        conn = sqlite3.connect('database.sqlite3')
        cursor = conn.execute("SELECT PASSWORD FROM OPERATOR WHERE EMAIL = '{}' " .format(self.__email))
        for row in cursor:
            database_password = row[0]
        if database_password == password:
            try:
                conn.execute("UPDATE OPERATOR EMAIL = '{}' WHERE EMAIL = '{}'" .format(newewmail, self.__email))
                conn.commit()
            except sqlite3.Error:
                print("error! something went wrong")
            else:
                print("Done!")


    def save_to_db(self):
        conn = sqlite3.connect('database.sqlite3')
        data = self.__dict__
        try:
            conn.execute('''INSERT INTO OPERATOR(EMAIL,PASSWORD) \
                        VALUES('{}','{}');'''.format(data['_operators__email'],data['_operators__password']))
            conn.commit()
        except sqlite3.Error:
            print("error! something went wrong")
        else:
            print("Done!")


    def total_rate(self):
        conn = sqlite3.connect('database.sqlite3')
        cur = conn.cursor()
        cu_count_query = "SELECT count(*) FROM COSTUMER"
        sl_count_query = "SELECT count(*) FROM SELLER"
        pr_count_query = "SELECT count(*) FROM PRODUCT"
        shop_count_query = "SELECT count(*) FROM SHOP"

        data_cu_count_query = cur.execute(cu_count_query)
        data_sl_count_query = cur.execute(sl_count_query)
        data_pr_count_query = cur.execute(pr_count_query)
        data_shop_count_query = cur.execute(shop_count_query)

        for row in data_cu_count_query:
            count_data_cu_count_query = row[0]
        for row in data_sl_count_query:
            count_data_sl_count_query = row[0]
        for row in data_pr_count_query:
            count_data_pr_count_query = row[0]
        for row in data_shop_count_query:
            count_data_shop_count_query = row[0]


        return count_data_cu_count_query, count_data_sl_count_query, count_data_pr_count_query, count_data_shop_count_query




    def load_cu_profile(self, CU_ID):
        conn = sqlite3.connect('database.sqlite3')
        cur = conn.cursor()
        information_query = "SELECT CU_ID, EMAIL, PASSWORD, LOCATION, SCORE, TOTAL_PURCHASE, ACTIVE_STATUS FROM COSTUMER WHERE CU_ID = '{}'" .format(CU_ID)
        order_list_query = "SELECT SL_ID, ORDER_LIST, DATE, STATUS FROM 'ORDER' WHERE CU_ID = '{}'" .format(CU_ID)
        basket_list_query = "SELECT BASKET FROM COSTUMER WHERE CU_ID = '{}'" .format(CU_ID)
        favorite_list_query = "SELECT FAVORIT FROM COSTUMER WHERE CU_ID = '{}'" .format(CU_ID)
        comments_list_query = "SELECT PR_ID, COMMENT FROM COMMENT_LIST WHERE CU_ID = '{}'" .format(CU_ID)
        wallet_query = "SELECT WALLET_INVENTORY FROM WALLET WHERE CU_ID = '{}'" .format(CU_ID)

        information_query_data = cur.execute(information_query)
        order_list_query_data = cur.execute(order_list_query)
        basket_list_query_data = cur.execute(basket_list_query)
        favorite_list_query_data = cur.execute(favorite_list_query)
        comments_list_query_data = cur.execute(comments_list_query)
        wallet_query_data = cur.execute(wallet_query)

        return information_query_data, order_list_query_data, basket_list_query_data, favorite_list_query_data, comments_list_query_data, wallet_query_data


    def load_SL_profile(self, SL_ID):
        conn = sqlite3.connect('database.sqlite3')
        cur = conn.cursor()
        information_query = "SELECT SL_ID, EMAIL, PASSWORD, STATUS, SCORE, LOCATION, ACTIVE_STATUS FROM SELLER WHERE SL_ID = '{}'" .format(SL_ID)
        product_list_query = "SELECT PRODUCTS FROM SELLER WHERE SL_ID = '{}'" .format(SL_ID)
        
        information_query_data = cur.execute(information_query)
        product_list_query_data = cur.execute(product_list_query)
        

        return information_query_data, product_list_query_data


    def check_product(self):
        conn = sqlite3.connect('database.sqlite3')
        cur = conn.cursor()
        query = "SELECT PR_ID, NAME, NUMBER, PRICE, SELLER_SL_ID, STATUS FROM 'PRODUCT' WHERE STATUS = 'NEW' "
        new_product_report_data = cur.execute(query)
        return new_product_report_data

    def accept_product(self, PR_ID):
        conn = sqlite3.connect('database.sqlite3')
        try:
            conn.execute('''UPDATE PRODUCT STATUS = ACCEPTED WHERE PR_ID = {};'''.format(PR_ID))
            conn.commit()
        except sqlite3.Error:
            print("error! something went wrong")
        else:
            print("Done!")


    def reject_product(self, PR_ID):
        conn = sqlite3.connect('database.sqlite3')
        cur = conn.cursor()
        try:
            conn.execute('''UPDATE PRODUCT STATUS = REJECTED WHERE PR_ID = {};'''.format(PR_ID))
            conn.commit()
        except sqlite3.Error:
            print("error! something went wrong")
        else:
            print("Done!")


    def check_seller(self):
        conn = sqlite3.connect('database.sqlite3')
        cur = conn.cursor()
        query = "SELECT SL_ID, EMAIL, PRODUCTS, STATUS, SCORE, LOCATION FROM SELLER  WHERE STATUS = 'NEW' "
        new_seller_report_data = cur.execute(query)
        return new_seller_report_data

    def accept_seller(self, SL_ID):
        conn = sqlite3.connect('database.sqlite3')
        try:
            conn.execute('''UPDATE SELLER STATUS = ACCEPTED WHERE SL_ID = {};'''.format(SL_ID))
            conn.commit()
        except sqlite3.Error:
            print("error! something went wrong")
        else:
            print("Done!")

    def reject_seller(self, SL_ID):
        conn = sqlite3.connect('database.sqlite3')
        try:
            conn.execute('''UPDATE SELLER STATUS = REJECTED WHERE SL_ID = {};'''.format(SL_ID))
            conn.commit()
        except sqlite3.Error:
            print("error! something went wrong")
        else:
            print("Done!")

    def check_order(self):
        conn = sqlite3.connect('database.sqlite3')
        cur = conn.cursor()
        query = "SELECT CU_ID, SL_ID, ORDER_LIST, DATE, STATUS FROM 'ORDER' WHERE STATUS = 'NEW' "
        new_order_report_data = cur.execute(query)
        return new_order_report_data

    def accept_order(self, CU_ID):
        conn = sqlite3.connect('database.sqlite3')
        try:
            conn.execute('''UPDATE 'ORDER' STATUS = ACCEPTED WHERE CU_ID = {};'''.format(CU_ID))
            conn.commit()
        except sqlite3.Error:
            print("error! something went wrong")
        else:
            print("Done!")

    def reject_order(self, CU_ID):
        conn = sqlite3.connect('database.sqlite3')
        try:
            conn.execute('''UPDATE 'ORDER' STATUS = REJECTED WHERE CU_ID = {};'''.format(CU_ID))
            conn.commit()
        except sqlite3.Error:
            print("error! something went wrong")
        else:
            print("Done!")
    

    def costumer_list (self):
        conn = sqlite3.connect('database.sqlite3')
        cur = conn.cursor()
        query = "SELECT CU_ID, EMAIL, LOCATION FROM COSTUMER WHERE ACTIVE_STATUS = 'ACTIVE'"
        costumer_list_data = cur.execute(query)
        return costumer_list_data

    def costumer_report (self):
        conn = sqlite3.connect('database.sqlite3')
        cur = conn.cursor()
        query = "SELECT CU_ID, SCORE, TOTAL_PURCHASE FROM COSTUMER WHERE ACTIVE_STATUS = 'ACTIVE'"
        costumer_report_data = cur.execute(query)
        return costumer_report_data

    def shop_reports(self):
        conn = sqlite3.connect('database.sqlite3')
        cur = conn.cursor()
        query = 'SELECT NAME, PRODUCTS_PR_ID, COSTUMER_CU_ID, SELLER_SL_ID  FROM SHOP'
        shop_report_data = cur.execute(query)
        return shop_report_data


    def seller_list(self):
        conn = sqlite3.connect('database.sqlite3')
        cur = conn.cursor()
        query = "SELECT SL_ID,EMAIL,SCORE FROM SELLER WHERE ACTIVE_STATUS = 'ACTIVE'"
        seller_report_data = cur.execute(query)
        return seller_report_data

    def seller_report(self):
        conn = sqlite3.connect('database.sqlite3')
        cur = conn.cursor()
        query = "SELECT SL_ID,SCORE, TOTAL_SALES, NET_INCOME FROM SELLER WHERE ACTIVE_STATUS = 'ACTIVE'"
        seller_list_data = cur.execute(query)
        return seller_list_data

    def product_report(self):
    # give list of all products and number of them 
        conn = sqlite3.connect('database.sqlite3')
        cur = conn.cursor()
        query = 'SELECT PR_ID,NAME,NUMBER, PRICE FROM PRODUCT'
        product_report_data = cur.execute(query)
        return product_report_data

    def sell_report(self):
        conn = sqlite3.connect('database.sqlite3')
        cur = conn.cursor()
        query = 'SELECT PR_ID, SHOP_NAME, SL_ID, DATE_TIME, CU_ID FROM SELL_REPORT'
        sell_report_data =  cur.execute(query)
        return sell_report_data

    def off_code_generator(self, EXP, PR_ID, CU_ID, NUM, PERC):
        num = str(rint(1000000,9999999))
        off_code = 'off{}' .format(num)
        conn = sqlite3.connect('database.sqlite3')
        conn.execute('''INSERT INTO OFF (CODE, PR_ID, EXP_DATE, CU_ID, NUMBER, PERCENTAGE) \
             VALUES('{}','{}','{}','{}','{}','{}');'''.format(off_code, PR_ID, EXP, CU_ID, NUM, PERC))
        conn.commit()
        conn.close()



    def cu_id_generator(self):
        '''
        in this method we generate id for costumers 'CU123456'
        '''
        conn = sqlite3.connect('database.sqlite3')
        cursor = conn.execute ("SELECT count(*) FROM CUSTOMER")
        for row in cursor:
            num_of_records = row[0]
        num = (111111 + num_of_records ) 
        CU_id = 'CU%d' %(num)
        return CU_id 

    def SL_id_generator(self):
        '''
        in this method we generate id for seller 'SL123456'
        '''
        conn = sqlite3.connect('database.sqlite3')
        cursor = conn.execute ("SELECT count(*) FROM CUSTOMER")
        for row in cursor:
            num_of_records = row[0]
        num = (111111 + num_of_records )  
        SL_id = 'SL%d' %(num)
        return SL_id 

# shop sql table

'''CREATE TABLE "SHOP" (
	"ID"	INTEGER NOT NULL UNIQUE,
	"NAME"	TEXT NOT NULL UNIQUE,
	"PRODUCTS_PR_ID"	TEXT,
	"CUSTOMER_CU_ID"	TEXT,
	"SELLER_SL_ID"	TEXT,
	"INVENTORY_WALLET"	INTEGER DEFAULT 0,
	FOREIGN KEY("CUSTOMER_CU_ID") REFERENCES "CUSTOMER"("CU_ID"),
	FOREIGN KEY("PRODUCTS_PR_ID") REFERENCES "PRODUCT"("PR_ID"),
	PRIMARY KEY("ID" AUTOINCREMENT)
);'''

class shop:
    def __init__(self, shop_name : str, seller : list , products : list, costumer : list, inventory_wallet : int):
        self.__shop_name = shop_name
        self.__seller = seller
        self.__products = products
        self.__costumer = costumer
        self.__inventory_wallet = inventory_wallet


    def add_to_db(self):
        conn = sqlite3.connect('database.sqlite3')
        data = self.__dict__
        try:
            conn.execute('''INSERT INTO SHOP(NAME, PRODUCTS_PR_ID, CUSTOMER_CU_ID, SELLER_SL_ID, INVENTORY_WALLET) \
            VALUES('{}', '{}', '{}', '{}', '{}');''' .format(data['_shop__shop_name'], data['_shop__products'],
                                                     data['_shop__costumer'], data['_shop__seller'], data['_shop__inventory_wallet']))
            conn.commit()           
        except sqlite3.Error:
            print("error!")
        else:
            print("Done!")
        
        
    def add_costumer_to_shop(self, CU_ID):
        conn = sqlite3.connect('database.sqlite3')
        try:
            conn.execute('''UPDATE COSTUMER ACTIVE_STATUS = ACTIVE WHERE CU_ID = {};''' .format(CU_ID))
            conn.commit()           
        except sqlite3.Error:
            print("error!")
        else:
            print("Done!")



    def del_customer_to_shop(self, CU_ID):
        conn = sqlite3.connect('database.sqlite3')
        try:
            conn.execute('''UPDATE COSTUMER ACTIVE_STATUS = SUSPENDED WHERE CU_ID = {};''' .format(CU_ID))
            conn.commit()           
        except sqlite3.Error:
            print("error!")
        else:
            print("Done!")



    def add_seller_to_shop(self, SL_ID):
        conn = sqlite3.connect('database.sqlite3')
        try:
            conn.execute('''UPDATE SELLER ACTIVE_STATUS = ACTIVE WHERE SL_ID = {};''' .format(SL_ID))
            conn.commit()           
        except sqlite3.Error:
            print("error!")
        else:
            print("Done!")



    def del_seller_to_shop(self, SL_ID):
        conn = sqlite3.connect('database.sqlite3')
        try:
            conn.execute('''UPDATE SELLER ACTIVE_STATUS = SUSPENDED WHERE SL_ID = {};''' .format(SL_ID))
            conn.commit()           
        except sqlite3.Error:
            print("error!")
        else:
            print("Done!")



    # def card_to_wallet(self, value):
    #     pass


    # def wallet_to_card(self, value):
    #     pass


    def time_compute(self, CU_location, SL_location):
        pass

















from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import * 
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import Qt



################################ start operator panel GUI ###################################

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
        self.new_seller_request_table.setColumnCount(8)
        self.new_seller_request_table.setRowCount(0)

    #_________________________ new seller request table fill __________________________
        self.new_seller_request_table.setColumnWidth(0,60)
        self.new_seller_request_table.setColumnWidth(1,60)
        self.new_seller_request_table.setColumnWidth(2,100)
        self.new_seller_request_table.setColumnWidth(3,150)
        self.new_seller_request_table.setColumnWidth(4,150)
        self.new_seller_request_table.setColumnWidth(5,150)
        self.new_seller_request_table.setColumnWidth(6,150)
        self.new_seller_request_table.setColumnWidth(7,150)

        self.new_seller_request_load_data()
        self.new_seller_request_table.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers) # make table un editable

        self.new_seller_request_table.setHorizontalHeaderLabels(['accept', 'reject', 'SL_ID','EMAIL', 'PRODUCTS', 'STATUS', 'SCORE', 'LOCATION' ])
        self.new_seller_request_table.verticalHeader().hide()
        self.new_seller_request_table.cellClicked.connect(self.print_test)

        for index in range(self.new_seller_request_table.rowCount()):
            self.seller_request_accept  = QPushButton("✅")
                
            self.new_seller_request_table.setCellWidget(index, 0, self.seller_request_accept )

        for index in range(self.new_seller_request_table.rowCount()):
            self.seller_request_reject  = QPushButton("❌")
            

            self.new_seller_request_table.setCellWidget(index, 1, self.seller_request_reject )

            # self.show_seller_profile.clicked.connect(self.get_buy_id)
    #________________________________________________________________________

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
        self.total_rate_refresh_button = QtWidgets.QPushButton(self.tab)
        self.total_rate_refresh_button.setObjectName("total_rate_refresh_button")
        self.gridLayout_6.addWidget(self.total_rate_refresh_button, 7, 4, 1, 1)
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
        self.total_rate_list = QtWidgets.QTableWidget(self.tab)
        self.total_rate_list.setObjectName("total_rate_list")
        self.total_rate_list.setColumnCount(0)
        self.total_rate_list.setRowCount(0)
        self.gridLayout_6.addWidget(self.total_rate_list, 1, 4, 5, 1)
        self.seller_list_line_edit = QtWidgets.QLineEdit(self.tab)
        self.seller_list_line_edit.setObjectName("seller_list_line_edit")

        self.seller_list_line_edit.setPlaceholderText("Search SL_ID ...")
        self.seller_list_line_edit.textChanged.connect(self.search_seller)


        self.gridLayout_6.addWidget(self.seller_list_line_edit, 4, 2, 1, 1)
        self.seller_report_refresh_button = QtWidgets.QPushButton(self.tab)
        self.seller_report_refresh_button.setObjectName("seller_report_refresh_button")
        self.gridLayout_6.addWidget(self.seller_report_refresh_button, 7, 3, 1, 1)
        self.seller_report_list = QtWidgets.QTableWidget(self.tab)
        self.seller_report_list.setObjectName("seller_report_list")
        self.seller_report_list.setColumnCount(4)
        self.seller_report_list.setRowCount(0)

        #_________________________ seller report table fill __________________________
        self.seller_report_list.setColumnWidth(0,100)
        self.seller_report_list.setColumnWidth(1,150)
        self.seller_report_list.setColumnWidth(2,150)
        self.seller_report_list.setColumnWidth(3,150)
        self.seller_report_list.setHorizontalHeaderLabels(['SL_ID', 'SCORE', 'TOTAL SALE', 'NET INCOME'])

        self.seller_report_load_data()
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
        self.costumer_report_table.setColumnCount(3)
        self.costumer_report_table.setRowCount(0)
      #_________________________ costumer report table fill __________________________
        self.costumer_report_table.setColumnWidth(0,100)
        self.costumer_report_table.setColumnWidth(1,100)
        self.costumer_report_table.setColumnWidth(2,200)

        
        self.costumer_report_table.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers) # make table un editable

        self.costumer_report_table.setHorizontalHeaderLabels(['CU_ID', 'SCORE', 'TOTAL PURCHASE'])

        self.costumer_report_list_load_data()

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
        self.label_4.setText(_translate("Form", "total rate"))
        self.sell_report_refresh_button.setText(_translate("Form", "refresh"))
        self.seller_list_refresh_button.setText(_translate("Form", "refresh"))
        self.total_rate_refresh_button.setText(_translate("Form", "refresh"))
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
    def __row_count_SPECIAL(self, table_name:str, SPECIAL, COLUMN_NAME):
        conn = sqlite3.connect('database.sqlite3')
        cursor = conn.execute("SELECT count(*) FROM '{}' WHERE {} = '{}'".format(table_name, COLUMN_NAME,SPECIAL))
        for row in cursor:
            return row[0]

    #_____________________ search_seller function _____________________
    def search_seller(self, SL_ID):
        self.seller_list_table.setCurrentItem(None)
        if not SL_ID:
            return 
        matching_items = self.seller_list_table.findItems(SL_ID, Qt.MatchContains)
        if matching_items:
            item = matching_items[0]  # Take the first.
            self.seller_list_table.setCurrentItem(item)

    #___________________________________________________________________

    #_____________________ seller report load data function _____________________

    def seller_report_load_data(self):
        row_count = self.__row_count_SPECIAL('SELLER', 'ACTIVE', 'ACTIVE_STATUS')
        self.seller_report_list.setRowCount(row_count)
        tablerow = 0 
        for row in the_operator.seller_report():
            self.seller_report_list.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.seller_report_list.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.seller_report_list.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.seller_report_list.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[3]))
            tablerow +=1

    #_____________________ costumer report list load data function _____________________
    def costumer_report_list_load_data(self):
        row_count = self.__row_count_SPECIAL('COSTUMER', 'ACTIVE', 'ACTIVE_STATUS')
        self.costumer_report_table.setRowCount(row_count)
        tablerow = 0 
        for row in the_operator.costumer_report():
            self.costumer_report_table.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.costumer_report_table.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.costumer_report_table.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            
            tablerow +=1
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
        row_count = self.__row_count_SPECIAL('PRODUCT','NEW', 'STATUS' )
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

    #_____________________ new seller request load data function _____________________
    def new_seller_request_load_data(self):
        row_count = self.__row_count_SPECIAL('SELLER','NEW', 'STATUS' )
        self.new_seller_request_table.setRowCount(row_count)
        tablerow = 0 
        for row in the_operator.check_product():
            self.new_seller_request_table.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[0]))
            self.new_seller_request_table.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[1]))
            self.new_seller_request_table.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row[2]))
            self.new_seller_request_table.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(row[3]))
            self.new_seller_request_table.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(row[4]))
            self.new_seller_request_table.setItem(tablerow, 7, QtWidgets.QTableWidgetItem(row[5]))
            tablerow +=1

    #__________________________________________________________________________________


    #_____________________ new buy request load data function _____________________
    def buy_request_load_data(self):
        row_count = self.__row_count_SPECIAL('ORDER','NEW', 'STATUS' )
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
        row_count = self.__row_count_SPECIAL('COSTUMER', 'ACTIVE', 'ACTIVE_STATUS')
        self.costumerlist_table.setRowCount(row_count)
        tablerow = 0 
        for row in the_operator.costumer_list():
            self.costumerlist_table.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[0]))
            self.costumerlist_table.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[1]))
            self.costumerlist_table.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[2]))
            tablerow +=1
        
    #________________________________________________________________________


    #_____________________ seller load data function ________________________
    def seller_load_data(self):
        
        row_count = self.__row_count_SPECIAL('SELLER', 'ACTIVE', 'ACTIVE_STATUS')

        self.seller_list_table.setRowCount(row_count)
        tablerow = 0 
        for row in the_operator.seller_list():
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


