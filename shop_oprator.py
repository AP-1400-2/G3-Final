# author : Ali Asgharpour 
# Github : https://github.com/Ali-Asgharpour

import sqlite3

# traceback for handel and finde sqlite errors
import traceback

import sys
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

    # change operator panel password 
    def changepassword(self, oldpassword, newpassword):
        '''
        this method is for change operator admin password it will get old password and compair with database 
        password and it was same change it with new password 
        '''
        conn = sqlite3.connect('database.sqlite3')
        cur = conn.cursor()
        query = "SELECT PASSWORD FROM OPERATOR WHERE EMAIL = '{}' " .format(self.__email)
        cur.execute(query)
        old_password = cur.fetchone[0]
        if old_password == oldpassword:
            try:
                conn.execute("UPDATE OPERATOR SET PASSWORD = '{}' WHERE EMAIL = '{}'" .format(newpassword, self.__email))
                conn.commit()            
            except sqlite3.Error as er:
                print('SQLite error: %s' % (' '.join(er.args)))
                print("Exception class is: ", er.__class__)
                print('SQLite traceback: ')
                exc_type, exc_value, exc_tb = sys.exc_info()
                print(traceback.format_exception(exc_type, exc_value, exc_tb))
            else:
                print("Done!")

    # change operator panel email
    def changeemail(self, newewmail, password):
        '''
        this method is for change operator admin email it will get password and compair with database 
        password and it was same change email
        '''
        conn = sqlite3.connect('database.sqlite3')
        cursor = conn.execute("SELECT PASSWORD FROM OPERATOR WHERE EMAIL = '{}' " .format(self.__email))
        for row in cursor:
            database_password = row[0]
        if database_password == password:
            try:
                conn.execute("UPDATE OPERATOR SET EMAIL = '{}' WHERE EMAIL = '{}'" .format(newewmail, self.__email))
                conn.commit()
            except sqlite3.Error as er:
                print('SQLite error: %s' % (' '.join(er.args)))
                print("Exception class is: ", er.__class__)
                print('SQLite traceback: ')
                exc_type, exc_value, exc_tb = sys.exc_info()
                print(traceback.format_exception(exc_type, exc_value, exc_tb))
            else:
                print("Done!")

    # save operator to data base
    def save_to_db(self):
        conn = sqlite3.connect('database.sqlite3')
        data = self.__dict__
        try:
            conn.execute('''INSERT INTO OPERATOR(EMAIL,PASSWORD) \
                        VALUES('{}','{}');'''.format(data['_operators__email'],data['_operators__password']))
            conn.commit()
        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            print("Exception class is: ", er.__class__)
            print('SQLite traceback: ')
            exc_type, exc_value, exc_tb = sys.exc_info()
            print(traceback.format_exception(exc_type, exc_value, exc_tb))
        else:
            print("Done!")

    def total_rate_cu(self):
        conn = sqlite3.connect('database.sqlite3')
        cur = conn.cursor()
        cu_count_query = "SELECT count(*) FROM COSTUMER"
        data_cu_count_query = cur.execute(cu_count_query)
        for row in data_cu_count_query:
            count_data_cu_count_query = row[0]
        return count_data_cu_count_query
        
        
    def total_rate_sl(self):
        conn = sqlite3.connect('database.sqlite3')
        cur = conn.cursor()
        sl_count_query = "SELECT count(*) FROM SELLER"
        data_sl_count_query = cur.execute(sl_count_query)
        for row in data_sl_count_query:
            count_data_sl_count_query = row[0]
        return count_data_sl_count_query
        
        

    def total_rate_pr(self):
        conn = sqlite3.connect('database.sqlite3')
        cur = conn.cursor()
        pr_count_query = "SELECT count(*) FROM PRODUCT"
        data_pr_count_query = cur.execute(pr_count_query)
        for row in data_pr_count_query:
            count_data_pr_count_query = row[0]
        return count_data_pr_count_query
       

    def total_rate_shop(self):
        conn = sqlite3.connect('database.sqlite3')
        cur = conn.cursor()
        shop_count_query = "SELECT count(*) FROM SHOP"
        data_shop_count_query = cur.execute(shop_count_query)
        for row in data_shop_count_query:
            count_data_shop_count_query = row[0]
        return count_data_shop_count_query
    

    def load_cu_profile_information(self, CU_ID):
        conn = sqlite3.connect('database.sqlite3')
        cur = conn.cursor()
        information_query = "SELECT CU_ID, EMAIL, LOCATION, SCORE, TOTAL_PURCHASE, ACTIVE_STATUS FROM COSTUMER WHERE CU_ID = '{}'" .format(CU_ID)
        information_query_data = cur.execute(information_query)
        return information_query_data
        

    def load_cu_profile_order_list(self, CU_ID):
        conn = sqlite3.connect('database.sqlite3')
        cur = conn.cursor()
        order_list_query = "SELECT SL_ID, ORDER_LIST, DATE, STATUS FROM 'ORDER' WHERE CU_ID = '{}'" .format(CU_ID)
        order_list_query_data = cur.execute(order_list_query)
        return order_list_query_data
        
    def load_cu_profile_basket_list(self, CU_ID):
        conn = sqlite3.connect('database.sqlite3')
        cur = conn.cursor()
        basket_list_query = "SELECT BASKET FROM COSTUMER WHERE CU_ID = '{}'" .format(CU_ID)
        basket_list_query_data = cur.execute(basket_list_query)
        return basket_list_query_data
        
    def load_cu_profile_favorite_list(self, CU_ID):
        conn = sqlite3.connect('database.sqlite3')
        cur = conn.cursor()
        favorite_list_query = "SELECT FAVORIT FROM COSTUMER WHERE CU_ID = '{}'" .format(CU_ID)
        favorite_list_query_data = cur.execute(favorite_list_query)
        return favorite_list_query_data
        
    def load_cu_profile_comments_list(self, CU_ID):
        conn = sqlite3.connect('database.sqlite3')
        cur = conn.cursor()
        comments_list_query = "SELECT PR_ID, COMMENT FROM COMMENT_LIST WHERE CU_ID = '{}'" .format(CU_ID)
        comments_list_query_data = cur.execute(comments_list_query)
        return comments_list_query_data
        
    def load_cu_profile_wallet(self, CU_ID):
        conn = sqlite3.connect('database.sqlite3')
        cur = conn.cursor()
        wallet_query = "SELECT WALLET_INVENTORY FROM WALLET WHERE SPECIAL_ID = '{}'" .format(CU_ID)
        wallet_query_data = cur.execute(wallet_query)
        return wallet_query_data

    def load_SL_profile_information(self, SL_ID):
        conn = sqlite3.connect('database.sqlite3')
        cur = conn.cursor()
        information_query = "SELECT SL_ID, EMAIL, STATUS, SCORE, LOCATION, TOTAL_SALES, NET_INCOME, ACTIVE_STATUS FROM SELLER WHERE SL_ID = '{}'" .format(SL_ID)
        information_query_data = cur.execute(information_query)
        return information_query_data

    def load_SL_profile_product(self, SL_ID):
        conn = sqlite3.connect('database.sqlite3')
        cur = conn.cursor()
        product_list_query = "SELECT PRODUCTS FROM SELLER WHERE SL_ID = '{}'" .format(SL_ID)
        product_list_query_data = cur.execute(product_list_query)
        return product_list_query_data

    def check_product(self):
        conn = sqlite3.connect('database.sqlite3')
        cur = conn.cursor()
        query = "SELECT PR_ID, NAME, NUMBER, PRICE, SELLER_SL_ID, STATUS FROM 'PRODUCT' WHERE STATUS = 'NEW' "
        new_product_report_data = cur.execute(query)
        return new_product_report_data
    def check_reject_product(self):
        conn = sqlite3.connect('database.sqlite3')
        cur = conn.cursor()
        query = "SELECT PR_ID, NAME, NUMBER, PRICE, SELLER_SL_ID, STATUS FROM 'PRODUCT' WHERE STATUS = 'REJECTED' "
        new_product_report_data = cur.execute(query)
        return new_product_report_data

    def accept_product(self, PR_ID):
        conn = sqlite3.connect('database.sqlite3')
        try:
            conn.execute('''UPDATE PRODUCT SET STATUS = 'ACCEPTED' WHERE PR_ID = '{}';'''.format(PR_ID))
            conn.commit()
        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            print("Exception class is: ", er.__class__)
            print('SQLite traceback: ')
            exc_type, exc_value, exc_tb = sys.exc_info()
            print(traceback.format_exception(exc_type, exc_value, exc_tb))
        else:
            print("Done!")


    def reject_product(self, PR_ID):
        conn = sqlite3.connect('database.sqlite3')
        cur = conn.cursor()
        try:
            conn.execute('''UPDATE PRODUCT SET STATUS = 'REJECTED' WHERE PR_ID = '{}';'''.format(PR_ID))
            conn.commit()
        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            print("Exception class is: ", er.__class__)
            print('SQLite traceback: ')
            exc_type, exc_value, exc_tb = sys.exc_info()
            print(traceback.format_exception(exc_type, exc_value, exc_tb))
        else:
            print("Done!")


    def check_seller(self):
        conn = sqlite3.connect('database.sqlite3')
        cur = conn.cursor()
        query = "SELECT SL_ID, EMAIL, PRODUCTS, STATUS, SCORE, LOCATION FROM SELLER  WHERE STATUS = 'NEW' "
        new_seller_report_data = cur.execute(query)
        return new_seller_report_data
    def check_reject_seller(self):
        conn = sqlite3.connect('database.sqlite3')
        cur = conn.cursor()
        query = "SELECT SL_ID, EMAIL, PRODUCTS, STATUS, SCORE, LOCATION FROM SELLER  WHERE STATUS = 'REJECTED' "
        new_seller_report_data = cur.execute(query)
        return new_seller_report_data

    def accept_seller(self, SL_ID):
        conn = sqlite3.connect('database.sqlite3')
        try:
            conn.execute('''UPDATE SELLER SET  STATUS = 'ACCEPTED' WHERE SL_ID = '{}';'''.format(SL_ID))
            conn.commit()
            conn.execute('''UPDATE SELLER SET  ACTIVE_STATUS = 'ACTIVE' WHERE SL_ID = '{}';'''.format(SL_ID))
            conn.commit()
        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            print("Exception class is: ", er.__class__)
            print('SQLite traceback: ')
            exc_type, exc_value, exc_tb = sys.exc_info()
            print(traceback.format_exception(exc_type, exc_value, exc_tb))
        else:
            print("Done!")

    def reject_seller(self, SL_ID):
        conn = sqlite3.connect('database.sqlite3')
        try:
            conn.execute('''UPDATE SELLER SET STATUS = 'REJECTED' WHERE SL_ID = '{}';'''.format(SL_ID))
            conn.commit()
        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            print("Exception class is: ", er.__class__)
            print('SQLite traceback: ')
            exc_type, exc_value, exc_tb = sys.exc_info()
            print(traceback.format_exception(exc_type, exc_value, exc_tb))
        else:
            print("Done!")

    def check_order(self):
        conn = sqlite3.connect('database.sqlite3')
        cur = conn.cursor()
        query = "SELECT CU_ID, SL_ID, ORDER_LIST, DATE, STATUS FROM 'ORDER' WHERE STATUS = 'NEW' "
        new_order_report_data = cur.execute(query)
        return new_order_report_data


    def check_reject_order(self):
        conn = sqlite3.connect('database.sqlite3')
        cur = conn.cursor()
        query = "SELECT CU_ID, SL_ID, ORDER_LIST, DATE, STATUS FROM 'ORDER' WHERE STATUS = 'REJECTED' "
        new_order_report_data = cur.execute(query)
        return new_order_report_data

    def accept_order(self, CU_ID):
        conn = sqlite3.connect('database.sqlite3')
        try:
            conn.execute('''UPDATE 'ORDER' SET STATUS = 'ACCEPTED' WHERE CU_ID = '{}';'''.format(CU_ID))
            conn.commit()
        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            print("Exception class is: ", er.__class__)
            print('SQLite traceback: ')
            exc_type, exc_value, exc_tb = sys.exc_info()
            print(traceback.format_exception(exc_type, exc_value, exc_tb))
        else:
            print("Done!")

    def reject_order(self, CU_ID):
        conn = sqlite3.connect('database.sqlite3')
        try:
            conn.execute('''UPDATE 'ORDER' SET STATUS = 'REJECTED' WHERE CU_ID = '{}';'''.format(CU_ID))
            conn.commit()
        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            print("Exception class is: ", er.__class__)
            print('SQLite traceback: ')
            exc_type, exc_value, exc_tb = sys.exc_info()
            print(traceback.format_exception(exc_type, exc_value, exc_tb))
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

    def costumer_sort(self):
        conn = sqlite3.connect('database.sqlite3')
        cur = conn.cursor()
        query = "SELECT CU_ID, EMAIL, LOCATION FROM COSTUMER WHERE ACTIVE_STATUS = 'ACTIVE' ORDER BY SCORE desc"
        order_costumer_list_data = cur.execute(query)
        return order_costumer_list_data


    def seller_list(self):
        conn = sqlite3.connect('database.sqlite3')
        cur = conn.cursor()
        query = "SELECT SL_ID,EMAIL,SCORE FROM SELLER WHERE ACTIVE_STATUS = 'ACTIVE'"
        seller_report_data = cur.execute(query)
        return seller_report_data

    def seller_sort(self):
        conn = sqlite3.connect('database.sqlite3')
        cur = conn.cursor()
        query = "SELECT SL_ID,EMAIL,SCORE FROM SELLER WHERE ACTIVE_STATUS = 'ACTIVE' ORDER BY SCORE desc"
        order_seller_report_data = cur.execute(query)
        return order_seller_report_data

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
        cursor = conn.execute ("SELECT count(*) FROM SELLER")
        for row in cursor:
            num_of_records = row[0]
        num = (111111 + num_of_records )  
        SL_id = 'SL%d' %(num)
        return SL_id 

    def add_costumer_to_shop(self, CU_ID):
        conn = sqlite3.connect('database.sqlite3')
        try:
            conn.execute("UPDATE COSTUMER SET ACTIVE_STATUS = 'ACTIVE' WHERE CU_ID ='{}'" .format(CU_ID))
            conn.commit()           
        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            print("Exception class is: ", er.__class__)
            print('SQLite traceback: ')
            exc_type, exc_value, exc_tb = sys.exc_info()
            print(traceback.format_exception(exc_type, exc_value, exc_tb))
        else:
            print("Done!")


    
    def del_customer_to_shop(self, CU_ID):
        conn = sqlite3.connect('database.sqlite3')
        try:
            conn.execute('''UPDATE COSTUMER SET ACTIVE_STATUS = 'SUSPENDED' WHERE CU_ID = '{}';''' .format(CU_ID))
            conn.commit()           
        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            print("Exception class is: ", er.__class__)
            print('SQLite traceback: ')
            exc_type, exc_value, exc_tb = sys.exc_info()
            print(traceback.format_exception(exc_type, exc_value, exc_tb))
        else:
            print("Done!")



    def add_seller_to_shop(self, SL_ID):
        conn = sqlite3.connect('database.sqlite3')
        try:
            conn.execute('''UPDATE SELLER SET ACTIVE_STATUS = 'ACTIVE' WHERE SL_ID = '{}';''' .format(SL_ID))
            conn.commit()                       
        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            print("Exception class is: ", er.__class__)
            print('SQLite traceback: ')
            exc_type, exc_value, exc_tb = sys.exc_info()
            print(traceback.format_exception(exc_type, exc_value, exc_tb))
        else:
            print("Done!")



    def del_seller_to_shop(self, SL_ID):
        conn = sqlite3.connect('database.sqlite3')
        try:
            conn.execute("UPDATE SELLER SET ACTIVE_STATUS = 'SUSPENDED' WHERE SL_ID = '{}'" .format(SL_ID))
            conn.commit()           
        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            print("Exception class is: ", er.__class__)
            print('SQLite traceback: ')
            exc_type, exc_value, exc_tb = sys.exc_info()
            print(traceback.format_exception(exc_type, exc_value, exc_tb))
        else:
            print("Done!")


    def persentage(self):
         pass


    def __cu_distance(self, CU_location):
        conn = sqlite3.connect('database.sqlite3')
        cur1 = conn.cursor()
        query = "SELECT DISTANCE FROM LOCATION WHERE LOCAT LIKE '%{}%'".format(CU_location)
        cur1.execute(query)
        result = cur1.fetchone()[0]
        return int(result)

    def __sl_distance(self, SL_location):
        conn = sqlite3.connect('database.sqlite3')
        cur2 = conn.cursor()
        query = "SELECT DISTANCE FROM LOCATION  WHERE LOCAT LIKE '%{}%'".format(SL_location)
        cur2.execute(query)
        result = cur2.fetchone()[0]
        return int(result)

    def time_compute(self, CU_location, SL_location):
        CU_DISTANCE_from = self.__cu_distance(CU_location)
        SL_DISTANCE_from = self.__sl_distance(SL_location)
        time_SL_to_storeroom = SL_DISTANCE_from * 5
        time_storeroom_to_CU = CU_DISTANCE_from * 5

        return (time_SL_to_storeroom + time_storeroom_to_CU)//1080





