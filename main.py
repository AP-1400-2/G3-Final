from customer import *
from shop_oprator import operator_panel
from shop_oprator import operators as op
# from ingredients.shop_oprator import shop as sh
import json

from shop_seller import *


import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import * 
from PyQt5.QtWidgets import * 

from PyQt5 import uic
################################ start login panel ###################################
my_operator = op('first@operator.com', 1234)


           
class addproduct(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('add.ui', self)
        self.addproductbtn.clicked.connect(self.insertproduct)
        self.backbtn.clicked.connect(self.backtoview)
        
    def backtoview(self):
        self.close()
        self.window=mainpage()
        self.window.show()
        
    def pr_id_generator(self):
        conn = sqlite3.connect('database.sqlite3')
        cursor = conn.execute ("SELECT count(*) FROM PRODUCT")
        for row in cursor:
            num_of_records = row[0]
        num = (111111 + num_of_records ) 
        PR_id = 'PR%d' %(num)
        return PR_id 

    def insertproduct(self):
        nameproduct= self.nameline.text()
        numberproduct= self.numberline.text()
        priceproduct= self.priceline.text()
        selleridproduct = self.selleridline.text()
        sllid = {selleridproduct:int(numberproduct)}
        sllid= json.dumps(sllid)
        conn= sqlite3.connect("database.sqlite3")
        cur = conn.cursor()
        PR= self.pr_id_generator()
        query = f"INSERT INTO PRODUCT (PR_ID,NAME,NUMBER,PRICE,SELLER_SL_ID,STATUS) VALUES ('{PR}','{nameproduct}','{numberproduct}','{priceproduct}','{sllid}','NEW')"
        cur.execute(query)
        conn.commit()
        

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

        # global operator_pass_input
        # operator_pass_input = self.operator_login_password_line.text()

        self.gridLayout_9.addWidget(self.operator_login_password_line, 1, 1, 1, 1)
        self.operator_login_email_line = QtWidgets.QLineEdit(self.page_2)
        self.operator_login_email_line.setObjectName("operator_login_email_line")

        # global operator_email_input
        # operator_email_input = self.operator_login_email_line.text()


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

        self.operator_login_push_button.clicked.connect(self.operator_login_function)

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
        
        #---------------------------
        self.seller_register_button.clicked.connect(self.goTologin)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Login / register"))
        self.costumer_login_push_button.setText(_translate("Form", "login"))
        self.login_email_label.setText(_translate("Form", "email"))
        self.login_pass_label.setText(_translate("Form", "password"))
        self.costumer_login_status.setText(_translate("Form", "Status"))
        self.label.setText(_translate("Form", "Welcome"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("Form", "Costumer"))
        self.login_email_label_2.setText(_translate("Form", "email"))
        self.login_pass_label_2.setText(_translate("Form", "password"))
        self.seler_login_push_button.setText(_translate("Form", "login"))
        self.seller_login_status.setText(_translate("Form", ""))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), _translate("Form", "Seller"))
        self.login_email_label_3.setText(_translate("Form", "email"))
        self.login_pass_label_3.setText(_translate("Form", "password"))
        self.operator_login_push_button.setText(_translate("Form", "login"))
        self.operator_login_status.setText(_translate("Form", ""))
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
        #-------------kia
        self.seller_register_button.clicked.connect(self.goTologin)
        self.seler_login_push_button.clicked.connect(self.goTomainpage)

    def goTologin(self):
        lineemail= self.seller_register_email_line.text()
        linepassword= self.seller_register_password_line.text()
        loc= self.seller_register_location_line.text()
        SL_ID2 = my_operator .SL_id_generator()
        conn= sqlite3.connect("database.sqlite3")
        cur = conn.cursor()
        query = f"INSERT INTO SELLER (SL_ID,EMAIL,PASSWORD,STATUS,LOCATION) VALUES ('{SL_ID2}','{lineemail}','{linepassword}','NEW','{loc}')"
        cur.execute(query)
        conn.commit()
       
        
        
    def goTomainpage(self):
        emailline = self.seller_email_login_line.text()
        passline = self.seller_password_login_line.text()
        
        if len(emailline) == 0 or len(passline) == 0:
            self.seller_login_status.setText("Please input all fields.")
        else:
            conn = sqlite3.connect("database.sqlite3")
            cur = conn.cursor()
            query = 'SELECT PASSWORD FROM SELLER WHERE EMAIL =\'' + emailline + "\'"
            cur.execute(query)
            result_pass = cur.fetchone()[0]
            if result_pass == passline:
                print("successfully loged in")
                cur.execute(f"SELECT SL_ID FROM SELLER WHERE EMAIL = '{emailline}'AND PASSWORD = '{passline}' ")
                self.sellerid= cur.fetchall()[0][0]
                #print(self.sellerid)
                self.seller_login_status.setText("successfully loged in")
                Form.close()
                self.window = mainpage()
                self.window.getsellerid(self.sellerid)
                self.window.show()
            else:
                self.seller_login_status.setText("Invalid user or pass")
    
        
        

    def operator_login_function(self):
        operator_pass_input = self.operator_login_password_line.text()
        operator_email_input = self.operator_login_email_line.text()
        
        if len(operator_email_input) == 0 or len(operator_pass_input) == 0:
            self.operator_login_status.setText("Please input your email and password!")
        else:
            conn = sqlite3.connect('database.sqlite3')
            cur = conn.cursor()
            query = 'SELECT PASSWORD FROM OPERATOR WHERE EMAIL = \'' + operator_email_input + "\'"
            cur.execute(query)
            result_pass = cur.fetchone()[0]
            if result_pass == operator_pass_input:
                self.switch_to_operator_panel()
            else:
                self.operator_login_status.setText("invalid email or password")

    def switch_to_operator_panel(self):
        self.window = QtWidgets.QWidget()
        self.ui = operator_panel()
        self.ui.setupUi(self.window)
        Form.hide()
        self.window.show()

