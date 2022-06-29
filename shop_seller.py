import sqlite3
from random import randint as rint


'''
CREATE TABLE "SELLER" (
	"ID"	INTEGER NOT NULL UNIQUE,
	"SL_ID"	TEXT NOT NULL UNIQUE,
	"EMAIL"	INTEGER NOT NULL UNIQUE,
	"PASSWORD"	TEXT NOT NULL,
	"INVENTORY_WALLET"	REAL DEFAULT 0,
	"PRODUCTS"	TEXT,
	"STATUS"	TEXT,
	"SCORE"	INTEGER,
	PRIMARY KEY("ID" AUTOINCREMENT)
);
'''
class seller:
    def __init__(self, SL_ID , email : str , password : str, products : list, location : str, score :int) -> None:
        self.__email = email
        self.__SL_ID = SL_ID
        self.__password = password
        self.__products = products
        self.__location = location
        self.__score= score



    def make_wallet(self):
        ''' in this method we make one wallet for seller'''
        conn = sqlite3.connect('database.sqlite3')
        role = 'seller'
        conn.execute("INSERT INTO WALLET (ROLE, SPECIAL_ID) \
            VALUES(%s, %s)" %(role, self.__SL_ID))
        conn.commit()
        conn.close()



    def changepassword(self, oldpassword, newpassword):
        conn = sqlite3.connect('database.sqlite3')
        cursor = conn.execute("SELECT PASSWORD FROM SELLER WHERE EMAIL = '%s' " %(self.__email))
        for row in cursor:
            old_password = row[0]
        if old_password == oldpassword:
            conn.execute("UPDATE SELLER PASSWORD = '%s' WHERE EMAIL = '%s'" %(newpassword, self.__email))
            conn.commit()
            conn.close()


    def changeemail(self, newewmail, password):
        conn = sqlite3.connect('database.sqlite3')
        cursor = conn.execute("SELECT PASSWORD FROM SELLER WHERE EMAIL = '%s' " %(self.__email))
        for row in cursor:
            database_password = row[0]
        if database_password == password:
            conn.execute("UPDATE SELLER EMAIL = '%s' WHERE EMAIL = '%s'" %(newewmail, self.__email))
            conn.commit()
            conn.close()


    #def rate(self, flag):
        


    def order_reports(self):
        conn= sqlite3.connect('database.sqlite3')
        cursor = conn.execute("SELECT * FROM ORDER")
        for row in cursor:
            CU_ID= row[0]
            order= row[1]
        conn.close()

    


    def PR_id_generator(self):
        conn = sqlite3.connect('database.sqlite3')
        cursor = conn.execute ("SELECT count(*) FROM PRODUCT")
        for row in cursor:
            num_of_records = row[0]
        num = (111111 + num_of_records ) 
        PR_id = 'PR%d' %(num)
        return PR_id 

    def scoremanager(self):
        conn= sqlite3.connect('database.sqlite3')
        conn.execute("UPDATE SELLER SCORE=SCORE - 0.001 WHERE SL_ID='%s'"%(self.__SL_ID))
        conn.commit()
        conn.close()

    

        



'''
CREATE TABLE "PRODUCT" (
	"ID"	INTEGER NOT NULL UNIQUE,
	"PR_ID"	TEXT NOT NULL UNIQUE,
	"NAME"	TEXT NOT NULL UNIQUE,
	"NUMBER"	INTEGER NOT NULL,
	"PRICE"	INTEGER NOT NULL,
	"SELLER_SL_ID"	TEXT,
	"STATUS"	TEXT,
	FOREIGN KEY("SELLER_SL_ID") REFERENCES "SELLER",
	PRIMARY KEY("ID" AUTOINCREMENT)
);
'''


class products:
    def __init__(self, name,  PR_ID, seller, number, price):
        self.__name = name 
        self.__PR_ID = PR_ID
        self.__seller = seller
        self.__number = number 
        self.__price = price


    # def save_to_db(self):
    #     conn = sqlite3.connect('database.sqlite3')
    #     data = self.__dict__

    def add_product(self, name):
        conn = sqlite3.connect('database.sqlite3')
        conn.execute("INSERT INTO PRODUCT (PR_ID,NAME,NUMBER,PRICE,SELLER_SL_ID,STATUS)VALUES(%s, %s,%s,%s,%s,%s)" %(self.__PR_ID,self.__name,self.__price,self.__number,self.__price,self.__seller,'NEW'))
        conn.commit()
        conn.close()