from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import * 
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import Qt



################################ start operator panel GUI ###################################

the_operator = operators('first@operator.com', 1234)

class operator_panel(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1582, 921)
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.page_status = QtWidgets.QLabel(Form)
        self.page_status.setText("")
        self.page_status.setObjectName("page_status")
        self.gridLayout_2.addWidget(self.page_status, 2, 2, 1, 1)

        # self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        # self.verticalLayout_2.setObjectName("verticalLayout_2")
        # self.profile_button = QtWidgets.QPushButton(Form)
        # self.profile_button.setObjectName("profile_button")
        # self.verticalLayout_2.addWidget(self.profile_button)
        # self.log_out_button = QtWidgets.QPushButton(Form)
        # self.log_out_button.setObjectName("log_out_button")
        # self.verticalLayout_2.addWidget(self.log_out_button)
        # self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 2, 1)

        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_20 = QtWidgets.QLabel(Form)
        self.label_20.setObjectName("label_20")
        self.gridLayout_3.addWidget(self.label_20, 0, 1, 1, 1)
        self.new_product_refresh = QtWidgets.QPushButton(Form)
        self.new_product_refresh.setObjectName("new_product_refresh")

        self.new_product_refresh.clicked.connect(self.new_product_request_load_data)

        self.gridLayout_3.addWidget(self.new_product_refresh, 2, 1, 1, 1)
        self.show_rejected_button = QtWidgets.QPushButton(Form)
        self.show_rejected_button.setObjectName("show_rejected_button")
        self.show_rejected_button.setText("Show rejected")

        self.show_rejected_button.clicked.connect(self.open_rejected_page)

        self.gridLayout_3.addWidget(self.show_rejected_button, 8, 0, 1, 4)
        self.new_seller_table_refresh = QtWidgets.QPushButton(Form)
        self.new_seller_table_refresh.setObjectName("new_seller_table_refresh")

        self.new_seller_table_refresh.clicked.connect(self.new_seller_request_load_data)

        self.gridLayout_3.addWidget(self.new_seller_table_refresh, 2, 2, 1, 1)
        self.new_buy_table_refresh = QtWidgets.QPushButton(Form)
        self.new_buy_table_refresh.setObjectName("new_buy_table_refresh")

        self.new_buy_table_refresh.clicked.connect(self.buy_request_load_data)

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

        for index in range(self.new_buy_request_table.rowCount()):
            self.buy_request_accept  = QPushButton("✅")
            self.buy_request_accept.clicked.connect(self.finde_new_buy_id_accept)
            self.buy_request_accept.clicked.connect(self.accept_buy_request_function)
            self.new_buy_request_table.setCellWidget(index, 0, self.buy_request_accept )

        for index in range(self.new_buy_request_table.rowCount()):
            self.buy_request_reject  = QPushButton("❌")
            self.buy_request_reject.clicked.connect(self.finde_new_buy_id_reject)
            self.buy_request_accept.clicked.connect(self.reject_buy_request_function)
            

            self.new_buy_request_table.setCellWidget(index, 1, self.buy_request_reject )

            # self.show_seller_profile.clicked.connect(self.get_buy_id)
        
        
        self.gridLayout_3.addWidget(self.new_buy_request_table, 1, 0, 1, 1)
        self.new_product_tabel = QtWidgets.QTableWidget(Form)
        self.new_product_tabel.setObjectName("new_product_tabel")
        self.new_product_tabel.setColumnCount(8)
        self.new_product_tabel.setRowCount(0)

    # buy request table fill 
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

        for index in range(self.new_product_tabel.rowCount()):
            self.product_request_accept  = QPushButton("✅")
            self.product_request_accept.clicked.connect(self.finde_new_product_id_accept)
            self.product_request_accept.clicked.connect(self.accept_new_product_function)
            self.new_product_tabel.setCellWidget(index, 0, self.product_request_accept )

        for index in range(self.new_product_tabel.rowCount()):
            self.product_request_reject  = QPushButton("❌")
            self.product_request_reject.clicked.connect(self.finde_new_product_id_reject)
            self.product_request_reject.clicked.connect(self.reject_new_product_function)

            self.new_product_tabel.setCellWidget(index, 1, self.product_request_reject )


        self.gridLayout_3.addWidget(self.new_product_tabel, 1, 1, 1, 1)
        self.new_seller_request_table = QtWidgets.QTableWidget(Form)
        self.new_seller_request_table.setObjectName("new_seller_request_table")
        self.new_seller_request_table.setColumnCount(8)
        self.new_seller_request_table.setRowCount(0)

    # new seller request table fill
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

        for index in range(self.new_seller_request_table.rowCount()):
            self.seller_request_accept  = QPushButton("✅")
            self.seller_request_accept.clicked.connect(self.finde_new_seller_id_accept)
            self.seller_request_accept.clicked.connect(self.accept_new_seller_function)
                
            self.new_seller_request_table.setCellWidget(index, 0, self.seller_request_accept )

        for index in range(self.new_seller_request_table.rowCount()):
            self.seller_request_reject  = QPushButton("❌")
            self.seller_request_reject.clicked.connect(self.finde_new_seller_id_reject)
            self.seller_request_reject.clicked.connect(self.reject_new_seller_function)
            

            self.new_seller_request_table.setCellWidget(index, 1, self.seller_request_reject )


        self.gridLayout_3.addWidget(self.new_seller_request_table, 1, 2, 1, 1)
        self.check_distance_button = QtWidgets.QPushButton(Form)
        self.check_distance_button.setText("check distance")
        self.check_distance_button.clicked.connect(self.open_distance_page)
        self.check_distance_button.setObjectName("check_distance_button")
        self.gridLayout_3.addWidget(self.check_distance_button, 9, 0, 1, 3)

        # self.combobox_1 = QtWidgets.QComboBox(Form)
        # self.combobox_1.setObjectName("combobox_1")
        # self.combobox_1.addItem('Buy Request')
        # self.combobox_1.addItem('New Product')
        # self.combobox_1.addItem('New Seller')

        # self.gridLayout_3.addWidget(self.combobox_1, 3, 0, 1, 1)

        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 0, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 0, 2, 1, 1)

        # self.IDs_search = QtWidgets.QLineEdit(Form)
        # self.IDs_search.setObjectName("IDs_search")
        # self.IDs_search.setPlaceholderText("Search ...")

        # self.combobox_1.activated.connect(self.select_table)
        # table = self.combobox_1.currentText()

        # if self.combobox_1.currentText() == 'New Seller':
        #     self.IDs_search.textChanged.connect(self.seller_search)
        # if self.combobox_1.currentText() == 'Buy Request':
        #     self.IDs_search.textChanged.connect(self.buy_search)
        # if self.combobox_1.currentText() == 'New Product':
        #     self.IDs_search.textChanged.connect(self.product_search)
        

        # self.gridLayout_3.addWidget(self.IDs_search, 3, 1, 1, 2)

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
        # OFF CODE TABLE 
        self.off_code_table.setColumnWidth(0,100)
        self.off_code_table.setColumnWidth(1,100)
        self.off_code_table.setColumnWidth(2,100)
        self.off_code_table.setColumnWidth(3,100)
        self.off_code_table.setColumnWidth(4,100)
        self.off_code_table.setColumnWidth(5,100)

        self.off_code_table.setHorizontalHeaderLabels(['CODE','PR_ID', 'EXP', 'CU_ID', 'NUMBER', 'PERCENTAGE'])

        self.load_off_data()

        self.verticalLayout_15.addWidget(self.off_code_table)
        self.refresh_off_table = QtWidgets.QPushButton(Form)
        self.refresh_off_table.setObjectName("refresh_off_table")

    # OFF CODE TABLE refresh button 
        self.refresh_off_table.clicked.connect(self.load_off_data)

        self.verticalLayout_15.addWidget(self.refresh_off_table)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.off_num = QtWidgets.QLineEdit(Form)
        self.off_num.setObjectName("off_num")
        self.off_num.setPlaceholderText("numbers")

        self.gridLayout_5.addWidget(self.off_num, 1, 1, 1, 1)
        self.off_EXP_date = QtWidgets.QLineEdit(Form)
        self.off_EXP_date.setObjectName("off_EXP_date")
        self.off_EXP_date.setPlaceholderText("year-mounth-day")


        self.gridLayout_5.addWidget(self.off_EXP_date, 0, 1, 1, 1)
        self.off_percentage = QtWidgets.QLineEdit(Form)
        self.off_percentage.setObjectName("off_percentage")
        self.off_percentage.setPlaceholderText("off percentage")

        self.gridLayout_5.addWidget(self.off_percentage, 4, 1, 1, 1)
        self.off_CU_ID = QtWidgets.QLineEdit(Form)
        self.off_CU_ID.setObjectName("off_CU_ID")
        self.off_CU_ID.setPlaceholderText("Costumer ID")

        self.gridLayout_5.addWidget(self.off_CU_ID, 2, 1, 1, 1)
        self.off_PR_ID = QtWidgets.QLineEdit(Form)
        self.off_PR_ID.setObjectName("off_PR_ID")
        self.off_PR_ID.setPlaceholderText("Product ID")

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
        # off code button 
        self.generate_off.clicked.connect(self.generate_off_code)
        
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

        self.seller_list_add_button.clicked.connect(self.seller_list_add_function)

        self.gridLayout_6.addWidget(self.seller_list_add_button, 7, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setObjectName("label_3")
        self.gridLayout_6.addWidget(self.label_3, 0, 3, 1, 1)
        self.seller_list_sort_button = QtWidgets.QPushButton(self.tab)

        self.seller_list_sort_button.clicked.connect(self.seller_load_data_order)

        self.seller_list_sort_button.setObjectName("seller_list_sort_button")
        self.gridLayout_6.addWidget(self.seller_list_sort_button, 2, 2, 1, 1)
        self.seller_list_delete_button = QtWidgets.QPushButton(self.tab)
        self.seller_list_delete_button.setObjectName("seller_list_delete_button")

        self.seller_list_delete_button.clicked.connect(self.seller_list_delete_function)
        
        

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
        # seller table fill
        self.seller_list_table.setColumnWidth(0,60)
        self.seller_list_table.setColumnWidth(1,100)
        self.seller_list_table.setColumnWidth(2,150)
        self.seller_list_table.setColumnWidth(3,100)

        self.seller_load_data() 
        self.seller_list_table.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers) # make table un editable

        self.seller_list_table.setHorizontalHeaderLabels(['profile', 'SL_ID', 'EMAIL', 'SCORE'])
        self.seller_list_table.verticalHeader().hide()

        for index in range(self.seller_list_table.rowCount()):
            self.show_seller_profile  = QPushButton("🙍")
            self.seller_list_table.setCellWidget(index, 0, self.show_seller_profile )

            self.show_seller_profile.clicked.connect(self.get_SL_ID)
            self.show_seller_profile.clicked.connect(self.switch_to_seller_profile)
            self.show_seller_profile.setStyleSheet("background-color : #c9c9c9")

        self.verticalLayout_7.addWidget(self.seller_list_table)
        self.gridLayout_6.addLayout(self.verticalLayout_7, 1, 2, 1, 1)
        self.sell_report_refresh_button = QtWidgets.QPushButton(self.tab)
        self.sell_report_refresh_button.setObjectName("sell_report_refresh_button")

        self.sell_report_refresh_button.clicked.connect(self.sell_report_load_data)

        self.gridLayout_6.addWidget(self.sell_report_refresh_button, 7, 0, 1, 1)
        self.seller_list_refresh_button = QtWidgets.QPushButton(self.tab)
        self.seller_list_refresh_button.setObjectName("seller_list_refresh_button")

        self.seller_list_refresh_button.clicked.connect(self.seller_load_data)

        self.gridLayout_6.addWidget(self.seller_list_refresh_button, 3, 2, 1, 1)
        self.total_rate_refresh_button = QtWidgets.QPushButton(self.tab)
        self.total_rate_refresh_button.setObjectName("total_rate_refresh_button")

        self.total_rate_refresh_button.clicked.connect(self.total_rate_load_data)

        self.gridLayout_6.addWidget(self.total_rate_refresh_button, 7, 4, 1, 1)
        self.sell_report_table = QtWidgets.QTableWidget(self.tab)
        self.sell_report_table.setObjectName("sell_report_table")
        self.sell_report_table.setColumnCount(5)
        self.sell_report_table.setRowCount(0)
        # sell table fill
        self.sell_report_table.setColumnWidth(0,100)
        self.sell_report_table.setColumnWidth(1,100)
        self.sell_report_table.setColumnWidth(2,100)
        self.sell_report_table.setColumnWidth(3,100)
        self.sell_report_table.setColumnWidth(4,100)

        self.sell_report_table.setHorizontalHeaderLabels(['PR_ID', 'SHOP_NAME','SL_ID', 'DATE', 'CU_ID'])

        self.sell_report_load_data()

        
        self.gridLayout_6.addWidget(self.sell_report_table, 1, 0, 5, 1)
        # self.Shop_report_refresh = QtWidgets.QPushButton(self.tab)
        # self.Shop_report_refresh.setObjectName("Shop_report_refresh")

        # self.Shop_report_refresh.clicked.connect(self.shop_report_load_data)

        # self.gridLayout_6.addWidget(self.Shop_report_refresh, 7, 5, 1, 1)
        # self.label_17 = QtWidgets.QLabel(self.tab)
        # self.label_17.setObjectName("label_17")
        # self.gridLayout_6.addWidget(self.label_17, 0, 5, 1, 1)
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label.setObjectName("label")
        self.gridLayout_6.addWidget(self.label, 0, 0, 1, 1)
        # self.shop_report_table = QtWidgets.QTableWidget(self.tab)
        # self.shop_report_table.setObjectName("shop_report_table")
        # self.shop_report_table.setColumnCount(4)
        # self.shop_report_table.setRowCount(0)
        # #_____________________shop report table fill_________________
        # self.shop_report_table.setColumnWidth(0, 100)
        # self.shop_report_table.setColumnWidth(1, 200)
        # self.shop_report_table.setColumnWidth(2, 200)
        # self.shop_report_table.setColumnWidth(3, 200)
        # self.shop_report_table.setHorizontalHeaderLabels(['Name', 'Products', 'Costumers', 'Sellers'])

        # self.shop_report_load_data()
        #____________________________________________________________

        # self.gridLayout_6.addWidget(self.shop_report_table, 1, 5, 5, 1)
        self.total_rate_list = QtWidgets.QTableWidget(self.tab)
        self.total_rate_list.setObjectName("total_rate_list")
        self.total_rate_list.setColumnCount(1)
        self.total_rate_list.setRowCount(4)
        # total_rate_list
        self.total_rate_list.setColumnWidth(0, 100)
        
        self.total_rate_list.setHorizontalHeaderLabels(['Count'])
        self.total_rate_list.setVerticalHeaderLabels(['Costumer', 'Seller', 'Products', 'Shops'])
        self.total_rate_load_data()


        self.gridLayout_6.addWidget(self.total_rate_list, 1, 4, 5, 1)
        self.seller_list_line_edit = QtWidgets.QLineEdit(self.tab)
        self.seller_list_line_edit.setObjectName("seller_list_line_edit")

        self.seller_list_line_edit.setPlaceholderText("Search SL_ID ...")
        self.seller_list_line_edit.textChanged.connect(self.search_seller)
        self.seller_list_line_edit.textChanged.connect(self.seller_id_finder)
        
        
        

        self.gridLayout_6.addWidget(self.seller_list_line_edit, 4, 2, 1, 1)
        self.seller_report_refresh_button = QtWidgets.QPushButton(self.tab)
        self.seller_report_refresh_button.setObjectName("seller_report_refresh_button")

        self.seller_report_refresh_button.clicked.connect(self.seller_report_load_data)

        self.gridLayout_6.addWidget(self.seller_report_refresh_button, 7, 3, 1, 1)
        self.seller_report_list = QtWidgets.QTableWidget(self.tab)
        self.seller_report_list.setObjectName("seller_report_list")
        self.seller_report_list.setColumnCount(4)
        self.seller_report_list.setRowCount(0)

        # seller report table fill 
        self.seller_report_list.setColumnWidth(0,100)
        self.seller_report_list.setColumnWidth(1,150)
        self.seller_report_list.setColumnWidth(2,150)
        self.seller_report_list.setColumnWidth(3,150)
        self.seller_report_list.setHorizontalHeaderLabels(['SL_ID', 'SCORE', 'TOTAL SALE', 'NET INCOME'])

        self.seller_report_load_data()
         

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

        self.delete_costumer.clicked.connect(self.delete_costumer_from_list)

        self.gridLayout_8.addWidget(self.delete_costumer, 4, 0, 1, 1)
        self.costumer_ID_line = QtWidgets.QLineEdit(self.tab_2)
        self.costumer_ID_line.setObjectName("costumer_ID_line")

        self.costumer_ID_line.setPlaceholderText("Search CU_ID ...")
        self.costumer_ID_line.textChanged.connect(self.search_costumer)
        self.costumer_ID_line.textChanged.connect(self.costumer_id_finder)


        self.gridLayout_8.addWidget(self.costumer_ID_line, 3, 0, 1, 1)
        self.costumer_list_refresh_button = QtWidgets.QPushButton(self.tab_2)
        self.costumer_list_refresh_button.setObjectName("costumer_list_refresh_button")
        self.gridLayout_8.addWidget(self.costumer_list_refresh_button, 7, 0, 1, 1)
        self.refresh_costumer_list_table_button = QtWidgets.QPushButton(self.tab_2)
        self.refresh_costumer_list_table_button.setObjectName("refresh_costumer_list_table_button")

        self.refresh_costumer_list_table_button.clicked.connect(self.costumer_load_data)

        self.gridLayout_8.addWidget(self.refresh_costumer_list_table_button, 7, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_8.addWidget(self.pushButton_5, 6, 0, 1, 1)
        self.addcostumer = QtWidgets.QPushButton(self.tab_2)
        self.addcostumer.setObjectName("addcostumer")

        self.addcostumer.clicked.connect(self.add_costumer_list)

        self.gridLayout_8.addWidget(self.addcostumer, 6, 0, 1, 1)
        self.costumer_list_sort = QtWidgets.QPushButton(self.tab_2)

        self.costumer_list_sort.clicked.connect(self.order_costumer_table_fill)

        self.costumer_list_sort.setObjectName("costumer_list_sort")
        self.gridLayout_8.addWidget(self.costumer_list_sort, 2, 0, 1, 1)
        self.costumerlist_table = QtWidgets.QTableWidget(self.tab_2)
        self.costumerlist_table.setObjectName("costumerlist_table")
        self.costumerlist_table.setColumnCount(4)
        self.costumerlist_table.setRowCount(0)

        # costumer table fill 
        self.costumerlist_table.setColumnWidth(0,60)
        self.costumerlist_table.setColumnWidth(1,100)
        self.costumerlist_table.setColumnWidth(2,200)
        self.costumerlist_table.setColumnWidth(3,100)

        
        self.costumerlist_table.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers) # make table un editable

        self.costumerlist_table.setHorizontalHeaderLabels(['profile', 'CU_ID', 'EMAIL', 'LOCATION'])
        self.costumerlist_table.verticalHeader().hide()
        self.costumer_load_data()

        for index in range(self.costumerlist_table.rowCount()):
            self.show_costumer_profile  = QPushButton("🙍")
            self.costumerlist_table.setCellWidget(index, 0, self.show_costumer_profile )

            self.show_costumer_profile .clicked.connect(self.get_CU_ID)
            self.show_costumer_profile .clicked.connect(self.switch_to_costumer_profile)
            self.show_costumer_profile.setStyleSheet("background-color : #c9c9c9")
        
        self.gridLayout_8.addWidget(self.costumerlist_table, 1, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout_8.addWidget(self.label_7, 0, 0, 1, 1)
        self.costumer_report_table = QtWidgets.QTableWidget(self.tab_2)
        self.costumer_report_table.setObjectName("costumer_report_table")
        self.costumer_report_table.setColumnCount(3)
        self.costumer_report_table.setRowCount(0)
      # costumer report table fill 
        self.costumer_report_table.setColumnWidth(0,100)
        self.costumer_report_table.setColumnWidth(1,100)
        self.costumer_report_table.setColumnWidth(2,200)

        
        self.costumer_report_table.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers) # make table un editable

        self.costumer_report_table.setHorizontalHeaderLabels(['CU_ID', 'SCORE', 'TOTAL PURCHASE'])

        self.costumer_report_list_load_data()



        self.gridLayout_8.addWidget(self.costumer_report_table, 1, 1, 6, 1)
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout_8.addWidget(self.label_8, 0, 1, 1, 1)
        self.costumer_report_refresh = QtWidgets.QPushButton(self.tab_2)
        self.costumer_report_refresh.setObjectName("costumer_report_refresh")

        self.costumer_report_refresh.clicked.connect(self.costumer_report_list_load_data)

        self.gridLayout_8.addWidget(self.costumer_report_refresh, 7, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout_8.addWidget(self.label_5, 0, 2, 1, 1)
        self.product_table_refresh = QtWidgets.QPushButton(self.tab_2)
        self.product_table_refresh.setObjectName("product_table_refresh")

        self.product_table_refresh.clicked.connect(self.product_table_load_data)

        self.gridLayout_8.addWidget(self.product_table_refresh, 7, 2, 1, 1)
        self.product_table = QtWidgets.QTableWidget(self.tab_2)
        self.product_table.setObjectName("product_table")
        self.product_table.setColumnCount(4)
        self.product_table.setRowCount(0)
        # product table fill 
        self.product_table.setColumnWidth(0,100)
        self.product_table.setColumnWidth(1,200)
        self.product_table.setColumnWidth(2,50)
        self.product_table.setColumnWidth(3,80)

        
        self.product_table.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers) # make table un editable

        self.product_table.setHorizontalHeaderLabels(['PR_ID', 'NAME', 'NUMBER', 'PRICE'])
        
        self.product_table_load_data()
        
        

        self.gridLayout_8.addWidget(self.product_table, 1, 2, 6, 1)
        self.gridLayout_7.addLayout(self.gridLayout_8, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout_2.addWidget(self.tabWidget, 0, 2, 2, 1)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def open_error_page(self):
        self.window = QtWidgets.QWidget()
        self.ui = error_page()
        self.ui.setupUi(self.window)
        self.window.show()

    def switch_to_seller_profile(self):
        self.window = QtWidgets.QWidget()
        self.ui = seller_profile()
        self.ui.setupUi(self.window)
        self.window.show()

    def switch_to_costumer_profile(self):
        self.window = QtWidgets.QWidget()
        self.ui = costumer_profile()
        self.ui.setupUi(self.window)
        self.window.show()
    
    def get_CU_ID(self):
        current_row = self.costumerlist_table.currentRow()
        current_column = self.costumerlist_table.currentColumn()
        cell_value = self.costumerlist_table.item(current_row, current_column + 1).text()
        global get_CU_ID_value
        get_CU_ID_value = cell_value

    def get_SL_ID(self):
        current_row = self.seller_list_table.currentRow()
        current_column = self.seller_list_table.currentColumn()
        cell_value = self.seller_list_table.item(current_row, current_column + 1).text()
        global get_SL_ID_value
        get_SL_ID_value = cell_value

    def finde_new_seller_id_accept(self):
        current_row = self.new_seller_request_table.currentRow()
        current_column = self.new_seller_request_table.currentColumn()
        cell_value = self.new_seller_request_table.item(current_row, current_column + 2).text()
        global New_SL_ID_value
        New_SL_ID_value = cell_value

    def finde_new_seller_id_reject(self):
        current_row = self.new_seller_request_table.currentRow()
        current_column = self.new_seller_request_table.currentColumn()
        cell_value = self.new_seller_request_table.item(current_row, current_column + 1).text()
        global New_SL_ID_value
        New_SL_ID_value = cell_value

    def finde_new_product_id_accept(self):
        current_row = self.new_product_tabel.currentRow()
        current_column = self.new_product_tabel.currentColumn()
        cell_value = self.new_product_tabel.item(current_row, current_column + 2).text()
        global New_PR_ID_value
        New_PR_ID_value = cell_value
        
    def finde_new_product_id_reject(self):
        current_row = self.new_product_tabel.currentRow()
        current_column = self.new_product_tabel.currentColumn()
        cell_value = self.new_product_tabel.item(current_row, current_column + 1).text()
        global New_PR_ID_value
        New_PR_ID_value = cell_value

    def finde_new_buy_id_accept(self):
        current_row = self.new_buy_request_table.currentRow()
        current_column = self.new_buy_request_table.currentColumn()
        cell_value = self.new_buy_request_table.item(current_row, current_column + 2).text()
        global New_Buy_ID_value
        New_Buy_ID_value = cell_value
        
    def finde_new_buy_id_reject(self):
        current_row = self.new_buy_request_table.currentRow()
        current_column = self.new_buy_request_table.currentColumn()
        cell_value = self.new_buy_request_table.item(current_row, current_column + 1).text()
        global New_Buy_ID_value
        New_Buy_ID_value = cell_value

        

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Operator panel"))
        # self.profile_button.setText(_translate("Form", "Profile"))
        # self.log_out_button.setText(_translate("Form", "logout"))
        self.label_20.setText(_translate("Form", "new product"))
        self.new_product_refresh.setText(_translate("Form", "refresh"))
        # self.show_rejected_button.setText(_translate("Form",))
        self.new_seller_table_refresh.setText(_translate("Form", "refresh"))
        self.new_buy_table_refresh.setText(_translate("Form", "refresh"))
        # self.label_6.setText(_translate("Form", "ID"))
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
        # self.Shop_report_refresh.setText(_translate("Form", "refresh"))
        # self.label_17.setText(_translate("Form", "shop report"))
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

    # total_rate_load_data function 
    def total_rate_load_data(self):
        CU_rate = the_operator.total_rate_cu()
        SL_rate = the_operator.total_rate_sl()
        PR_rate = the_operator.total_rate_pr()
        Shop_rate = the_operator.total_rate_shop()

        self.total_rate_list.setItem(0, 0, QtWidgets.QTableWidgetItem(str(CU_rate)))
        self.total_rate_list.setItem(1, 0, QtWidgets.QTableWidgetItem(str(SL_rate)))
        self.total_rate_list.setItem(2, 0, QtWidgets.QTableWidgetItem(str(PR_rate)))
        self.total_rate_list.setItem(3, 0, QtWidgets.QTableWidgetItem(str(Shop_rate)))
    
    def seller_id_finder(self,SL_ID):
        global THE_SL_ID 
        THE_SL_ID = SL_ID
    def costumer_id_finder(self, CU_ID):
        global THE_CU_ID 
        THE_CU_ID = CU_ID
    # search function 
    def search_seller(self, SL_ID):
        self.seller_list_table.setCurrentItem(None)
        if not SL_ID:
            return 
        matching_items = self.seller_list_table.findItems(SL_ID, Qt.MatchContains)
        if matching_items:
            item = matching_items[0]  # Take the first.
            self.seller_list_table.setCurrentItem(item)
        

    def search_costumer(self, CU_ID):
        self.costumerlist_table.setCurrentItem(None)
        if not CU_ID:
            return 
        matching_items = self.costumerlist_table.findItems(CU_ID, Qt.MatchContains)
        if matching_items:
            item = matching_items[0]  # Take the first.
            self.costumerlist_table.setCurrentItem(item)

    # seller report load data function 

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

    # costumer report list load data function
    def costumer_report_list_load_data(self):
        row_count = self.__row_count_SPECIAL('COSTUMER', 'ACTIVE', 'ACTIVE_STATUS')
        self.costumer_report_table.setRowCount(row_count)
        tablerow = 0 
        for row in the_operator.costumer_report():
            self.costumer_report_table.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.costumer_report_table.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.costumer_report_table.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            
            tablerow +=1
    # product load data function
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



    # new product request load data function 
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


    # new seller request load data function 
    def new_seller_request_load_data(self):
        row_count = self.__row_count_SPECIAL('SELLER','NEW', 'STATUS' )
        self.new_seller_request_table.setRowCount(row_count)
        tablerow = 0 
        for row in the_operator.check_seller():
            self.new_seller_request_table.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[0]))
            self.new_seller_request_table.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[1]))
            self.new_seller_request_table.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row[2]))
            self.new_seller_request_table.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(row[3]))
            self.new_seller_request_table.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(row[4]))
            self.new_seller_request_table.setItem(tablerow, 7, QtWidgets.QTableWidgetItem(row[5]))
            tablerow +=1


    # new buy request load data function
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



    # costumer load data function
    def costumer_load_data(self):
        row_count = self.__row_count_SPECIAL('COSTUMER', 'ACTIVE', 'ACTIVE_STATUS')
        self.costumerlist_table.setRowCount(row_count)
        tablerow = 0 
        for row in the_operator.costumer_list():
            self.costumerlist_table.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[0]))
            self.costumerlist_table.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[1]))
            self.costumerlist_table.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[2]))
            tablerow +=1
        
    def order_costumer_table_fill(self):
        row_count = self.__row_count_SPECIAL('COSTUMER', 'ACTIVE', 'ACTIVE_STATUS')
        self.costumerlist_table.setRowCount(row_count)
        tablerow = 0 
        for row in the_operator.costumer_sort():
            self.costumerlist_table.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[0]))
            self.costumerlist_table.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[1]))
            self.costumerlist_table.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[2]))
            tablerow +=1

    def delete_costumer_from_list(self):
        the_operator.del_customer_to_shop(THE_CU_ID)
        self.seller_load_data()

    def add_costumer_list(self):
        the_operator.add_costumer_to_shop(THE_CU_ID)
        self.seller_load_data()



    # seller load data function
    def seller_load_data(self):
        
        row_count = self.__row_count_SPECIAL('SELLER', 'ACTIVE', 'ACTIVE_STATUS')

        self.seller_list_table.setRowCount(row_count)
        tablerow = 0 
        for row in the_operator.seller_list():
            self.seller_list_table.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[0]))
            self.seller_list_table.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[1]))
            self.seller_list_table.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[2]))
            tablerow +=1

    def seller_load_data_order(self):
        row_count = self.__row_count_SPECIAL('SELLER', 'ACTIVE', 'ACTIVE_STATUS')
        self.seller_list_table.setRowCount(row_count)
        tablerow = 0 
        for row in the_operator.seller_sort():
            self.seller_list_table.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[0]))
            self.seller_list_table.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[1]))
            self.seller_list_table.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[2]))
            tablerow +=1

    def seller_list_delete_function(self):
        print(THE_SL_ID)
        the_operator.del_seller_to_shop(str(THE_SL_ID))
        self.seller_load_data()

    def seller_list_add_function(self):
        print(THE_SL_ID)
        the_operator.add_costumer_to_shop(str(THE_SL_ID))
        self.seller_load_data()

    def accept_buy_request_function(self):
        the_operator.accept_order(str(New_Buy_ID_value))
        self.buy_request_load_data()
    def reject_buy_request_function(self):
        the_operator.reject_order(str(New_Buy_ID_value))
        self.buy_request_load_data()

    def accept_new_seller_function(self):
        the_operator.accept_seller(str(New_SL_ID_value))
        self.new_seller_request_load_data()
    def reject_new_seller_function(self):
        the_operator.reject_seller(str(New_SL_ID_value))
        self.new_seller_request_load_data()

    def accept_new_product_function(self):
        the_operator.accept_product(str(New_PR_ID_value))
        self.new_product_request_load_data()
    def reject_new_product_function(self):
        the_operator.reject_product(str(New_PR_ID_value))
        self.new_product_request_load_data()


    # sell report load data function 
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



    # generate off code 
    def generate_off_code(self):
        exp = self.off_EXP_date.text()
        num = self.off_num.text()
        perecentage = self.off_percentage.text()
        off_cu_id = self.off_CU_ID.text()
        off_pr_id = self.off_PR_ID.text()

        if len(exp)==0 or len(num)==0 or len(perecentage)==0 or len(off_cu_id)==0 or len(off_pr_id)==0 :
            self.open_error_page()
        else:
            the_operator.off_code_generator(exp, off_pr_id,off_cu_id,num,perecentage)
            self.load_off_data()

    #  load off data
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

    def open_rejected_page(self):
        self.window = QtWidgets.QWidget()
        self.ui = rejected_page()
        self.ui.setupUi(self.window)
        self.window.show()

    def open_distance_page(self):
        self.window = QtWidgets.QWidget()
        self.ui = check_distance()
        self.ui.setupUi(self.window)
        self.window.show()
