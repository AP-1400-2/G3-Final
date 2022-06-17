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
        old_password = conn.execute("SELECT PASSWORD FROM OPERATOR WHERE EMAIL = '%s' " %(self.__email))
        if old_password == oldpassword:
            try:
                conn.execute("UPDATE OPERATOR PASSWORD = '%s' WHERE EMAIL = '%s'" %(newpassword, self.__email))
                conn.commit()            
            except sqlite3.Error:
                print("error! something went wrong")
            else:
                print("Done!")


    def changeemail(self, newewmail, password):
        conn = sqlite3.connect('database.sqlite3')
        cursor = conn.execute("SELECT PASSWORD FROM OPERATOR WHERE EMAIL = '%s' " %(self.__email))
        for row in cursor:
            database_password = row[0]
        if database_password == password:
            try:
                conn.execute("UPDATE OPERATOR EMAIL = '%s' WHERE EMAIL = '%s'" %(newewmail, self.__email))
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
                        VALUES('%s','%s');'''%(data['_operators__email'],data['_operators__password']))
            conn.commit()
        except sqlite3.Error:
            print("error! something went wrong")
        else:
            print("Done!")



    def check_product(self):
        pass

    def accept_product(self, PR_ID):
       pass



    def check_seller(self):
        pass

    def accept_seller(self, SL_ID):
        pass

    def check_order(self):
        pass

    def accept_order(self, CU_ID):
        pass
    

    def report(self, subject):
        pass



    def report_rate(self, shop_name):
        pass


    def off_code_generator(self, EXP, PR_ID, CU_ID, NUM, PERC):
        num = str(rint(1000000,9999999))
        off_code = 'off%s' %(num)
        conn = sqlite3.connect('database.sqlite3')
        conn.execute('''INSERT INTO OFF (CODE, PR_ID, EXP_DATE, CU_ID, NUMBER, PERCENTAGE) \
            VALUES('%s','%s','%s','%s','%s');'''%(off_code, PR_ID, str(EXP), CU_ID, str(NUM), str(PERC)))
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
        pass

    def add_costumer(self, CU_ID):
        pass



    def del_customer(self, CU_ID):
        pass



    def add_seller(self, SL_ID):
        pass


    def del_seller(self, SL_ID):
        pass



    def card_to_wallet(self, value):
        pass


    def wallet_to_card(self, value):
        pass


    def time_compute(self):
        pass