################################ end login panel #####################################
class mainpage(QDialog):
        def __init__(self):
            super().__init__()
            uic.loadUi('viwe.ui', self)
            self.pushButton_2.clicked.connect(self.gotoaddproduct)
            self.pushButton.clicked.connect(self.gotorefresh)
            self.viewdata()
        def getsellerid(self,sellerid):
            self.sellerid = sellerid
            return self.sellerid
            
            
        def viewdata(self):
            conn = sqlite3.connect('database.sqlite3')
            cursor = conn.execute ("SELECT count(*) FROM PRODUCT")
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM PRODUCT WHERE NUMBER > 5 or Number < 5 ")
            getall= cursor.fetchall()
            productname_dict = {}
            productnumber_dict = {}
            productprice_dict ={}
            index = 0
            height = 140
            for i in getall:
                productname= i[2]
                productnumber= i[3]
                productprice= i[4]
                
                productname_dict[index]= QLabel(self)
                productname_dict[index].setText(productname)
                productname_dict[index].setGeometry(120,height,71,20)
                productname_dict[index].setObjectName("Product Name")
                
                productnumber_dict[index]= QLabel(self)
                productnumber_dict[index].setText(productnumber)
                productnumber_dict[index].setGeometry(250,height,71,20)
                productnumber_dict[index].setObjectName("Product Number")
                
                productprice_dict[index]= QLabel(self)
                productprice_dict[index].setText(productprice)
                productprice_dict[index].setGeometry(390,height,71,20)
                productprice_dict[index].setObjectName("Product Price")
                
                
                
                index+=1
                height +=60
            #print(getall)
        
            
        
        def gotorefresh(self):
            self.close()
            self.window = mainpage()
            self.window.show()
            
        def gotoaddproduct(self):
           self.close()
           self.window = addproduct()
           self.window.show()



################################ start shop ###################################

################################ end   shop ###################################


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = login_register()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