################################ end operator panel #####################################


################################ start costumer profile #################################
class costumer_profile(object):
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
        self.costumer_profile_information_table.setColumnCount(1)
        self.costumer_profile_information_table.setRowCount(6)
        # seller_profile_information_table
        self.costumer_profile_information_table.setColumnWidth(0,200)
        
        self.costumer_profile_information_table.setHorizontalHeaderLabels(['information'])
        self.costumer_profile_information_table.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers) # make table un editable
        self.costumer_profile_information_table.setVerticalHeaderLabels(['CU_ID', 'EMAIL', 'LOCATION', 'SCORE', 'TOTAL PURCHASE', 'ACTIVE STATUS'])

        self.costumer_profile_information_table_load_data(get_CU_ID_value)


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
        # costumer_profile_wallet_label
        for info in the_operator.load_cu_profile_wallet(get_CU_ID_value):
            self.costumer_profile_wallet_label.setText('Wallet: '+str(info[0])+'$')
        
        self.gridLayout_5.addWidget(self.costumer_profile_wallet_label, 1, 0, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.costumer_profile_order_table = QtWidgets.QTableWidget(self.page_2)
        self.costumer_profile_order_table.setObjectName("costumer_profile_order_table")
        self.costumer_profile_order_table.setColumnCount(5)
        self.costumer_profile_order_table.setRowCount(0)
        # costumer_profile_order_table 
        self.costumer_profile_order_table.setColumnWidth(0,200)
        
        self.costumer_profile_order_table.setHorizontalHeaderLabels(['seller name', 'ORDER' , 'number' , 'date', 'status'])
        self.costumer_profile_order_table.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers) # make table un editable
        self.costumer_profile_order_table.setVerticalHeaderLabels([''])

        self.costumer_profile_order_table_load_data(get_CU_ID_value)
        

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
        self.costumer_profile_basket_table.setColumnCount(1)
        self.costumer_profile_basket_table.setRowCount(0)
        # costumer_profile_basket_table 
        self.costumer_profile_basket_table.setColumnWidth(0,300)
        
        self.costumer_profile_basket_table.setHorizontalHeaderLabels(['Basket items'])
        self.costumer_profile_basket_table.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers) # make table un editable
        self.costumer_profile_basket_table.setVerticalHeaderLabels([''])

        self.costumer_profile_basket_table_load_data(get_CU_ID_value)
 
        self.horizontalLayout_7.addWidget(self.costumer_profile_basket_table)
        self.costumer_profile_favorite_table = QtWidgets.QTableWidget(self.page_3)
        self.costumer_profile_favorite_table.setObjectName("costumer_profile_favorite_table")
        self.costumer_profile_favorite_table.setColumnCount(1)
        self.costumer_profile_favorite_table.setRowCount(0)
        # costumer_profile_favorite_table 
        self.costumer_profile_favorite_table.setColumnWidth(0,300)
        
        self.costumer_profile_favorite_table.setHorizontalHeaderLabels(['Favorite items'])
        self.costumer_profile_favorite_table.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers) # make table un editable
        self.costumer_profile_favorite_table.setVerticalHeaderLabels([''])

        self.costumer_profile_favorite_table_load_data(get_CU_ID_value)
         

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
        self.costumer_profile_comment_table = QtWidgets.QTableWidget(self.page_4)
        self.costumer_profile_comment_table.setObjectName("costumer_profile_comment_table")
        self.costumer_profile_comment_table.setColumnCount(2)
        self.costumer_profile_comment_table.setRowCount(0)
        # costumer_profile_comment_table 
        self.costumer_profile_comment_table.setColumnWidth(0,80)
        self.costumer_profile_comment_table.setColumnWidth(1,800)

        self.costumer_profile_comment_table.setHorizontalHeaderLabels(['PR_ID', 'Comment'])
        self.costumer_profile_comment_table.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers) # make table un editable
        self.costumer_profile_comment_table_load_data(get_CU_ID_value)
        
        self.horizontalLayout_6.addWidget(self.costumer_profile_comment_table)
        self.gridLayout_4.addLayout(self.horizontalLayout_6, 1, 0, 1, 1)
        self.toolBox.addItem(self.page_4, "")
        self.gridLayout.addWidget(self.toolBox, 0, 0, 1, 1)

        self.retranslateUi(Form)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Costumer profile"))
        self.label.setText(_translate("Form", "CU ID "))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("Form", "Information"))
        self.label_5.setText(_translate("Form", "order list"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("Form", "Order list "))
        self.label_4.setText(_translate("Form", "Basket"))
        self.label_3.setText(_translate("Form", "favorit"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), _translate("Form", "Basket / Favorite"))
        self.label_6.setText(_translate("Form", "Comments list"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_4), _translate("Form", "Comments"))

    
    

    # costumer_profile_comment_table_load_data  
    def costumer_profile_comment_table_load_data(self,CU_ID):
        row_count = self.__row_count_SPECIAL('COMMENT_LIST', CU_ID, 'CU_ID')
        self.costumer_profile_comment_table.setRowCount(row_count)

        tablerow = 0 
        for row in the_operator.load_cu_profile_comments_list(CU_ID):
            self.costumer_profile_comment_table.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.costumer_profile_comment_table.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            tablerow +=1
        
        
            
     

    # costumer_profile_favorite_table_load_data  
    def costumer_profile_favorite_table_load_data(self,CU_ID):
        result = the_operator.load_cu_profile_favorite_list(CU_ID)
        for item in result:
            favorite = item[0].split(',')
        self.costumer_profile_favorite_table.setRowCount(len(favorite))
        for row in range(len(favorite)):
            self.costumer_profile_favorite_table.setItem(row, 0, QtWidgets.QTableWidgetItem(favorite[row]))
            
    # costumer_profile_basket_table_load_data  
    def costumer_profile_basket_table_load_data(self,CU_ID):
        result = the_operator.load_cu_profile_basket_list(CU_ID)
        for item in result:
            basket = item[0].split(',')
        self.costumer_profile_basket_table.setRowCount(len(basket))
        for row in range(len(basket)):
            self.costumer_profile_basket_table.setItem(row, 0, QtWidgets.QTableWidgetItem(basket[row]))
            
 
    # costumer_profile_information_table_load_data  
    def costumer_profile_information_table_load_data(self,CU_ID):
        result = the_operator.load_cu_profile_information(CU_ID)
        for row in result:
            self.costumer_profile_information_table.setItem(0, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.costumer_profile_information_table.setItem(1, 0, QtWidgets.QTableWidgetItem(row[1]))
            self.costumer_profile_information_table.setItem(2, 0, QtWidgets.QTableWidgetItem(row[2]))
            self.costumer_profile_information_table.setItem(3, 0, QtWidgets.QTableWidgetItem(row[3]))
            self.costumer_profile_information_table.setItem(4, 0, QtWidgets.QTableWidgetItem(row[4]))
            self.costumer_profile_information_table.setItem(5, 0, QtWidgets.QTableWidgetItem(row[5]))
 
    
    # costumer_profile_order_table_load_data  
    def costumer_profile_order_table_load_data(self,CU_ID):
        result = the_operator.load_cu_profile_order_list(CU_ID)
        for order in result:
            seller_name = order[0]
            orders = eval(order[1])
            date = order[2]
            status = order[3]

        orders_num = len(list(orders.keys()))

        self.costumer_profile_order_table.setRowCount(orders_num)

        for row in range(orders_num):
            self.costumer_profile_order_table.setItem(row, 0, QtWidgets.QTableWidgetItem(seller_name))
            
        for row in range(orders_num):
            self.costumer_profile_order_table.setItem(row, 1, QtWidgets.QTableWidgetItem(list(orders.keys())[row]))

        rowcounter = 0
        for row in list(orders.keys()):
            self.costumer_profile_order_table.setItem(rowcounter, 2, QtWidgets.QTableWidgetItem(str(orders[row])))
            rowcounter += 1

        for row in range(orders_num):
            self.costumer_profile_order_table.setItem(row, 3, QtWidgets.QTableWidgetItem(date))

        for row in range(orders_num):
            self.costumer_profile_order_table.setItem(row, 4, QtWidgets.QTableWidgetItem(status))
            
 

################################  end costumer profile  #################################

################################ start seller profile ###################################
class seller_profile(object):
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
        self.seller_profile_information_table.setColumnCount(1)
        self.seller_profile_information_table.setRowCount(8)
        # seller_profile_information_table 
        self.seller_profile_information_table.setColumnWidth(0,700)
        
        self.seller_profile_information_table.setHorizontalHeaderLabels(['Information'])
        self.seller_profile_information_table.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers) # make table un editable
        self.seller_profile_information_table.setVerticalHeaderLabels(['SL_ID', 'EMAIL', 'STATUS', 'SCORE', 'LOCATION', 'TOTAL SALES', 'NET INCOME', 'ACTIVE STATUS'])

        self.seller_profile_information_table_load_data(get_SL_ID_value)

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
        self.seller_profile_products_table.setColumnCount(1)
        self.seller_profile_products_table.setRowCount(0)
        # seller_profile_information_table 
        self.seller_profile_products_table.setColumnWidth(0,800)
        
        self.seller_profile_products_table.setHorizontalHeaderLabels(['Product'])
        self.seller_profile_products_table.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers) # make table un editable
        self.seller_profile_products_table.setVerticalHeaderLabels([])

        self.seller_profile_product_table_load_data(get_SL_ID_value)
 
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
        Form.setWindowTitle(_translate("Form", "Seller profile"))
        self.label.setText(_translate("Form", "SL ID"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("Form", "Information"))
        self.label_5.setText(_translate("Form", "product list"))
        self.label_2.setText(_translate("Form", "wallet inventory"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("Form", "Product list"))
    # seller_profile_information_table_load_data  
    def seller_profile_information_table_load_data(self, SL_ID):
        information_query  = the_operator.load_SL_profile_information(SL_ID)
        
        for row in information_query:
            self.seller_profile_information_table.setItem(0, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.seller_profile_information_table.setItem(1, 0, QtWidgets.QTableWidgetItem(row[1]))
            self.seller_profile_information_table.setItem(2, 0, QtWidgets.QTableWidgetItem(row[2]))
            self.seller_profile_information_table.setItem(3, 0, QtWidgets.QTableWidgetItem(row[3]))
            self.seller_profile_information_table.setItem(4, 0, QtWidgets.QTableWidgetItem(row[4]))
            self.seller_profile_information_table.setItem(5, 0, QtWidgets.QTableWidgetItem(row[5]))
            self.seller_profile_information_table.setItem(6, 0, QtWidgets.QTableWidgetItem(row[6]))
            self.seller_profile_information_table.setItem(7, 0, QtWidgets.QTableWidgetItem(row[7]))
     
    # seller_profile_product_table_load_data  
    def seller_profile_product_table_load_data(self, SL_ID):
        product_query  = the_operator.load_SL_profile_product(SL_ID)
        for i in product_query:
            data = i[0].split(',')
        print(data)
        self.seller_profile_products_table.setRowCount(len(data))
        for row in range(len(data)):
            self.seller_profile_products_table.setItem(row, 0, QtWidgets.QTableWidgetItem(data[row]))
            
 
################################  end seller profile  ###################################

################################  start rejected page ###################################

class rejected_page(object):
    def __row_count_SPECIAL(self, table_name:str, SPECIAL, COLUMN_NAME):
        conn = sqlite3.connect('database.sqlite3')
        cursor = conn.execute("SELECT count(*) FROM '{}' WHERE {} = '{}'".format(table_name, COLUMN_NAME,SPECIAL))
        for row in cursor:
            return row[0]
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(904, 563)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Buy_table = QtWidgets.QTableWidget(Form)
        self.Buy_table.setObjectName("Buy_table")
        self.Buy_table.setColumnCount(6)
        self.Buy_table.setRowCount(0)


        self.Buy_table.setColumnWidth(0,60)
        self.Buy_table.setColumnWidth(1,100)
        self.Buy_table.setColumnWidth(2,150)
        self.Buy_table.setColumnWidth(3,150)
        self.Buy_table.setColumnWidth(4,150)
        self.Buy_table.setColumnWidth(5,150)


        self.buy_reject_load_data()
        self.Buy_table.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers) # make table un editable

        self.Buy_table.setHorizontalHeaderLabels(['accept', 'CU_ID','SL_ID', 'ORDER LIST', 'DATE', 'STATUS' ])
        self.Buy_table.verticalHeader().hide()

        for index in range(self.Buy_table.rowCount()):
            self.buy_request_accept  = QPushButton("✅")
            self.buy_request_accept.clicked.connect(self.finde_new_buy_id)
            self.buy_request_accept.clicked.connect(self.accept_buy_request_function)
            self.Buy_table.setCellWidget(index, 0, self.buy_request_accept )


        self.horizontalLayout.addWidget(self.Buy_table)
        self.Product_table = QtWidgets.QTableWidget(Form)
        self.Product_table.setObjectName("Product_table")
        self.Product_table.setColumnCount(8)
        self.Product_table.setRowCount(0)

        self.product_request_load_data()
        self.Product_table.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers) # make table un editable

        self.Product_table.setHorizontalHeaderLabels(['accept','PR_ID','NAME', 'NUMBER', 'PRICE', 'SELLER LIST', 'STATUS' ])
        self.Product_table.verticalHeader().hide()

        for index in range(self.Product_table.rowCount()):
            self.product_request_accept  = QPushButton("✅")
            self.product_request_accept.clicked.connect(self.finde_product_id)
            self.product_request_accept.clicked.connect(self.accept_product_function)
            self.Product_table.setCellWidget(index, 0, self.product_request_accept )


        self.horizontalLayout.addWidget(self.Product_table)
        self.Seller_table = QtWidgets.QTableWidget(Form)
        self.Seller_table.setObjectName("Seller_table")
        self.Seller_table.setColumnCount(7)
        self.Seller_table.setRowCount(0)

        self.seller_request_load_data()
        self.Seller_table.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers) # make table un editable

        self.Seller_table.setHorizontalHeaderLabels(['accept', 'SL_ID','EMAIL', 'PRODUCTS', 'STATUS', 'SCORE', 'LOCATION' ])
        self.Seller_table.verticalHeader().hide()

        for index in range(self.Seller_table.rowCount()):
            self.seller_request_accept  = QPushButton("✅")
            self.seller_request_accept.clicked.connect(self.finde_seller_id)
            self.seller_request_accept.clicked.connect(self.accept_seller_function)
                
            self.Seller_table.setCellWidget(index, 0, self.seller_request_accept )


        self.horizontalLayout.addWidget(self.Seller_table)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Rejected items"))
        self.label_3.setText(_translate("Form", "Buy request"))
        self.label_2.setText(_translate("Form", "New product"))
        self.label.setText(_translate("Form", "New seller"))

    def accept_buy_request_function(self):
        the_operator.accept_order(str(Reject_Buy_ID_value))
        self.buy_reject_load_data()

    def finde_new_buy_id(self):
        current_row = self.Buy_table.currentRow()
        current_column = self.Buy_table.currentColumn()
        cell_value = self.Buy_table.item(current_row, current_column + 1).text()
        print(cell_value)
        global Reject_Buy_ID_value
        Reject_Buy_ID_value = cell_value

    def buy_reject_load_data(self):
        row_count = self.__row_count_SPECIAL('ORDER','REJECTED', 'STATUS' )
        self.Buy_table.setRowCount(row_count)
        tablerow = 0 
        for row in the_operator.check_reject_order():
            self.Buy_table.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[0]))
            self.Buy_table.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[1]))
            self.Buy_table.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[2]))
            self.Buy_table.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row[3]))
            self.Buy_table.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(row[4]))
            tablerow +=1


    def seller_request_load_data(self):
        row_count = self.__row_count_SPECIAL('SELLER','REJECTED', 'STATUS' )
        self.Seller_table.setRowCount(row_count)
        tablerow = 0 
        for row in the_operator.check_reject_seller():
            self.Seller_table.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[0]))
            self.Seller_table.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[1]))
            self.Seller_table.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[2]))
            self.Seller_table.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row[3]))
            self.Seller_table.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(row[4]))
            self.Seller_table.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(row[5]))
            tablerow +=1


    def accept_seller_function(self):
        the_operator.accept_seller(str(Reject_seller_ID_value))
        self.seller_request_load_data()
    def finde_seller_id(self):
        current_row = self.Seller_table.currentRow()
        current_column = self.Seller_table.currentColumn()
        cell_value = self.Seller_table.item(current_row, current_column + 1).text()
        print(cell_value)
        global Reject_seller_ID_value
        Reject_seller_ID_value = cell_value


    def product_request_load_data(self):
        row_count = self.__row_count_SPECIAL('PRODUCT','REJECTED', 'STATUS' )
        self.Product_table.setRowCount(row_count)
        tablerow = 0 
        for row in the_operator.check_reject_product():
            self.Product_table.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[0]))
            self.Product_table.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[1]))
            self.Product_table.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[2]))
            self.Product_table.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row[3]))
            self.Product_table.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(row[4]))
            self.Product_table.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(row[5]))
            tablerow +=1

    def finde_product_id(self):
        current_row = self.Product_table.currentRow()
        current_column = self.Product_table.currentColumn()
        cell_value = self.Product_table.item(current_row, current_column + 1).text()
        print(cell_value)
        global Reject_product_ID_value
        Reject_product_ID_value = cell_value

    def accept_product_function(self):
        the_operator.accept_product(str(Reject_seller_ID_value))
        self.product_request_load_data()
        

################################  end rejected page ###################################

################################  start check distance ################################

class check_distance(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(291, 562)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.result_label = QtWidgets.QLabel(Form)
        self.result_label.setText("")
        self.result_label.setObjectName("label")
        self.gridLayout.addWidget(self.result_label, 5, 0, 1, 2)
        self.sl_location_line = QtWidgets.QLineEdit(Form)
        self.sl_location_line.setObjectName("sl_location_line")
        global sl_location
        sl_location = str(self.sl_location_line.text())

        self.gridLayout.addWidget(self.sl_location_line, 3, 1, 1, 1)
        self.cu_location_line = QtWidgets.QLineEdit(Form)
        self.cu_location_line.setObjectName("cu_location_line")
        global cu_location
        cu_location = str(self.cu_location_line.text())

        self.gridLayout.addWidget(self.cu_location_line, 1, 1, 1, 1)
        self.check_button = QtWidgets.QPushButton(Form)
        self.check_button.setObjectName("check_button")

        self.check_button.clicked.connect(self.time_compute_function)

        self.gridLayout.addWidget(self.check_button, 4, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.location_table = QtWidgets.QTableWidget(Form)
        self.location_table.setObjectName("location_table")
        self.location_table.setColumnCount(2)
        self.location_table.setRowCount(0)


        self.location_table.setHorizontalHeaderLabels(['Location', 'Distance'])
        self.location_table.setColumnWidth(0,100)
        self.location_table.setColumnWidth(1,100)
        self.location_load_data()

        self.gridLayout.addWidget(self.location_table, 0, 0, 1, 2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def time_compute_function(self):
        result = the_operator.time_compute(sl_location, cu_location)
        if len(sl_location) == 0 or len(cu_location):
            self.result_label.setText("Please enter values")
        else:
            self.result_label.setText(str(result) + " Day")
    def __row_count(self, table_name:str):
        conn = sqlite3.connect('database.sqlite3')
        cursor = conn.execute("SELECT count(*) FROM '{}';" .format(table_name))
        for row in cursor:
            return row[0]
    def location_load_data(self):
        conn = sqlite3.connect('database.sqlite3')
        cur = conn.cursor()
        query = "SELECT LOCAT, DISTANCE FROM LOCATION"
        cur.execute(query)
        row_count = self.__row_count('LOCATION')
        self.location_table.setRowCount(row_count)
        tablerow = 0 
        for row in cur:
            self.location_table.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.location_table.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            tablerow +=1

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Time compute"))
        self.label_3.setText(_translate("Form", "Seller location"))
        self.check_button.setText(_translate("Form", "Check"))
        self.label_2.setText(_translate("Form", "Costumer location"))
################################  end check distance #################################

################################  start error page ###################################

class error_page (object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(269, 60)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.label.setText("error")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "error"))
################################  start error page ###################################


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = operator_panel()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())